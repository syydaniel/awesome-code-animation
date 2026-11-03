#!/usr/bin/env python3
"""把网页版里用代码画的画风小样图导出成 PNG，并拼出 README 顶部的横幅。

需要 Playwright：
    pip install playwright && playwright install chromium
先运行 scripts/build.py 生成 docs/index.html，再运行本脚本。
如果想用系统里已有的 Chrome，可以设置环境变量 CHROME_PATH。
"""
import base64
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "index.html"
OUT = ROOT / "assets"

BANNER_JS = r"""
() => {
  const S = 2, W = 1280, H = 476;
  const cv = document.createElement('canvas'); cv.width = W * S; cv.height = H * S;
  const c = cv.getContext('2d'); c.scale(S, S);
  c.fillStyle = '#0F1116'; c.fillRect(0, 0, W, H);
  c.textBaseline = 'alphabetic';
  c.fillStyle = '#F2F3F6'; c.font = '900 68px "Noto Serif SC", "Songti SC", serif'; c.fillText('代码画风图鉴', 56, 100);
  c.fillStyle = '#93A5FF'; c.font = '500 22px "IBM Plex Mono", monospace'; c.fillText('Awesome Code Animation', 56, 142);
  c.fillStyle = '#9AA1B0'; c.font = '400 18px "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif';
  c.fillText(`用代码做动画和 MV 的 ${DATA.length} 个开源项目 · 按 ${STYLES.length} 种画风索引`, 56, 176);
  const x0 = 56, y0 = 208, gap = 10, cols = 6, cw = (W - 2 * x0 - gap * (cols - 1)) / cols, ch = cw * 0.4;
  STYLES.forEach((s, i) => {
    const src = document.querySelector(`canvas[data-swatch="${s.key}"]`);
    const x = x0 + (i % cols) * (cw + gap), y = y0 + Math.floor(i / cols) * (ch + gap);
    c.save(); c.beginPath(); c.roundRect(x, y, cw, ch, 8); c.clip();
    c.drawImage(src, x, y, cw, ch);
    c.font = '600 13px "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif';
    const tw = c.measureText(s.name).width;
    c.fillStyle = 'rgba(10,12,16,.72)'; c.fillRect(x, y + ch - 24, tw + 16, 24);
    c.fillStyle = '#F2F3F6'; c.fillText(s.name, x + 8, y + ch - 7.5);
    c.restore();
  });
  return cv.toDataURL('image/png');
}
"""


def save(data_url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(base64.b64decode(data_url.split(",", 1)[1]))


def main():
    with sync_playwright() as p:
        kwargs = {"executable_path": os.environ["CHROME_PATH"]} if os.environ.get("CHROME_PATH") else {}
        browser = p.chromium.launch(**kwargs)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(PAGE.as_uri())
        page.wait_for_function("document.fonts.status === 'loaded'")
        page.evaluate("drawSwatches()")
        keys = page.eval_on_selector_all("canvas[data-swatch]", "els => els.map(e => e.dataset.swatch)")
        for key in keys:
            url = page.eval_on_selector(f'canvas[data-swatch="{key}"]', "el => el.toDataURL('image/png')")
            save(url, OUT / "styles" / f"{key}.png")
        save(page.evaluate(BANNER_JS), OUT / "banner.png")
        browser.close()
    print(f"已导出 {len(keys)} 张画风样图和 assets/banner.png")


if __name__ == "__main__":
    main()
