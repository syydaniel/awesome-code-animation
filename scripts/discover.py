#!/usr/bin/env python3
"""在 GitHub 上搜还没收录的候选项目，整理成一个 Issue（每周更新同一个 Issue）。

只负责「找」，不会自动收录：画面是不是代码渲染、有没有调用生成模型或 Blender，
需要人看过 README 再决定。看过不收的项目请写进 data/excluded.json，以后就不会再出现。

用法：
    python scripts/discover.py            # 输出候选列表（Markdown）
    python scripts/discover.py --issue    # 创建或更新候选 Issue（需要 GITHUB_TOKEN 和 GITHUB_REPOSITORY）
"""
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rules import ACTIVE_DAYS, MAIN_MIN_STARS_ACTIVE, RELAXED_MIN_STARS_ACTIVE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY", "syydaniel/awesome-code-animation")
ISSUE_TITLE = "每周候选项目"
MAX_ROWS = 150

# (搜索条件, 推荐画风, 门槛)。门槛 relaxed 对应小众画风区和 Claude / Opus 区。
QUERIES = [
    ("topic:creative-coding", "gen", "main"),
    ("topic:generative-art -diffusion", "gen", "main"),
    ("topic:motion-graphics", "mg", "main"),
    ("topic:programmatic-video", "short", "main"),
    ("topic:animation-library", "mg", "main"),
    ("topic:remotion", "short", "main"),
    ("topic:manim", "math", "main"),
    ("topic:shaders", "shader", "main"),
    ("topic:glsl", "shader", "main"),
    ("topic:live-coding", "live", "main"),
    ("topic:music-visualizer", "audio", "main"),
    ("topic:audio-visualizer", "audio", "main"),
    ("topic:ascii-art", "ascii", "main"),
    ("topic:pixel-art", "pixel", "main"),
    ("topic:svg-animation", "mg", "main"),
    ("topic:kinetic-typography", "type", "main"),
    ("topic:hyperframes", "agent", "relaxed"),
    ("claude animation in:description", "agent", "relaxed"),
    ("claude video in:description", "agent", "relaxed"),
    ("opus video in:description", "agent", "relaxed"),
    ("\"drawn in code\" in:description", "agent", "relaxed"),
    ("纯代码 视频", "agent", "relaxed"),
    ("代码 动画 skill", "agent", "relaxed"),
    ("topic:pen-plotter", "plotter", "relaxed"),
    ("topic:plotter", "plotter", "relaxed"),
    ("topic:dithering", "dither", "relaxed"),
    ("topic:risograph", "riso", "relaxed"),
    ("topic:oscilloscope music", "scope", "relaxed"),
    ("topic:cellular-automata", "alife", "relaxed"),
    ("topic:artificial-life", "alife", "relaxed"),
    ("topic:procedural-generation", "procgen", "relaxed"),
    ("topic:fractal", "fractal", "relaxed"),
    ("topic:isometric", "iso", "relaxed"),
    ("topic:sci-fi", "scifi", "relaxed"),
    ("topic:demoscene", "demoscene", "relaxed"),
    ("chinese painting procedural", "ink", "relaxed"),
    ("水墨 动画", "ink", "relaxed"),
    ("stroke order animation", "hanzi", "relaxed"),
]

# 描述里出现这些词，多半是在用生成模型出画面，标出来提醒人工检查
WARN = ["stable diffusion", "diffusion", "sora", "veo", "kling", "seedance", "runway", "flux", "midjourney",
        "text-to-video", "image-to-video", "text-to-image", "comfyui", "blender", "生图", "视频模型", "文生视频"]


def api(url, method="GET", body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "awesome-code-animation-discover",
                                          "Content-Type": "application/json",
                                          **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def search(q, min_stars, since):
    full = f"{q} stars:>={min_stars} pushed:>={since} archived:false"
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": full, "sort": "stars", "per_page": 30})
    return api(url).get("items", [])


def main():
    known = {p["repo"].lower() for p in json.loads((ROOT / "data" / "projects.json").read_text(encoding="utf-8"))}
    known |= {e["repo"].lower() for e in json.loads((ROOT / "data" / "excluded.json").read_text(encoding="utf-8"))["excluded"]}
    since = (datetime.date.today() - datetime.timedelta(days=ACTIVE_DAYS)).isoformat()
    found = {}
    for q, style, tier in QUERIES:
        min_stars = MAIN_MIN_STARS_ACTIVE if tier == "main" else RELAXED_MIN_STARS_ACTIVE
        try:
            items = search(q, min_stars, since)
        except Exception as e:  # 搜索偶尔限流，跳过这一条
            print(f"搜索失败：{q}（{e}）", file=sys.stderr)
            items = []
        for it in items:
            key = it["full_name"].lower()
            if key in known:
                continue
            entry = found.setdefault(key, {"repo": it["full_name"], "stars": it["stargazers_count"],
                                           "pushed": it["pushed_at"][:10], "desc": (it.get("description") or "").strip(),
                                           "styles": set()})
            entry["styles"].add(style)
        time.sleep(2.5 if not TOKEN else 1.2)

    # 被多个搜索命中、或属于小众 / Claude 区的排在前面，再按星数排
    relaxed = {s for _, s, tier in QUERIES if tier == "relaxed"}
    cands = sorted(found.values(), key=lambda e: (-len(e["styles"]), -bool(e["styles"] & relaxed), -e["stars"]))
    total = len(cands)
    cands = cands[:MAX_ROWS]
    lines = [
        f"自动整理于 {datetime.date.today().isoformat()}，共 {total} 个还没收录的候选"
        + (f"，这里列出最相关的 {len(cands)} 个。" if total > len(cands) else "。"),
        "",
        "收录前请先看 README，确认画面由代码绘制或渲染，没有用视频或图像生成模型，也不靠 Blender 出画面。"
        "要收录的：按 CONTRIBUTING.md 加进 `data/projects.json`；确认不收的：写进 `data/excluded.json`，下周就不会再出现。",
        "",
        "| 收录？ | 项目 | 星数 | 最近提交 | 可能的画风 | 简介 |",
        "| :---: | --- | ---: | --- | --- | --- |",
    ]
    for e in cands:
        low = e["desc"].lower()
        warn = " ⚠️ 可能用到生成模型或 Blender" if any(w in low for w in WARN) else ""
        desc = e["desc"].replace("|", "\\|")[:140]
        lines.append(f"| ☐ | [{e['repo']}](https://github.com/{e['repo']}) | {e['stars']} | {e['pushed']} | {'、'.join(sorted(e['styles']))} | {desc}{warn} |")
    body = "\n".join(lines)

    if "--issue" not in sys.argv:
        print(body)
        return
    if not TOKEN:
        sys.exit("需要 GITHUB_TOKEN 才能创建 Issue")
    base = f"https://api.github.com/repos/{REPO}/issues"
    open_issues = api(base + "?state=open&per_page=100")
    existing = next((i for i in open_issues if i["title"] == ISSUE_TITLE and "pull_request" not in i), None)
    if existing:
        api(f"{base}/{existing['number']}", "PATCH", {"body": body})
        print(f"已更新 Issue #{existing['number']}，{len(cands)} 个候选")
    else:
        created = api(base, "POST", {"title": ISSUE_TITLE, "body": body})
        print(f"已创建 Issue #{created['number']}，{len(cands)} 个候选")


if __name__ == "__main__":
    main()
