#!/usr/bin/env python3
"""根据 data/ 里的数据生成 README.md、README.en.md 和 docs/index.html。

用法：
    python scripts/build.py            # 生成文件
    python scripts/build.py --check    # 只检查生成结果是否和仓库里的一致（CI 用）
    python scripts/build.py --artifact # 把网页正文输出到标准输出
"""
import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPO = "syydaniel/awesome-code-animation"
REPO_URL = f"https://github.com/{REPO}"
PAGES_URL = "https://syydaniel.github.io/awesome-code-animation/"
CJK = re.compile(r"[\u4e00-\u9fff]")


def page_url(anchor="", en=False):
    """网页版地址，带上语言，这样从哪个 README 点过去就是哪种语言。"""
    return f"{PAGES_URL}?lang={'en' if en else 'zh'}" + (f"#{anchor}" if anchor else "")


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


projects = load("projects.json")
styles = load("styles.json")
picks = load("picks.json")
meta = load("meta.json")
rel_data = load("relations.json")
showcase = load("showcase.json")["items"] if (DATA / "showcase.json").exists() else []
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
untranslated = [p["repo"] for p in projects if not p.get("desc_en")]
if untranslated and "--quiet" not in sys.argv:
    print(f"这些项目还没有英文说明（desc_en），英文版先用 GitHub 简介：{'、'.join(untranslated)}", file=sys.stderr)


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


def link(p, en=False):
    name = (p.get("name_en") or p["name"]) if en else p["name"]
    return f"[{cell(name)}](https://github.com/{p['repo']})"


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


def swatch(key, en=False):
    """小样图：少数画了文字的样图有单独的英文版。"""
    if en and (ROOT / "assets" / "styles" / f"{key}.en.png").exists():
        return f"assets/styles/{key}.en.png"
    return f"assets/styles/{key}.png"


def index_grid(group, en=False, cols=3):
    cells = []
    for s in group:
        n = len(in_style(s["key"]))
        title = s["en"] if en else s["name"]
        sub = f"{n} projects" if en else f"{s['en']} · {n} 个项目"
        cells.append(
            f'<td align="center" width="33%"><a href="#{s["key"]}">'
            f'<img src="{swatch(s["key"], en)}" alt="{title}" width="260"></a><br>'
            f'<b><a href="#{s["key"]}">{title}</a></b><br><sub>{sub}</sub></td>'
        )
    rows = ["<table>"]
    for i in range(0, len(cells), cols):
        rows.append("<tr>" + "".join(cells[i:i + cols]) + "</tr>")
    rows.append("</table>")
    return "\n".join(rows)


def picks_table(en=False):
    rows = ["| Goal | Start with |" if en else "| 想做什么 | 先看这几个 |", "| --- | --- |"]
    for pk in picks:
        links = [link(BYREPO[r], en) for r in pk["projects"] if r in BYREPO]
        rows.append(f"| {pk.get('goal_en', pk['goal']) if en else pk['goal']} | {' · '.join(links)} |")
    return "\n".join(rows)


