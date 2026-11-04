#!/usr/bin/env python3
"""根据 data/ 里的数据生成 README.md、README.en.md 和 docs/index.html。

用法：
    python scripts/build.py            # 生成文件
    python scripts/build.py --check    # 只检查生成结果是否和仓库里的一致（CI 用）
    python scripts/build.py --artifact # 把网页正文输出到标准输出
"""
import datetime
import json
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPO = "syydaniel/awesome-code-animation"
REPO_URL = f"https://github.com/{REPO}"
PAGES_URL = "https://syydaniel.github.io/awesome-code-animation/"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


projects = load("projects.json")
styles = load("styles.json")
picks = load("picks.json")
meta = load("meta.json")
rel_data = load("relations.json")
UPDATED = meta["updated"]
SNAP = datetime.date.fromisoformat(UPDATED)
SMAP = {s["key"]: s for s in styles}
MAIN = [s for s in styles if s.get("zone") != "niche"]
NICHE = [s for s in styles if s.get("zone") == "niche"]
BYREPO = {p["repo"]: p for p in projects}
RTYPES = {t["key"]: t for t in rel_data["types"]}

for p in projects:
    for t in p["tags"]:
        if t not in SMAP:
            sys.exit(f"未知画风 {t!r}（{p['repo']}），请先在 data/styles.json 里定义")

relations, dropped = [], []
for r in rel_data["relations"]:
    if r["from"] in BYREPO and r["to"] in BYREPO and r["type"] in RTYPES:
        relations.append(r)
    else:
        dropped.append(r)
if dropped and "--quiet" not in sys.argv:
    for r in dropped:
        print(f"跳过关系 {r['from']} → {r['to']}：项目不在列表里或类型未定义", file=sys.stderr)


def fmt_stars(n):
    if n >= 100_000:
        return f"{n / 1000:.0f}k"
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def status(p):
    if p.get("archived"):
        return "⚪", "已归档", "archived"
    days = (SNAP - datetime.date.fromisoformat(p["pushed_at"])).days
    if days <= 183:
        return "🟢", "活跃", "active"
    if days <= 730:
        return "🟡", "放缓", "slowing"
    return "⚪", "停更", "dormant"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def link(p):
    return f"[{cell(p['name'])}](https://github.com/{p['repo']})"


def badge(label, value, color):
    return f"![{label}](https://img.shields.io/badge/{quote(label)}-{quote(str(value).replace('-', '--'))}-{color})"


def by_stars(items):
    return sorted(items, key=lambda p: -p["stars"])


def in_style(key):
    return by_stars([p for p in projects if key in p["tags"]])


def style_title(s):
    words = [w for w in s["en"].replace(",", " ").replace("&", " ").lower().split() if len(w) > 1]
    return s["name"] if any(w in s["name"].lower() for w in words) else f"{s['name']} · {s['en']}"


# ---------------------------------------------------------------- README (中文)

def style_table(key):
    rows = ["| 项目 | 星数 | 状态 | 写法 | 说明 |", "| --- | ---: | :---: | --- | --- |"]
    for p in in_style(key):
        emoji, label, _ = status(p)
        others = [SMAP[t]["name"] for t in p["tags"] if t != key]
        extra = f"适合：{p['use']}"
        if others:
            extra += " · 也在：" + "、".join(others)
        desc = cell(p["desc"]) + f"<br><sub>{cell(extra)}</sub>"
        if p.get("note"):
            desc += f"<br><sub>⚠️ {cell(p['note'])}</sub>"
        rows.append(f"| {link(p)} | {fmt_stars(p['stars'])} | {emoji} {label} | {cell(p['lang'])} | {desc} |")
    return "\n".join(rows)


def index_grid(group, en=False, cols=3):
    cells = []
    for s in group:
        n = len(in_style(s["key"]))
        title = s["en"] if en else s["name"]
        sub = f"{s['name']} · {n} projects" if en else f"{s['en']} · {n} 个项目"
        cells.append(
            f'<td align="center" width="33%"><a href="#{s["key"]}">'
            f'<img src="assets/styles/{s["key"]}.png" alt="{title}" width="260"></a><br>'
            f'<b><a href="#{s["key"]}">{title}</a></b><br><sub>{sub}</sub></td>'
        )
    rows = ["<table>"]
    for i in range(0, len(cells), cols):
        rows.append("<tr>" + "".join(cells[i:i + cols]) + "</tr>")
    rows.append("</table>")
    return "\n".join(rows)


def picks_table():
    rows = ["| 想做什么 | 先看这几个 |", "| --- | --- |"]
    for pk in picks:
        links = [link(BYREPO[r]) for r in pk["projects"] if r in BYREPO]
        rows.append(f"| {pk['goal']} | {' · '.join(links)} |")
    return "\n".join(rows)


