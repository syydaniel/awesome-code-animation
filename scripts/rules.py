"""收录标准，update_stats.py 和 discover.py 共用。"""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES = json.loads((ROOT / "data" / "styles.json").read_text(encoding="utf-8"))
# 小众画风区用放宽后的门槛；让 Claude / Opus 等 AI 编程助手写代码出片的项目（agent 标记）也放宽
NICHE = {s["key"] for s in STYLES if s.get("zone") == "niche"}

MAIN_MIN_STARS_ANYTIME = 1000
MAIN_MIN_STARS_ACTIVE = 200
NICHE_MIN_STARS_ACTIVE = 20
AGENT_MIN_STARS_ACTIVE = 50
ACTIVE_DAYS = 365


def days_since(pushed_at, today=None):
    today = today or datetime.date.today()
    return (today - datetime.date.fromisoformat(pushed_at[:10])).days


def qualifies(stars, pushed_at, archived, tags, agent=False, today=None):
    """返回 (是否符合, 原因)。"""
    if archived:
        return False, "仓库已归档"
    days = days_since(pushed_at, today)
    if stars >= MAIN_MIN_STARS_ANYTIME:
        return True, ""
    if days <= ACTIVE_DAYS and stars >= MAIN_MIN_STARS_ACTIVE:
        return True, ""
    if set(tags) & NICHE and days <= ACTIVE_DAYS and stars >= NICHE_MIN_STARS_ACTIVE:
        return True, ""
    if agent and days <= ACTIVE_DAYS and stars >= AGENT_MIN_STARS_ACTIVE:
        return True, ""
    if days > ACTIVE_DAYS:
        return False, f"{stars} 星，{days} 天未更新"
    return False, f"星数 {stars} 未达门槛"