def relations_section():
    parts = [
        f"[![关系图谱](assets/graph.png)]({page_url('graph-sec')})",
        "",
        f"<sub>点图打开[可交互的关系图谱]({page_url('graph-sec')})：箭头从源头指向从它演化出来的项目，点线是同类、常搭配和同一作者；可以拖动、缩放、切换「演化树」卡片视图，点项目看完整演化链。</sub>",
        "",
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
    agent = sum(1 for p in projects if p.get("agent"))
    niche = len({p["repo"] for s in NICHE for p in in_style(s["key"])})
    return active, agent, niche


def showcase_tool_link(r, it, en=False):
    return link(BYREPO[r], en) if r in BYREPO else f"[{it.get('names', {}).get(r, r)}](https://github.com/{r})"


def showcase_tools(it):
    """作品用到的工具：优先用 tools，否则从 breakdown 里按出现顺序去重。"""
    if it.get("tools"):
        return it["tools"]
    return list(dict.fromkeys(r for row in it.get("breakdown", []) for r in row["tools"]))


def showcase_style_cell(row, en=False):
    s = row.get("style")
    if s in SMAP:
        return f"[{SMAP[s]['en' if en else 'name']}](#{s})"
    return row.get("style_name_en" if en else "style_name", "")


def showcase_breakdown_md(it, en=False):
    rows = it.get("breakdown")
    if not rows:
        return []
    title = it.get("breakdown_title_en" if en else "breakdown_title") or ("Tools used" if en else "用到的工具")
    head = "| Style | Tools | At | How it's used |" if en else "| 画风 | 工具 | 片中位置 | 这段怎么做的 |"
    out = [f"<details><summary>{title}</summary>", "", head, "| --- | --- | --- | --- |"]
    prev = None
    for row in rows:
        key = row.get("style") or row.get("style_name")
        style = showcase_style_cell(row, en) if key != prev else ""
        prev = key
        at = "Throughout" if en else "全片"
        if row.get("t") is not None:
            at = f"{int(row['t'] // 60):02d}:{int(row['t'] % 60):02d}"
            if it.get("bilibili"):
                at = f"[{at}](https://www.bilibili.com/video/{it['bilibili']}/?t={int(row['t'])})"
        tools = " · ".join(showcase_tool_link(r, it, en) for r in row["tools"])
        out.append(f"| {style} | {tools} | {at} | {cell(row['what_en' if en else 'what'])} |")
    return out + ["", "</details>", ""]


def showcase_md(en=False):
    if not showcase:
        return []
    out = ['<a name="showcase"></a>', "", "## 🎬 Showcase" if en else "## 🎬 作品展示", ""]
    for it in showcase:
        cover = (it.get("readme_cover_en") or it.get("poster_en")) if en else None
        cover = cover or it.get("readme_cover") or it.get("poster")
        watch = page_url("showcase", en)
        title = it.get("title_en", it["title"]) if en else it["title"]
        if cover:
            out += [f'[![{title}]({cover})]({watch})', ""]
        head = f"**{title}**"
        if it.get("author"):
            head += f" · {('by ' if en else '作者：')}" + (f"[{it['author']}]({it['author_url']})" if it.get("author_url") else it["author"])
        out += [head, ""]
        links = [f"[▶ {'Watch the full film, with sound' if en else '在网页版看完整 MV（有声音）'}]({watch})"] + [f"[{l.get('label_en', l['label']) if en else l['label']}]({l['url']})" for l in it.get("links", [])]
        out += [" · ".join(links), ""]
        for key in ("desc", "credits", "note"):
            if it.get(f"{key}_en" if en else key):
                out += [it[f"{key}_en" if en else key], ""]
        tools = [showcase_tool_link(r, it, en) for r in showcase_tools(it)]
        if tools:
            out += [("Built with: " if en else "用到的工具：") + " · ".join(tools), ""]
        if it.get("styles"):
            out += [("Styles: " if en else "画风：") + "、".join(f"[{SMAP[s]['en' if en else 'name']}](#{s})" for s in it["styles"] if s in SMAP), ""]
        out += showcase_breakdown_md(it, en)
    return out


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
            badge("活跃项目", active, "1E8A4B"),
            badge("数据更新", UPDATED, "5B6273"),
        ]), "",
        f"**[🌐 网页版]({page_url()})**<sub>（按画风筛选、搜索、排序，可切换中英文）</sub> · **[🕸️ 关系图谱]({page_url('graph-sec')})**<sub>（可拖动缩放、看演化树）</sub> · **[🎨 画风索引](#index)**", "",
        " · ".join([
            "[画风索引](#index)", "[小众画风区](#niche)", "[关系图谱](#relations)",
            "[收录标准](#rules)", "[全部项目](#all)",
            f"[推荐项目]({REPO_URL}/issues/new/choose)",
        ]), "",
        "</div>", "",
        *showcase_md(),
        "## 这是什么", "",
        "想用代码做一支 MV、一段讲解动画、一个片头，第一个问题往往是「我想要的那种画风，该用什么工具做」。"
        "这里把 GitHub 上用代码做动画、做视频的开源项目按**画风**归类：3B1B 式数学讲解、扁平 MG、着色器迷幻光影、像素复古、ASCII 终端、音乐可视化、二次元 MMD……"
        "先挑画风，再挑工具。一个项目常能做好几种画风，所以会同时出现在几个画风里。", "",
        f"除了 {len(MAIN)} 种主流画风，还有收录小众画风的[小众画风区](#niche)（水墨山水、汉字笔顺、示波器、绘图仪、人工生命……），"
        f"其中 {agent} 个是让 Claude、Opus 等 AI 编程助手写代码出片的技能和作品，也都按画风归在各自的分类里。[关系图谱](#relations)把有关系的项目连在一起，看得出谁从谁演化而来、谁能替换谁。", "",
        '<a name="rules"></a>', "",
        "## 收录标准", "",
        "- **画面必须由代码绘制或渲染。** 用视频生成、图像生成模型出画面的项目不收，用 Blender 等 3D 软件出画面的也不收。个别项目带有可选的生成功能或 Blender 选项，会在说明里注明。",
        "- **主流画风：** GitHub 星数 1000 以上，或近一年内有更新且星数 200 以上。",
        "- **小众画风区：** 门槛放宽到近一年内有更新、星数 20 以上，星数不高但有意思的项目也能被看到。",
        "- **让 Claude / Opus 等 AI 编程助手写代码出片的技能和作品：** 照样按画风归类，门槛放宽到近一年内有更新、星数 50 以上。",
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
        "## 关系图谱", "",
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
        "- [awesome-demoscene](https://github.com/psykon/awesome-demoscene)：Demoscene 的工具、代码和资料。",
        "- [awesome-glsl](https://github.com/vanrez-nez/awesome-glsl)：学习 GLSL 着色器的资源合集。",
        "- [Awesome-Unity-Shader](https://github.com/QianMo/Awesome-Unity-Shader)：浅墨整理的炫酷 Unity 着色器合集（中文）。", "",
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
        "本仓库的整理内容以 [CC0 1.0](LICENSE) 发布，可以自由使用。`docs/showcase/` 里的作品（视频、封面）版权归各自作者，不在 CC0 范围内。各项目的许可证以其仓库为准，商用前请自行核对。", "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- README (English)

