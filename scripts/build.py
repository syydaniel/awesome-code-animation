#!/usr/bin/env python3
"""根据 data/ 里的数据生成 README.md 和 docs/index.html。

用法：
    python scripts/build.py           # 生成文件
    python scripts/build.py --check   # 只检查生成结果是否和仓库里的一致（CI 用）
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
UPDATED = meta["updated"]
SNAP = datetime.date.fromisoformat(UPDATED)
SMAP = {s["key"]: s for s in styles}
BYREPO = {p["repo"]: p for p in projects}

for p in projects:
    for t in p["tags"]:
        if t not in SMAP:
            sys.exit(f"未知画风 {t!r}（{p['repo']}），请先在 data/styles.json 里定义")


def fmt_stars(n):
    if n >= 100_000:
        return f"{n / 1000:.0f}k"
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def status(p):
    if p.get("archived"):
        return "⚪", "已归档"
    days = (SNAP - datetime.date.fromisoformat(p["pushed_at"])).days
    if days <= 183:
        return "🟢", "活跃"
    if days <= 730:
        return "🟡", "放缓"
    return "⚪", "停更"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def badge(label, value, color):
    return f"![{label}](https://img.shields.io/badge/{quote(label)}-{quote(str(value).replace('-', '--'))}-{color})"


def by_stars(items):
    return sorted(items, key=lambda p: -p["stars"])


def style_table(key):
    rows = [
        "| 项目 | 星数 | 状态 | 写法 | 说明 |",
        "| --- | ---: | :---: | --- | --- |",
    ]
    for p in by_stars([p for p in projects if key in p["tags"]]):
        emoji, label = status(p)
        others = [SMAP[t]["name"] for t in p["tags"] if t != key]
        extra = f"适合：{p['use']}"
        if others:
            extra += " · 也在：" + "、".join(others)
        desc = cell(p["desc"]) + f"<br><sub>{cell(extra)}</sub>"
        if p.get("note"):
            desc += f"<br><sub>⚠️ {cell(p['note'])}</sub>"
        rows.append(
            f"| [{cell(p['name'])}](https://github.com/{p['repo']}) | {fmt_stars(p['stars'])} "
            f"| {emoji} {label} | {cell(p['lang'])} | {desc} |"
        )
    return "\n".join(rows)


def index_grid(cols=3):
    cells = []
    for s in styles:
        n = sum(1 for p in projects if s["key"] in p["tags"])
        cells.append(
            f'<td align="center" width="33%"><a href="#{s["key"]}">'
            f'<img src="assets/styles/{s["key"]}.png" alt="{s["name"]}" width="260"></a><br>'
            f'<b><a href="#{s["key"]}">{s["name"]}</a></b><br>'
            f'<sub>{s["en"]} · {n} 个项目</sub></td>'
        )
    rows = ["<table>"]
    for i in range(0, len(cells), cols):
        rows.append("<tr>" + "".join(cells[i:i + cols]) + "</tr>")
    rows.append("</table>")
    return "\n".join(rows)


def picks_table():
    rows = ["| 想做什么 | 先看这几个 |", "| --- | --- |"]
    for pk in picks:
        links = [f"[{BYREPO[r]['name']}](https://github.com/{r})" for r in pk["projects"] if r in BYREPO]
        rows.append(f"| {pk['goal']} | {' · '.join(links)} |")
    return "\n".join(rows)


def all_table():
    rows = ["| 项目 | 星数 | 画风 | 状态 |", "| --- | ---: | --- | :---: |"]
    for p in by_stars(projects):
        emoji, label = status(p)
        tags = "、".join(f"[{SMAP[t]['name']}](#{t})" for t in p["tags"])
        rows.append(f"| [{cell(p['name'])}](https://github.com/{p['repo']}) | {fmt_stars(p['stars'])} | {tags} | {emoji} |")
    return "\n".join(rows)


def readme():
    active = sum(1 for p in projects if status(p)[1] == "活跃")
    parts = [
        '<div align="center">',
        "",
        '<img src="assets/banner.png" alt="代码画风图鉴 · Awesome Code Animation" width="100%">',
        "",
        "# 代码画风图鉴 · Awesome Code Animation",
        "",
        "**用代码画动画、做 MV 的开源项目合集，按画风索引。**",
        "",
        "A curated list of open-source tools for making animations and music videos **with code**, indexed by visual style.",
        "",
        " ".join([
            "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
            badge("项目", len(projects), "2E49D4"),
            badge("画风", len(styles), "9265D9"),
            badge("活跃项目", active, "1E8A4B"),
            badge("数据更新", UPDATED, "5B6273"),
        ]),
        "",
        f"**[🔎 网页版：可按画风筛选、搜索、排序]({PAGES_URL})**",
        "",
        f"[画风索引](#index) · [按目的先挑](#picks) · [收录标准](#rules) · [全部项目](#all) · [推荐项目]({REPO_URL}/issues/new/choose)",
        "",
        "</div>",
        "",
        "## 这是什么",
        "",
        "想用代码做一支 MV、一段讲解动画、一个片头，第一个问题往往是「我想要的那种画风，该用什么工具做」。"
        "这里把 GitHub 上用代码做动画、做视频的开源项目按**画风**归类：3B1B 式数学讲解、扁平 MG、着色器迷幻光影、像素复古、ASCII 终端、音乐可视化、二次元 MMD……"
        "先挑画风，再挑工具。一个项目常能做好几种画风，所以会同时出现在几个画风里。",
        "",
        '<a name="rules"></a>',
        "",
        "## 收录标准",
        "",
        "- **画面由代码绘制或渲染。** 用视频生成、图像生成模型出画面的项目不收。AI 只负责写代码、画面仍由代码渲染的，归在「AI 写代码出片」。",
        "- **GitHub 星数 1000 以上，或近一年内仍有更新且星数 200 以上。**",
        "- **已归档（只读）的仓库不收。**",
        "- 状态按仓库最近一次推送计算：🟢 活跃（半年内）· 🟡 放缓（两年内）· ⚪ 停更（超过两年，多数仍能用，只是不再加新功能）。",
        f"- 星数和状态每周一由 GitHub Actions 自动刷新，当前数据更新于 {UPDATED}。",
        "",
        '<a name="picks"></a>',
        "",
        "## 按目的先挑",
        "",
        picks_table(),
        "",
        '<a name="index"></a>',
        "",
        "## 画风索引",
        "",
        "点图片跳到对应画风的项目表。每张小样图都是用代码画出来的，代码在 [`site/template.html`](site/template.html) 里。",
        "",
        index_grid(),
        "",
    ]
    for s in styles:
        n = sum(1 for p in projects if s["key"] in p["tags"])
        words = [w for w in s["en"].replace(",", " ").replace("&", " ").lower().split() if len(w) > 1]
        title = s["name"] if any(w in s["name"].lower() for w in words) else f"{s['name']} · {s['en']}"
        parts += [
            f'<a name="{s["key"]}"></a>',
            "",
            f"## {title}",
            "",
            f'<img src="assets/styles/{s["key"]}.png" alt="{s["name"]}样图" width="240" align="right">',
            "",
            f"> {s['look']}",
            "",
            f"共 {n} 个项目，按星数排序。",
            "",
            '<br clear="right">',
            "",
            style_table(s["key"]),
            "",
            "<sub>[↑ 回到画风索引](#index)</sub>",
            "",
        ]
    parts += [
        '<a name="all"></a>',
        "",
        "## 全部项目",
        "",
        f"<details>\n<summary>展开全部 {len(projects)} 个项目（按星数排序）</summary>\n",
        all_table(),
        "",
        "</details>",
        "",
        "## 相关合集",
        "",
        "- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding)：创意编程资源大全，覆盖教程、书籍和工具（英文）。",
        "- [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)：用 Claude Opus 5.5 写代码做出的视频，附提示词。",
        "- [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills)：让编程助手做视频的技能合集。其中部分项目会调用生成模型，和本仓库的收录标准不同。",
        "",
        "## 参与贡献",
        "",
        f"发现好项目？欢迎[提 Issue 推荐]({REPO_URL}/issues/new/choose)，或者直接修改 [`data/projects.json`](data/projects.json) 提 Pull Request，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。",
        "README 和网页版都由 `python scripts/build.py` 从数据文件自动生成，请不要直接改 README。",
        "",
        "如果这份合集帮到了你，点个 ⭐ Star 能让更多人找到它。",
        "",
        "## Star History",
        "",
        f"[![Star History Chart](https://api.star-history.com/svg?repos={REPO}&type=Date)](https://star-history.com/#{REPO}&Date)",
        "",
        "## 许可",
        "",
        "本仓库的整理内容以 [CC0 1.0](LICENSE) 发布，可以自由使用。各项目的许可证以其仓库为准，商用前请自行核对。",
        "",
    ]
    return "\n".join(parts)


def page(standalone=True):
    tpl = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    body = (tpl.replace("__PROJECTS__", dump(projects))
               .replace("__STYLES__", dump(styles))
               .replace("__PICKS__", dump(picks))
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
    outputs = {ROOT / "README.md": readme(), ROOT / "docs" / "index.html": page()}
    if "--artifact" in sys.argv:
        print(page(standalone=False))
        return
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
    print(f"已生成 README.md 和 docs/index.html：{len(projects)} 个项目，{len(styles)} 种画风。")


if __name__ == "__main__":
    main()
