#!/usr/bin/env python3
"""把网页版里用代码画的画风小样图导出成 PNG，并拼出 README 顶部的横幅。

需要 Playwright：
    pip install playwright && playwright install chromium
先运行 scripts/build.py 生成 docs/index.html，再运行本脚本。
如果想用系统里已有的 Chrome，可以设置环境变量 CHROME_PATH。
"""
import base64
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "index.html"
OUT = ROOT / "assets"
TEXT_SWATCHES = {"type", "liquid"}  # 这两张样图上画了文字，有单独的英文版

BANNER_JS = r"""
() => {
  const S = 2, W = 1280, cols = 8, gap = 8, x0 = 56, y0 = 208;
  const cw = (W - 2 * x0 - gap * (cols - 1)) / cols, ch = cw * 0.4;
  const rows = Math.ceil(STYLES.length / cols), H = y0 + rows * (ch + gap) + 40;
  const cv = document.createElement('canvas'); cv.width = W * S; cv.height = H * S;
  const c = cv.getContext('2d'); c.scale(S, S);
  c.fillStyle = '#0F1116'; c.fillRect(0, 0, W, H);
  c.textBaseline = 'alphabetic';
  c.fillStyle = '#F2F3F6'; c.font = '900 68px "Noto Serif SC", "Songti SC", serif'; c.fillText(EN ? 'Awesome Code Animation' : '代码画风图鉴', 56, 100);
  c.fillStyle = '#93A5FF'; c.font = '500 22px "IBM Plex Mono", monospace'; c.fillText(EN ? 'Indexed by visual style' : 'Awesome Code Animation', 56, 142);
  c.fillStyle = '#9AA1B0'; c.font = '400 18px "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif';
  const nNiche = STYLES.filter(s => s.zone === 'niche').length;
  c.fillText(EN ? `${DATA.length} open-source projects for animation and music videos made with code · ${STYLES.length - nNiche} main styles + ${nNiche} niche styles` : `用代码做动画和 MV 的 ${DATA.length} 个开源项目 · ${STYLES.length - nNiche} 种主流画风 + ${nNiche} 种小众画风 · ${RELS.length} 条项目关系`, 56, 176);
  STYLES.forEach((s, i) => {
    const src = document.querySelector(`canvas[data-swatch="${s.key}"]`);
    const x = x0 + (i % cols) * (cw + gap), y = y0 + Math.floor(i / cols) * (ch + gap);
    c.save(); c.beginPath(); c.roundRect(x, y, cw, ch, 7); c.clip();
    c.drawImage(src, x, y, cw, ch);
    let fs = 11.5;
    do { c.font = `600 ${fs}px "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif`; fs -= .5; } while (c.measureText(s.name).width > cw - 16 && fs > 8);
    const tw = c.measureText(s.name).width;
    c.fillStyle = 'rgba(10,12,16,.74)'; c.fillRect(x, y + ch - 21, tw + 14, 21);
    c.fillStyle = '#F2F3F6'; c.fillText(s.name, x + 7, y + ch - 6.5);
    c.restore();
  });
  return cv.toDataURL('image/png');
}
"""


def save(data_url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(base64.b64decode(data_url.split(",", 1)[1]))


def render(browser, lang):
    """中文导出全部样图、横幅和图谱；英文只导出带文字的样图（*.en.png）、banner.en.png 和 graph.en.png。"""
    suffix = ".en" if lang == "en" else ""
    page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2, color_scheme="light")
    page.goto(PAGE.as_uri() + f"?lang={lang}")
    page.wait_for_function("document.fonts.status === 'loaded'")
    page.evaluate("drawSwatches()")
    keys = page.eval_on_selector_all("canvas[data-swatch]", "els => els.map(e => e.dataset.swatch)")
    for key in keys:
        if lang == "en" and key not in TEXT_SWATCHES:
            continue
        url = page.eval_on_selector(f'canvas[data-swatch="{key}"]', "el => el.toDataURL('image/png')")
        save(url, OUT / "styles" / f"{key}{suffix}.png")
    save(page.evaluate(BANNER_JS), OUT / f"banner{suffix}.png")
    page.wait_for_function("window.__graph !== undefined", timeout=20000)
    page.add_style_tag(content=".graph-zoom,.graph-hint,.graph-tip{display:none!important}")
    page.locator("#graph-stage").screenshot(path=str(OUT / f"graph{suffix}.png"))
    page.close()
    return len(keys)


def main():
    langs = [sys.argv[sys.argv.index("--lang") + 1]] if "--lang" in sys.argv else ["zh", "en"]
    with sync_playwright() as p:
        kwargs = {"executable_path": os.environ["CHROME_PATH"]} if os.environ.get("CHROME_PATH") else {}
        browser = p.chromium.launch(**kwargs)
        counts = [render(browser, lang) for lang in langs]
        browser.close()
    print(f"已导出 {counts[0]} 张画风样图、横幅和关系图谱（{'、'.join(langs)}）")


if __name__ == "__main__":
    main()
