/* 3D 画风入口 · three.js
 *
 * 两层画风转盘：上层是主流画风，下层是小众画风。每块面板上的画面，就是下面「画风索引」里那张用代码画的小样图。
 * 拖动转盘，点一块面板（或底部的画风按钮）进入这种画风的展厅：转盘把它转到正面、镜头推近，
 * data/featured.json 里这种画风的精品项目排成一道卡片廊飞出来，旁边（手机上是底部）列出同样的项目。
 *
 * 「最新更新」窗口：桌面上在右上角，窄屏上是底部按钮条最前面的「最新」，网址带 #latest 时直接打开。
 * 打开后展厅换成两个列表：「新收录」（scripts/build.py 按 projects.json 的 added 挑出最近几批）和「最近有提交」，
 * 卡片廊停在两圈转盘之间，转盘调暗继续慢慢转。新收录可能有几十个，卡片只在翻到附近时才画。
 *
 * 性能：three.js 只在首屏可见时才按需加载；面板小样图分帧慢慢画；离开首屏或切到别的标签页就停止渲染；
 * 没有动画在跑时也停下来。系统开了「减少动态效果」时转盘不自动转，镜头直接切换。
 * 没有 WebGL 2 或 three.js 加载失败时，退回到平铺的小样图墙，展厅照样能用。
 *
 * 这个文件由 scripts/build.py 原样嵌进 docs/index.html，数据和工具函数从页面主脚本的 window.ACA 拿。
 */
const A = window.ACA;
const root = document.getElementById('gateway');
if (A && root) gateway();