def en_desc(p):
    return p.get("desc_en") or p.get("gh_desc") or p["desc"]


def en_style_table(key):
    rows = ["| Project | Stars | Status | Language | Description |", "| --- | ---: | :---: | --- | --- |"]
    for p in in_style(key):
        emoji, _, state = status(p)
        others = [SMAP[t]["en"] for t in p["tags"] if t != key]
        extra = f"Good for: {p.get('use_en') or p['use']}"
        if others:
            extra += " · Also in: " + ", ".join(others)
        desc = cell(en_desc(p)) + f"<br><sub>{cell(extra)}</sub>"
        if p.get("note"):
            desc += f"<br><sub>⚠️ {cell(p.get('note_en') or p['note'])}</sub>"
        rows.append(f"| {link(p, True)} | {fmt_stars(p['stars'])} | {emoji} {state.capitalize()} | {cell(p.get('lang_en') or p['lang'])} | {desc} |")
    return "\n".join(rows)


def en_style_section(s):
    return [
        f'<a name="{s["key"]}"></a>', "",
        f"### {s['en']}", "",
        f'<img src="{swatch(s["key"], True)}" alt="{s["en"]} sample" width="240" align="right">', "",
        f"> {s.get('look_en') or s['look']}", "",
        f"{len(in_style(s['key']))} projects, sorted by stars.", "",
        '<br clear="right">', "",
        en_style_table(s["key"]), "",
        "<sub>[↑ Back to the style index](#index)</sub>", "",
    ]