def relations_section():
    parts = [
        f"共 {len(relations)} 条关系。想换工具时先看「同类可替换」，想扩展功能时看「插件 / 扩展」和「基于」。",
        "",
    ]
    for t in rel_data["types"]:
        rows = [r for r in relations if r["type"] == t["key"]]
        if not rows:
            continue
        parts += [f"### {t['name']}", "", f"<sub>{t['desc']}</sub>", "",
                  "| 项目 | 关系 | 项目 | 说明 |", "| --- | :---: | --- | --- |"]
        for r in rows:
            parts.append(f"| {link(BYREPO[r['from']])} | {t['name']} | {link(BYREPO[r['to']])} | {cell(r.get('note', ''))} |")
        parts.append("")
    return "\n".join(parts)


def all_table():
    rows = ["| 项目 | 星数 | 画风 | 状态 |", "| --- | ---: | --- | :---: |"]
    for p in by_stars(projects):
        tags = "、".join(f"[{SMAP[t]['name']}](#{t})" for t in p["tags"])
        rows.append(f"| {link(p)} | {fmt_stars(p['stars'])} | {tags} | {status(p)[0]} |")
    return "\n".join(rows)


def style_section(s, en=False):
    n = len(in_style(s["key"]))
    if en:
        head = [f'<a name="{s["key"]}"></a>', "", f"### {s['en']}", "", f"> {s['name']} · {n} projects", "", en_style_table(s["key"]), "",
                "<sub>[↑ Back to the style index](#index)</sub>", ""]
        return head
    return [
        f'<a name="{s["key"]}"></a>', "",
        f"### {style_title(s)}", "",
        f'<img src="assets/styles/{s["key"]}.png" alt="{s["name"]}样图" width="240" align="right">', "",
        f"> {s['look']}", "",
        f"共 {n} 个项目，按星数排序。", "",
        '<br clear="right">', "",
        style_table(s["key"]), "",
        "<sub>[↑ 回到画风索引](#index)</sub>", "",
    ]


def counts():
    active = sum(1 for p in projects if status(p)[2] == "active")
    agent = len(in_style("agent"))
    niche = len({p["repo"] for s in NICHE for p in in_style(s["key"])})
    return active, agent, niche


