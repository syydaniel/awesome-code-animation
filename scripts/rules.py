"""收录标准，update_stats.py 和 discover.py 共用。"""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES = json.loads((ROOT / "data" / "styles.json").read_text(encoding="utf-8"))
# 小众画风区和 Claude / Opus 区用放宽后的门槛
RELAXED = {s["key"] for s in STYLES if s.get("zone") == "niche"} | {"agent"}

MAIN_MIN_STARS_ANYTIME = 1000
MAIN_MIN_STARS_ACTIVE = 200
RELAXED_MIN_STARS_ACTIVE = 50
ACTIVE_DAYS = 365


def days_since(pushed_at, today=None):
    today = today or datetime.date.today()
    return (today - datetime.date.fromisoformat(pushed_at[:10])).days


def qualifies(stars, pushed_at, archived, tags, today=None):
    """返回 (是否符合, 原因)。"""
    if archived:
        return False, "仓库已归档"
    days = days_since(pushed_at, today)
    if stars >= MAIN_MIN_STARS_ANYTIME:
        return True, ""
    if days <= ACTIVE_DAYS and stars >= MAIN_MIN_STARS_ACTIVE:
        return True, ""
    if set(tags) & RELAXED and days <= ACTIVE_DAYS and stars >= RELAXED_MIN_STARS_ACTIVE:
        return True, ""
    if days > ACTIVE_DAYS:
        return False, f"{stars} 星，{days} 天未更新"
    return False, f"星数 {stars} 未达门槛"