function gateway() {
  const { REPO_URL, DATA, MAIN, NICHE, SMAP, BYREPO, FEATURED, LATEST, EN, L, esc, fmtStars, status, swatchCanvas, TEXT_SWATCHES } = A;
  const stage = document.getElementById('gw-stage');
  const hall = document.getElementById('gw-hall');
  const rail = document.getElementById('gw-rail');
  const tip = document.getElementById('gw-tip');
  const news = document.getElementById('gw-news');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const THREE_URL = 'https://cdn.jsdelivr.net/npm/three@0.178.0/build/three.module.min.js';
  const ORDER = [...MAIN, ...NICHE];
  const COUNT = {};
  DATA.forEach(p => p.tags.forEach(t => { COUNT[t] = (COUNT[t] || 0) + 1; }));
  const picksOf = key => (FEATURED[key] || []).map(r => BYREPO[r]).filter(Boolean);
  // 「最新更新」窗口借用展厅的位置，用一个不会和画风撞名的 key
  const LKEY = '__latest', NEW_C = '#7CF0B0';
  const latestOf = t => ((LATEST && LATEST[t]) || []).map(r => BYREPO[r]).filter(Boolean);
  const BATCH0 = LATEST && LATEST.batches[0];
  let tab = BATCH0 ? 'new' : 'recent';
  const cardsOf = key => key === LKEY ? latestOf(tab) : picksOf(key);
  const day = d => {
    const [, m, dd] = d.split('-').map(Number);
    return EN ? new Date(Date.UTC(2000, m - 1, dd)).toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' }) : `${m}月${dd}日`;
  };
  const SERIF = '"Noto Serif SC", "Songti SC", "STSong", "SimSun", serif';
  const SANS = 'system-ui, -apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif';
  const MONO = '"IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace';
  let world = null, current = null;

  /* ---------- 底部的画风按钮：键盘和读屏都靠它，3D 没加载出来也能用 ---------- */
  const latestChip = LATEST ? `<button type="button" class="gw-chip gw-chip-new" data-gw="${LKEY}" aria-pressed="false"><i style="background:${NEW_C}"></i>${L('最新', 'Latest')}${BATCH0 ? `<b>+${BATCH0.n}</b>` : ''}</button>` : '';
  rail.innerHTML = latestChip + [[MAIN, L('主流', 'Main')], [NICHE, L('小众', 'Niche')]].map(([group, label]) =>
    `<span class="gw-rail-k">${label}</span>` + group.map(s =>
      `<button type="button" class="gw-chip" data-gw="${s.key}" aria-pressed="false"><i style="background:${s.color}"></i>${esc(s.name)}</button>`).join('')).join('');
  rail.addEventListener('click', e => { const b = e.target.closest('[data-gw]'); if (b) open(b.dataset.gw); });
  // 指到或用 Tab 走到某个按钮时，转盘先把这种画风转到正面给你看
  rail.addEventListener('pointerover', e => { const b = e.target.closest('[data-gw]'); if (b && world) world.peek(b.dataset.gw); });
  rail.addEventListener('pointerleave', () => { if (world) world.peek(null); });
  rail.addEventListener('focusin', e => { const b = e.target.closest('[data-gw]'); if (b && world) world.peek(b.dataset.gw); });
  rail.addEventListener('focusout', e => { if (world && !rail.contains(e.relatedTarget)) world.peek(null); });

  /* ---------- 右上角的「最新更新」小窗口 ---------- */
  if (news && LATEST) {
    const top3 = (BATCH0 ? latestOf('new').filter(p => p.added === BATCH0.date) : latestOf('recent')).slice(0, 3);
    news.innerHTML = `<div class="gw-news-h"><i class="gw-pulse"></i><span>${L('最新更新', 'Latest')}</span><time datetime="${BATCH0 ? BATCH0.date : LATEST.date}">${day(BATCH0 ? BATCH0.date : LATEST.date)}</time></div>
      ${BATCH0 ? `<p class="gw-news-n"><b>+${BATCH0.n}</b><span>${L('个新收录的项目', 'new projects added')}</span></p>`
        : `<p class="gw-news-n"><b>${LATEST.recent.length}</b><span>${L('个项目最近有提交', 'projects with recent commits')}</span></p>`}
      <ul>${top3.map(p => `<li><i style="background:${SMAP[p.tags[0]].color}"></i><span>${esc(p.name)}</span><em>★ ${fmtStars(p.stars)}</em></li>`).join('')}</ul>
      <div class="gw-news-f"><button type="button" class="gw-news-go">${L('打开窗口 →', 'Open →')}</button><a href="${REPO_URL}" target="_blank" rel="noopener">${L('★ 点个 Star 收藏', '★ Star to keep it handy')}</a></div>`;
    news.hidden = false;
    news.addEventListener('click', e => { if (!e.target.closest('a')) open(LKEY); });
  }

  /* ---------- 展厅（HTML 部分） ---------- */
  const starCta = () => `<a class="gw-star-cta" href="${REPO_URL}" target="_blank" rel="noopener"><b>${L('★ 觉得有用？去 GitHub 点个 Star', '★ Find this useful? Star it on GitHub')}</b><span>${L('每周一刷新数据、不定期收录新项目。点 Star 收藏起来方便回来看，也能让更多人找到这份合集。', 'Data refreshes every Monday and new projects land regularly. A star keeps the list handy and helps more people find it.')}</span></a>`;
  function latestHtml() {
    const list = latestOf(tab), multi = LATEST.batches.length > 1;
    let lastDay = null;
    const items = list.map((p, k) => {
      const d = tab === 'new' ? p.added : p.pushed_at;
      const b = tab === 'new' && multi && d !== lastDay ? LATEST.batches.find(x => x.date === d) : null;
      lastDay = d;
      const head = b ? `<li class="gw-day">${L(`${day(d)} · 新收录 ${b.n} 个`, `${day(d)} · ${b.n} added`)}</li>` : '';
      const styles = p.tags.map(t => `<span><i class="gw-dot" style="background:${SMAP[t].color}"></i>${esc(SMAP[t].name)}</span>`).join(' · ');
      const when = tab === 'new' ? L(`${day(d)}收录`, `Added ${day(d)}`) : L(`${day(d)}有提交`, `Pushed ${day(d)}`);
      return head + `<li data-k="${k}">
        <div class="gw-pick-top"><span class="gw-n">${String(k + 1).padStart(2, '0')}</span><a href="https://github.com/${esc(p.repo)}" target="_blank" rel="noopener">${esc(p.name)}</a><span class="gw-star">★ ${fmtStars(p.stars)}</span></div>
        <p class="gw-desc">${esc(p.desc)}</p>
        <p class="gw-meta">${styles} · ${when}</p>
      </li>`;
    }).join('');
    const intro = tab === 'new'
      ? L(`${day(BATCH0.date)}新收录 ${BATCH0.n} 个项目${multi ? '，往下是更早的几批' : ''}，同一批按星数排。往下滚、左右拖动卡片，或者按 ← → 键翻看。`,
          `${BATCH0.n} projects added on ${day(BATCH0.date)}${multi ? ', then earlier batches' : ''}, sorted by stars within each batch. Scroll, drag the cards or press ← → to browse.`)
      : L(`最近有代码提交的 ${list.length} 个活跃项目，最新的在前。星数和提交时间每周一刷新，这次是 ${day(LATEST.date)}。`,
          `The ${list.length} active projects with the most recent commits, newest first. Stars and commit dates refresh every Monday; this data is from ${day(LATEST.date)}.`);
    const tabs = (BATCH0 ? `<button type="button" data-tab="new" aria-pressed="${tab === 'new'}">${L('新收录', 'New')}<span>${LATEST.new.length}</span></button>` : '')
      + `<button type="button" data-tab="recent" aria-pressed="${tab === 'recent'}">${L('最近有提交', 'Recent commits')}<span>${LATEST.recent.length}</span></button>`;
    return `<div class="gw-hall-bar"><p class="gw-k">${L('数据更新于', 'Data as of')} ${LATEST.date}</p>
        <div class="gw-nav"><button type="button" data-close aria-label="${L('关闭窗口', 'Close')}">✕</button></div></div>
      <h2 tabindex="-1"><i style="background:${NEW_C};color:${NEW_C}"></i>${L('最新更新', 'Latest updates')}</h2>
      <div class="gw-tabs" role="group" aria-label="${L('列表', 'List')}">${tabs}</div>
      <p class="gw-look">${intro}</p>
      <ol class="gw-picks gw-latest">${items}</ol>
      <button type="button" class="gw-all" data-latest-all>${tab === 'new' ? L('在总表里按收录时间看 →', 'Sort the table by date added →') : L('在总表里按最近提交看 →', 'Sort the table by latest push →')}</button>
      ${starCta()}`;
  }
  function hallHtml(key) {
    if (key === LKEY) return latestHtml();
    const s = SMAP[key], ps = picksOf(key), i = ORDER.indexOf(s), n = COUNT[key] || 0;
    const prev = ORDER[(i - 1 + ORDER.length) % ORDER.length], next = ORDER[(i + 1) % ORDER.length];
    const items = ps.map((p, k) => {
      const [cls, lbl] = status(p);
      return `<li data-k="${k}">
        <div class="gw-pick-top"><span class="gw-n">${String(k + 1).padStart(2, '0')}</span><a href="https://github.com/${esc(p.repo)}" target="_blank" rel="noopener">${esc(p.name)}</a><span class="gw-star">★ ${fmtStars(p.stars)}</span></div>
        <p class="gw-desc">${esc(p.desc)}</p>
        <p class="gw-meta"><span class="st ${cls}"><i></i>${lbl}</span> · ${esc(p.lang)}</p>
      </li>`;
    }).join('');
    return `<div class="gw-hall-bar"><p class="gw-k">${s.zone === 'niche' ? L('小众画风', 'Niche style') : L('主流画风', 'Main style')} · ${String(i + 1).padStart(2, '0')} / ${ORDER.length}</p>
        <div class="gw-nav"><button type="button" data-go="${prev.key}" aria-label="${esc(L('上一个画风：', 'Previous style: ') + prev.name)}">‹</button><button type="button" data-go="${next.key}" aria-label="${esc(L('下一个画风：', 'Next style: ') + next.name)}">›</button><button type="button" data-close aria-label="${L('关闭展厅', 'Close gallery')}">✕</button></div></div>
      <h2 tabindex="-1"><i style="background:${s.color};color:${s.color}"></i>${esc(s.name)}</h2>
      <p class="gw-look">${esc(s.look)}</p>
      <p class="gw-k">${L(`精品 ${ps.length} 个 · 这种画风共收录 ${n} 个`, `${ps.length} picks · ${n} listed in this style`)}</p>
      <ol class="gw-picks">${items}</ol>
      <button type="button" class="gw-all" data-all="${key}">${L(`在总表里看全部 ${n} 个 →`, `See all ${n} in the table →`)}</button>
      ${starCta()}`;
  }
  // 标出列表里对应正中那张卡片的一项；翻卡片（拖动、按键、点侧面的卡）时把它滚进视野，鼠标在列表上指着时不滚
  let pickK = 0;
  function markPick(k, scroll) {
    pickK = k;
    hall.querySelectorAll('.gw-picks li[data-k]').forEach(li => {
      const on = +li.dataset.k === k;
      li.classList.toggle('on', on);
      if (on && scroll) {
        const hr = hall.getBoundingClientRect(), lr = li.getBoundingClientRect();
        if (lr.top < hr.top + 10) hall.scrollTop += lr.top - hr.top - 10;
        else if (lr.bottom > hr.bottom - 10) hall.scrollTop += lr.bottom - hr.bottom + 10;
      }
    });
  }
  function centerChip(key) {
    const chip = rail.querySelector(`[data-gw="${key}"]`); if (!chip) return;
    const rr = rail.getBoundingClientRect(), cr = chip.getBoundingClientRect();
    rail.scrollTo({ left: rail.scrollLeft + (cr.left - rr.left) - (rr.width - cr.width) / 2, behavior: reduce ? 'auto' : 'smooth' });
  }
  function open(key, { focus = true } = {}) {
    if (!SMAP[key] && !(key === LKEY && LATEST)) return;
    current = key;
    hall.innerHTML = hallHtml(key);
    hall.hidden = false;
    hall.scrollTop = 0;
    root.classList.add('gw-open');
    rail.querySelectorAll('[data-gw]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.gw === key)));
    centerChip(key);
    markPick(0);
    hideTip();
    if (world) world.focus(key);
    if (focus) hall.querySelector('h2').focus({ preventScroll: true });
  }
  function close() {
    if (!current) return;
    const key = current, hadFocus = hall.contains(document.activeElement);
    current = null;
    hall.hidden = true;
    root.classList.remove('gw-open');
    rail.querySelectorAll('[data-gw]').forEach(b => b.setAttribute('aria-pressed', 'false'));
    if (world) world.focus(null);
    if (hadFocus) { const chip = rail.querySelector(`[data-gw="${key}"]`); if (chip) chip.focus({ preventScroll: true }); }
    if (key === LKEY && location.hash === '#latest') history.replaceState(null, '', location.pathname + location.search);
  }
  hall.addEventListener('click', e => {
    if (e.target.closest('[data-close]')) { close(); return; }
    const tb = e.target.closest('[data-tab]');
    if (tb) {
      if (tb.dataset.tab === tab) return;
      tab = tb.dataset.tab;
      hall.innerHTML = latestHtml();
      hall.scrollTop = 0;
      markPick(0);
      if (world) world.focus(LKEY);
      hall.querySelector(`[data-tab="${tab}"]`).focus({ preventScroll: true });
      return;
    }
    if (e.target.closest('[data-latest-all]')) { const by = tab === 'new' ? 'added' : 'pushed'; close(); A.showLatest(by); return; }
    const go = e.target.closest('[data-go]'); if (go) { open(go.dataset.go, { focus: false }); return; }
    const all = e.target.closest('[data-all]'); if (all) { close(); A.showStyle(all.dataset.all); }
  });
  const pickFromEvent = e => { const li = e.target.closest('li[data-k]'); if (li && world) world.front(+li.dataset.k); else if (li) markPick(+li.dataset.k); };
  hall.addEventListener('pointerover', pickFromEvent);
  hall.addEventListener('focusin', pickFromEvent);
  document.addEventListener('keydown', e => {
    if (!current || e.defaultPrevented || (e.target.closest && e.target.closest('input, textarea, select'))) return;
    if (root.getBoundingClientRect().bottom < 120) return;
    if (e.key === 'Escape') { close(); return; }
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
      if (current === LKEY) {
        // 最新更新窗口里左右键翻卡片
        const k = Math.max(0, Math.min(latestOf(tab).length - 1, pickK + (e.key === 'ArrowRight' ? 1 : -1)));
        if (world) world.front(k, true); else markPick(k, true);
        e.preventDefault();
        return;
      }
      const i = ORDER.findIndex(s => s.key === current);
      open(ORDER[(i + (e.key === 'ArrowRight' ? 1 : -1) + ORDER.length) % ORDER.length].key, { focus: false });
      e.preventDefault();
    }
  });

  // 网址带 #latest（README 和顶栏的「✦ 最新」链接）：回到首屏，打开最新更新窗口
  function goLatest(smooth) {
    if (!LATEST) return;
    const top = root.getBoundingClientRect().top;
    if (Math.abs(top) > 2) root.scrollIntoView({ behavior: smooth && !reduce ? 'smooth' : 'auto', block: 'start' });
    open(LKEY, { focus: false });
  }
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href="#latest"]');
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    if (location.hash !== '#latest') history.pushState(null, '', '#latest');
    goLatest(true);
  });
  addEventListener('hashchange', () => { if (location.hash === '#latest') goLatest(true); });
  if (location.hash === '#latest') goLatest(false);

  /* ---------- 悬停提示 ---------- */
  function showTip(s, x, y) {
    tip.innerHTML = `<b>${esc(s.name)}</b><span>${esc(s.look)}</span><em>${L(`${COUNT[s.key] || 0} 个项目 · 点击进入展厅`, `${COUNT[s.key] || 0} projects · click to open`)}</em>`;
    tip.hidden = false;
    const w = tip.offsetWidth, h = tip.offsetHeight, W = root.clientWidth, H = root.clientHeight;
    let left = x + 16, top = y + 18;
    if (left + w > W - 10) left = x - w - 16;
    if (top + h > H - 10) top = y - h - 14;
    tip.style.transform = `translate(${Math.max(8, left)}px, ${Math.max(8, top)}px)`;
  }
  function hideTip() { tip.hidden = true; }

  /* ---------- 退路：平铺的小样图墙 ---------- */
  function flat() {
    if (stage.classList.contains('gw-flat')) return;
    stage.classList.add('gw-flat');
    stage.innerHTML = `<div class="gw-wall">${ORDER.map(s => `<button type="button" tabindex="-1" data-gw="${s.key}" style="--c:${s.color}"><span>${esc(s.name)}</span></button>`).join('')}</div>`;
    stage.querySelectorAll('.gw-wall button').forEach(b => b.prepend(swatchCanvas(b.dataset.gw, 320, 128)));
    stage.addEventListener('click', e => { const b = e.target.closest('[data-gw]'); if (b) open(b.dataset.gw); });
    root.classList.add('gw-ready');
  }

  /* ---------- 启动：首屏可见时才去加载 three.js ---------- */
  function boot() {
    let ok = false;
    try { ok = !!(window.WebGL2RenderingContext && document.createElement('canvas').getContext('webgl2')); } catch (e) { ok = false; }
    if (!ok) { flat(); return; }
    import(THREE_URL).then(T => {
      world = build(T);
      requestAnimationFrame(() => root.classList.add('gw-ready'));
      if (current) world.focus(current);
    }).catch(err => { console.warn('3D 入口没加载成功，改用平铺样图：', err); flat(); });
  }
  const r0 = root.getBoundingClientRect();
  if (!('IntersectionObserver' in window) || (r0.bottom > 0 && r0.top < innerHeight)) boot();
  else {
    // 从 README 直接跳到下面某一节的访客，等滚回首屏再加载
    const bootIO = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { bootIO.disconnect(); boot(); } });
    bootIO.observe(root);
  }

  /* ======================================================================= */
  function build(T) {
    const renderer = new T.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
    renderer.setClearColor(0x000000, 0);
    renderer.outputColorSpace = T.SRGBColorSpace;
    const canvas = renderer.domElement;
    canvas.className = 'gw-canvas';
    stage.append(canvas);
    const scene = new T.Scene();
    const camera = new T.PerspectiveCamera(34, 1, 0.1, 400);
    const aniso = Math.min(8, renderer.capabilities.getMaxAnisotropy());
    const mk = (w, h) => { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; };
    const toTex = (cv, srgb = true) => { const t = new T.CanvasTexture(cv); if (srgb) t.colorSpace = T.SRGBColorSpace; t.anisotropy = aniso; return t; };
    const rrect = (x, px, py, w, h, r) => { x.beginPath(); if (x.roundRect) x.roundRect(px, py, w, h, r); else x.rect(px, py, w, h); };
    const smooth = (a, b, v) => { const t = Math.min(1, Math.max(0, (v - a) / (b - a))); return t * t * (3 - 2 * t); };
    const ease = t => 1 - Math.pow(1 - t, 3);
    const wrapAngle = a => Math.atan2(Math.sin(a), Math.cos(a));
    const nearest = (from, to) => from + wrapAngle(to - from);

    // ---- 共用贴图：圆角遮罩、面板背后的光晕、星点、地面的光
    function mask(w, h, r) { const c = mk(w, h), x = c.getContext('2d'); x.fillStyle = '#000'; x.fillRect(0, 0, w, h); x.fillStyle = '#fff'; rrect(x, 3, 3, w - 6, h - 6, r); x.fill(); return toTex(c, false); }
    const PANEL_MASK = mask(512, 256, 16), CARD_MASK = mask(512, 320, 20);
    const HALO = (() => { const c = mk(256, 160), x = c.getContext('2d'); x.shadowColor = '#fff'; x.shadowBlur = 40; x.fillStyle = '#fff'; rrect(x, 48, 40, 160, 80, 10); x.fill(); x.fill(); return toTex(c, false); })();
    const radial = (size, stops) => { const c = mk(size, size), x = c.getContext('2d'), g = x.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2); stops.forEach(([o, col]) => g.addColorStop(o, col)); x.fillStyle = g; x.fillRect(0, 0, size, size); return toTex(c, false); };
    const DOT = radial(64, [[0, 'rgba(255,255,255,1)'], [0.25, 'rgba(255,255,255,.55)'], [1, 'rgba(255,255,255,0)']]);
    const FLOOR = radial(512, [[0, 'rgba(110,130,255,.55)'], [0.45, 'rgba(70,80,170,.18)'], [1, 'rgba(0,0,0,0)']]);

    // ---- 面板：上面是小样图，下面一条写画风名和项目数
    const PW = 640, PH = 320, SH = 256;
    const swatchCache = new Map();
    const swatchOf = key => { if (!swatchCache.has(key)) swatchCache.set(key, swatchCanvas(key, PW, SH)); return swatchCache.get(key); };
    function paintPanel(pn, withSwatch) {
      const c = pn.cv.getContext('2d'), s = pn.s;
      c.clearRect(0, 0, PW, PH);
      if (withSwatch) c.drawImage(swatchOf(s.key), 0, 0);
      else {
        const g = c.createLinearGradient(0, 0, PW, SH); g.addColorStop(0, s.color); g.addColorStop(1, '#0B0D13');
        c.fillStyle = g; c.globalAlpha = 0.5; c.fillRect(0, 0, PW, SH); c.globalAlpha = 1;
      }
      c.fillStyle = '#0B0D13'; c.fillRect(0, SH, PW, PH - SH);
      c.fillStyle = s.color; c.fillRect(0, SH, PW, 5);
      c.beginPath(); c.arc(30, SH + 36, 8, 0, Math.PI * 2); c.fill();
      c.textBaseline = 'middle';
      const ct = String(COUNT[s.key] || 0);
      c.font = `500 22px ${MONO}`;
      const cw = c.measureText(ct).width;
      c.fillStyle = '#8E95A6'; c.fillText(ct, PW - 24 - cw, SH + 37);
      let fs = 32;
      do { c.font = `700 ${fs}px ${SERIF}`; fs -= 1; } while (c.measureText(s.name).width > PW - 110 - cw && fs > 16);
      c.fillStyle = '#F2F3F6'; c.fillText(s.name, 50, SH + 37);
      pn.painted = withSwatch;
      if (pn.map) pn.map.needsUpdate = true;
    }

    const RAD = 8.6;
    const RINGS = [
      { list: MAIN, y: 0.92, w: 2.6, spin: 0.045 },
      { list: NICHE, y: -0.94, w: 2.04, spin: -0.032 },
    ];
    const panels = [], hits = [];
    RINGS.forEach((ring, ri) => {
      ring.group = new T.Group(); ring.group.position.y = ring.y; scene.add(ring.group);
      ring.theta = ri ? Math.PI / ring.list.length : 0; ring.vel = 0; ring.goal = null;
      const n = ring.list.length, w = ring.w, h = w / 2;
      ring.h = h;
      const geo = new T.PlaneGeometry(w, h), haloGeo = new T.PlaneGeometry(w * 1.6, h * 2);
      ring.list.forEach((s, i) => {
        const a = -(i / n) * Math.PI * 2;
        const pivot = new T.Group(); pivot.rotation.y = a; ring.group.add(pivot);
        const pn = { s, ring, a, pivot, cv: mk(PW, PH), lift: 0, glow: 0.18, dim: 1, painted: false };
        paintPanel(pn, false);
        pn.map = toTex(pn.cv);
        pn.mat = new T.MeshBasicMaterial({ map: pn.map, alphaMap: PANEL_MASK, transparent: true, alphaTest: 0.02 });
        pn.mesh = new T.Mesh(geo, pn.mat); pn.mesh.position.z = RAD; pivot.add(pn.mesh);
        pn.hmat = new T.MeshBasicMaterial({ map: HALO, color: new T.Color(s.color), transparent: true, opacity: 0, blending: T.AdditiveBlending, depthWrite: false });
        pn.halo = new T.Mesh(haloGeo, pn.hmat); pn.halo.position.z = RAD - 0.05; pivot.add(pn.halo);
        pn.mesh.userData.pn = pn;
        panels.push(pn); hits.push(pn.mesh);
      });
      const pts = [];
      for (let k = 0; k <= 180; k++) { const t = k / 180 * Math.PI * 2; pts.push(new T.Vector3(Math.sin(t) * RAD, -h / 2 - 0.16, Math.cos(t) * RAD)); }
      ring.group.add(new T.Line(new T.BufferGeometry().setFromPoints(pts), new T.LineBasicMaterial({ color: 0x4A5482, transparent: true, opacity: 0.6 })));
    });
    const PANEL = Object.fromEntries(panels.map(pn => [pn.s.key, pn]));
    const MID_Y = (RINGS[0].y - RINGS[0].h / 2 + RINGS[1].y + RINGS[1].h / 2) / 2;  // 两圈转盘之间的高度，最新更新的卡片廊停在这里
    const LZ = 2.4;  // 最新更新的卡片比转盘往前多少

    // 小样图分帧画：先画正对镜头的，每帧一张，避免一次卡住主线程
    const queue = [...panels];
    const idle = window.requestIdleCallback ? cb => requestIdleCallback(cb, { timeout: 120 }) : cb => setTimeout(cb, 16);
    function paintNext() {
      if (!queue.length) return;
      queue.sort((p, q) => Math.cos(q.a + q.ring.theta) - Math.cos(p.a + p.ring.theta));
      const t0 = performance.now();
      while (queue.length && performance.now() - t0 < 12) paintPanel(queue.shift(), true);
      kick();
      if (queue.length) idle(paintNext);
    }
    idle(paintNext);

    // ---- 星空和地面的光
    const NS = innerWidth < 760 ? 700 : 1500;
    const sp = new Float32Array(NS * 3), sc = new Float32Array(NS * 3);
    const palette = ORDER.map(s => new T.Color(s.color)), white = new T.Color(0xC9D1EA);
    for (let i = 0; i < NS; i++) {
      const u = Math.random() * 2 - 1, th = Math.random() * Math.PI * 2, r = 45 + Math.random() * 110, q = Math.sqrt(1 - u * u);
      sp.set([q * Math.cos(th) * r, u * r * 0.55 + 4, q * Math.sin(th) * r], i * 3);
      const col = Math.random() < 0.2 ? palette[i % palette.length] : white, b = 0.35 + Math.random() * 0.65;
      sc.set([col.r * b, col.g * b, col.b * b], i * 3);
    }
    const sg = new T.BufferGeometry();
    sg.setAttribute('position', new T.BufferAttribute(sp, 3));
    sg.setAttribute('color', new T.BufferAttribute(sc, 3));
    const stars = new T.Points(sg, new T.PointsMaterial({ size: 0.9, map: DOT, vertexColors: true, transparent: true, depthWrite: false, blending: T.AdditiveBlending }));
    scene.add(stars);
    const floor = new T.Mesh(new T.CircleGeometry(RAD * 1.7, 64), new T.MeshBasicMaterial({ map: FLOOR, transparent: true, depthWrite: false, blending: T.AdditiveBlending, opacity: 0.7 }));
    floor.rotation.x = -Math.PI / 2;
    floor.position.y = RINGS[1].y - RINGS[1].h / 2 - 0.55;
    scene.add(floor);

    // ---- 精品卡片
    const CW = 512, CH = 320, CARD_W = 2.0, CARD_H = CARD_W * CH / CW;
    const cardGeo = new T.PlaneGeometry(CARD_W, CARD_H);
    const cardGroup = new T.Group(); scene.add(cardGroup);
    let cards = [], dying = [], frontK = 0, frontF = 0;
    const CJK = /[⺀-鿿豈-﫿＀-￯　-〿]/;
    const TOKENS = /[⺀-鿿豈-﫿＀-￯　-〿]|[^\s⺀-鿿豈-﫿＀-￯　-〿]+|\s+/g;
    function clip(c, text, maxW) {
      if (c.measureText(text).width <= maxW) return text;
      while (text && c.measureText(text + '…').width > maxW) text = text.slice(0, -1);
      return text + '…';
    }
    function wrap(c, text, maxW, maxLines) {
      const tokens = String(text).match(TOKENS) || [];
      const lines = []; let line = '', overflow = false;
      for (const t of tokens) {
        const test = line + t;
        if (line.trim() && c.measureText(test).width > maxW && !/^\s+$/.test(t)) {
          lines.push(line.trim());
          line = t;
          if (lines.length === maxLines) { overflow = true; break; }
        } else line = test;
      }
      if (!overflow && line.trim()) lines.push(line.trim());
      if (overflow) lines[maxLines - 1] = clip(c, lines[maxLines - 1] + (CJK.test(line) ? '' : ' ') + line.trim(), maxW);
      return lines.slice(0, maxLines);
    }
    function paintCard(cd) {
      const c = cd.cv.getContext('2d'), p = cd.p, s = cd.s, [cls, lbl] = status(p);
      const g = c.createLinearGradient(0, 0, 0, CH); g.addColorStop(0, '#191D29'); g.addColorStop(1, '#0D1017');
      c.fillStyle = g; c.fillRect(0, 0, CW, CH);
      c.fillStyle = s.color; c.fillRect(0, 0, CW, 7);
      c.textBaseline = 'alphabetic';
      c.font = `500 18px ${MONO}`;
      const star = `★ ${fmtStars(p.stars)}`, sw = c.measureText(star).width;
      c.fillStyle = '#F2D27A'; c.fillText(star, CW - 28 - sw, 48);
      c.fillStyle = '#7F879A'; c.fillText(clip(c, `${String(cd.k + 1).padStart(2, '0')} · ${cd.label}`, CW - 80 - sw), 28, 48);
      let fs = 40;
      do { c.font = `700 ${fs}px ${SERIF}`; fs -= 1; } while (c.measureText(p.name).width > CW - 56 && fs > 22);
      c.fillStyle = '#F4F5F8'; c.fillText(clip(c, p.name, CW - 56), 28, 101);
      c.font = `400 16px ${MONO}`; c.fillStyle = '#727A8C'; c.fillText(clip(c, p.repo, CW - 56), 28, 131);
      c.font = `400 22px ${SANS}`; c.fillStyle = '#C6CBD7';
      wrap(c, p.desc, CW - 56, 3).forEach((ln, i) => c.fillText(ln, 28, 176 + i * 33));
      c.font = `600 18px ${SANS}`;
      const gh = 'GitHub ↗', gw = c.measureText(gh).width;
      c.fillStyle = '#A9B6FF'; c.fillText(gh, CW - 28 - gw, CH - 25);
      c.fillStyle = cls === 'ok' ? '#4CC27E' : cls === 'slow' ? '#E3AE55' : '#6B7280';
      c.beginPath(); c.arc(34, CH - 31, 6, 0, Math.PI * 2); c.fill();
      c.font = `400 18px ${SANS}`; c.fillStyle = '#9AA1B0'; c.fillText(clip(c, `${cd.foot || lbl} · ${p.lang}`, CW - 100 - gw), 48, CH - 25);
      if (cd.tex) cd.tex.needsUpdate = true;
    }
    function buildCards(key) {
      clearCards();
      const latest = key === LKEY;
      let anchor, src;
      if (latest) {
        // 停在两圈转盘之间、往前挪一点；从右上角（小窗口的方向）飞进来
        anchor = new T.Vector3(0, MID_Y, RAD + LZ);
        src = new T.Vector3(2.6, RINGS[0].y + 1.7, RAD + LZ - 0.6);
      } else {
        const ring = PANEL[key].ring;
        anchor = new T.Vector3(0, ring.y - ring.h / 2 - 0.34 - CARD_H / 2, RAD + 1.0);
        src = new T.Vector3(0, ring.y, RAD + 0.4);
      }
      frontK = 0; frontF = 0;
      cards = cardsOf(key).map((p, k) => {
        const s = latest ? SMAP[p.tags[0]] : SMAP[key];
        const foot = !latest ? null : tab === 'new' ? L(`${day(p.added)}收录`, `Added ${day(p.added)}`) : L(`${day(p.pushed_at)}有提交`, `Pushed ${day(p.pushed_at)}`);
        const cd = { p, k, s, label: s.name, foot, cv: null, tex: null, age: 0, delay: Math.min(k, 6) * 0.07, hv: 0, anchor, src };
        // 贴图等卡片翻到附近再画（ensureCard），几十张新收录也不会一下子占满显存
        cd.mat = new T.MeshBasicMaterial({ alphaMap: CARD_MASK, transparent: true, opacity: 0, alphaTest: 0.02, color: 0x161a24 });
        cd.mesh = new T.Mesh(cardGeo, cd.mat);
        cd.mesh.position.copy(src);
        cd.mesh.scale.setScalar(0.2);
        cd.mesh.visible = false;
        cd.mesh.userData.card = cd;
        cardGroup.add(cd.mesh);
        return cd;
      });
    }
    function ensureCard(cd) {
      if (cd.tex) return;
      cd.cv = mk(CW, CH);
      paintCard(cd);
      cd.tex = toTex(cd.cv);
      cd.mat.map = cd.tex; cd.mat.color.set(0xffffff); cd.mat.needsUpdate = true;
    }
    function clearCards() { cards.forEach(cd => { cd.out = 0; dying.push(cd); }); cards = []; hoverCard = null; }
    function setFront(k, scroll) {
      if (!cards.length) return;
      frontK = Math.max(0, Math.min(cards.length - 1, k));
      markPick(frontK, scroll);
      kick();
    }

    // ---- 字体：网页字体到了以后重画面板和卡片上的字
    if (document.fonts && document.fonts.load) {
      const sample = ORDER.map(s => s.name).join('') + Object.values(FEATURED).flat().map(r => (BYREPO[r] || {}).name || '').join('')
        + [...latestOf('new'), ...latestOf('recent')].map(p => p.name).join('');
      Promise.all([document.fonts.load(`700 32px ${SERIF}`, sample), document.fonts.load(`500 20px ${MONO}`, '0123456789★·k')]).then(() => {
        panels.forEach(pn => {
          if (TEXT_SWATCHES.has(pn.s.key)) swatchCache.delete(pn.s.key);
          paintPanel(pn, pn.painted);
        });
        cards.forEach(cd => { if (cd.cv) paintCard(cd); });
        kick();
      }).catch(() => {});
    }

    /* ---------- 镜头 ---------- */
    const cam = { pos: new T.Vector3(0, 2, 20), look: new T.Vector3(0, 0, RAD), n: new T.Vector2() };
    const goal = { pos: new T.Vector3(), look: new T.Vector3(), n: new T.Vector2() };
    const sway = new T.Vector2(), swayGoal = new T.Vector2();
    let fovT = Math.tan(T.MathUtils.degToRad(camera.fov / 2));
    // 内容要落在屏幕上的哪一块：避开标题、底部按钮和展厅面板
    function region() {
      const rr = root.getBoundingClientRect(), vw = rr.width, vh = rr.height;
      const portrait = vw / vh < 0.9;
      const rel = el => el.getBoundingClientRect();
      const h1 = rel(root.querySelector('h1')), brand = rel(root.querySelector('.gw-brand')), bottom = rel(root.querySelector('.gw-bottom'));
      let x0 = 0.02, x1 = 0.98, y0, y1;
      if (current) {
        const hr = rel(hall);
        // 手机上展厅打开时标题会隐藏，内容可以一直放到右上角按钮下面
        y0 = ((portrait ? rel(root.querySelector('.gw-corner')).bottom : h1.bottom) - rr.top) / vh + 0.03;
        if (portrait) y1 = (hr.top - rr.top) / vh - 0.02;
        else { x1 = (hr.left - rr.left) / vw - 0.03; y1 = (bottom.top - rr.top) / vh; }
      } else {
        // 右上角的最新更新小窗口比标题区高时，转盘再往下让一点
        const nb = news && !news.hidden && news.offsetParent ? rel(news).bottom : 0;
        y0 = (Math.max(brand.bottom, nb) - rr.top) / vh + 0.01;
        y1 = (bottom.top - rr.top) / vh - 0.01;
      }
      if (y1 - y0 < 0.3) y0 = Math.max(0.04, y1 - 0.3);
      return { r: [x0, y0, x1, y1], portrait };
    }
    function frame(snap) {
      const { r, portrait } = region();
      const aspect = camera.aspect;
      let C, wc, hc, elev;
      if (current === LKEY) {
        const top = MID_Y + CARD_H / 2 + 0.22, bot = MID_Y - CARD_H / 2 - 0.22;
        C = new T.Vector3(0, (top + bot) / 2, RAD + LZ);
        wc = CARD_W * (portrait ? 1.15 : 2.1); hc = top - bot; elev = 0.05;
      } else if (current) {
        const ring = PANEL[current].ring;
        const top = ring.y + ring.h / 2 * 1.08, bot = ring.y - ring.h / 2 - 0.34 - CARD_H;
        C = new T.Vector3(0, (top + bot) / 2, RAD + 0.7);
        wc = Math.max(ring.w * 1.1, CARD_W * (portrait ? 1.12 : 2.2)); hc = top - bot + 0.15; elev = 0.07;
      } else {
        const top = RINGS[0].y + RINGS[0].h / 2, bot = RINGS[1].y - RINGS[1].h / 2 - 0.25;
        C = new T.Vector3(0, (top + bot) / 2, RAD);
        wc = portrait ? RINGS[0].w * 1.2 : 8.6; hc = top - bot + 0.5; elev = 0.15;
      }
      const fw = r[2] - r[0], fh = r[3] - r[1];
      const d = Math.min(42, Math.max(wc / (2 * fovT * aspect * fw), hc / (2 * fovT * fh)));
      goal.look.copy(C);
      goal.pos.set(C.x, C.y + elev * d, C.z + d);
      goal.n.set(r[0] + r[2] - 1, 1 - (r[1] + r[3]));
      if (snap) { cam.pos.copy(goal.pos); cam.look.copy(goal.look); cam.n.copy(goal.n); }
      kick();
    }
    function applyCamera() {
      camera.position.copy(cam.pos);
      if (!current) { camera.position.x += sway.x * 0.5; camera.position.y -= sway.y * 0.3; }
      camera.lookAt(cam.look);
      camera.rotateY(Math.atan(cam.n.x * fovT * camera.aspect));
      camera.rotateX(-Math.atan(cam.n.y * fovT));
    }

    /* ---------- 每帧更新；返回 true 表示还有东西在动 ---------- */
    let hover = null, hoverCard = null, peekKey = null, drag = null, pausedUntil = 0;
    let recede = 0;  // 最新更新窗口开着时，两圈转盘缩小、退到卡片后面去
    // 最新更新窗口开着时，转盘调暗后照样慢慢转
    const spinning = now => !reduce && (!current || current === LKEY) && !drag && !hover && !peekKey && now > pausedUntil;
    function pauseSpin(ms) { pausedUntil = performance.now() + ms; setTimeout(kick, ms + 30); }
    function update(dt, now) {
      let busy = false;
      const k = reduce ? 1 : 1 - Math.exp(-dt * 7);
      const spin = spinning(now);
      const rg = current === LKEY ? 1 : 0;
      recede = reduce ? rg : recede + (rg - recede) * (1 - Math.exp(-dt * 3.4));
      if (Math.abs(rg - recede) > 0.002) busy = true; else recede = rg;
      const rs = 1 - 0.42 * recede;
      RINGS.forEach(ring => {
        if (ring.goal != null) {
          const d = ring.goal - ring.theta;
          ring.theta = Math.abs(d) < 1e-4 || reduce ? ring.goal : ring.theta + d * (1 - Math.exp(-dt * 5.5));
          ring.vel = 0;
          if (ring.theta !== ring.goal) busy = true;
        } else if (!(drag && drag.moved && drag.ring === ring)) {
          if (Math.abs(ring.vel) > 1e-3) { ring.theta += ring.vel * dt; ring.vel *= Math.exp(-dt * 2.4); busy = true; } else ring.vel = 0;
          if (spin) ring.theta += ring.spin * dt;
        }
        ring.group.rotation.y = ring.theta;
        ring.group.scale.setScalar(rs); ring.group.position.y = ring.y * rs;
      });
      panels.forEach(pn => {
        const facing = Math.cos(wrapAngle(pn.a + pn.ring.theta));
        const vis = smooth(0.05, 0.85, facing);
        const sel = current === pn.s.key, hov = hover === pn || (!current && peekKey === pn.s.key);
        const tl = sel ? 0.3 : hov ? 0.32 : 0, tg = sel ? 0.95 : hov ? 0.9 : 0.2, td = current && !sel ? (current === LKEY ? 0.2 : 0.1) : 1;
        pn.lift += (tl - pn.lift) * k; pn.glow += (tg - pn.glow) * k; pn.dim += (td - pn.dim) * k;
        if (Math.abs(tl - pn.lift) + Math.abs(tg - pn.glow) + Math.abs(td - pn.dim) > 0.003) busy = true;
        const s = 1 + pn.lift * 0.14;
        pn.mesh.position.z = RAD + pn.lift; pn.mesh.scale.setScalar(s);
        pn.halo.position.z = RAD + pn.lift - 0.05; pn.halo.scale.setScalar(s);
        const b = (0.16 + 0.84 * vis) * pn.dim;
        pn.mat.color.setRGB(b, b, b);
        pn.hmat.opacity = pn.glow * vis * (sel ? 1 : pn.dim);
        pn.mesh.visible = pn.halo.visible = facing > -0.15;
      });
      // 卡片廊：正中一张正对镜头，两侧往里斜、往后退
      frontF += (frontK - frontF) * (reduce ? 1 : 1 - Math.exp(-dt * 8));
      if (Math.abs(frontK - frontF) > 1e-3) busy = true; else frontF = frontK;
      cards.forEach(cd => {
        cd.age += dt;
        const tt = reduce ? 1 : Math.min(1, Math.max(0, (cd.age - cd.delay) / 0.7)), e = ease(tt);
        if (tt < 1) busy = true;
        const o = cd.k - frontF, ao = Math.abs(o), so = Math.sign(o), m1 = Math.min(ao, 1), m2 = Math.max(ao - 1, 0);
        const tx = so * (m1 * CARD_W * 0.8 + m2 * CARD_W * 0.36), tz = -(m1 * 0.95 + m2 * 0.5), ry = -so * m1 * 0.85;
        // 离正中太远的卡片淡出、不画；翻到附近才去画它的贴图
        const fade = 1 - smooth(2.6, 3.6, ao);
        cd.mesh.visible = fade > 0.01;
        if (!cd.mesh.visible) return;
        ensureCard(cd);
        const th = hoverCard === cd ? 1 : 0;
        cd.hv += (th - cd.hv) * k; if (Math.abs(th - cd.hv) > 0.003) busy = true;
        cd.mesh.position.set(
          cd.src.x + (cd.anchor.x + tx - cd.src.x) * e,
          cd.src.y + (cd.anchor.y + cd.hv * 0.07 - cd.src.y) * e,
          cd.src.z + (cd.anchor.z + tz + cd.hv * 0.18 - cd.src.z) * e);
        cd.mesh.rotation.y = ry * e;
        cd.mesh.scale.setScalar((0.2 + 0.8 * e) * (1 + cd.hv * 0.035));
        cd.mat.opacity = e * Math.max(0.18, 1 - ao * 0.26) * fade;
        cd.mesh.renderOrder = 20 - Math.round(ao * 3);
      });
      dying = dying.filter(cd => {
        cd.out += reduce ? 1 : dt / 0.28;
        cd.mat.opacity = Math.max(0, 1 - cd.out) * 0.9;
        cd.mesh.position.z -= dt * 1.2;
        if (cd.out < 1) { busy = true; return true; }
        cardGroup.remove(cd.mesh); if (cd.tex) cd.tex.dispose(); cd.mat.dispose();
        return false;
      });
      // 镜头缓动 + 跟着指针的轻微视差
      const kc = reduce ? 1 : 1 - Math.exp(-dt * 3.4);
      cam.pos.lerp(goal.pos, kc); cam.look.lerp(goal.look, kc); cam.n.lerp(goal.n, kc);
      if (cam.pos.distanceToSquared(goal.pos) > 1e-5 || cam.n.distanceToSquared(goal.n) > 1e-7) busy = true;
      if (!reduce) { sway.lerp(swayGoal, 1 - Math.exp(-dt * 2.5)); if (sway.distanceToSquared(swayGoal) > 1e-5) busy = true; }
      if (spin) stars.rotation.y += dt * 0.006;
      applyCamera();
      return busy;
    }

    /* ---------- 渲染循环：看不见就停 ---------- */
    let running = false, visible = true, last = 0;
    function kick() {
      if (running || !visible || document.hidden) return;
      running = true; last = performance.now();
      requestAnimationFrame(loop);
    }
    function loop(now) {
      if (!visible || document.hidden) { running = false; return; }
      const dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now;
      const busy = update(dt, now);
      renderer.render(scene, camera);
      if (busy || spinning(now) || (drag && drag.moved)) requestAnimationFrame(loop); else running = false;
    }
    new IntersectionObserver(es => { visible = es.some(e => e.isIntersecting); kick(); }).observe(root);
    document.addEventListener('visibilitychange', kick);

    function resize() {
      const w = stage.clientWidth, h = stage.clientHeight;
      if (!w || !h) return;
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, w < 760 ? 1.6 : 1.75));
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      fovT = Math.tan(T.MathUtils.degToRad(camera.fov / 2));
      frame(!resize.done); resize.done = true;
    }
    if ('ResizeObserver' in window) new ResizeObserver(resize).observe(stage); else addEventListener('resize', resize);
    resize();

    /* ---------- 指针：拖动转盘、悬停、点击 ---------- */
    const ray = new T.Raycaster(), ndc = new T.Vector2(), tmp = new T.Vector3();
    function pick(x, y) {
      const r = canvas.getBoundingClientRect();
      ndc.set(((x - r.left) / r.width) * 2 - 1, -((y - r.top) / r.height) * 2 + 1);
      ray.setFromCamera(ndc, camera);
      const hit = ray.intersectObjects(cards.length ? [...cards.map(c => c.mesh), ...hits] : hits, false).find(h => h.object.visible);
      return hit ? hit.object.userData : null;
    }
    function ringAt(y) {
      const mid = (RINGS[0].y - RINGS[0].h / 2 + RINGS[1].y + RINGS[1].h / 2) / 2;
      tmp.set(0, mid, RAD).project(camera);
      const r = canvas.getBoundingClientRect();
      return y < r.top + (1 - tmp.y) / 2 * r.height ? RINGS[0] : RINGS[1];
    }
    canvas.addEventListener('pointerdown', e => {
      if (e.button !== 0) return;
      const hit = pick(e.clientX, e.clientY);
      drag = { id: e.pointerId, x0: e.clientX, y0: e.clientY, x: e.clientX, lt: performance.now(), hit, ring: hit && hit.pn ? hit.pn.ring : ringAt(e.clientY), moved: false, acc: 0 };
    });
    let hx = 0, hy = 0, hoverQueued = false;
    canvas.addEventListener('pointermove', e => {
      hx = e.clientX; hy = e.clientY;
      if (drag && e.pointerId === drag.id) {
        const now = performance.now(), dx = e.clientX - drag.x;
        if (!drag.moved && Math.hypot(e.clientX - drag.x0, e.clientY - drag.y0) > 6) {
          drag.moved = true; canvas.classList.add('is-drag'); hideTip();
          try { canvas.setPointerCapture(e.pointerId); } catch (err) { /* ignore */ }
        }
        if (drag.moved) {
          if (current) {
            // 展厅里左右拖动是翻卡片
            drag.acc += dx;
            while (drag.acc <= -80) { setFront(frontK + 1); drag.acc += 80; }
            while (drag.acc >= 80) { setFront(frontK - 1); drag.acc -= 80; }
          } else {
            const dth = dx / Math.max(320, stage.clientWidth) * 2.6, v = dth / Math.max(0.008, (now - drag.lt) / 1000);
            drag.ring.theta += dth; drag.ring.vel = drag.ring.vel * 0.4 + v * 0.6;
          }
        }
        drag.x = e.clientX; drag.lt = now;
        kick();
        return;
      }
      if (!hoverQueued) { hoverQueued = true; requestAnimationFrame(doHover); }
    });
    function doHover() {
      hoverQueued = false;
      if (drag && drag.moved) return;
      const hit = pick(hx, hy), pn = (hit && hit.pn) || null, cd = (hit && hit.card) || null;
      if (pn !== hover || cd !== hoverCard) { hover = pn; hoverCard = cd; kick(); }
      canvas.classList.toggle('is-point', !!(pn || cd));
      const rr = root.getBoundingClientRect();
      if (pn && !current) showTip(pn.s, hx - rr.left, hy - rr.top); else hideTip();
      swayGoal.set((hx - rr.left) / rr.width - 0.5, (hy - rr.top) / rr.height - 0.5);
      if (!reduce) kick();
    }
    function endDrag(e) {
      if (!drag || e.pointerId !== drag.id) return;
      const d = drag; drag = null;
      canvas.classList.remove('is-drag');
      if (d.moved) { if (!current) pauseSpin(2600); kick(); return; }
      if (e.type !== 'pointerup') return;
      const hit = d.hit;
      if (!hit) { if (current) close(); return; }
      if (hit.card) {
        if (hit.card.k === frontK) window.open('https://github.com/' + hit.card.p.repo, '_blank', 'noopener');
        else setFront(hit.card.k);
        return;
      }
      if (hit.pn) { if (current === hit.pn.s.key) close(); else open(hit.pn.s.key, { focus: false }); }
    }
    canvas.addEventListener('pointerup', endDrag);
    canvas.addEventListener('pointercancel', endDrag);
    canvas.addEventListener('pointerleave', () => {
      if (drag && drag.moved) return;
      hover = null; hoverCard = null; hideTip(); swayGoal.set(0, 0);
      canvas.classList.remove('is-point'); kick();
    });

    /* ---------- 给外面用的接口 ---------- */
    function focus(key) {
      peekKey = null;
      if (key === LKEY) {
        RINGS.forEach(r => { r.vel = 0; r.goal = null; });
        buildCards(key);
        markPick(0);
      } else if (key) {
        const pn = PANEL[key];
        RINGS.forEach(r => { r.vel = 0; if (r !== pn.ring) r.goal = null; });
        pn.ring.goal = nearest(pn.ring.theta, -pn.a);
        buildCards(key);
        markPick(0);
      } else {
        RINGS.forEach(r => { r.goal = null; });
        clearCards();
        pauseSpin(2200);
      }
      requestAnimationFrame(() => frame(false));
    }
    function peek(key) {
      if (current) return;
      if (key && !PANEL[key]) key = null;  // 「最新」按钮没有对应的面板
      peekKey = key;
      if (key) { const pn = PANEL[key]; RINGS.forEach(r => { r.goal = null; r.vel = 0; }); pn.ring.goal = nearest(pn.ring.theta, -pn.a); }
      else { RINGS.forEach(r => { r.goal = null; }); pauseSpin(1500); }
      kick();
    }
    return { focus, peek, front: setFront };
  }
}
