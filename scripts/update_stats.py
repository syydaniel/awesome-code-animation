#!/usr/bin/env python3
"""从 GitHub 刷新每个项目的星数、最近推送时间、是否归档、许可证和英文简介。

在 GitHub Actions 里会自动带上 GITHUB_TOKEN；本地运行可以先 export GITHUB_TOKEN=...
（不设也能跑，只是匿名请求每小时只有 60 次额度）。
"""
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rules import qualifies  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "data" / "projects.json"
META = ROOT / "data" / "meta.json"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def fetch(repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "awesome-code-animation-updater",
                 **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    today = datetime.date.today()
    problems = []
    for p in projects:
        try:
            info = fetch(p["repo"])
        except urllib.error.HTTPError as e:
            problems.append(f"{p['repo']}: 请求失败（HTTP {e.code}），数据保持不变")
            continue
        if info["full_name"] != p["repo"]:
            problems.append(f"{p['repo']} 已改名为 {info['full_name']}，已自动更新")
            p["repo"] = info["full_name"]
        p["stars"] = info["stargazers_count"]
        p["pushed_at"] = info["pushed_at"][:10]
        p["archived"] = info["archived"]
        p["license"] = (info.get("license") or {}).get("spdx_id")
        p["gh_desc"] = (info.get("description") or "").strip()
        ok, why = qualifies(p["stars"], p["pushed_at"], p["archived"], p["tags"], today)
        if not ok:
            problems.append(f"{p['repo']} 不再满足收录标准（{why}）")
        time.sleep(0.1 if TOKEN else 1.0)

    projects.sort(key=lambda p: -p["stars"])
    PROJECTS.write_text(json.dumps(projects, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    META.write_text(json.dumps({"updated": today.isoformat()}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"已刷新 {len(projects)} 个项目。")
    for line in problems:
        print("注意：" + line)


if __name__ == "__main__":
    sys.exit(main())
