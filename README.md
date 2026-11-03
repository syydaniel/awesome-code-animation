<div align="center">

<img src="assets/banner.png" alt="代码画风图鉴 · Awesome Code Animation" width="100%">

# 代码画风图鉴 · Awesome Code Animation

**用代码画动画、做 MV 的开源项目合集，按画风索引。**

A curated list of open-source tools for making animations and music videos **with code**, indexed by visual style.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![项目](https://img.shields.io/badge/%E9%A1%B9%E7%9B%AE-159-2E49D4) ![画风](https://img.shields.io/badge/%E7%94%BB%E9%A3%8E-18-9265D9) ![活跃项目](https://img.shields.io/badge/%E6%B4%BB%E8%B7%83%E9%A1%B9%E7%9B%AE-120-1E8A4B) ![数据更新](https://img.shields.io/badge/%E6%95%B0%E6%8D%AE%E6%9B%B4%E6%96%B0-2026--11--03-5B6273)

**[🔎 网页版：可按画风筛选、搜索、排序](https://syydaniel.github.io/awesome-code-animation/)**

[画风索引](#index) · [按目的先挑](#picks) · [收录标准](#rules) · [全部项目](#all) · [推荐项目](https://github.com/syydaniel/awesome-code-animation/issues/new/choose)

</div>

## 这是什么

想用代码做一支 MV、一段讲解动画、一个片头，第一个问题往往是「我想要的那种画风，该用什么工具做」。这里把 GitHub 上用代码做动画、做视频的开源项目按**画风**归类：3B1B 式数学讲解、扁平 MG、着色器迷幻光影、像素复古、ASCII 终端、音乐可视化、二次元 MMD……先挑画风，再挑工具。一个项目常能做好几种画风，所以会同时出现在几个画风里。

<a name="rules"></a>

## 收录标准

- **画面由代码绘制或渲染。** 用视频生成、图像生成模型出画面的项目不收。AI 只负责写代码、画面仍由代码渲染的，归在「AI 写代码出片」。
- **GitHub 星数 1000 以上，或近一年内仍有更新且星数 200 以上。**
- **已归档（只读）的仓库不收。**
- 状态按仓库最近一次推送计算：🟢 活跃（半年内）· 🟡 放缓（两年内）· ⚪ 停更（超过两年，多数仍能用，只是不再加新功能）。
- 星数和状态每周一由 GitHub Actions 自动刷新，当前数据更新于 2026-11-03。

<a name="picks"></a>

## 按目的先挑

| 想做什么 | 先看这几个 |
| --- | --- |
| 做知识讲解视频 | [Manim 社区版](https://github.com/ManimCommunity/manim) · [Motion Canvas](https://github.com/motion-canvas/motion-canvas) · [Animate](https://github.com/cth9191/animate) |
| 做 MV、批量出短视频 | [Remotion](https://github.com/remotion-dev/remotion) · [HyperFrames](https://github.com/heygen-com/hyperframes) · [three.js](https://github.com/mrdoob/three.js) |
| 让 AI 帮你写代码出片 | [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) · [Remotion Skills](https://github.com/remotion-dev/skills) · [html-video](https://github.com/nexu-io/html-video) |
| 现场 VJ、迷幻画面 | [Hydra](https://github.com/hydra-synth/hydra) · [TiXL](https://github.com/tixl3d/tixl) · [cables](https://github.com/cables-gl/cables) |
| 音乐可视化 | [Butterchurn](https://github.com/jberg/butterchurn) · [projectM](https://github.com/projectM-visualizer/projectm) · [Astrofox](https://github.com/astrofox-io/astrofox) |
| 程序员科普视频 | [Slidev](https://github.com/slidevjs/slidev) · [VHS](https://github.com/charmbracelet/vhs) · [Gource](https://github.com/acaudwell/Gource) |

<a name="index"></a>

## 画风索引

点图片跳到对应画风的项目表。每张小样图都是用代码画出来的，代码在 [`site/template.html`](site/template.html) 里。

<table>
<tr><td align="center" width="33%"><a href="#math"><img src="assets/styles/math.png" alt="数学讲解风" width="260"></a><br><b><a href="#math">数学讲解风</a></b><br><sub>Math Explainer · 12 个项目</sub></td><td align="center" width="33%"><a href="#mg"><img src="assets/styles/mg.png" alt="扁平 MG 动效" width="260"></a><br><b><a href="#mg">扁平 MG 动效</a></b><br><sub>Motion Graphics · 37 个项目</sub></td><td align="center" width="33%"><a href="#code"><img src="assets/styles/code.png" alt="代码演示风" width="260"></a><br><b><a href="#code">代码演示风</a></b><br><sub>Code & Terminal Demo · 12 个项目</sub></td></tr>
<tr><td align="center" width="33%"><a href="#type"><img src="assets/styles/type.png" alt="动态文字 · 歌词" width="260"></a><br><b><a href="#type">动态文字 · 歌词</a></b><br><sub>Kinetic Type & Lyrics · 18 个项目</sub></td><td align="center" width="33%"><a href="#short"><img src="assets/styles/short.png" alt="短视频 · 字幕 · 快剪" width="260"></a><br><b><a href="#short">短视频 · 字幕 · 快剪</a></b><br><sub>Shorts, Captions & Editing · 17 个项目</sub></td><td align="center" width="33%"><a href="#agent"><img src="assets/styles/agent.png" alt="AI 写代码出片" width="260"></a><br><b><a href="#agent">AI 写代码出片</a></b><br><sub>Agent-Coded Video · 20 个项目</sub></td></tr>
<tr><td align="center" width="33%"><a href="#hand"><img src="assets/styles/hand.png" alt="手绘 · 白板 · 水彩" width="260"></a><br><b><a href="#hand">手绘 · 白板 · 水彩</a></b><br><sub>Hand-drawn & Whiteboard · 9 个项目</sub></td><td align="center" width="33%"><a href="#gen"><img src="assets/styles/gen.png" alt="生成艺术 · 几何" width="260"></a><br><b><a href="#gen">生成艺术 · 几何</a></b><br><sub>Generative Art · 19 个项目</sub></td><td align="center" width="33%"><a href="#shader"><img src="assets/styles/shader.png" alt="着色器 · 迷幻光影" width="260"></a><br><b><a href="#shader">着色器 · 迷幻光影</a></b><br><sub>Shaders & Psychedelic · 21 个项目</sub></td></tr>
<tr><td align="center" width="33%"><a href="#live"><img src="assets/styles/live.png" alt="Live Coding · VJ" width="260"></a><br><b><a href="#live">Live Coding · VJ</a></b><br><sub>Live Coding & VJ · 7 个项目</sub></td><td align="center" width="33%"><a href="#audio"><img src="assets/styles/audio.png" alt="音乐可视化" width="260"></a><br><b><a href="#audio">音乐可视化</a></b><br><sub>Music Visualization · 13 个项目</sub></td><td align="center" width="33%"><a href="#3d"><img src="assets/styles/3d.png" alt="3D 渲染" width="260"></a><br><b><a href="#3d">3D 渲染</a></b><br><sub>3D · 29 个项目</sub></td></tr>
<tr><td align="center" width="33%"><a href="#anime"><img src="assets/styles/anime.png" alt="二次元 · MMD · VRM" width="260"></a><br><b><a href="#anime">二次元 · MMD · VRM</a></b><br><sub>Anime, MMD & VRM · 6 个项目</sub></td><td align="center" width="33%"><a href="#particle"><img src="assets/styles/particle.png" alt="粒子 · 流体 · 物理" width="260"></a><br><b><a href="#particle">粒子 · 流体 · 物理</a></b><br><sub>Particles & Physics · 13 个项目</sub></td><td align="center" width="33%"><a href="#glitch"><img src="assets/styles/glitch.png" alt="故障 · 后期特效" width="260"></a><br><b><a href="#glitch">故障 · 后期特效</a></b><br><sub>Glitch & Post FX · 9 个项目</sub></td></tr>
<tr><td align="center" width="33%"><a href="#pixel"><img src="assets/styles/pixel.png" alt="像素 · 复古" width="260"></a><br><b><a href="#pixel">像素 · 复古</a></b><br><sub>Pixel & Retro · 9 个项目</sub></td><td align="center" width="33%"><a href="#ascii"><img src="assets/styles/ascii.png" alt="ASCII · 终端" width="260"></a><br><b><a href="#ascii">ASCII · 终端</a></b><br><sub>ASCII & Terminal · 12 个项目</sub></td><td align="center" width="33%"><a href="#data"><img src="assets/styles/data.png" alt="数据可视化动画" width="260"></a><br><b><a href="#data">数据可视化动画</a></b><br><sub>Data Animation · 18 个项目</sub></td></tr>
</table>

<a name="math"></a>

## 数学讲解风 · Math Explainer

<img src="assets/styles/math.png" alt="数学讲解风样图" width="240" align="right">

> 公式、坐标系、几何变换，3B1B 式的蓝黑画面

共 12 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.1k | 🟢 活跃 | Python | 3Blue1Brown 本人做视频用的数学动画引擎（ManimGL），公式、坐标系、图形变换，经典蓝黑讲解画风。<br><sub>适合：讲解视频 · 也在：数据可视化动画</sub><br><sub>⚠️ 文档较少，新手建议先用社区版。</sub> |
| [Manim 社区版](https://github.com/ManimCommunity/manim) | 42.2k | 🟢 活跃 | Python | Manim 社区维护版，文档和教程最全，B 站大量数学、物理、算法科普视频用它制作。<br><sub>适合：讲解视频 · 也在：数据可视化动画、代码演示风</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 19.7k | 🟢 活跃 | TypeScript | 用 TypeScript 生成器函数写动画，带时间轴编辑器，可以对着音频卡点，很适合讲解视频和代码演示。<br><sub>适合：讲解视频 · MV · 也在：扁平 MG 动效、代码演示风</sub> |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | ⚪ 停更 | Python | 基于 Manim 的机器学习概念动画：神经网络、卷积等结构的讲解动画。<br><sub>适合：讲解视频 · 也在：数据可视化动画</sub> |
| [Code2Video](https://github.com/showlab/Code2Video) | 2.2k | 🟢 活跃 | Python | 学术项目：让大模型编写 Manim 代码，自动生成教学讲解视频，画面全部由代码渲染。<br><sub>适合：讲解视频 · 也在：AI 写代码出片</sub> |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | ⚪ 停更 | JavaScript | 浏览器里的 3D 数学可视化：曲面、向量场、坐标网格，画面干净有质感。<br><sub>适合：讲解视频 · 也在：3D 渲染</sub> |
| [Animate](https://github.com/cth9191/animate) | 1.4k | 🟢 活跃 | JavaScript / Canvas | Claude Code 技能：用单个 canvas 程序化绘制短动画，内置剪纸、排线墨水、Riso 印刷、速写本、数学、像素、等距 7 种画风。<br><sub>适合：讲解视频 · 短片 · 也在：AI 写代码出片、手绘 · 白板 · 水彩、像素 · 复古</sub> |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.2k | 🟡 放缓 | Haskell | Haskell 写的 SVG 动画库，支持 LaTeX 公式，画面风格接近 3B1B。<br><sub>适合：讲解视频 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 语言小众，社区较小。</sub> |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 974 | 🟢 活跃 | Python | 把 Manim 动画做成可以逐页播放的演示幻灯片，也能导出成网页。<br><sub>适合：讲解视频 · 演讲 · 也在：代码演示风</sub> |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | 936 | 🟢 活跃 | Python | 用自然语言描述，由大模型写出 Manim 代码并渲染成动画。<br><sub>适合：讲解视频 · 也在：AI 写代码出片</sub> |
| [manim-physics](https://github.com/Matheart/manim-physics) | 412 | 🟢 活跃 | Python | Manim 的物理模拟扩展：刚体、电磁场、波动、单摆等物理动画。<br><sub>适合：讲解视频 · 也在：粒子 · 流体 · 物理</sub> |
| [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | 326 | 🟢 活跃 | Python | 给 Manim 动画加配音，按语音时间自动对齐动画节奏。<br><sub>适合：讲解视频</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="mg"></a>

## 扁平 MG 动效 · Motion Graphics

<img src="assets/styles/mg.png" alt="扁平 MG 动效样图" width="240" align="right">

> 扁平图形、弹性缓动、形状变换

共 37 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 78.1k | 🟢 活跃 | HTML / CSS / GSAP | HeyGen 开源，用 HTML/CSS 写画面、GSAP 做动画，直接渲染成 MP4，专门为 AI 编程助手设计。<br><sub>适合：MV · 短视频 · AI 生成 · 也在：AI 写代码出片、动态文字 · 歌词、短视频 · 字幕 · 快剪</sub> |
| [anime.js](https://github.com/juliangarnier/anime) | 74.2k | 🟢 活跃 | JavaScript | 轻量 JS 动画库，时间轴、交错（stagger）、SVG 描边动画都很顺手。<br><sub>适合：网页动画 · MV · 也在：动态文字 · 歌词</sub> |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.5k | 🟢 活跃 | HTML / JS | 用 HTML 写演示文稿，Auto-Animate 能让元素在页面之间自动补间过渡。<br><sub>适合：讲解视频 · 演讲 · 也在：代码演示风</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 70.3k | 🟢 活跃 | React / TS | 用 React 组件写视频，渲染成 MP4，可批量生成；官方有字幕、音频可视化、three.js 等扩展包。<br><sub>适合：MV · 短视频 · 批量出片 · 也在：短视频 · 字幕 · 快剪、动态文字 · 歌词、3D 渲染</sub><br><sub>⚠️ 个人和小公司免费（含商用），较大的公司需购买公司授权。</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 51.1k | 🟢 活跃 | React | 大量带动画的 React 组件：文字特效、动态背景、交互动效，复制即用。<br><sub>适合：网页动效 · 素材 · 也在：动态文字 · 歌词、着色器 · 迷幻光影</sub> |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.6k | 🟢 活跃 | TypeScript | 高性能 2D 渲染引擎（WebGL / WebGPU），适合大量精灵、滤镜和 2D 动效。<br><sub>适合：网页动画 · MV · 也在：粒子 · 流体 · 物理、生成艺术 · 几何</sub> |
| [Motion](https://github.com/motiondivision/motion) | 34.8k | 🟢 活跃 | React / JS | 原 Framer Motion，React 和 JS 动画库，弹簧、手势、布局过渡都很顺手。<br><sub>适合：网页动效</sub> |
| [Lottie](https://github.com/airbnb/lottie-web) | 32.3k | 🟡 放缓 | JavaScript | 在网页里播放 After Effects 导出的动画（Bodymovin JSON），扁平插画和图标动画的通用格式。<br><sub>适合：特效素材 · 网页动画</sub><br><sub>⚠️ 动画本身通常在 AE 里做，代码负责播放和控制。</sub> |
| [GSAP](https://github.com/greensock/GSAP) | 30.1k | 🟡 放缓 | JavaScript | 老牌 JS 动画引擎，SplitText、MorphSVG 等插件现已全部免费，文字拆分动画和 SVG 变形很强。<br><sub>适合：MV · 网页动画 · 也在：动态文字 · 歌词</sub><br><sub>⚠️ 免费且可商用，但使用 GreenSock 自有许可，不是 OSI 认证的开源许可。</sub> |
| [react-spring](https://github.com/pmndrs/react-spring) | 29.3k | 🟢 活跃 | React | 基于弹簧物理的 React 动画库，动作自然有弹性。<br><sub>适合：网页动效</sub> |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.1k | 🟢 活跃 | React | 带动效的 React 组件库：文字动画、流光边框、粒子背景等。<br><sub>适合：网页动效 · 也在：动态文字 · 歌词</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 19.7k | 🟢 活跃 | TypeScript | 用 TypeScript 生成器函数写动画，带时间轴编辑器，可以对着音频卡点，很适合讲解视频和代码演示。<br><sub>适合：讲解视频 · MV · 也在：代码演示风、数学讲解风</sub> |
| [mo.js](https://github.com/mojs/mojs) | 18.9k | 🟢 活跃 | JavaScript | 专做 Motion Graphics 的 JS 库：爆裂、波纹、形状弹出等 MG 小动效。<br><sub>适合：特效素材</sub> |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 16.4k | 🟢 活跃 | React / TS | AI 编程助手技能：截取你的真实网页，用 Remotion 做成电影感的产品宣传片。<br><sub>适合：产品宣传片 · 也在：AI 写代码出片、短视频 · 字幕 · 快剪</sub> |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | 🟢 活跃 | JavaScript | 矢量图形脚本框架，路径运算和贝塞尔曲线很强，适合矢量风生成艺术。<br><sub>适合：生成艺术 · 也在：生成艺术 · 几何</sub> |
| [Theatre.js](https://github.com/theatre-js/theatre) | 12.8k | ⚪ 停更 | TypeScript | 网页动画的可视化时间轴：代码里定义属性，界面里拖关键帧，常配 three.js 做 3D 镜头动画。<br><sub>适合：MV · 网页动画 · 也在：3D 渲染</sub> |
| [SVG.js](https://github.com/svgdotjs/svg.js) | 11.9k | 🟢 活跃 | JavaScript | 轻量的 SVG 操作和动画库。<br><sub>适合：网页动画</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 11.5k | 🟢 活跃 | JavaScript | 代码实现的影片画风工具箱：66 种现成画风（孟菲斯、地铁线路图、黑板等），让 AI 编程助手按画风出片，全部用代码绘制。<br><sub>适合：MV · 短片 · 也在：AI 写代码出片、手绘 · 白板 · 水彩、像素 · 复古</sub><br><sub>⚠️ 画风针对 Claude 调校，用其他模型效果可能不同。</sub> |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | ⚪ 停更 | JavaScript | 伪 3D 扁平引擎，画出圆润可爱的扁平立体图形。<br><sub>适合：网页动画 · 也在：3D 渲染</sub><br><sub>⚠️ 多年未更新，功能简单稳定。</sub> |
| [Two.js](https://github.com/jonobr1/two.js) | 8.7k | 🟢 活跃 | JavaScript | 2D 矢量绘图 API，同一套代码可输出 SVG、Canvas 或 WebGL，适合几何扁平动画。<br><sub>适合：网页动画 · 也在：生成艺术 · 几何</sub> |
| [EffectCraft](https://github.com/storytold/effectcraft) | 8.4k | 🟢 活跃 | Rust（图形界面） | 从零写的开源合成软件，思路类似 After Effects：图层、关键帧、表达式、三百多种特效。<br><sub>适合：MG · 后期合成 · 也在：故障 · 后期特效</sub><br><sub>⚠️ 以图形界面为主，表达式部分可以写代码。</sub> |
| [Remotion Skills](https://github.com/remotion-dev/skills) | 6.2k | 🟢 活跃 | Markdown 技能 | Remotion 官方的 AI 编程助手技能，让 Claude Code 等直接写 Remotion 视频。<br><sub>适合：MV · 短视频 · 也在：AI 写代码出片</sub> |
| [PAG](https://github.com/Tencent/libpag) | 5.8k | 🟢 活跃 | C++ / 多端 | 腾讯开源的 AE 动画方案，思路类似 Lottie，支持更多 AE 特性，可以用代码替换里面的文字和图片。<br><sub>适合：特效素材</sub> |
| [html-video](https://github.com/nexu-io/html-video) | 4.8k | 🟢 活跃 | HTML / CSS | 让本地 AI 编程助手把 HTML/CSS 写成视频，自带动态字体、瑞士网格、数据卡片等 21 个模板。<br><sub>适合：短视频 · 宣传片 · 也在：AI 写代码出片、动态文字 · 歌词</sub> |
| [VAP](https://github.com/Tencent/vap) | 4.2k | 🟢 活跃 | 多端 | 腾讯开源的带透明通道的视频动画播放方案，常用于直播礼物这类复杂特效。<br><sub>适合：特效素材</sub> |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | 🟢 活跃 | TypeScript | 从 Motion Canvas 分出来的版本，主打无界面渲染，可通过 API 批量生成视频。<br><sub>适合：短视频 · 批量出片 · 也在：短视频 · 字幕 · 快剪</sub> |
| [onetake](https://github.com/feitangyuan/onetake) | 3.7k | 🟢 活跃 | Python / HTML | 一镜到底的动效短片技能：每个画面都从上一个画面里长出来，不像 PPT 那样换页。<br><sub>适合：产品发布片 · 也在：AI 写代码出片</sub><br><sub>⚠️ 另有付费的 Pro 版。</sub> |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | 🟢 活跃 | Rust / SVG | 用 Rust 和 SVG 写视频，在 GPU 上渲染，主打速度；也附带给 AI 编程助手用的技能。<br><sub>适合：批量出片 · 也在：短视频 · 字幕 · 快剪</sub> |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3k | 🟢 活跃 | React / TS | 输入一个话题，生成黑底动态图形讲解视频（带配音和字幕），画面全部由代码渲染。<br><sub>适合：讲解视频 · 也在：AI 写代码出片、数据可视化动画</sub> |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | 2.7k | 🟢 活跃 | Markdown 技能 | 教 AI 助手动效设计原则：节奏、缓动、编排和迪士尼动画法则。<br><sub>适合：动效设计 · 也在：AI 写代码出片</sub> |
| [Pixel2Motion](https://github.com/nolangz/pixel2motion) | 2.6k | 🟢 活跃 | Python / SVG | 把位图 Logo 转成干净的 SVG，再做成 Logo 动画和视频预览。<br><sub>适合：Logo 动画 · 也在：AI 写代码出片</sub> |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 2.2k | 🟢 活跃 | JavaScript | 国人作品：让 AI 编程助手做产品发布片，自己写配乐，可以指着画面改。<br><sub>适合：产品宣传片 · 也在：AI 写代码出片、3D 渲染</sub> |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | 🟢 活跃 | TypeScript（图形界面） | 把音频做成可视化视频的动效软件：频谱、波形、文字、3D 图层可组合导出。<br><sub>适合：音乐可视化 · MV · 也在：音乐可视化</sub><br><sub>⚠️ 以图形界面为主。</sub> |
| [remocn](https://github.com/Remocn/remocn) | 1.7k | 🟢 活跃 | React / TS | 给 Remotion 用的现成动画、转场、背景和场景组件。<br><sub>适合：MV · 短视频 · 也在：短视频 · 字幕 · 快剪</sub><br><sub>⚠️ 需配合 Remotion 使用，Remotion 自身的授权条款仍然适用。</sub> |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.2k | 🟡 放缓 | Haskell | Haskell 写的 SVG 动画库，支持 LaTeX 公式，画面风格接近 3B1B。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub><br><sub>⚠️ 语言小众，社区较小。</sub> |
| [motion-skills](https://github.com/iart-ai/motion-skills) | 1.2k | 🟢 活跃 | Markdown 技能 | 50 个 AI 编程助手技能：动态文字、数据可视化、讲解视频、竖屏短视频、WebGL、Manim。<br><sub>适合：各类视频 · 也在：AI 写代码出片</sub> |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | 937 | 🟢 活跃 | TypeScript | LottieFiles 官方的 Lottie / dotLottie 网页播放器，基于 Rust + WASM，性能更好。<br><sub>适合：特效素材 · 网页动画</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="code"></a>

## 代码演示风 · Code & Terminal Demo

<img src="assets/styles/code.png" alt="代码演示风样图" width="240" align="right">

> 代码高亮、逐行出现、终端录屏、算法动画

共 12 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.5k | 🟢 活跃 | HTML / JS | 用 HTML 写演示文稿，Auto-Animate 能让元素在页面之间自动补间过渡。<br><sub>适合：讲解视频 · 演讲 · 也在：扁平 MG 动效</sub> |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.4k | ⚪ 停更 | JavaScript | 把排序、图、动态规划等算法的执行过程画成动画。<br><sub>适合：讲解视频 · 也在：数据可视化动画</sub> |
| [Slidev](https://github.com/slidevjs/slidev) | 49.3k | 🟢 活跃 | Markdown / Vue | 用 Markdown 写演示文稿，内置代码高亮和代码平滑过渡动画，支持录制。<br><sub>适合：讲解视频 · 演讲</sub> |
| [Manim 社区版](https://github.com/ManimCommunity/manim) | 42.2k | 🟢 活跃 | Python | Manim 社区维护版，文档和教程最全，B 站大量数学、物理、算法科普视频用它制作。<br><sub>适合：讲解视频 · 也在：数学讲解风、数据可视化动画</sub> |
| [VHS](https://github.com/charmbracelet/vhs) | 21.3k | 🟢 活跃 | VHS 脚本 | 用脚本写好终端操作，自动录成 GIF 或视频，做命令行演示最方便。<br><sub>适合：讲解视频 · GIF · 也在：ASCII · 终端</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 19.7k | 🟢 活跃 | TypeScript | 用 TypeScript 生成器函数写动画，带时间轴编辑器，可以对着音频卡点，很适合讲解视频和代码演示。<br><sub>适合：讲解视频 · MV · 也在：扁平 MG 动效、数学讲解风</sub> |
| [asciinema](https://github.com/asciinema/asciinema) | 17.9k | 🟢 活跃 | Rust（命令行） | 录制终端会话，用网页播放器回放，体积小、文字可复制。<br><sub>适合：讲解视频 · 也在：ASCII · 终端</sub> |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | ⚪ 停更 | JavaScript（命令行） | 录制终端操作，渲染成带窗口样式的 GIF 动图。<br><sub>适合：GIF · 也在：ASCII · 终端</sub> |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | 🟡 放缓 | C++（命令行） | 把 Git 提交历史渲染成「代码生长」动画视频，经典的程序员视频素材。<br><sub>适合：程序员视频 · 也在：数据可视化动画</sub> |
| [Code Hike](https://github.com/code-hike/codehike) | 5.4k | 🟡 放缓 | React / Markdown | 用 Markdown 和 React 做代码讲解，可以配合 Remotion 渲染成代码讲解视频。<br><sub>适合：讲解视频</sub> |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | 🟢 活跃 | Python | 把 Git 命令的效果画成图示和动画（底层基于 Manim），适合做 Git 教学视频。<br><sub>适合：讲解视频 · 也在：数据可视化动画</sub> |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 974 | 🟢 活跃 | Python | 把 Manim 动画做成可以逐页播放的演示幻灯片，也能导出成网页。<br><sub>适合：讲解视频 · 演讲 · 也在：数学讲解风</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="type"></a>

## 动态文字 · 歌词 · Kinetic Type & Lyrics

<img src="assets/styles/type.png" alt="动态文字 · 歌词样图" width="240" align="right">

> 字形变形、逐字出场、跟着歌词卡点

共 18 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 78.1k | 🟢 活跃 | HTML / CSS / GSAP | HeyGen 开源，用 HTML/CSS 写画面、GSAP 做动画，直接渲染成 MP4，专门为 AI 编程助手设计。<br><sub>适合：MV · 短视频 · AI 生成 · 也在：AI 写代码出片、扁平 MG 动效、短视频 · 字幕 · 快剪</sub> |
| [anime.js](https://github.com/juliangarnier/anime) | 74.2k | 🟢 活跃 | JavaScript | 轻量 JS 动画库，时间轴、交错（stagger）、SVG 描边动画都很顺手。<br><sub>适合：网页动画 · MV · 也在：扁平 MG 动效</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 70.3k | 🟢 活跃 | React / TS | 用 React 组件写视频，渲染成 MP4，可批量生成；官方有字幕、音频可视化、three.js 等扩展包。<br><sub>适合：MV · 短视频 · 批量出片 · 也在：扁平 MG 动效、短视频 · 字幕 · 快剪、3D 渲染</sub><br><sub>⚠️ 个人和小公司免费（含商用），较大的公司需购买公司授权。</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 51.1k | 🟢 活跃 | React | 大量带动画的 React 组件：文字特效、动态背景、交互动效，复制即用。<br><sub>适合：网页动效 · 素材 · 也在：扁平 MG 动效、着色器 · 迷幻光影</sub> |
| [GSAP](https://github.com/greensock/GSAP) | 30.1k | 🟡 放缓 | JavaScript | 老牌 JS 动画引擎，SplitText、MorphSVG 等插件现已全部免费，文字拆分动画和 SVG 变形很强。<br><sub>适合：MV · 网页动画 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 免费且可商用，但使用 GreenSock 自有许可，不是 OSI 认证的开源许可。</sub> |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.1k | 🟢 活跃 | React | 带动效的 React 组件库：文字动画、流光边框、粒子背景等。<br><sub>适合：网页动效 · 也在：扁平 MG 动效</sub> |
| [Typed.js](https://github.com/mattboldt/typed.js) | 16.3k | 🟡 放缓 | JavaScript | 打字机效果的文字动画库。<br><sub>适合：网页动效</sub> |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.7k | ⚪ 停更 | TypeScript | 手绘风格的标注动画：圈出、划线、高亮文字。<br><sub>适合：讲解视频 · 网页动画 · 也在：手绘 · 白板 · 水彩</sub> |
| [editly](https://github.com/mifi/editly) | 5.6k | 🟡 放缓 | JSON / Node | 用 JSON 或命令行声明式剪视频，自带转场、标题、Ken Burns 推拉等效果。<br><sub>适合：快剪 · 短视频 · 也在：短视频 · 字幕 · 快剪</sub> |
| [html-video](https://github.com/nexu-io/html-video) | 4.8k | 🟢 活跃 | HTML / CSS | 让本地 AI 编程助手把 HTML/CSS 写成视频，自带动态字体、瑞士网格、数据卡片等 21 个模板。<br><sub>适合：短视频 · 宣传片 · 也在：AI 写代码出片、扁平 MG 动效</sub> |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | 🟢 活跃 | Python | 终端文字特效库，几十种文字出场动画（燃烧、雨落、解码等）。<br><sub>适合：片头 · 文字特效 · 也在：ASCII · 终端</sub> |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | 🟢 活跃 | React / Vue | 国人开发的类 Apple Music 歌词组件：逐字高亮、弹性滚动、流体背景。<br><sub>适合：歌词 MV · 播放器 · 也在：音乐可视化</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2k | 🟢 活跃 | React / TS | 口播视频技能：按配音逐字对齐，用 Remotion 渲染动态字卡和运镜。<br><sub>适合：口播视频 · 也在：AI 写代码出片、短视频 · 字幕 · 快剪</sub> |
| [Splitting](https://github.com/shshaw/Splitting) | 1.8k | ⚪ 停更 | JavaScript | 把文字拆成单个字符或单词并加上 CSS 变量，方便做逐字动画。<br><sub>适合：网页动效</sub> |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | 🟢 活跃 | TypeScript | 给网页里的图片、视频、文字加 WebGL 特效：故障、RGB 偏移、扭曲等。<br><sub>适合：网页特效 · MV · 也在：故障 · 后期特效</sub> |
| [DrawBot](https://github.com/typemytype/drawbot) | 455 | 🟢 活跃 | Python | 用 Python 画 2D 图形并导出 GIF/MP4，字体设计圈常用来做文字动画。<br><sub>适合：动态字体 · GIF · 也在：生成艺术 · 几何</sub><br><sub>⚠️ 只支持 macOS。</sub> |
| [Coldtype](https://github.com/coldtype/coldtype) | 341 | 🟢 活跃 | Python | Python 写的展示型排版与动画工具，可以跟着音频节奏做字形变化，适合歌词 MV 和动态字体。<br><sub>适合：歌词 MV · 动态字体 · 也在：生成艺术 · 几何</sub> |
| [Remotion TikTok 模板](https://github.com/remotion-dev/template-tiktok) | 301 | 🟢 活跃 | React / TS | Remotion 官方模板：语音自动识别，生成逐字跳动的短视频字幕。<br><sub>适合：短视频 · 也在：短视频 · 字幕 · 快剪</sub><br><sub>⚠️ 授权条款同 Remotion。</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="short"></a>

## 短视频 · 字幕 · 快剪 · Shorts, Captions & Editing

<img src="assets/styles/short.png" alt="短视频 · 字幕 · 快剪样图" width="240" align="right">

> 自动字幕、转场、用代码批量剪辑出片

共 17 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 78.1k | 🟢 活跃 | HTML / CSS / GSAP | HeyGen 开源，用 HTML/CSS 写画面、GSAP 做动画，直接渲染成 MP4，专门为 AI 编程助手设计。<br><sub>适合：MV · 短视频 · AI 生成 · 也在：AI 写代码出片、扁平 MG 动效、动态文字 · 歌词</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 70.3k | 🟢 活跃 | React / TS | 用 React 组件写视频，渲染成 MP4，可批量生成；官方有字幕、音频可视化、three.js 等扩展包。<br><sub>适合：MV · 短视频 · 批量出片 · 也在：扁平 MG 动效、动态文字 · 歌词、3D 渲染</sub><br><sub>⚠️ 个人和小公司免费（含商用），较大的公司需购买公司授权。</sub> |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 66.4k | 🟢 活跃 | C（命令行） | 几乎所有代码出片工具的底层：转码、拼接、滤镜、字幕烧录都能用命令行完成。<br><sub>适合：剪辑合成 · 后期 · 也在：故障 · 后期特效</sub><br><sub>⚠️ GitHub 上是镜像仓库。</sub> |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 16.4k | 🟢 活跃 | React / TS | AI 编程助手技能：截取你的真实网页，用 Remotion 做成电影感的产品宣传片。<br><sub>适合：产品宣传片 · 也在：AI 写代码出片、扁平 MG 动效</sub> |
| [MoviePy](https://github.com/Zulko/moviepy) | 15.1k | 🟢 活跃 | Python | Python 视频剪辑库：切片、拼接、加字幕、合成都能用代码完成。<br><sub>适合：剪辑合成</sub> |
| [editly](https://github.com/mifi/editly) | 5.6k | 🟡 放缓 | JSON / Node | 用 JSON 或命令行声明式剪视频，自带转场、标题、Ken Burns 推拉等效果。<br><sub>适合：快剪 · 短视频 · 也在：动态文字 · 歌词</sub> |
| [OpenFilm](https://github.com/openfilm/openfilm) | 4.4k | 🟢 活跃 | HTML / CSS | 让编程助手把影片写成网页，再用本地 Studio 编辑器手动调整。<br><sub>适合：短片 · 宣传片 · 也在：AI 写代码出片</sub><br><sub>⚠️ 可以导入外部视频和图片素材，本身不依赖生成模型。</sub> |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | 🟢 活跃 | TypeScript | 从 Motion Canvas 分出来的版本，主打无界面渲染，可通过 API 批量生成视频。<br><sub>适合：短视频 · 批量出片 · 也在：扁平 MG 动效</sub> |
| [FFCreator](https://github.com/tnfe/FFCreator) | 3.2k | 🟡 放缓 | Node.js | 腾讯团队开源的 Node.js 短视频生成库，用图片、文字和转场快速合成视频。<br><sub>适合：短视频 · 批量出片</sub> |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | 🟢 活跃 | Rust / SVG | 用 Rust 和 SVG 写视频，在 GPU 上渲染，主打速度；也附带给 AI 编程助手用的技能。<br><sub>适合：批量出片 · 也在：扁平 MG 动效</sub> |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.2k | 🟢 活跃 | GLSL | 开源 GLSL 转场合集，可以接进 editly 等剪辑工具使用。<br><sub>适合：转场 · 也在：故障 · 后期特效</sub> |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2k | 🟢 活跃 | React / TS | 口播视频技能：按配音逐字对齐，用 Remotion 渲染动态字卡和运镜。<br><sub>适合：口播视频 · 也在：AI 写代码出片、动态文字 · 歌词</sub> |
| [remocn](https://github.com/Remocn/remocn) | 1.7k | 🟢 活跃 | React / TS | 给 Remotion 用的现成动画、转场、背景和场景组件。<br><sub>适合：MV · 短视频 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 需配合 Remotion 使用，Remotion 自身的授权条款仍然适用。</sub> |
| [Diffusion Studio Core](https://github.com/diffusionstudio/core) | 1.3k | 🟡 放缓 | TypeScript | 浏览器端视频引擎，用代码剪辑和合成视频，基于 WebCodecs。<br><sub>适合：剪辑合成</sub> |
| [Etro](https://github.com/etro-js/etro) | 1.2k | 🟢 活跃 | TypeScript | 在浏览器里用 TypeScript 合成视频：图层、特效、关键帧，可导出。<br><sub>适合：剪辑合成</sub> |
| [Remotion TikTok 模板](https://github.com/remotion-dev/template-tiktok) | 301 | 🟢 活跃 | React / TS | Remotion 官方模板：语音自动识别，生成逐字跳动的短视频字幕。<br><sub>适合：短视频 · 也在：动态文字 · 歌词</sub><br><sub>⚠️ 授权条款同 Remotion。</sub> |
| [Remotion 音频图模板](https://github.com/remotion-dev/template-audiogram) | 275 | 🟢 活跃 | React / TS | Remotion 官方模板：把播客音频做成带波形和字幕的短视频。<br><sub>适合：短视频 · 播客 · 也在：音乐可视化</sub><br><sub>⚠️ 授权条款同 Remotion。</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="agent"></a>

## AI 写代码出片 · Agent-Coded Video

<img src="assets/styles/agent.png" alt="AI 写代码出片样图" width="240" align="right">

> AI 编程助手写代码，画面仍由代码渲染，不用生成模型

共 20 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 78.1k | 🟢 活跃 | HTML / CSS / GSAP | HeyGen 开源，用 HTML/CSS 写画面、GSAP 做动画，直接渲染成 MP4，专门为 AI 编程助手设计。<br><sub>适合：MV · 短视频 · AI 生成 · 也在：扁平 MG 动效、动态文字 · 歌词、短视频 · 字幕 · 快剪</sub> |
| [Blender MCP](https://github.com/ahujasid/mcp-for-blender) | 33.2k | 🟢 活跃 | Python | 让大模型通过代码控制 Blender：建模、布光、做动画。<br><sub>适合：3D 动画 · 也在：3D 渲染</sub><br><sub>⚠️ 社区插件，不是 Blender 官方项目。</sub> |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 20.2k | 🟢 活跃 | Python / three.js | AI 编程助手技能：照着参考图，用纯代码重建程序化的 three.js 3D 模型，可直接做动画。<br><sub>适合：3D 素材 · 也在：3D 渲染</sub> |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 16.4k | 🟢 活跃 | React / TS | AI 编程助手技能：截取你的真实网页，用 Remotion 做成电影感的产品宣传片。<br><sub>适合：产品宣传片 · 也在：扁平 MG 动效、短视频 · 字幕 · 快剪</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 11.5k | 🟢 活跃 | JavaScript | 代码实现的影片画风工具箱：66 种现成画风（孟菲斯、地铁线路图、黑板等），让 AI 编程助手按画风出片，全部用代码绘制。<br><sub>适合：MV · 短片 · 也在：扁平 MG 动效、手绘 · 白板 · 水彩、像素 · 复古</sub><br><sub>⚠️ 画风针对 Claude 调校，用其他模型效果可能不同。</sub> |
| [Remotion Skills](https://github.com/remotion-dev/skills) | 6.2k | 🟢 活跃 | Markdown 技能 | Remotion 官方的 AI 编程助手技能，让 Claude Code 等直接写 Remotion 视频。<br><sub>适合：MV · 短视频 · 也在：扁平 MG 动效</sub> |
| [html-video](https://github.com/nexu-io/html-video) | 4.8k | 🟢 活跃 | HTML / CSS | 让本地 AI 编程助手把 HTML/CSS 写成视频，自带动态字体、瑞士网格、数据卡片等 21 个模板。<br><sub>适合：短视频 · 宣传片 · 也在：扁平 MG 动效、动态文字 · 歌词</sub> |
| [OpenFilm](https://github.com/openfilm/openfilm) | 4.4k | 🟢 活跃 | HTML / CSS | 让编程助手把影片写成网页，再用本地 Studio 编辑器手动调整。<br><sub>适合：短片 · 宣传片 · 也在：短视频 · 字幕 · 快剪</sub><br><sub>⚠️ 可以导入外部视频和图片素材，本身不依赖生成模型。</sub> |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 3.9k | 🟢 活跃 | JavaScript | 244 个用代码写的像素特效动画：火焰、爆炸、魔法、天气等，可导出精灵图；附带 AI 编程助手技能。<br><sub>适合：像素特效素材 · 也在：像素 · 复古</sub> |
| [onetake](https://github.com/feitangyuan/onetake) | 3.7k | 🟢 活跃 | Python / HTML | 一镜到底的动效短片技能：每个画面都从上一个画面里长出来，不像 PPT 那样换页。<br><sub>适合：产品发布片 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 另有付费的 Pro 版。</sub> |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3k | 🟢 活跃 | React / TS | 输入一个话题，生成黑底动态图形讲解视频（带配音和字幕），画面全部由代码渲染。<br><sub>适合：讲解视频 · 也在：数据可视化动画、扁平 MG 动效</sub> |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | 2.7k | 🟢 活跃 | Markdown 技能 | 教 AI 助手动效设计原则：节奏、缓动、编排和迪士尼动画法则。<br><sub>适合：动效设计 · 也在：扁平 MG 动效</sub> |
| [Pixel2Motion](https://github.com/nolangz/pixel2motion) | 2.6k | 🟢 活跃 | Python / SVG | 把位图 Logo 转成干净的 SVG，再做成 Logo 动画和视频预览。<br><sub>适合：Logo 动画 · 也在：扁平 MG 动效</sub> |
| [Code2Video](https://github.com/showlab/Code2Video) | 2.2k | 🟢 活跃 | Python | 学术项目：让大模型编写 Manim 代码，自动生成教学讲解视频，画面全部由代码渲染。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub> |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 2.2k | 🟢 活跃 | JavaScript | 国人作品：让 AI 编程助手做产品发布片，自己写配乐，可以指着画面改。<br><sub>适合：产品宣传片 · 也在：扁平 MG 动效、3D 渲染</sub> |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2k | 🟢 活跃 | React / TS | 口播视频技能：按配音逐字对齐，用 Remotion 渲染动态字卡和运镜。<br><sub>适合：口播视频 · 也在：短视频 · 字幕 · 快剪、动态文字 · 歌词</sub> |
| [Animate](https://github.com/cth9191/animate) | 1.4k | 🟢 活跃 | JavaScript / Canvas | Claude Code 技能：用单个 canvas 程序化绘制短动画，内置剪纸、排线墨水、Riso 印刷、速写本、数学、像素、等距 7 种画风。<br><sub>适合：讲解视频 · 短片 · 也在：手绘 · 白板 · 水彩、像素 · 复古、数学讲解风</sub> |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 1.2k | 🟢 活跃 | TypeScript | AI 编程助手技能：用代码画插画、循环动画和带配乐的短片，几十种画风，每次渲染结果一致。<br><sub>适合：插画 · 循环动画 · 短片 · 也在：手绘 · 白板 · 水彩、生成艺术 · 几何</sub> |
| [motion-skills](https://github.com/iart-ai/motion-skills) | 1.2k | 🟢 活跃 | Markdown 技能 | 50 个 AI 编程助手技能：动态文字、数据可视化、讲解视频、竖屏短视频、WebGL、Manim。<br><sub>适合：各类视频 · 也在：扁平 MG 动效</sub> |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | 936 | 🟢 活跃 | Python | 用自然语言描述，由大模型写出 Manim 代码并渲染成动画。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="hand"></a>

## 手绘 · 白板 · 水彩 · Hand-drawn & Whiteboard

<img src="assets/styles/hand.png" alt="手绘 · 白板 · 水彩样图" width="240" align="right">

> 草图线条、逐笔绘制、水彩笔触

共 9 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [Blender](https://github.com/blender/blender) | 21.6k | 🟢 活跃 | Python API | 开源 3D 软件，Python API 可以程序化生成场景和动画；Grease Pencil 能做 2D 手绘动画。<br><sub>适合：MV · 3D 动画 · 也在：3D 渲染</sub><br><sub>⚠️ GitHub 上是镜像，开发主站在 projects.blender.org。</sub> |
| [Rough.js](https://github.com/rough-stuff/rough) | 21.3k | ⚪ 停更 | JavaScript | 生成手绘草图风格的线条和图形，可以和其他动画库组合做手绘风动画。<br><sub>适合：讲解视频 · 网页动画</sub> |
| [Vivus](https://github.com/maxwellito/vivus) | 15.5k | ⚪ 停更 | JavaScript | SVG 描线动画，让线稿一笔一笔画出来。<br><sub>适合：网页动画</sub><br><sub>⚠️ 2022 年后未更新，功能简单稳定。</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 11.5k | 🟢 活跃 | JavaScript | 代码实现的影片画风工具箱：66 种现成画风（孟菲斯、地铁线路图、黑板等），让 AI 编程助手按画风出片，全部用代码绘制。<br><sub>适合：MV · 短片 · 也在：AI 写代码出片、扁平 MG 动效、像素 · 复古</sub><br><sub>⚠️ 画风针对 Claude 调校，用其他模型效果可能不同。</sub> |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.7k | ⚪ 停更 | TypeScript | 手绘风格的标注动画：圈出、划线、高亮文字。<br><sub>适合：讲解视频 · 网页动画 · 也在：动态文字 · 歌词</sub> |
| [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) | 2.1k | 🟢 活跃 | TypeScript | 把 Excalidraw 白板图变成逐笔绘制的动画，可导出成视频。<br><sub>适合：讲解视频</sub> |
| [Animate](https://github.com/cth9191/animate) | 1.4k | 🟢 活跃 | JavaScript / Canvas | Claude Code 技能：用单个 canvas 程序化绘制短动画，内置剪纸、排线墨水、Riso 印刷、速写本、数学、像素、等距 7 种画风。<br><sub>适合：讲解视频 · 短片 · 也在：AI 写代码出片、像素 · 复古、数学讲解风</sub> |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 1.2k | 🟢 活跃 | TypeScript | AI 编程助手技能：用代码画插画、循环动画和带配乐的短片，几十种画风，每次渲染结果一致。<br><sub>适合：插画 · 循环动画 · 短片 · 也在：AI 写代码出片、生成艺术 · 几何</sub> |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.2k | 🟢 活跃 | JavaScript | 给 p5.js 加自然笔刷、水彩填充和排线，做出手绘、水彩质感的画面。<br><sub>适合：生成艺术 · MV · 也在：生成艺术 · 几何</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="gen"></a>

## 生成艺术 · 几何 · Generative Art

<img src="assets/styles/gen.png" alt="生成艺术 · 几何样图" width="240" align="right">

> 算法图案、流场、无缝循环

共 19 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.6k | 🟢 活跃 | TypeScript | 高性能 2D 渲染引擎（WebGL / WebGPU），适合大量精灵、滤镜和 2D 动效。<br><sub>适合：网页动画 · MV · 也在：扁平 MG 动效、粒子 · 流体 · 物理</sub> |
| [p5.js](https://github.com/processing/p5.js) | 24.3k | 🟢 活跃 | JavaScript | 最流行的创意编程库，在网页上画图、做交互和动画，中文教程也很多。<br><sub>适合：生成艺术 · MV · 也在：粒子 · 流体 · 物理、音乐可视化</sub><br><sub>⚠️ 导出视频需要额外步骤（逐帧保存或录屏）。</sub> |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | 🟢 活跃 | JavaScript | 矢量图形脚本框架，路径运算和贝塞尔曲线很强，适合矢量风生成艺术。<br><sub>适合：生成艺术 · 也在：扁平 MG 动效</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 活跃 | C++ | C++ 创意编程框架，性能强，常用于互动装置、舞台视觉和音乐可视化。<br><sub>适合：演出 · 装置 · MV · 也在：音乐可视化、3D 渲染</sub> |
| [Two.js](https://github.com/jonobr1/two.js) | 8.7k | 🟢 活跃 | JavaScript | 2D 矢量绘图 API，同一套代码可输出 SVG、Canvas 或 WebGL，适合几何扁平动画。<br><sub>适合：网页动画 · 也在：扁平 MG 动效</sub> |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.3k | ⚪ 停更 | JavaScript | 几行代码生成动态 3D 背景：波浪、飞鸟、雾气、网格等。<br><sub>适合：背景素材 · 也在：3D 渲染</sub> |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | 🟢 活跃 | Rust | Rust 创意编程框架，带音频和 OSC 模块，适合实时音画作品。<br><sub>适合：生成艺术 · 演出 · 也在：音乐可视化</sub> |
| [css-doodle](https://github.com/css-doodle/css-doodle) | 6.1k | 🟢 活跃 | CSS | 用 CSS 规则批量生成图案和动画的网页组件。<br><sub>适合：生成艺术</sub> |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | 🟡 放缓 | C++ | C++ 创意编程框架，偏专业的实时图形与装置作品。<br><sub>适合：演出 · 装置 · 也在：3D 渲染</sub> |
| [Pts](https://github.com/williamngan/pts) | 5.4k | 🟢 活跃 | TypeScript | 围绕点、线、面几何关系的可视化与创意编程库。<br><sub>适合：生成艺术 · 也在：数据可视化动画</sub> |
| [canvas-sketch](https://github.com/mattdesl/canvas-sketch) | 5.3k | 🟢 活跃 | JavaScript | 生成艺术工作流，支持导出高清帧、GIF 和 MP4，适合做无缝循环动画。<br><sub>适合：生成艺术 · 循环动画</sub> |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | 🟢 活跃 | TypeScript | 由上百个 TypeScript 包组成的生成艺术与可视化工具集，作者长期维护。<br><sub>适合：生成艺术 · 也在：数据可视化动画</sub> |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 1.2k | 🟢 活跃 | TypeScript | AI 编程助手技能：用代码画插画、循环动画和带配乐的短片，几十种画风，每次渲染结果一致。<br><sub>适合：插画 · 循环动画 · 短片 · 也在：AI 写代码出片、手绘 · 白板 · 水彩</sub> |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.2k | 🟢 活跃 | JavaScript | 给 p5.js 加自然笔刷、水彩填充和排线，做出手绘、水彩质感的画面。<br><sub>适合：生成艺术 · MV · 也在：手绘 · 白板 · 水彩</sub> |
| [OPENRNDR](https://github.com/openrndr/openrndr) | 985 | 🟢 活跃 | Kotlin | Kotlin 创意编程框架，适合做生成图形和实时视觉。<br><sub>适合：生成艺术 · 演出</sub> |
| [play.core](https://github.com/ertdfgcvb/play.core) | 544 | 🟡 放缓 | JavaScript | 用 JS 写 ASCII 字符动画的实验平台，每个字符就是一个“像素”。<br><sub>适合：生成艺术 · 也在：ASCII · 终端</sub> |
| [Processing](https://github.com/processing/processing4) | 532 | 🟢 活跃 | Java | 创意编程的老牌工具，可以逐帧保存图片再合成视频。<br><sub>适合：生成艺术</sub> |
| [DrawBot](https://github.com/typemytype/drawbot) | 455 | 🟢 活跃 | Python | 用 Python 画 2D 图形并导出 GIF/MP4，字体设计圈常用来做文字动画。<br><sub>适合：动态字体 · GIF · 也在：动态文字 · 歌词</sub><br><sub>⚠️ 只支持 macOS。</sub> |
| [Coldtype](https://github.com/coldtype/coldtype) | 341 | 🟢 活跃 | Python | Python 写的展示型排版与动画工具，可以跟着音频节奏做字形变化，适合歌词 MV 和动态字体。<br><sub>适合：歌词 MV · 动态字体 · 也在：动态文字 · 歌词</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="shader"></a>

## 着色器 · 迷幻光影 · Shaders & Psychedelic

<img src="assets/styles/shader.png" alt="着色器 · 迷幻光影样图" width="240" align="right">

> 程序化光影、噪声、流体渐变、抽象造型

共 21 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 117k | 🟢 活跃 | JavaScript | 网页 3D 的事实标准：场景、材质、粒子、后期处理都有，案例极多。<br><sub>适合：MV · 网页 3D · 也在：3D 渲染、粒子 · 流体 · 物理</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 51.1k | 🟢 活跃 | React | 大量带动画的 React 组件：文字特效、动态背景、交互动效，复制即用。<br><sub>适合：网页动效 · 素材 · 也在：扁平 MG 动效、动态文字 · 歌词</sub> |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.8k | 🟡 放缓 | JavaScript | 浏览器里的实时流体模拟，彩色烟雾效果很出片。<br><sub>适合：特效素材 · 也在：粒子 · 流体 · 物理</sub> |
| [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | 7.1k | 🟡 放缓 | GLSL | 着色器入门书（有中文版），一步步学写片元着色器。<br><sub>适合：教程</sub> |
| [Shaders](https://github.com/shader-effects-inc/shaders) | 5.8k | 🟢 活跃 | TypeScript | WebGPU 特效组件，支持 React、Vue、Svelte、Solid 等框架。<br><sub>适合：网页特效</sub> |
| [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | 5.4k | 🟢 活跃 | GLSL / C++ | 命令行着色器查看器，可以把 shader 作品录成帧序列，适合把 Shadertoy 式画面做成视频。<br><sub>适合：MV · 特效素材</sub> |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.3k | 🟢 活跃 | TypeScript | 在真实网页界面上叠加 WebGL 流体、着色器和 3D 特效的组件库。<br><sub>适合：网页特效 · 也在：粒子 · 流体 · 物理</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 活跃 | 节点连线 / C# | 原 Tooll3，开源实时动态图形软件，节点加时间轴，常用于音乐视频和现场演出。<br><sub>适合：MV · 现场演出 · 也在：Live Coding · VJ、3D 渲染</sub> |
| [SHADERed](https://github.com/dfranx/SHADERed) | 4.8k | ⚪ 停更 | GLSL / C++ | 跨平台着色器 IDE，可以单步调试 shader、搭多 pass 特效。<br><sub>适合：特效素材</sub><br><sub>⚠️ 2023 年后未更新。</sub> |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | 🟢 活跃 | C++ | 开源的 MilkDrop 兼容可视化引擎，可嵌入播放器或做 MV 背景。<br><sub>适合：音乐可视化 · MV · 也在：音乐可视化</sub> |
| [Paper Shaders](https://github.com/paper-design/shaders) | 3.9k | 🟢 活跃 | TypeScript | Paper 团队的着色器组件：网格渐变、颗粒、金属光泽等，零依赖。<br><sub>适合：背景素材 · 网页</sub> |
| [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | 3.5k | 🟢 活跃 | GLSL / HLSL / WGSL | 大型着色器函数库：噪声、光照、颜色、滤镜，搭迷幻画面的积木。<br><sub>适合：特效素材</sub><br><sub>⚠️ 非商用免费；商用需要另外获得授权。</sub> |
| [ShaderGradient](https://github.com/ruucm/shadergradient) | 3.1k | 🟢 活跃 | TypeScript | 可调参数的动态 3D 渐变，近年很流行的流体渐变画风。<br><sub>适合：背景素材</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.7k | 🟡 放缓 | JavaScript | 浏览器里的实时视频合成器，模仿模拟信号合成器，几行代码就能出反馈、扭曲、色彩迷幻的画面。<br><sub>适合：现场 VJ · MV · 也在：Live Coding · VJ、故障 · 后期特效</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | 🟡 放缓 | JavaScript | WebGL 版 MilkDrop 音乐可视化，自带大量经典迷幻预设。<br><sub>适合：音乐可视化 · MV · 也在：音乐可视化</sub> |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.5k | 🟢 活跃 | C++（Windows） | MilkDrop 的延续版本，支持任意音源、双预设混合等新功能。<br><sub>适合：音乐可视化 · 也在：音乐可视化</sub> |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | 🟡 放缓 | GLSL | Demoscene「Shader Showdown」比赛用的实时着色器写码工具，现场写代码现场出画面。<br><sub>适合：现场演出 · 也在：Live Coding · VJ</sub> |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | 🟢 活跃 | GLSL | RetroArch 的着色器合集：CRT 扫描线、像素放大等复古显示效果。<br><sub>适合：复古后期 · 也在：像素 · 复古</sub> |
| [twigl](https://github.com/doxas/twigl) | 1.1k | 🟡 放缓 | GLSL | 极简 GLSL 在线编辑器，日本「推特 GLSL」圈常用，可以导出 GIF 和视频。<br><sub>适合：短片 · GIF · 也在：Live Coding · VJ</sub> |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 831 | 🟢 活跃 | JavaScript | 用类 JS 语法写 SDF 着色器，做出雕塑感的 3D 抽象造型。<br><sub>适合：MV · 生成艺术 · 也在：3D 渲染</sub> |
| [cables](https://github.com/cables-gl/cables) | 572 | 🟢 活跃 | 节点连线 / JS | 节点式可视化编程平台，在浏览器里连线做实时 WebGL 画面，常用于 MV 和演出视觉。<br><sub>适合：MV · 现场演出 · 也在：Live Coding · VJ、3D 渲染</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="live"></a>

## Live Coding · VJ

<img src="assets/styles/live.png" alt="Live Coding · VJ样图" width="240" align="right">

> 现场写代码出画面，视频合成器质感

共 7 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | 🟢 活跃 | Lua / JS 等 | 幻想主机（240×136 像素、16 色），demoscene 小体积作品和直播 Byte Jam 常用。<br><sub>适合：像素动画 · 现场 · 也在：像素 · 复古</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 活跃 | 节点连线 / C# | 原 Tooll3，开源实时动态图形软件，节点加时间轴，常用于音乐视频和现场演出。<br><sub>适合：MV · 现场演出 · 也在：着色器 · 迷幻光影、3D 渲染</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.7k | 🟡 放缓 | JavaScript | 浏览器里的实时视频合成器，模仿模拟信号合成器，几行代码就能出反馈、扭曲、色彩迷幻的画面。<br><sub>适合：现场 VJ · MV · 也在：故障 · 后期特效、着色器 · 迷幻光影</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [ossia score](https://github.com/ossia/score) | 2.1k | 🟢 活跃 | C++（图形界面） | 多媒体时间线编排工具，可同步音频、视频、灯光和着色器。<br><sub>适合：演出 · 装置</sub> |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | 🟡 放缓 | GLSL | Demoscene「Shader Showdown」比赛用的实时着色器写码工具，现场写代码现场出画面。<br><sub>适合：现场演出 · 也在：着色器 · 迷幻光影</sub> |
| [twigl](https://github.com/doxas/twigl) | 1.1k | 🟡 放缓 | GLSL | 极简 GLSL 在线编辑器，日本「推特 GLSL」圈常用，可以导出 GIF 和视频。<br><sub>适合：短片 · GIF · 也在：着色器 · 迷幻光影</sub> |
| [cables](https://github.com/cables-gl/cables) | 572 | 🟢 活跃 | 节点连线 / JS | 节点式可视化编程平台，在浏览器里连线做实时 WebGL 画面，常用于 MV 和演出视觉。<br><sub>适合：MV · 现场演出 · 也在：着色器 · 迷幻光影、3D 渲染</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="audio"></a>

## 音乐可视化 · Music Visualization

<img src="assets/styles/audio.png" alt="音乐可视化样图" width="240" align="right">

> 频谱、波形、MilkDrop 式随音乐律动

共 13 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [p5.js](https://github.com/processing/p5.js) | 24.3k | 🟢 活跃 | JavaScript | 最流行的创意编程库，在网页上画图、做交互和动画，中文教程也很多。<br><sub>适合：生成艺术 · MV · 也在：生成艺术 · 几何、粒子 · 流体 · 物理</sub><br><sub>⚠️ 导出视频需要额外步骤（逐帧保存或录屏）。</sub> |
| [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js) | 10.5k | 🟢 活跃 | TypeScript | 网页音频波形绘制与播放，可做波形动画和音频编辑界面。<br><sub>适合：音频波形</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 活跃 | C++ | C++ 创意编程框架，性能强，常用于互动装置、舞台视觉和音乐可视化。<br><sub>适合：演出 · 装置 · MV · 也在：生成艺术 · 几何、3D 渲染</sub> |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | 🟢 活跃 | Rust | Rust 创意编程框架，带音频和 OSC 模块，适合实时音画作品。<br><sub>适合：生成艺术 · 演出 · 也在：生成艺术 · 几何</sub> |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | 🟢 活跃 | C（命令行） | 终端里的音频频谱可视化。<br><sub>适合：音乐可视化 · 也在：ASCII · 终端</sub> |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | 🟢 活跃 | C++ | 开源的 MilkDrop 兼容可视化引擎，可嵌入播放器或做 MV 背景。<br><sub>适合：音乐可视化 · MV · 也在：着色器 · 迷幻光影</sub> |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | 🟢 活跃 | React / Vue | 国人开发的类 Apple Music 歌词组件：逐字高亮、弹性滚动、流体背景。<br><sub>适合：歌词 MV · 播放器 · 也在：动态文字 · 歌词</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | 🟢 活跃 | TypeScript（图形界面） | 把音频做成可视化视频的动效软件：频谱、波形、文字、3D 图层可组合导出。<br><sub>适合：音乐可视化 · MV · 也在：扁平 MG 动效</sub><br><sub>⚠️ 以图形界面为主。</sub> |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | 🟡 放缓 | JavaScript | WebGL 版 MilkDrop 音乐可视化，自带大量经典迷幻预设。<br><sub>适合：音乐可视化 · MV · 也在：着色器 · 迷幻光影</sub> |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.5k | 🟢 活跃 | C++（Windows） | MilkDrop 的延续版本，支持任意音源、双预设混合等新功能。<br><sub>适合：音乐可视化 · 也在：着色器 · 迷幻光影</sub> |
| [Musializer](https://github.com/tsoding/musializer) | 1.5k | 🟢 活跃 | C | C 语言写的音乐可视化工具，可以直接渲染输出成视频。<br><sub>适合：音乐可视化 · MV</sub> |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 968 | 🟢 活跃 | JavaScript | 高分辨率实时频谱分析器，柱状、圆形等频谱样式可调。<br><sub>适合：音乐可视化 · 也在：数据可视化动画</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [Remotion 音频图模板](https://github.com/remotion-dev/template-audiogram) | 275 | 🟢 活跃 | React / TS | Remotion 官方模板：把播客音频做成带波形和字幕的短视频。<br><sub>适合：短视频 · 播客 · 也在：短视频 · 字幕 · 快剪</sub><br><sub>⚠️ 授权条款同 Remotion。</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="3d"></a>

## 3D 渲染

<img src="assets/styles/3d.png" alt="3D 渲染样图" width="240" align="right">

> 三维场景、镜头运动、材质灯光

共 29 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 117k | 🟢 活跃 | JavaScript | 网页 3D 的事实标准：场景、材质、粒子、后期处理都有，案例极多。<br><sub>适合：MV · 网页 3D · 也在：粒子 · 流体 · 物理、着色器 · 迷幻光影</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 70.3k | 🟢 活跃 | React / TS | 用 React 组件写视频，渲染成 MP4，可批量生成；官方有字幕、音频可视化、three.js 等扩展包。<br><sub>适合：MV · 短视频 · 批量出片 · 也在：扁平 MG 动效、短视频 · 字幕 · 快剪、动态文字 · 歌词</sub><br><sub>⚠️ 个人和小公司免费（含商用），较大的公司需购买公司授权。</sub> |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | 33.5k | 🟢 活跃 | React / TS | 用 React 写 three.js 场景，可以配合 Remotion 渲染 3D 视频。<br><sub>适合：MV · 网页 3D</sub> |
| [Blender MCP](https://github.com/ahujasid/mcp-for-blender) | 33.2k | 🟢 活跃 | Python | 让大模型通过代码控制 Blender：建模、布光、做动画。<br><sub>适合：3D 动画 · 也在：AI 写代码出片</sub><br><sub>⚠️ 社区插件，不是 Blender 官方项目。</sub> |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | 🟢 活跃 | Python | Python 高性能并行计算，常用来写流体、弹性体、粒子等物理模拟。<br><sub>适合：物理模拟 · 也在：粒子 · 流体 · 物理</sub> |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | 26.3k | 🟢 活跃 | TypeScript | 微软团队维护的网页 3D 引擎，功能全，自带在线编辑工具。<br><sub>适合：网页 3D · MV</sub> |
| [Blender](https://github.com/blender/blender) | 21.6k | 🟢 活跃 | Python API | 开源 3D 软件，Python API 可以程序化生成场景和动画；Grease Pencil 能做 2D 手绘动画。<br><sub>适合：MV · 3D 动画 · 也在：手绘 · 白板 · 水彩</sub><br><sub>⚠️ GitHub 上是镜像，开发主站在 projects.blender.org。</sub> |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 20.2k | 🟢 活跃 | Python / three.js | AI 编程助手技能：照着参考图，用纯代码重建程序化的 three.js 3D 模型，可直接做动画。<br><sub>适合：3D 素材 · 也在：AI 写代码出片</sub> |
| [PlayCanvas](https://github.com/playcanvas/engine) | 17.2k | 🟢 活跃 | JavaScript | 网页 3D 引擎，支持 WebGL / WebGPU 和高斯泼溅。<br><sub>适合：网页 3D</sub> |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.7k | 🟢 活跃 | TypeScript | 大规模地理数据可视化：轨迹动画、3D 柱状地图等。<br><sub>适合：地图动画 · 也在：数据可视化动画</sub> |
| [Theatre.js](https://github.com/theatre-js/theatre) | 12.8k | ⚪ 停更 | TypeScript | 网页动画的可视化时间轴：代码里定义属性，界面里拖关键帧，常配 three.js 做 3D 镜头动画。<br><sub>适合：MV · 网页动画 · 也在：扁平 MG 动效</sub> |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | ⚪ 停更 | JavaScript | 伪 3D 扁平引擎，画出圆润可爱的扁平立体图形。<br><sub>适合：网页动画 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 多年未更新，功能简单稳定。</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 活跃 | C++ | C++ 创意编程框架，性能强，常用于互动装置、舞台视觉和音乐可视化。<br><sub>适合：演出 · 装置 · MV · 也在：生成艺术 · 几何、音乐可视化</sub> |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.3k | ⚪ 停更 | JavaScript | 几行代码生成动态 3D 背景：波浪、飞鸟、雾气、网格等。<br><sub>适合：背景素材 · 也在：生成艺术 · 几何</sub> |
| [ThreeUI](https://github.com/MengTo/threeui) | 7.1k | 🟢 活跃 | three.js | three.js 交互组件目录，每个组件都带可调参数和源码。<br><sub>适合：网页 3D · 素材</sub> |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | 🟢 活跃 | TypeScript | 蚂蚁集团开源的 Web 图形引擎，2D、3D、粒子、Lottie 都能用。<br><sub>适合：网页 3D · 互动 · 也在：粒子 · 流体 · 物理</sub> |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | 🟡 放缓 | C++ | C++ 创意编程框架，偏专业的实时图形与装置作品。<br><sub>适合：演出 · 装置 · 也在：生成艺术 · 几何</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 活跃 | 节点连线 / C# | 原 Tooll3，开源实时动态图形软件，节点加时间轴，常用于音乐视频和现场演出。<br><sub>适合：MV · 现场演出 · 也在：Live Coding · VJ、着色器 · 迷幻光影</sub> |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 2.9k | 🟢 活跃 | JavaScript | three.js 后期处理库：辉光、色差、故障、景深等。<br><sub>适合：3D 后期 · 也在：故障 · 后期特效</sub> |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | 🟢 活跃 | TypeScript | JavaScript 写的 3D 渲染器，直接把 3D 画面渲染在终端里。<br><sub>适合：终端动画 · 也在：ASCII · 终端</sub> |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | 🟢 活跃 | TypeScript | pixiv 出品，在 three.js 里使用 VRM 二次元虚拟形象。<br><sub>适合：二次元 MV · 虚拟形象 · 也在：二次元 · MMD · VRM</sub> |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 2.2k | 🟢 活跃 | JavaScript | 国人作品：让 AI 编程助手做产品发布片，自己写配乐，可以指着画面改。<br><sub>适合：产品宣传片 · 也在：AI 写代码出片、扁平 MG 动效</sub> |
| [VRM Add-on for Blender](https://github.com/saturday06/VRM-Addon-for-Blender) | 1.7k | 🟢 活跃 | Python | 在 Blender 里导入、编辑、导出 VRM 二次元模型。<br><sub>适合：二次元 MV · 也在：二次元 · MMD · VRM</sub> |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | ⚪ 停更 | JavaScript | 浏览器里的 3D 数学可视化：曲面、向量场、坐标网格，画面干净有质感。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub> |
| [Goo Engine](https://github.com/dillongoostudios/goo-engine) | 1.5k | 🟢 活跃 | Blender 定制版 | 专做动漫画风的 Blender 定制版，卡通着色控制更细。<br><sub>适合：二次元 3D 动画 · 也在：二次元 · MMD · VRM</sub> |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.2k | 🟢 活跃 | TypeScript | three.js 的粒子特效系统：火焰、爆炸、魔法等 VFX。<br><sub>适合：3D 特效 · 也在：粒子 · 流体 · 物理</sub> |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 831 | 🟢 活跃 | JavaScript | 用类 JS 语法写 SDF 着色器，做出雕塑感的 3D 抽象造型。<br><sub>适合：MV · 生成艺术 · 也在：着色器 · 迷幻光影</sub> |
| [cables](https://github.com/cables-gl/cables) | 572 | 🟢 活跃 | 节点连线 / JS | 节点式可视化编程平台，在浏览器里连线做实时 WebGL 画面，常用于 MV 和演出视觉。<br><sub>适合：MV · 现场演出 · 也在：Live Coding · VJ、着色器 · 迷幻光影</sub> |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 261 | 🟢 活跃 | TypeScript | 在 Babylon.js 里加载并播放 MMD 模型和动作，做二次元角色舞蹈 MV。<br><sub>适合：二次元 MV · 也在：二次元 · MMD · VRM</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="anime"></a>

## 二次元 · MMD · VRM

<img src="assets/styles/anime.png" alt="二次元 · MMD · VRM样图" width="240" align="right">

> 动漫角色、虚拟形象、舞蹈 MV

共 6 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | 5.7k | 🟡 放缓 | TypeScript | 用摄像头捕捉面部和身体动作，驱动 VRM / Live2D 角色。<br><sub>适合：虚拟形象</sub> |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | 🟢 活跃 | TypeScript | pixiv 出品，在 three.js 里使用 VRM 二次元虚拟形象。<br><sub>适合：二次元 MV · 虚拟形象 · 也在：3D 渲染</sub> |
| [VRM Add-on for Blender](https://github.com/saturday06/VRM-Addon-for-Blender) | 1.7k | 🟢 活跃 | Python | 在 Blender 里导入、编辑、导出 VRM 二次元模型。<br><sub>适合：二次元 MV · 也在：3D 渲染</sub> |
| [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | 1.5k | ⚪ 停更 | TypeScript | 在 PixiJS 里显示和驱动 Live2D 模型，做 2D 二次元角色动画。<br><sub>适合：二次元动画</sub> |
| [Goo Engine](https://github.com/dillongoostudios/goo-engine) | 1.5k | 🟢 活跃 | Blender 定制版 | 专做动漫画风的 Blender 定制版，卡通着色控制更细。<br><sub>适合：二次元 3D 动画 · 也在：3D 渲染</sub> |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 261 | 🟢 活跃 | TypeScript | 在 Babylon.js 里加载并播放 MMD 模型和动作，做二次元角色舞蹈 MV。<br><sub>适合：二次元 MV · 也在：3D 渲染</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="particle"></a>

## 粒子 · 流体 · 物理 · Particles & Physics

<img src="assets/styles/particle.png" alt="粒子 · 流体 · 物理样图" width="240" align="right">

> 烟雾、流体、烟花、碰撞模拟

共 13 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 117k | 🟢 活跃 | JavaScript | 网页 3D 的事实标准：场景、材质、粒子、后期处理都有，案例极多。<br><sub>适合：MV · 网页 3D · 也在：3D 渲染、着色器 · 迷幻光影</sub> |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.6k | 🟢 活跃 | TypeScript | 高性能 2D 渲染引擎（WebGL / WebGPU），适合大量精灵、滤镜和 2D 动效。<br><sub>适合：网页动画 · MV · 也在：扁平 MG 动效、生成艺术 · 几何</sub> |
| [particles.js](https://github.com/VincentGarreau/particles.js) | 30.2k | ⚪ 停更 | JavaScript | 经典的网页粒子背景库。<br><sub>适合：背景素材</sub><br><sub>⚠️ 多年未更新，新项目建议用 tsParticles。</sub> |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | 🟢 活跃 | Python | Python 高性能并行计算，常用来写流体、弹性体、粒子等物理模拟。<br><sub>适合：物理模拟 · 也在：3D 渲染</sub> |
| [p5.js](https://github.com/processing/p5.js) | 24.3k | 🟢 活跃 | JavaScript | 最流行的创意编程库，在网页上画图、做交互和动画，中文教程也很多。<br><sub>适合：生成艺术 · MV · 也在：生成艺术 · 几何、音乐可视化</sub><br><sub>⚠️ 导出视频需要额外步骤（逐帧保存或录屏）。</sub> |
| [Matter.js](https://github.com/liabru/matter-js) | 18.6k | 🟢 活跃 | JavaScript | 2D 物理引擎，碰撞、弹跳、堆叠等物理动画。<br><sub>适合：物理动画</sub> |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.8k | 🟡 放缓 | JavaScript | 浏览器里的实时流体模拟，彩色烟雾效果很出片。<br><sub>适合：特效素材 · 也在：着色器 · 迷幻光影</sub> |
| [canvas-confetti](https://github.com/catdad/canvas-confetti) | 12.8k | 🟡 放缓 | JavaScript | 一行代码放彩带和烟花效果。<br><sub>适合：网页特效</sub> |
| [tsParticles](https://github.com/tsparticles/tsparticles) | 9.1k | 🟢 活跃 | TypeScript | 粒子、彩带、烟花等效果库，改配置就能用。<br><sub>适合：网页特效</sub> |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | 🟢 活跃 | TypeScript | 蚂蚁集团开源的 Web 图形引擎，2D、3D、粒子、Lottie 都能用。<br><sub>适合：网页 3D · 互动 · 也在：3D 渲染</sub> |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.3k | 🟢 活跃 | TypeScript | 在真实网页界面上叠加 WebGL 流体、着色器和 3D 特效的组件库。<br><sub>适合：网页特效 · 也在：着色器 · 迷幻光影</sub> |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.2k | 🟢 活跃 | TypeScript | three.js 的粒子特效系统：火焰、爆炸、魔法等 VFX。<br><sub>适合：3D 特效 · 也在：3D 渲染</sub> |
| [manim-physics](https://github.com/Matheart/manim-physics) | 412 | 🟢 活跃 | Python | Manim 的物理模拟扩展：刚体、电磁场、波动、单摆等物理动画。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="glitch"></a>

## 故障 · 后期特效 · Glitch & Post FX

<img src="assets/styles/glitch.png" alt="故障 · 后期特效样图" width="240" align="right">

> RGB 偏移、扭曲、辉光、像素排序、合成

共 9 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 66.4k | 🟢 活跃 | C（命令行） | 几乎所有代码出片工具的底层：转码、拼接、滤镜、字幕烧录都能用命令行完成。<br><sub>适合：剪辑合成 · 后期 · 也在：短视频 · 字幕 · 快剪</sub><br><sub>⚠️ GitHub 上是镜像仓库。</sub> |
| [EffectCraft](https://github.com/storytold/effectcraft) | 8.4k | 🟢 活跃 | Rust（图形界面） | 从零写的开源合成软件，思路类似 After Effects：图层、关键帧、表达式、三百多种特效。<br><sub>适合：MG · 后期合成 · 也在：扁平 MG 动效</sub><br><sub>⚠️ 以图形界面为主，表达式部分可以写代码。</sub> |
| [Natron](https://github.com/NatronGitHub/Natron) | 5.6k | 🟢 活跃 | C++ / Python | 开源节点式合成软件，可用 Python 脚本控制，做后期合成和特效。<br><sub>适合：后期合成</sub> |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | 🟢 活跃 | C++（Windows） | 在 Windows 桌面上叠加 CRT、像素等复古着色器，录屏就能得到复古画面。<br><sub>适合：复古后期 · 也在：像素 · 复古</sub> |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 2.9k | 🟢 活跃 | JavaScript | three.js 后期处理库：辉光、色差、故障、景深等。<br><sub>适合：3D 后期 · 也在：3D 渲染</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.7k | 🟡 放缓 | JavaScript | 浏览器里的实时视频合成器，模仿模拟信号合成器，几行代码就能出反馈、扭曲、色彩迷幻的画面。<br><sub>适合：现场 VJ · MV · 也在：Live Coding · VJ、着色器 · 迷幻光影</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.2k | 🟢 活跃 | GLSL | 开源 GLSL 转场合集，可以接进 editly 等剪辑工具使用。<br><sub>适合：转场 · 也在：短视频 · 字幕 · 快剪</sub> |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | 🟢 活跃 | TypeScript | 给网页里的图片、视频、文字加 WebGL 特效：故障、RGB 偏移、扭曲等。<br><sub>适合：网页特效 · MV · 也在：动态文字 · 歌词</sub> |
| [pixelsort](https://github.com/satyarth/pixelsort) | 876 | 🟢 活跃 | Python | 像素排序故障艺术：按亮度等规则重新排列像素。<br><sub>适合：故障艺术</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="pixel"></a>

## 像素 · 复古 · Pixel & Retro

<img src="assets/styles/pixel.png" alt="像素 · 复古样图" width="240" align="right">

> 低分辨率、有限色板、CRT 扫描线

共 9 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [Pyxel](https://github.com/kitao/pyxel) | 18.5k | 🟢 活跃 | Python | Python 复古游戏引擎，16 色像素画面，也适合做像素风小动画。<br><sub>适合：像素动画</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 11.5k | 🟢 活跃 | JavaScript | 代码实现的影片画风工具箱：66 种现成画风（孟菲斯、地铁线路图、黑板等），让 AI 编程助手按画风出片，全部用代码绘制。<br><sub>适合：MV · 短片 · 也在：AI 写代码出片、扁平 MG 动效、手绘 · 白板 · 水彩</sub><br><sub>⚠️ 画风针对 Claude 调校，用其他模型效果可能不同。</sub> |
| [LÖVE](https://github.com/love2d/love) | 8.9k | 🟢 活跃 | Lua | 用 Lua 写 2D 游戏和动画的框架，像素风作品很多。<br><sub>适合：像素动画 · 小游戏</sub> |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | 🟢 活跃 | Lua / JS 等 | 幻想主机（240×136 像素、16 色），demoscene 小体积作品和直播 Byte Jam 常用。<br><sub>适合：像素动画 · 现场 · 也在：Live Coding · VJ</sub> |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | 🟢 活跃 | C++（Windows） | 在 Windows 桌面上叠加 CRT、像素等复古着色器，录屏就能得到复古画面。<br><sub>适合：复古后期 · 也在：故障 · 后期特效</sub> |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 3.9k | 🟢 活跃 | JavaScript | 244 个用代码写的像素特效动画：火焰、爆炸、魔法、天气等，可导出精灵图；附带 AI 编程助手技能。<br><sub>适合：像素特效素材 · 也在：AI 写代码出片</sub> |
| [WASM-4](https://github.com/aduros/wasm4) | 1.5k | 🟢 活跃 | 多种语言 | 极简幻想主机（160×160 像素、4 色），可以用多种语言写像素小作品。<br><sub>适合：像素动画</sub> |
| [Animate](https://github.com/cth9191/animate) | 1.4k | 🟢 活跃 | JavaScript / Canvas | Claude Code 技能：用单个 canvas 程序化绘制短动画，内置剪纸、排线墨水、Riso 印刷、速写本、数学、像素、等距 7 种画风。<br><sub>适合：讲解视频 · 短片 · 也在：AI 写代码出片、手绘 · 白板 · 水彩、数学讲解风</sub> |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | 🟢 活跃 | GLSL | RetroArch 的着色器合集：CRT 扫描线、像素放大等复古显示效果。<br><sub>适合：复古后期 · 也在：着色器 · 迷幻光影</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="ascii"></a>

## ASCII · 终端

<img src="assets/styles/ascii.png" alt="ASCII · 终端样图" width="240" align="right">

> 字符画、代码雨、终端里的文字特效

共 12 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [VHS](https://github.com/charmbracelet/vhs) | 21.3k | 🟢 活跃 | VHS 脚本 | 用脚本写好终端操作，自动录成 GIF 或视频，做命令行演示最方便。<br><sub>适合：讲解视频 · GIF · 也在：代码演示风</sub> |
| [asciinema](https://github.com/asciinema/asciinema) | 17.9k | 🟢 活跃 | Rust（命令行） | 录制终端会话，用网页播放器回放，体积小、文字可复制。<br><sub>适合：讲解视频 · 也在：代码演示风</sub> |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | ⚪ 停更 | JavaScript（命令行） | 录制终端操作，渲染成带窗口样式的 GIF 动图。<br><sub>适合：GIF · 也在：代码演示风</sub> |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | 🟢 活跃 | C（命令行） | 终端里的音频频谱可视化。<br><sub>适合：音乐可视化 · 也在：音乐可视化</sub> |
| [Chafa](https://github.com/hpjansson/chafa) | 5.4k | 🟢 活跃 | C（命令行） | 把图片和动画转成终端字符画，支持多种字符集和颜色模式。<br><sub>适合：字符画素材</sub> |
| [CMatrix](https://github.com/abishekvashok/cmatrix) | 5.3k | ⚪ 停更 | C（命令行） | 终端里的《黑客帝国》代码雨。<br><sub>适合：终端动画</sub> |
| [asciimatics](https://github.com/peterbrittain/asciimatics) | 4.3k | 🟢 活跃 | Python | Python 终端动画和字符界面库，可以搭字符画特效场景。<br><sub>适合：终端动画</sub> |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | 🟢 活跃 | Python | 终端文字特效库，几十种文字出场动画（燃烧、雨落、解码等）。<br><sub>适合：片头 · 文字特效 · 也在：动态文字 · 歌词</sub> |
| [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | 3.6k | ⚪ 停更 | Go（命令行） | 把图片和 GIF 转成彩色字符画的命令行工具。<br><sub>适合：字符画素材</sub> |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | 🟢 活跃 | TypeScript | JavaScript 写的 3D 渲染器，直接把 3D 画面渲染在终端里。<br><sub>适合：终端动画 · 也在：3D 渲染</sub> |
| [video-to-ascii](https://github.com/joelibaceta/video-to-ascii) | 1.9k | 🟡 放缓 | Python | 把视频在终端里以字符画的形式播放。<br><sub>适合：特效素材</sub> |
| [play.core](https://github.com/ertdfgcvb/play.core) | 544 | 🟡 放缓 | JavaScript | 用 JS 写 ASCII 字符动画的实验平台，每个字符就是一个“像素”。<br><sub>适合：生成艺术 · 也在：生成艺术 · 几何</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="data"></a>

## 数据可视化动画 · Data Animation

<img src="assets/styles/data.png" alt="数据可视化动画样图" width="240" align="right">

> 图表生长、条形图竞赛、Git 历史动画

共 18 个项目，按星数排序。

<br clear="right">

| 项目 | 星数 | 状态 | 写法 | 说明 |
| --- | ---: | :---: | --- | --- |
| [D3](https://github.com/d3/d3) | 114k | 🟢 活跃 | JavaScript | 数据可视化底层库，过渡动画能力强，常用于数据新闻动画。<br><sub>适合：数据视频 · 网页</sub> |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.1k | 🟢 活跃 | Python | 3Blue1Brown 本人做视频用的数学动画引擎（ManimGL），公式、坐标系、图形变换，经典蓝黑讲解画风。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub><br><sub>⚠️ 文档较少，新手建议先用社区版。</sub> |
| [Apache ECharts](https://github.com/apache/echarts) | 67.7k | 🟢 活跃 | TypeScript | 国内最常用的图表库之一，自带丰富的过渡动画和时间轴播放。<br><sub>适合：数据视频 · 网页</sub> |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.4k | ⚪ 停更 | JavaScript | 把排序、图、动态规划等算法的执行过程画成动画。<br><sub>适合：讲解视频 · 也在：代码演示风</sub> |
| [Manim 社区版](https://github.com/ManimCommunity/manim) | 42.2k | 🟢 活跃 | Python | Manim 社区维护版，文档和教程最全，B 站大量数学、物理、算法科普视频用它制作。<br><sub>适合：讲解视频 · 也在：数学讲解风、代码演示风</sub> |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | 23.4k | 🟢 活跃 | Python | Python 最基础的绘图库，用 FuncAnimation 就能做数据动画并导出视频。<br><sub>适合：数据视频</sub> |
| [Plotly](https://github.com/plotly/plotly.py) | 18.9k | 🟢 活跃 | Python | Python 交互图表库，支持按帧播放的动画图表。<br><sub>适合：数据动画</sub> |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.7k | 🟢 活跃 | TypeScript | 大规模地理数据可视化：轨迹动画、3D 柱状地图等。<br><sub>适合：地图动画 · 也在：3D 渲染</sub> |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | 🟡 放缓 | C++（命令行） | 把 Git 提交历史渲染成「代码生长」动画视频，经典的程序员视频素材。<br><sub>适合：程序员视频 · 也在：代码演示风</sub> |
| [Pts](https://github.com/williamngan/pts) | 5.4k | 🟢 活跃 | TypeScript | 围绕点、线、面几何关系的可视化与创意编程库。<br><sub>适合：生成艺术 · 也在：生成艺术 · 几何</sub> |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | 🟢 活跃 | Python | 把 Git 命令的效果画成图示和动画（底层基于 Manim），适合做 Git 教学视频。<br><sub>适合：讲解视频 · 也在：代码演示风</sub> |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | 🟢 活跃 | TypeScript | 由上百个 TypeScript 包组成的生成艺术与可视化工具集，作者长期维护。<br><sub>适合：生成艺术 · 也在：生成艺术 · 几何</sub> |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | ⚪ 停更 | Python | 基于 Manim 的机器学习概念动画：神经网络、卷积等结构的讲解动画。<br><sub>适合：讲解视频 · 也在：数学讲解风</sub> |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3k | 🟢 活跃 | React / TS | 输入一个话题，生成黑底动态图形讲解视频（带配音和字幕），画面全部由代码渲染。<br><sub>适合：讲解视频 · 也在：AI 写代码出片、扁平 MG 动效</sub> |
| [gganimate](https://github.com/thomasp85/gganimate) | 2k | 🟡 放缓 | R | R 语言 ggplot2 的动画扩展，把静态图表变成动画。<br><sub>适合：数据视频</sub> |
| [Logstalgia](https://github.com/acaudwell/Logstalgia) | 1.8k | 🟡 放缓 | C++（命令行） | 把网站访问日志变成乒乓球式的动画。<br><sub>适合：趣味可视化</sub> |
| [bar_chart_race](https://github.com/dexplo/bar_chart_race) | 1.5k | ⚪ 停更 | Python | 几行 Python 生成「条形图竞赛」动画视频。<br><sub>适合：数据视频</sub> |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 968 | 🟢 活跃 | JavaScript | 高分辨率实时频谱分析器，柱状、圆形等频谱样式可调。<br><sub>适合：音乐可视化 · 也在：音乐可视化</sub><br><sub>⚠️ AGPL-3.0：用在对外提供的网络服务里时，需要公开修改后的源码。</sub> |

<sub>[↑ 回到画风索引](#index)</sub>

<a name="all"></a>

## 全部项目

<details>
<summary>展开全部 159 个项目（按星数排序）</summary>

| 项目 | 星数 | 画风 | 状态 |
| --- | ---: | --- | :---: |
| [three.js](https://github.com/mrdoob/three.js) | 117k | [3D 渲染](#3d)、[粒子 · 流体 · 物理](#particle)、[着色器 · 迷幻光影](#shader) | 🟢 |
| [D3](https://github.com/d3/d3) | 114k | [数据可视化动画](#data) | 🟢 |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.1k | [数学讲解风](#math)、[数据可视化动画](#data) | 🟢 |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 78.1k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg)、[动态文字 · 歌词](#type)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [anime.js](https://github.com/juliangarnier/anime) | 74.2k | [扁平 MG 动效](#mg)、[动态文字 · 歌词](#type) | 🟢 |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.5k | [代码演示风](#code)、[扁平 MG 动效](#mg) | 🟢 |
| [Remotion](https://github.com/remotion-dev/remotion) | 70.3k | [扁平 MG 动效](#mg)、[短视频 · 字幕 · 快剪](#short)、[动态文字 · 歌词](#type)、[3D 渲染](#3d) | 🟢 |
| [Apache ECharts](https://github.com/apache/echarts) | 67.7k | [数据可视化动画](#data) | 🟢 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 66.4k | [短视频 · 字幕 · 快剪](#short)、[故障 · 后期特效](#glitch) | 🟢 |
| [React Bits](https://github.com/DavidHDev/react-bits) | 51.1k | [扁平 MG 动效](#mg)、[动态文字 · 歌词](#type)、[着色器 · 迷幻光影](#shader) | 🟢 |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.4k | [代码演示风](#code)、[数据可视化动画](#data) | ⚪ |
| [Slidev](https://github.com/slidevjs/slidev) | 49.3k | [代码演示风](#code) | 🟢 |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.6k | [扁平 MG 动效](#mg)、[粒子 · 流体 · 物理](#particle)、[生成艺术 · 几何](#gen) | 🟢 |
| [Manim 社区版](https://github.com/ManimCommunity/manim) | 42.2k | [数学讲解风](#math)、[数据可视化动画](#data)、[代码演示风](#code) | 🟢 |
| [Motion](https://github.com/motiondivision/motion) | 34.8k | [扁平 MG 动效](#mg) | 🟢 |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | 33.5k | [3D 渲染](#3d) | 🟢 |
| [Blender MCP](https://github.com/ahujasid/mcp-for-blender) | 33.2k | [3D 渲染](#3d)、[AI 写代码出片](#agent) | 🟢 |
| [Lottie](https://github.com/airbnb/lottie-web) | 32.3k | [扁平 MG 动效](#mg) | 🟡 |
| [particles.js](https://github.com/VincentGarreau/particles.js) | 30.2k | [粒子 · 流体 · 物理](#particle) | ⚪ |
| [GSAP](https://github.com/greensock/GSAP) | 30.1k | [扁平 MG 动效](#mg)、[动态文字 · 歌词](#type) | 🟡 |
| [react-spring](https://github.com/pmndrs/react-spring) | 29.3k | [扁平 MG 动效](#mg) | 🟢 |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | [粒子 · 流体 · 物理](#particle)、[3D 渲染](#3d) | 🟢 |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | 26.3k | [3D 渲染](#3d) | 🟢 |
| [p5.js](https://github.com/processing/p5.js) | 24.3k | [生成艺术 · 几何](#gen)、[粒子 · 流体 · 物理](#particle)、[音乐可视化](#audio) | 🟢 |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | 23.4k | [数据可视化动画](#data) | 🟢 |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.1k | [扁平 MG 动效](#mg)、[动态文字 · 歌词](#type) | 🟢 |
| [Blender](https://github.com/blender/blender) | 21.6k | [3D 渲染](#3d)、[手绘 · 白板 · 水彩](#hand) | 🟢 |
| [Rough.js](https://github.com/rough-stuff/rough) | 21.3k | [手绘 · 白板 · 水彩](#hand) | ⚪ |
| [VHS](https://github.com/charmbracelet/vhs) | 21.3k | [代码演示风](#code)、[ASCII · 终端](#ascii) | 🟢 |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 20.2k | [3D 渲染](#3d)、[AI 写代码出片](#agent) | 🟢 |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 19.7k | [扁平 MG 动效](#mg)、[代码演示风](#code)、[数学讲解风](#math) | 🟢 |
| [mo.js](https://github.com/mojs/mojs) | 18.9k | [扁平 MG 动效](#mg) | 🟢 |
| [Plotly](https://github.com/plotly/plotly.py) | 18.9k | [数据可视化动画](#data) | 🟢 |
| [Matter.js](https://github.com/liabru/matter-js) | 18.6k | [粒子 · 流体 · 物理](#particle) | 🟢 |
| [Pyxel](https://github.com/kitao/pyxel) | 18.5k | [像素 · 复古](#pixel) | 🟢 |
| [asciinema](https://github.com/asciinema/asciinema) | 17.9k | [代码演示风](#code)、[ASCII · 终端](#ascii) | 🟢 |
| [PlayCanvas](https://github.com/playcanvas/engine) | 17.2k | [3D 渲染](#3d) | 🟢 |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.8k | [粒子 · 流体 · 物理](#particle)、[着色器 · 迷幻光影](#shader) | 🟡 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 16.4k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [Typed.js](https://github.com/mattboldt/typed.js) | 16.3k | [动态文字 · 歌词](#type) | 🟡 |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | [代码演示风](#code)、[ASCII · 终端](#ascii) | ⚪ |
| [Vivus](https://github.com/maxwellito/vivus) | 15.5k | [手绘 · 白板 · 水彩](#hand) | ⚪ |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | [生成艺术 · 几何](#gen)、[扁平 MG 动效](#mg) | 🟢 |
| [MoviePy](https://github.com/Zulko/moviepy) | 15.1k | [短视频 · 字幕 · 快剪](#short) | 🟢 |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.7k | [数据可视化动画](#data)、[3D 渲染](#3d) | 🟢 |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | [数据可视化动画](#data)、[代码演示风](#code) | 🟡 |
| [Theatre.js](https://github.com/theatre-js/theatre) | 12.8k | [扁平 MG 动效](#mg)、[3D 渲染](#3d) | ⚪ |
| [canvas-confetti](https://github.com/catdad/canvas-confetti) | 12.8k | [粒子 · 流体 · 物理](#particle) | 🟡 |
| [SVG.js](https://github.com/svgdotjs/svg.js) | 11.9k | [扁平 MG 动效](#mg) | 🟢 |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 11.5k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg)、[手绘 · 白板 · 水彩](#hand)、[像素 · 复古](#pixel) | 🟢 |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | [扁平 MG 动效](#mg)、[3D 渲染](#3d) | ⚪ |
| [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js) | 10.5k | [音乐可视化](#audio) | 🟢 |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | [生成艺术 · 几何](#gen)、[音乐可视化](#audio)、[3D 渲染](#3d) | 🟢 |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.7k | [手绘 · 白板 · 水彩](#hand)、[动态文字 · 歌词](#type) | ⚪ |
| [tsParticles](https://github.com/tsparticles/tsparticles) | 9.1k | [粒子 · 流体 · 物理](#particle) | 🟢 |
| [LÖVE](https://github.com/love2d/love) | 8.9k | [像素 · 复古](#pixel) | 🟢 |
| [Two.js](https://github.com/jonobr1/two.js) | 8.7k | [扁平 MG 动效](#mg)、[生成艺术 · 几何](#gen) | 🟢 |
| [EffectCraft](https://github.com/storytold/effectcraft) | 8.4k | [扁平 MG 动效](#mg)、[故障 · 后期特效](#glitch) | 🟢 |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.3k | [3D 渲染](#3d)、[生成艺术 · 几何](#gen) | ⚪ |
| [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | 7.1k | [着色器 · 迷幻光影](#shader) | 🟡 |
| [ThreeUI](https://github.com/MengTo/threeui) | 7.1k | [3D 渲染](#3d) | 🟢 |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | [生成艺术 · 几何](#gen)、[音乐可视化](#audio) | 🟢 |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | [音乐可视化](#audio)、[ASCII · 终端](#ascii) | 🟢 |
| [Remotion Skills](https://github.com/remotion-dev/skills) | 6.2k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg) | 🟢 |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | [像素 · 复古](#pixel)、[Live Coding · VJ](#live) | 🟢 |
| [css-doodle](https://github.com/css-doodle/css-doodle) | 6.1k | [生成艺术 · 几何](#gen) | 🟢 |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | [3D 渲染](#3d)、[粒子 · 流体 · 物理](#particle) | 🟢 |
| [PAG](https://github.com/Tencent/libpag) | 5.8k | [扁平 MG 动效](#mg) | 🟢 |
| [Shaders](https://github.com/shader-effects-inc/shaders) | 5.8k | [着色器 · 迷幻光影](#shader) | 🟢 |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | 5.7k | [二次元 · MMD · VRM](#anime) | 🟡 |
| [Natron](https://github.com/NatronGitHub/Natron) | 5.6k | [故障 · 后期特效](#glitch) | 🟢 |
| [editly](https://github.com/mifi/editly) | 5.6k | [短视频 · 字幕 · 快剪](#short)、[动态文字 · 歌词](#type) | 🟡 |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | [生成艺术 · 几何](#gen)、[3D 渲染](#3d) | 🟡 |
| [Code Hike](https://github.com/code-hike/codehike) | 5.4k | [代码演示风](#code) | 🟡 |
| [Chafa](https://github.com/hpjansson/chafa) | 5.4k | [ASCII · 终端](#ascii) | 🟢 |
| [Pts](https://github.com/williamngan/pts) | 5.4k | [生成艺术 · 几何](#gen)、[数据可视化动画](#data) | 🟢 |
| [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | 5.4k | [着色器 · 迷幻光影](#shader) | 🟢 |
| [canvas-sketch](https://github.com/mattdesl/canvas-sketch) | 5.3k | [生成艺术 · 几何](#gen) | 🟢 |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.3k | [着色器 · 迷幻光影](#shader)、[粒子 · 流体 · 物理](#particle) | 🟢 |
| [CMatrix](https://github.com/abishekvashok/cmatrix) | 5.3k | [ASCII · 终端](#ascii) | ⚪ |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | [Live Coding · VJ](#live)、[着色器 · 迷幻光影](#shader)、[3D 渲染](#3d) | 🟢 |
| [SHADERed](https://github.com/dfranx/SHADERed) | 4.8k | [着色器 · 迷幻光影](#shader) | ⚪ |
| [html-video](https://github.com/nexu-io/html-video) | 4.8k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg)、[动态文字 · 歌词](#type) | 🟢 |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | [代码演示风](#code)、[数据可视化动画](#data) | 🟢 |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | [音乐可视化](#audio)、[着色器 · 迷幻光影](#shader) | 🟢 |
| [OpenFilm](https://github.com/openfilm/openfilm) | 4.4k | [AI 写代码出片](#agent)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | [像素 · 复古](#pixel)、[故障 · 后期特效](#glitch) | 🟢 |
| [asciimatics](https://github.com/peterbrittain/asciimatics) | 4.3k | [ASCII · 终端](#ascii) | 🟢 |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | [ASCII · 终端](#ascii)、[动态文字 · 歌词](#type) | 🟢 |
| [VAP](https://github.com/Tencent/vap) | 4.2k | [扁平 MG 动效](#mg) | 🟢 |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | [扁平 MG 动效](#mg)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [Paper Shaders](https://github.com/paper-design/shaders) | 3.9k | [着色器 · 迷幻光影](#shader) | 🟢 |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 3.9k | [像素 · 复古](#pixel)、[AI 写代码出片](#agent) | 🟢 |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | [生成艺术 · 几何](#gen)、[数据可视化动画](#data) | 🟢 |
| [onetake](https://github.com/feitangyuan/onetake) | 3.7k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg) | 🟢 |
| [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | 3.6k | [ASCII · 终端](#ascii) | ⚪ |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | [数学讲解风](#math)、[数据可视化动画](#data) | ⚪ |
| [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | 3.5k | [着色器 · 迷幻光影](#shader) | 🟢 |
| [FFCreator](https://github.com/tnfe/FFCreator) | 3.2k | [短视频 · 字幕 · 快剪](#short) | 🟡 |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | [扁平 MG 动效](#mg)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [ShaderGradient](https://github.com/ruucm/shadergradient) | 3.1k | [着色器 · 迷幻光影](#shader) | 🟢 |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3k | [AI 写代码出片](#agent)、[数据可视化动画](#data)、[扁平 MG 动效](#mg) | 🟢 |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 2.9k | [故障 · 后期特效](#glitch)、[3D 渲染](#3d) | 🟢 |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.7k | [Live Coding · VJ](#live)、[故障 · 后期特效](#glitch)、[着色器 · 迷幻光影](#shader) | 🟡 |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | 2.7k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg) | 🟢 |
| [Pixel2Motion](https://github.com/nolangz/pixel2motion) | 2.6k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg) | 🟢 |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | [ASCII · 终端](#ascii)、[3D 渲染](#3d) | 🟢 |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | [二次元 · MMD · VRM](#anime)、[3D 渲染](#3d) | 🟢 |
| [Code2Video](https://github.com/showlab/Code2Video) | 2.2k | [数学讲解风](#math)、[AI 写代码出片](#agent) | 🟢 |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.2k | [短视频 · 字幕 · 快剪](#short)、[故障 · 后期特效](#glitch) | 🟢 |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 2.2k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg)、[3D 渲染](#3d) | 🟢 |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | [动态文字 · 歌词](#type)、[音乐可视化](#audio) | 🟢 |
| [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) | 2.1k | [手绘 · 白板 · 水彩](#hand) | 🟢 |
| [ossia score](https://github.com/ossia/score) | 2.1k | [Live Coding · VJ](#live) | 🟢 |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2k | [AI 写代码出片](#agent)、[短视频 · 字幕 · 快剪](#short)、[动态文字 · 歌词](#type) | 🟢 |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | [音乐可视化](#audio)、[扁平 MG 动效](#mg) | 🟢 |
| [gganimate](https://github.com/thomasp85/gganimate) | 2k | [数据可视化动画](#data) | 🟡 |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | [音乐可视化](#audio)、[着色器 · 迷幻光影](#shader) | 🟡 |
| [video-to-ascii](https://github.com/joelibaceta/video-to-ascii) | 1.9k | [ASCII · 终端](#ascii) | 🟡 |
| [Logstalgia](https://github.com/acaudwell/Logstalgia) | 1.8k | [数据可视化动画](#data) | 🟡 |
| [Splitting](https://github.com/shshaw/Splitting) | 1.8k | [动态文字 · 歌词](#type) | ⚪ |
| [VRM Add-on for Blender](https://github.com/saturday06/VRM-Addon-for-Blender) | 1.7k | [二次元 · MMD · VRM](#anime)、[3D 渲染](#3d) | 🟢 |
| [remocn](https://github.com/Remocn/remocn) | 1.7k | [扁平 MG 动效](#mg)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [WASM-4](https://github.com/aduros/wasm4) | 1.5k | [像素 · 复古](#pixel) | 🟢 |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.5k | [音乐可视化](#audio)、[着色器 · 迷幻光影](#shader) | 🟢 |
| [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | 1.5k | [二次元 · MMD · VRM](#anime) | ⚪ |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | [数学讲解风](#math)、[3D 渲染](#3d) | ⚪ |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | [着色器 · 迷幻光影](#shader)、[Live Coding · VJ](#live) | 🟡 |
| [Musializer](https://github.com/tsoding/musializer) | 1.5k | [音乐可视化](#audio) | 🟢 |
| [Goo Engine](https://github.com/dillongoostudios/goo-engine) | 1.5k | [二次元 · MMD · VRM](#anime)、[3D 渲染](#3d) | 🟢 |
| [bar_chart_race](https://github.com/dexplo/bar_chart_race) | 1.5k | [数据可视化动画](#data) | ⚪ |
| [Animate](https://github.com/cth9191/animate) | 1.4k | [AI 写代码出片](#agent)、[手绘 · 白板 · 水彩](#hand)、[像素 · 复古](#pixel)、[数学讲解风](#math) | 🟢 |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | [像素 · 复古](#pixel)、[着色器 · 迷幻光影](#shader) | 🟢 |
| [Diffusion Studio Core](https://github.com/diffusionstudio/core) | 1.3k | [短视频 · 字幕 · 快剪](#short) | 🟡 |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 1.2k | [AI 写代码出片](#agent)、[手绘 · 白板 · 水彩](#hand)、[生成艺术 · 几何](#gen) | 🟢 |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.2k | [数学讲解风](#math)、[扁平 MG 动效](#mg) | 🟡 |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.2k | [手绘 · 白板 · 水彩](#hand)、[生成艺术 · 几何](#gen) | 🟢 |
| [motion-skills](https://github.com/iart-ai/motion-skills) | 1.2k | [AI 写代码出片](#agent)、[扁平 MG 动效](#mg) | 🟢 |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.2k | [粒子 · 流体 · 物理](#particle)、[3D 渲染](#3d) | 🟢 |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | [故障 · 后期特效](#glitch)、[动态文字 · 歌词](#type) | 🟢 |
| [Etro](https://github.com/etro-js/etro) | 1.2k | [短视频 · 字幕 · 快剪](#short) | 🟢 |
| [twigl](https://github.com/doxas/twigl) | 1.1k | [着色器 · 迷幻光影](#shader)、[Live Coding · VJ](#live) | 🟡 |
| [OPENRNDR](https://github.com/openrndr/openrndr) | 985 | [生成艺术 · 几何](#gen) | 🟢 |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 974 | [数学讲解风](#math)、[代码演示风](#code) | 🟢 |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 968 | [音乐可视化](#audio)、[数据可视化动画](#data) | 🟢 |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | 937 | [扁平 MG 动效](#mg) | 🟢 |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | 936 | [数学讲解风](#math)、[AI 写代码出片](#agent) | 🟢 |
| [pixelsort](https://github.com/satyarth/pixelsort) | 876 | [故障 · 后期特效](#glitch) | 🟢 |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 831 | [着色器 · 迷幻光影](#shader)、[3D 渲染](#3d) | 🟢 |
| [cables](https://github.com/cables-gl/cables) | 572 | [Live Coding · VJ](#live)、[着色器 · 迷幻光影](#shader)、[3D 渲染](#3d) | 🟢 |
| [play.core](https://github.com/ertdfgcvb/play.core) | 544 | [ASCII · 终端](#ascii)、[生成艺术 · 几何](#gen) | 🟡 |
| [Processing](https://github.com/processing/processing4) | 532 | [生成艺术 · 几何](#gen) | 🟢 |
| [DrawBot](https://github.com/typemytype/drawbot) | 455 | [动态文字 · 歌词](#type)、[生成艺术 · 几何](#gen) | 🟢 |
| [manim-physics](https://github.com/Matheart/manim-physics) | 412 | [数学讲解风](#math)、[粒子 · 流体 · 物理](#particle) | 🟢 |
| [Coldtype](https://github.com/coldtype/coldtype) | 341 | [动态文字 · 歌词](#type)、[生成艺术 · 几何](#gen) | 🟢 |
| [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | 326 | [数学讲解风](#math) | 🟢 |
| [Remotion TikTok 模板](https://github.com/remotion-dev/template-tiktok) | 301 | [短视频 · 字幕 · 快剪](#short)、[动态文字 · 歌词](#type) | 🟢 |
| [Remotion 音频图模板](https://github.com/remotion-dev/template-audiogram) | 275 | [音乐可视化](#audio)、[短视频 · 字幕 · 快剪](#short) | 🟢 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 261 | [二次元 · MMD · VRM](#anime)、[3D 渲染](#3d) | 🟢 |

</details>

## 相关合集

- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding)：创意编程资源大全，覆盖教程、书籍和工具（英文）。
- [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)：用 Claude Opus 5.5 写代码做出的视频，附提示词。
- [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills)：让编程助手做视频的技能合集。其中部分项目会调用生成模型，和本仓库的收录标准不同。

## 参与贡献

发现好项目？欢迎[提 Issue 推荐](https://github.com/syydaniel/awesome-code-animation/issues/new/choose)，或者直接修改 [`data/projects.json`](data/projects.json) 提 Pull Request，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
README 和网页版都由 `python scripts/build.py` 从数据文件自动生成，请不要直接改 README。

如果这份合集帮到了你，点个 ⭐ Star 能让更多人找到它。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=syydaniel/awesome-code-animation&type=Date)](https://star-history.com/#syydaniel/awesome-code-animation&Date)

## 许可

本仓库的整理内容以 [CC0 1.0](LICENSE) 发布，可以自由使用。各项目的许可证以其仓库为准，商用前请自行核对。