def en_relations_section():
    graph = "assets/graph.en.png" if (ROOT / "assets" / "graph.en.png").exists() else "assets/graph.png"
    parts = [
        f"[![Relationship graph]({graph})]({page_url('graph-sec', True)})",
        "",
        f"<sub>Click the image for the [interactive graph]({page_url('graph-sec', True)}). Arrows point from a source to what grew out of it, and dotted lines mean similar, often paired, or same author. You can drag, zoom, switch to the Family tree card view, and click a project to see its full lineage.</sub>",
        "",
        f"{len(relations)} relationships. Looking to switch tools? See Alternative. Want more features? See Plugin / extension and Built on.",
        "",
    ]
    for t in rel_data["types"]:
        rows = [r for r in relations if r["type"] == t["key"]]
        if not rows:
            continue
        name = t.get("name_en") or t["name"]
        parts += [f"### {name}", "", f"<sub>{t.get('desc_en') or t['desc']}</sub>", "",
                  "| Project | Relation | Project | Note |", "| --- | :---: | --- | --- |"]
        for r in rows:
            parts.append(f"| {link(BYREPO[r['from']], True)} | {name} | {link(BYREPO[r['to']], True)} | {cell(r.get('note_en') or r.get('note', ''))} |")
        parts.append("")
    return "\n".join(parts)


def en_all_table():
    rows = ["| Project | Stars | Styles | Status |", "| --- | ---: | --- | :---: |"]
    for p in by_stars(projects):
        tags = ", ".join(f"[{SMAP[t]['en']}](#{t})" for t in p["tags"])
        rows.append(f"| {link(p, True)} | {fmt_stars(p['stars'])} | {tags} | {status(p)[0]} |")
    return "\n".join(rows)