def readme():
    active, agent, niche = counts()
    parts = [
        '<div align="center">', "",
        '<img src="assets/banner.png" alt="代码画风图鉴 · Awesome Code Animation" width="100%">', "",
        "# 代码画风图鉴 · Awesome Code Animation", "",
        "**用代码画动画、做 MV 的开源项目合集，按画风索引。**", "",
        "A curated list of open-source tools for making animations and music videos **with code**, indexed by visual style. [English](README.en.md)", "",
        " ".join([
            "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
            badge("项目", len(projects), "2E49D4"),
            badge("画风", f"{len(MAIN)}+{len(NICHE)}", "9265D9"),
            badge("Claude/Opus", agent, "7B4FD0"),
            badge("活跃项目", active, "1E8A4B"),
            badge("数据更新", UPDATED, "5B6273"),
        ]), "",
        f"**[🔎 网页版：可按画风筛选、搜索、排序、看项目关系]({PAGES_URL})**", "",
        " · ".join([
            "[画风索引](#index)", "[小众画风区](#niche)", "[Claude / Opus 写代码出片](#agent)",
            "[项目关系表](#relations)", "[收录标准](#rules)", "[全部项目](#all)",
            f"[推荐项目]({REPO_URL}/issues/new/choose)",
        ]), "",
        "</div>", "",
        "## 这是什么", "",
        "想用代码做一支 MV、一段讲解动画、一个片头，第一个问题往往是「我想要的那种画风，该用什么工具做」。"
        "这里把 GitHub 上用代码做动画、做视频的开源项目按**画风**归类：3B1B 式数学讲解、扁平 MG、着色器迷幻光影、像素复古、ASCII 终端、音乐可视化、二次元 MMD……"
        "先挑画风，再挑工具。一个项目常能做好几种画风，所以会同时出现在几个画风里。", "",
        f"除了 {len(MAIN)} 种主流画风，还有收录小众画风的[小众画风区](#niche)（水墨山水、汉字笔顺、示波器、绘图仪、人工生命……），"
        f"以及 {agent} 个让 Claude、Opus 等 AI 编程助手[用纯代码出片](#agent)的项目。[项目关系表](#relations)说明了谁基于谁、谁能替换谁。", "",
        '<a name="rules"></a>', "",
        "## 收录标准", "",
        "- **画面必须由代码绘制或渲染。** 用视频生成、图像生成模型出画面的项目不收；Claude / Opus 写代码出片的项目，调用 Blender 出画面的也不收。个别项目带有可选的生成功能，会在说明里注明。",
        "- **主流画风：** GitHub 星数 1000 以上，或近一年内有更新且星数 200 以上。",
        "- **小众画风区和 Claude / Opus 区：** 门槛放宽到近一年内有更新、星数 50 以上，好让有潜力的新项目早点被看到。",
        "- **已归档（只读）的仓库不收。** 看过但没收的项目和原因记在 [`data/excluded.json`](data/excluded.json)。",
        "- 状态按仓库最近一次推送计算：🟢 活跃（半年内）· 🟡 放缓（两年内）· ⚪ 停更（超过两年，多数仍能用，只是不再加新功能）。",
        f"- 星数和状态每周一由 GitHub Actions 自动刷新，新项目候选每周自动整理成 Issue，当前数据更新于 {UPDATED}。", "",
        '<a name="picks"></a>', "",
        "## 按目的先挑", "",
        picks_table(), "",
        '<a name="index"></a>', "",
        "## 画风索引", "",
        "点图片跳到对应画风的项目表。每张小样图都是用代码画出来的，代码在 [`site/template.html`](site/template.html) 里。", "",
        index_grid(MAIN), "",
        "### 小众画风区", "",
        index_grid(NICHE), "",
        "## 主流画风", "",
    ]
    for s in MAIN:
        parts += style_section(s)
    parts += [
        '<a name="niche"></a>', "",
        "## 小众画风区", "",
        f"这些画风用的人不多，但很有辨识度。门槛放宽到近一年内有更新、星数 50 以上；共 {niche} 个项目。", "",
    ]
    for s in NICHE:
        parts += style_section(s)
    parts += [
        '<a name="relations"></a>', "",
        "## 项目关系表", "",
        relations_section(),
        '<a name="all"></a>', "",
        "## 全部项目", "",
        f"<details>\n<summary>展开全部 {len(projects)} 个项目（按星数排序）</summary>\n",
        all_table(), "", "</details>", "",
        "## 相关合集", "",
        "**创意编程**", "",
        "- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding)：创意编程资源大全，覆盖教程、书籍和工具（英文）。",
        "- [awesome-plotters](https://github.com/beardicus/awesome-plotters)：绘图仪相关的代码和资源。",
        "- [morphogenesis-resources](https://github.com/jasonwebb/morphogenesis-resources)：用代码「长出」形态的资料大全：反应扩散、差异生长、黏菌、L 系统。",
        "- [awesome-demoscene](https://github.com/psykon/awesome-demoscene)：Demoscene 的工具、代码和资料。", "",
        "**Claude / Opus 作品合集**：这些合集收的是网友用 Claude 做出的视频和提示词，可以当灵感来源。其中少数作品调用了 Blender 或视频生成模型，合集里通常有标注，请自行甄别。", "",
        "- [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)：用 Claude Opus 5.5 做出的视频和背后的提示词。",
        "- [opus-video-prompts](https://github.com/joeseesun/opus-video-prompts)：中文整理的 Opus 5.5 代码视频案例和可复制的提示词。",
        "- [awesome-claude-5-5-videos](https://github.com/athemeroy/awesome-claude-5-5-videos)：标注了来源和模型的 Claude 5.5 视频工作流。",
        "- [awesome-opus-5.5-video](https://github.com/zhuyansen/awesome-opus-5.5-video)：Opus 5.5 做的视频、动态图形、3D 场景和游戏。",
        "- [awesome-claude-video](https://github.com/opusvideo/awesome-claude-video)：Claude Opus 5.5 视频和动画合集。", "",
        "**AI 做视频的技能**", "",
        "- [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills)：让编程助手做视频的技能合集，其中部分项目会调用生成模型，和本仓库的收录标准不同。",
        "- [awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills)：动效设计方向的 AI 技能合集。", "",
        "## 参与贡献", "",
        f"发现好项目？欢迎[提 Issue 推荐]({REPO_URL}/issues/new/choose)，或者直接修改 [`data/projects.json`](data/projects.json) 提 Pull Request，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。",
        "每周一会自动在 GitHub 上搜一遍新项目，把候选整理成一个 Issue，欢迎在里面帮忙判断哪些值得收录。",
        "README 和网页版都由 `python scripts/build.py` 从数据文件自动生成，请不要直接改 README。", "",
        "如果这份合集帮到了你，点个 ⭐ Star 能让更多人找到它。", "",
        "## Star History", "",
        f"[![Star History Chart](https://api.star-history.com/svg?repos={REPO}&type=Date)](https://star-history.com/#{REPO}&Date)", "",
        "## 许可", "",
        "本仓库的整理内容以 [CC0 1.0](LICENSE) 发布，可以自由使用。各项目的许可证以其仓库为准，商用前请自行核对。", "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- README (English)

EN_REL = {"fork": "forked from", "built_on": "built on", "plugin": "plugin for", "official": "official add-on for",
          "uses": "renders with", "data": "uses data from", "alt": "alternative to", "pair": "pairs with", "author": "same author as"}


def en_desc(p):
    return p.get("gh_desc") or p["desc"]


def en_style_table(key):
    rows = ["| Project | Stars | Status | Description |", "| --- | ---: | :---: | --- |"]
    for p in in_style(key):
        rows.append(f"| {link(p)} | {fmt_stars(p['stars'])} | {status(p)[0]} | {cell(en_desc(p))} |")
    return "\n".join(rows)


def readme_en():
    active, agent, niche = counts()
    parts = [
        '<div align="center">', "",
        '<img src="assets/banner.png" alt="Awesome Code Animation" width="100%">', "",
        "# Awesome Code Animation", "",
        "**Open-source tools for making animations and music videos with code, indexed by visual style.** [中文](README.md)", "",
        " ".join([
            "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
            badge("projects", len(projects), "2E49D4"),
            badge("styles", f"{len(MAIN)}+{len(NICHE)}", "9265D9"),
            badge("Claude/Opus", agent, "7B4FD0"),
            badge("updated", UPDATED, "5B6273"),
        ]), "",
        f"**[🔎 Interactive version: filter by style, search, sort, see how projects relate]({PAGES_URL})** (Chinese UI)", "",
        "</div>", "",
        "## What this is", "",
        "Pick a look first, then a tool. Every project here draws or renders its frames in code: Manim-style math explainers, flat motion graphics, "
        "shaders, pixel art, ASCII, music visualizers, MMD dance videos, ink-wash landscapes, oscilloscope art, plotter drawings and more. "
        "A project that can do several looks appears under each of them.", "",
        "## Rules", "",
        "- **Frames must be drawn or rendered by code.** Projects that make their pictures with image or video generation models are left out; "
        "agent projects that render through Blender are left out too. Optional generation features are noted per project.",
        "- **Main styles:** 1,000+ stars, or 200+ stars with a push in the last year.",
        "- **Niche styles and the Claude / Opus section:** 50+ stars with a push in the last year.",
        "- Archived repositories are not listed. Status: 🟢 pushed within 6 months · 🟡 within 2 years · ⚪ older.",
        f"- Stars and status refresh every Monday through GitHub Actions. Data as of {UPDATED}.", "",
        '<a name="index"></a>', "",
        "## Style index", "",
        index_grid(MAIN, en=True), "",
        "### Niche styles", "",
        index_grid(NICHE, en=True), "",
        "## Main styles", "",
    ]
    for s in MAIN:
        parts += style_section(s, en=True)
    parts += ["## Niche styles", ""]
    for s in NICHE:
        parts += style_section(s, en=True)
    parts += ["## How projects relate", "", "| Project | Relation | Project |", "| --- | :---: | --- |"]
    for r in relations:
        parts.append(f"| {link(BYREPO[r['from']])} | {EN_REL[r['type']]} | {link(BYREPO[r['to']])} |")
    parts += [
        "", "## Contributing", "",
        f"Suggest a project through [an issue]({REPO_URL}/issues/new/choose) or edit [`data/projects.json`](data/projects.json) and open a pull request. "
        "The READMEs and the web page are generated by `python scripts/build.py`; please don't edit them by hand.", "",
        "## License", "", "The curation is released under [CC0 1.0](LICENSE). Each project keeps its own license.", "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- web page

def page(standalone=True):
    tpl = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    slim = [{k: v for k, v in p.items() if k != "gh_desc"} for p in projects]
    body = (tpl.replace("__PROJECTS__", dump(slim))
               .replace("__STYLES__", dump(styles))
               .replace("__PICKS__", dump(picks))
               .replace("__RELATIONS__", dump(relations))
               .replace("__RELTYPES__", dump(rel_data["types"]))
               .replace("__DATE__", UPDATED)
               .replace("__REPO_URL__", REPO_URL))
    if not standalone:
        return body
    head, sep, rest = body.partition("<style>")
    return ("<!doctype html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + sep + rest.replace("</style>", "</style>\n</head>\n<body>", 1)
            + "\n</body>\n</html>\n")


def main():
    if "--artifact" in sys.argv:
        print(page(standalone=False))
        return
    outputs = {ROOT / "README.md": readme(), ROOT / "README.en.md": readme_en(), ROOT / "docs" / "index.html": page()}
    if "--check" in sys.argv:
        stale = [str(p.relative_to(ROOT)) for p, text in outputs.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            sys.exit("这些文件需要重新生成，请运行 python scripts/build.py：" + "、".join(stale))
        print("生成结果是最新的。")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"已生成 README.md、README.en.md 和 docs/index.html：{len(projects)} 个项目，"
          f"{len(MAIN)} 种主流画风 + {len(NICHE)} 种小众画风，{len(relations)} 条项目关系。")


if __name__ == "__main__":
    main()