def readme_en():
    active, agent, niche = counts()
    banner = "assets/banner.en.png" if (ROOT / "assets" / "banner.en.png").exists() else "assets/banner.png"
    parts = [
        '<div align="center">', "",
        f'<img src="{banner}" alt="Awesome Code Animation" width="100%">', "",
        "# Awesome Code Animation", "",
        "**Open-source tools for making animations and music videos with code, indexed by visual style.** [Chinese version](README.md)", "",
        " ".join([
            "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
            badge("projects", len(projects), "2E49D4"),
            badge("styles", f"{len(MAIN)}+{len(NICHE)}", "9265D9"),
            badge("active", active, "1E8A4B"),
            badge("updated", UPDATED, "5B6273"),
        ]), "",
        f"**[🌐 Web version]({page_url(en=True)})**<sub> (filter by style, search, sort, switch languages)</sub> · **[🕸️ Relationship graph]({page_url('graph-sec', True)})**<sub> (drag, zoom, family trees)</sub> · **[🎨 Style index](#index)**", "",
        " · ".join([
            "[Style index](#index)", "[Niche styles](#niche)", "[Relationships](#relations)",
            "[Rules](#rules)", "[All projects](#all)",
            f"[Suggest a project]({REPO_URL}/issues/new/choose)",
        ]), "",
        "</div>", "",
        *showcase_md(en=True),
        "## What this is", "",
        "When you want to make a music video, an explainer or an intro with code, the first question is usually which tool makes the look you have in mind. "
        "This list sorts open-source animation and video projects on GitHub by **visual style**: 3Blue1Brown-style math, flat motion graphics, psychedelic shaders, "
        "pixel art, ASCII, music visualizers, anime dance videos and more. Pick a style first, then pick a tool. One project often does several styles, so it can appear under several.", "",
        f"Beyond the {len(MAIN)} main styles, the [niche section](#niche) covers ink-wash landscapes, Chinese stroke-order animation, oscilloscope art, plotters, artificial life and others. "
        f"{agent} entries are skills and films where AI coding agents like Claude or Opus write the code, and they're filed by style like everything else. "
        "The [relationship graph](#relations) links related projects, so you can see what grew out of what and what can replace what.", "",
        '<a name="rules"></a>', "",
        "## What gets listed", "",
        "- **Frames must be drawn or rendered by code.** Projects that make their pictures with video or image generation models aren't listed, and neither are ones that render through Blender or other 3D apps. A few projects have an optional generation feature or Blender option, which is noted on the entry.",
        "- **Main styles:** 1,000+ GitHub stars, or 200+ stars with a push in the last year.",
        "- **Niche styles:** 20+ stars with a push in the last year, so small and interesting projects get seen too.",
        "- **Skills and films where AI coding agents like Claude or Opus write the code:** filed by style as usual, with 50+ stars and a push in the last year.",
        "- **Archived (read-only) repositories aren't listed.** Projects we looked at and left out are recorded in [`data/excluded.json`](data/excluded.json), with reasons in Chinese.",
        "- Status follows the latest push: 🟢 Active (within 6 months) · 🟡 Slowing (within 2 years) · ⚪ Dormant (older; most still work, they just don't get new features).",
        f"- Stars and status refresh every Monday through GitHub Actions, and new candidates are collected into a weekly issue. Data as of {UPDATED}.", "",
        '<a name="picks"></a>', "",
        "## Start from your goal", "",
        picks_table(en=True), "",
        '<a name="index"></a>', "",
        "## Style index", "",
        "Click a picture to jump to that style's table. Every thumbnail is drawn with code, and the code is in [`site/template.html`](site/template.html).", "",
        index_grid(MAIN, en=True), "",
        "### Niche styles", "",
        index_grid(NICHE, en=True), "",
        "## Main styles", "",
    ]
    for s in MAIN:
        parts += en_style_section(s)
    parts += [
        '<a name="niche"></a>', "",
        "## Niche styles", "",
        f"Fewer people use these, but you'd recognize them anywhere. The bar is lower here, at 20+ stars with a push in the last year. {niche} projects in all.", "",
    ]
    for s in NICHE:
        parts += en_style_section(s)
    parts += [
        '<a name="relations"></a>', "",
        "## Relationships", "",
        en_relations_section(),
        '<a name="all"></a>', "",
        "## All projects", "",
        f"<details>\n<summary>Show all {len(projects)} projects, sorted by stars</summary>\n",
        en_all_table(), "", "</details>", "",
        "## Related lists", "",
        "**Creative coding**", "",
        "- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding): tutorials, books and tools for creative coding.",
        "- [awesome-plotters](https://github.com/beardicus/awesome-plotters): code and resources for pen plotters.",
        "- [morphogenesis-resources](https://github.com/jasonwebb/morphogenesis-resources): growing forms with code, including reaction-diffusion, differential growth, slime molds and L-systems.",
        "- [awesome-demoscene](https://github.com/psykon/awesome-demoscene): demoscene tools, code and reading.",
        "- [awesome-glsl](https://github.com/vanrez-nez/awesome-glsl): resources for learning GLSL shaders.",
        "- [Awesome-Unity-Shader](https://github.com/QianMo/Awesome-Unity-Shader): a collection of striking Unity shaders, written up in Chinese.", "",
        "**Claude / Opus galleries**: videos and prompts people made with Claude, good for inspiration. A few works use Blender or video generation models, which these lists usually mark, so check before relying on them.", "",
        "- [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos): videos made with Claude Opus 5.5 and the prompts behind them.",
        "- [opus-video-prompts](https://github.com/joeseesun/opus-video-prompts): Opus 5.5 code-video examples and copyable prompts, in Chinese.",
        "- [awesome-claude-5-5-videos](https://github.com/athemeroy/awesome-claude-5-5-videos): Claude 5.5 video workflows with source and model noted.",
        "- [awesome-opus-5.5-video](https://github.com/zhuyansen/awesome-opus-5.5-video): videos, motion graphics, 3D scenes and games made with Opus 5.5.",
        "- [awesome-claude-video](https://github.com/opusvideo/awesome-claude-video): Claude Opus 5.5 videos and animation.", "",
        "**AI video skills**", "",
        "- [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills): skills that let coding agents make videos. Some call generation models, so its rules differ from this list.",
        "- [awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills): AI skills for motion design.", "",
        "## Contributing", "",
        f"Found a good project? [Suggest it in an issue]({REPO_URL}/issues/new/choose), or edit [`data/projects.json`](data/projects.json) and open a pull request. See [CONTRIBUTING.en.md](CONTRIBUTING.en.md).",
        "Every Monday a search collects new candidates into an issue, and help judging them is welcome.",
        "The READMEs and the web page are generated by `python scripts/build.py`, so please don't edit them by hand.", "",
        "If this list helped you, a ⭐ star helps other people find it.", "",
        "## Star History", "",
        f"[![Star History Chart](https://api.star-history.com/svg?repos={REPO}&type=Date)](https://star-history.com/#{REPO}&Date)", "",
        "## License", "",
        "The curation is released under [CC0 1.0](LICENSE) and is free to use. Works in `docs/showcase/` (videos and posters) stay with their authors and are not covered by CC0. Each project keeps its own license, so check it before commercial use.", "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- web page

def page_showcase(standalone):
    """网页版用的作品数据：docs/ 下的文件改成相对网页的路径；在 artifact 里改用线上地址。"""
    items = []
    for it in showcase:
        x = dict(it)
        x.pop("readme_cover", None)  # 只给 README 用
        x.pop("readme_cover_en", None)
        for k in ("video", "poster", "poster_en"):
            if x.get(k):
                rel = x[k][5:] if x[k].startswith("docs/") else x[k]
                x[k] = rel
        if not standalone:
            # artifact 页面不能加载外站的图片和视频：封面内嵌成 data URI，视频改成去网页版观看
            x.pop("video", None)
            x.pop("bilibili", None)
            for k in ("poster", "poster_en"):
                src = ROOT / it.get(k, "")
                if it.get(k) and src.is_file():
                    import base64, mimetypes
                    mime = mimetypes.guess_type(src.name)[0] or "image/jpeg"
                    x[k] = f"data:{mime};base64," + base64.b64encode(src.read_bytes()).decode()
        x["watch"] = PAGES_URL + "#showcase"
        items.append(x)
    return items


def page(standalone=True):
    tpl = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    def slim(p):
        x = {k: v for k, v in p.items() if k != "gh_desc"}
        # 还没翻译的新项目，英文版先用 GitHub 简介
        if not x.get("desc_en") and p.get("gh_desc") and not CJK.search(p["gh_desc"]):
            x["desc_en"] = p["gh_desc"]
        return x

    body = (tpl.replace("__PROJECTS__", dump([slim(p) for p in projects]))
               .replace("__STYLES__", dump(styles))
               .replace("__PICKS__", dump(picks))
               .replace("__RELATIONS__", dump(relations))
               .replace("__RELTYPES__", dump(rel_data["types"]))
               .replace("__SHOWCASE__", dump(page_showcase(standalone)))
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
    # 英文版只放英文：README.en.md 里出现中文或全角标点就算失败。
    leftovers = [l for l in readme_en().splitlines() if CJK.search(l) or re.search(r"[\uff00-\uffef\u3000-\u303f]", l)]
    if leftovers:
        print("README.en.md 还有中文：", *[l[:100] for l in leftovers[:8]], sep="\n  ", file=sys.stderr)
        if "--check" in sys.argv:
            sys.exit(1)
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
