<div align="center">

<img src="assets/banner.en.png" alt="Awesome Code Animation" width="100%">

# Awesome Code Animation

**Open-source tools for making animations and music videos with code, indexed by visual style.** [Chinese version](README.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![GitHub Stars](https://img.shields.io/github/stars/syydaniel/awesome-code-animation?style=social)](https://github.com/syydaniel/awesome-code-animation) ![projects](https://img.shields.io/badge/projects-485-2E49D4) ![styles](https://img.shields.io/badge/styles-17%2B21-9265D9) ![active](https://img.shields.io/badge/active-362-1E8A4B) ![updated](https://img.shields.io/badge/updated-2026--11--23-5B6273)

**[🌌 3D style gateway](https://syydaniel.github.io/awesome-code-animation/?lang=en)**<sub> (spin the style carousel, open a gallery of picks for each style)</sub> · **[🌐 Web version](https://syydaniel.github.io/awesome-code-animation/?lang=en#table-sec)**<sub> (filter by style, search, sort)</sub> · **[🕸️ Relationship graph](https://syydaniel.github.io/awesome-code-animation/?lang=en#graph-sec)** · **[🎨 Style index](#index)**

[Latest](#latest) · [three.js films](#threejs) · [Style index](#index) · [Niche styles](#niche) · [Relationships](#relations) · [Rules](#rules) · [All projects](#all) · [Suggest a project](https://github.com/syydaniel/awesome-code-animation/issues/new/choose)

⭐ **Find it useful? [Star the repo](https://github.com/syydaniel/awesome-code-animation)** so you can come back for new additions, and so more people can find it.

</div>

<a name="showcase"></a>

## 🎬 Showcase

[![Clashing Styles](docs/showcase/huafeng-buhe-cover.en.jpg)](https://syydaniel.github.io/awesome-code-animation/?lang=en#showcase)

**Clashing Styles** · by [syydaniel](https://github.com/syydaniel)

[▶ Watch the full film, with sound](https://syydaniel.github.io/awesome-code-animation/?lang=en#showcase) · [Watch on Bilibili](https://www.bilibili.com/video/BV1DNxU6WEqv/)

The promo film for this list. He lives in a line of code, she sits on a sheet of watercolor paper, and they keep switching styles to reach each other, always one frame apart. The film moves through 18 styles and 28 looks. All of it is rendered by code, with no AI-generated video, and each shot names its tools in the corner.

The song's lyrics, music and vocals are AI-made: Claude Code wrote the lyrics, and ACE-Step 1.5 composed and sang. Claude Code also wrote the code. Edited in DaVinci Resolve.

The 159 and 18 at the end were the numbers when the film was made. The list has grown since, and the 18th style, AI-written code, no longer has its own category. Shiki and Claude Code are not in this list. Every other tool is. The song is sung in Chinese.

Built with: [Manim Community](https://github.com/ManimCommunity/manim) · [MathBox](https://github.com/unconed/mathbox) · [GSAP](https://github.com/greensock/GSAP) · [anime.js](https://github.com/juliangarnier/anime) · [mo.js](https://github.com/mojs/mojs) · [Zdog](https://github.com/metafizzy/zdog) · [PixiJS](https://github.com/pixijs/pixijs) · [Shiki](https://github.com/shikijs/shiki) · [Splitting](https://github.com/shshaw/Splitting) · [Claude Code](https://github.com/anthropics/claude-code) · [p5.brush](https://github.com/acamposuribe/p5.brush) · [Rough.js](https://github.com/rough-stuff/rough) · [p5.js](https://github.com/processing/p5.js) · [Paper.js](https://github.com/paperjs/paper.js) · [LYGIA](https://github.com/patriciogonzalezvivo/lygia) · [Paper Shaders](https://github.com/paper-design/shaders) · [Hydra](https://github.com/hydra-synth/hydra) · [Butterchurn](https://github.com/jberg/butterchurn) · [three.js](https://github.com/mrdoob/three.js) · [postprocessing](https://github.com/pmndrs/postprocessing) · [Vanta.js](https://github.com/tengbao/vanta) · [three-vrm](https://github.com/pixiv/three-vrm) · [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) · [Matter.js](https://github.com/liabru/matter-js) · [Taichi](https://github.com/taichi-dev/taichi) · [pixelsort](https://github.com/satyarth/pixelsort) · [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) · [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) · [D3](https://github.com/d3/d3) · [Apache ECharts](https://github.com/apache/echarts) · [Gource](https://github.com/acaudwell/Gource) · [deck.gl](https://github.com/visgl/deck.gl) · [GL Transitions](https://github.com/gl-transitions/gl-transitions)

<details><summary>Which tools made each of the 18 styles and 28 looks</summary>

| Style | Tools | At | How it's used |
| --- | --- | --- | --- |
| [Math Explainer](#math) | [Manim Community](https://github.com/ManimCommunity/manim) | [00:10](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=10) | Every frame is rendered by Manim Community, then played back on the beat |
|  | [MathBox](https://github.com/unconed/mathbox) | [01:13](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=73) | A 3D surface that folds into a heart-shaped level set on the beat, with the equation beside it |
| [Motion Graphics](#mg) | [GSAP](https://github.com/greensock/GSAP) · [anime.js](https://github.com/juliangarnier/anime) · [mo.js](https://github.com/mojs/mojs) | [00:52](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=52) | GSAP and anime.js timelines, with bursts and streaks from mo.js |
|  | [Zdog](https://github.com/metafizzy/zdog) | [02:40](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=160) | A toy box where the characters and every prop are Zdog shapes |
|  | [PixiJS](https://github.com/pixijs/pixijs) | [02:41](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=161) | A neon night street, with wet reflections, glow and shockwaves from pixi-filters |
| [Code & Terminal Demo](#code) | [Shiki](https://github.com/shikijs/shiki) | [00:11](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=11) | The editor shows this film's own script, highlighted by Shiki |
| [Kinetic Type & Lyrics](#type) | [Splitting](https://github.com/shshaw/Splitting) · [GSAP](https://github.com/greensock/GSAP) | [00:49](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=49) | Splitting breaks up the glyphs and GSAP drives each one |
| [Shorts, Captions & Editing](#short) | [GSAP](https://github.com/greensock/GSAP) | [01:37](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=97) | Phones slide past while captions bounce in one word at a time |
| AI-written code | [Claude Code](https://github.com/anthropics/claude-code) | [00:08](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=8) | A terminal prints this film's file names, commands and source next to a preview window |
| [Hand-drawn & Whiteboard](#hand) | [p5.brush](https://github.com/acamposuribe/p5.brush) · [Rough.js](https://github.com/rough-stuff/rough) | [00:23](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=23) | p5.brush paints the watercolor and Rough.js draws the pencil lines |
| [Generative Art](#gen) | [p5.js](https://github.com/processing/p5.js) | [01:11](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=71) | A flow-field print whose lines bend around the character, leaving it as negative space |
|  | [Paper.js](https://github.com/paperjs/paper.js) | [00:34](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=34) | A liquid Bauhaus poster of vector paths that morph on the beat |
| [Shaders & Psychedelic](#shader) | [LYGIA](https://github.com/patriciogonzalezvivo/lygia) · [Paper Shaders](https://github.com/paper-design/shaders) | [01:18](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=78) | Color fields from LYGIA's GLSL functions, with a vein layer from Paper Shaders' neuro-noise |
| [Live Coding & VJ](#live) | [Hydra](https://github.com/hydra-synth/hydra) | [01:22](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=82) | The code on screen is the code running: each finished line changes the picture |
| [Music Visualization](#audio) | [Butterchurn](https://github.com/jberg/butterchurn) | [01:23](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=83) | Butterchurn is fed the song's own audio, over a real spectrum on the ground line |
| [3D](#3d) | [three.js](https://github.com/mrdoob/three.js) · [postprocessing](https://github.com/pmndrs/postprocessing) | [00:54](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=54) | A PBR character, mirror floor and glowing grid, with bloom and depth of field |
|  | [Vanta.js](https://github.com/tengbao/vanta) | [00:50](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=50) | Vanta.js birds flock around the character and sometimes form a heart |
| [Anime, MMD & VRM](#anime) | [three-vrm](https://github.com/pixiv/three-vrm) | [02:32](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=152) | The same model as the 3D world, restyled with MToon toon shading |
| [Particles & Physics](#particle) | [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | [01:24](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=84) | A GPU fluid solver, with the scarf pouring ink into the flow |
|  | [Matter.js](https://github.com/liabru/matter-js) | [00:46](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=46) | The title's glyphs and black blocks rain down and land on the beat |
|  | [Taichi](https://github.com/taichi-dev/taichi) | [01:45](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=105) | 104,000 MLS-MPM particles, baked ahead of time to an image sequence |
| [Glitch & Post FX](#glitch) | [postprocessing](https://github.com/pmndrs/postprocessing) · [pixelsort](https://github.com/satyarth/pixelsort) | [01:26](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=86) | Plates sorted by pixelsort, with glitch and chromatic aberration from postprocessing |
| [Pixel & Retro](#pixel) | [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | [00:56](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=56) | A 320×180 8-bit platformer, through the crt-lottes CRT shader |
| [ASCII & Terminal](#ascii) | [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | [00:15](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=15) | Boot text from TerminalTextEffects, with the scene turned into characters by brightness |
| [Data Animation](#data) | [D3](https://github.com/d3/d3) | [00:37](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=37) | A dark dashboard charting the GitHub stars of projects in this list |
|  | [Apache ECharts](https://github.com/apache/echarts) | [02:43](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=163) | A constellation of all 159 projects the list had at the time |
|  | [Gource](https://github.com/acaudwell/Gource) | [01:44](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=104) | The real commit history of three.js growing into a tree of light |
|  | [deck.gl](https://github.com/visgl/deck.gl) | [01:45](https://www.bilibili.com/video/BV1DNxU6WEqv/?t=105) | 160,000 points aggregated into an isometric data city |
| Transitions | [GL Transitions](https://github.com/gl-transitions/gl-transitions) | Throughout | 42 kinds of transition across 108 shots |

</details>

## What this is

When you want to make a music video, an explainer or an intro with code, the first question is usually which tool makes the look you have in mind. This list sorts open-source animation and video projects on GitHub by **visual style**: 3Blue1Brown-style math, flat motion graphics, psychedelic shaders, pixel art, ASCII, music visualizers, anime dance videos and more. Pick a style first, then pick a tool. One project often does several styles, so it can appear under several.

Beyond the 17 main styles, the [niche section](#niche) covers ink-wash landscapes, Chinese stroke-order animation, oscilloscope art, plotters, artificial life and others. 108 entries are skills and films where AI coding agents like Claude or Opus write the code, and they're filed by style like everything else. The [relationship graph](#relations) links related projects, so you can see what grew out of what and what can replace what.

<a name="latest"></a>

## Latest additions

**2026-11-16 · 7 new:** [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) · [line-art-animation](https://github.com/JDhruv14/line-art-animation) · [Kubai Icons](https://github.com/kubai087/kubai-icons) · [Cinematic Skill](https://github.com/Moh4696/cinematic-skill) · [Content Studio (design-agent)](https://github.com/langchain-ai/design-agent) · [code-brand-film](https://github.com/nutllwhy/code-brand-film) · [Kalem](https://github.com/leodavincs/kalem)

**2026-11-15 · 35 new:** [Graphite](https://github.com/GraphiteEditor/Graphite) · [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) · [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) · [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) · [ManimGX](https://github.com/academa-labs/manimgx) · [vgpu](https://github.com/vercel-labs/vgpu) · [AI Animation Skills](https://github.com/Unclecheng-li/AI_Animation) · [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) · [Diorama](https://github.com/sloemo01/diorama) · [Procedural Terrains](https://github.com/ZyFou/ProceduralTerrains) · [snapcn](https://github.com/shadcn-labs/snapcn) · [LiquidGlass](https://github.com/ybouane/liquidglass) · [Fabric](https://github.com/Fabric-Project/Fabric) · [Glass SDK Liquid Glass](https://github.com/Glass-HQ/liquid-glass) · [Remotion Bits](https://github.com/av/remotion-bits) · [manim-web](https://github.com/maloyan/manim-web) · [ASCII Magic](https://github.com/kailashsr38/ascii-magic-art) · [liquid_glass_renderer](https://github.com/whynotmake-it/flutter_liquid_glass) · [react-native-effects](https://github.com/blazejkustra/react-native-effects) · [lemo-wake](https://github.com/lemomo-ai/lemo-wake) · [iso-figure](https://github.com/MrBongoC/ai-iso-skill) · [Infinite](https://github.com/n1m21n/Infinite) · [Plasma UI](https://github.com/CruxGarden/plasma-ui) · [svg-text-animate](https://github.com/oubenruing/svg-text-animate) · [Dither Guy](https://github.com/manoelpiovesan/dither-guy) · [isometric](https://github.com/elchininet/isometric) · [Codixel](https://github.com/mankidev/codixel) · [Patchies](https://github.com/heypoom/patchies) · [HyperFrames Motion Reel](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) · [genart](https://github.com/camilleroux/genart-skill) · [Fractal Garden](https://github.com/trebeljahr/fractal-garden) · [Galaxy Simulation](https://github.com/N0rvel/galaxy_sim) · [persian-motion-director](https://github.com/atmirrr/persian-motion-director) and more

Flip through them as cards in the [✦ Latest window](https://syydaniel.github.io/awesome-code-animation/?lang=en#latest) on the web version, which also lists projects with recent commits.

⭐ New projects land every week. [Star the repo](https://github.com/syydaniel/awesome-code-animation) to come back and see what's new.

<a name="threejs"></a>

## ◆ three.js Film Channel

Hand-picked projects for making videos with three.js: pipelines that render scenes to MP4, coding-agent skills and films built on three.js, and the effects you'll reach for in your shots. In the web version this is a gate in the 3D carousel that opens into a tunnel of [18 cards](https://syydaniel.github.io/awesome-code-animation/?lang=en#threejs).

**Pipeline**: Turn three.js scenes into video

- [Remotion](https://github.com/remotion-dev/remotion) ★ 75.1k: Its official @remotion/three package puts three.js and React Three Fiber scenes into React videos and renders them frame by frame to MP4.
- [React Three Fiber](https://github.com/pmndrs/react-three-fiber) ★ 33.9k: Write three.js scenes as React components; the most common way to make 3D videos together with Remotion.
- [Theatre.js](https://github.com/theatre-js/theatre) ★ 13.1k: A visual timeline: keyframe three.js cameras and objects in an editor, good for precise camera moves.
- [frame.js](https://github.com/mrdoob/frame.js) ★ 1.2k: A timeline editor by the author of three.js for sequencing shots and effects into web demos.
- [three.js](https://github.com/mrdoob/three.js) ★ 119k: The foundation: scenes, materials, lights, particles and post-processing.

**Coding agents making three.js films**: Skills and films where coding agents write the three.js code

- [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) ★ 4.6k: One-minute vertical story shorts: 2D characters in a colourful 3D town, rendered with three.js inside Remotion.
- [Claude Animation Skills](https://github.com/artemnovitckii/claude-animation-skills) ★ 1.1k: Six short-video animation skills, including three.js 3D cartoon explainers and exploded views.
- [Diorama](https://github.com/sloemo01/diorama) ★ 715: Coding agents build three.js dioramas with jointed little characters, in a dithered pixel look by default.
- [Code Video Showcase](https://github.com/Moessif/code-video-showcase) ★ 546: A beat-synced showcase video skill that renders HTML, Canvas and three.js frame by frame.
- [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) ★ 430: Offers three directions with previews before rendering frame by frame; three.js is one of the 3D engines it uses.
- [img2threejs](https://github.com/img2threejs/img2threejs) ★ 21.8k: Rebuilds three.js models from a reference image in pure code, handy for props and characters in 3D shorts.
- [Athenaion](https://github.com/Leonxlnx/athenaion) ★ 733: An ancient Greek city built by Claude entirely in three.js code with no assets; a good reference for 3D scenes.

**Looks for your shots**: Post-processing, particles, lighting and scenes for three.js shots

- [postprocessing](https://github.com/pmndrs/postprocessing) ★ 3k: Bloom, chromatic aberration, depth of field and glitch: the go-to post-processing library for three.js videos.
- [three.quarks](https://github.com/Alchemist0823/three.quarks) ★ 1.3k: Fire, explosions and magic particles: VFX for your shots.
- [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) ★ 2.1k: GPU path tracing for realistic light, reflections and depth of field, good for offline-quality renders.
- [three-vrm](https://github.com/pixiv/three-vrm) ★ 2.3k: Drive VRM avatars in three.js for anime-style music videos.
- [Singularity](https://github.com/MisterPrada/singularity) ★ 319: A black hole written in three.js's TSL shading language that runs on WebGPU or WebGL, made for space shots.
- [Poseidon](https://github.com/owenyuwono/poseidon) ★ 325: A real-time GPU FFT ocean in three.js with WebGPU, made for sea shots.

<a name="rules"></a>

## What gets listed

- **Frames must be drawn or rendered by code.** Projects that make their pictures with video or image generation models aren't listed, and neither are ones that render through Blender or other 3D apps. A few projects have an optional generation feature or Blender option, which is noted on the entry.
- **Main styles:** 1,000+ GitHub stars, or 200+ stars with a push in the last year.
- **Niche styles:** 20+ stars with a push in the last year, so small and interesting projects get seen too.
- **Skills and films where AI coding agents like Claude or Opus write the code:** filed by style as usual, with 50+ stars and a push in the last year.
- **Archived (read-only) repositories aren't listed.** Projects we looked at and left out are recorded in [`data/excluded.json`](data/excluded.json), with reasons in Chinese.
- Status follows the latest push: 🟢 Active (within 6 months) · 🟡 Slowing (within 2 years) · ⚪ Dormant (older; most still work, they just don't get new features).
- Stars and status refresh every Monday through GitHub Actions, and new candidates are collected into a weekly issue. Data as of 2026-11-23.

<a name="picks"></a>

## Start from your goal

| Goal | Start with |
| --- | --- |
| Explainer videos | [Manim Community](https://github.com/ManimCommunity/manim) · [Motion Canvas](https://github.com/motion-canvas/motion-canvas) · [Animate](https://github.com/cth9191/animate) |
| Music videos and batch-made shorts | [Remotion](https://github.com/remotion-dev/remotion) · [HyperFrames](https://github.com/heygen-com/hyperframes) · [three.js](https://github.com/mrdoob/three.js) |
| Have Claude / Opus code your video | [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) · [Remotion Skills](https://github.com/remotion-dev/skills) · [Code Animation Style Prompts](https://github.com/XiaoyeCodes/code-animation-prompts) |
| Chinese style: ink wash, characters, poetry | [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) · [Hanzi Writer](https://github.com/chanind/hanzi-writer) · [code-poem-film](https://github.com/bangbuilds/code-poem-film) |
| Live VJ sets and psychedelic visuals | [Hydra](https://github.com/hydra-synth/hydra) · [TiXL](https://github.com/tixl3d/tixl) · [cables](https://github.com/cables-gl/cables) |
| Music visualization | [Butterchurn](https://github.com/jberg/butterchurn) · [projectM](https://github.com/projectM-visualizer/projectm) · [Astrofox](https://github.com/astrofox-io/astrofox) |
| Tech explainers for programmers | [Slidev](https://github.com/slidevjs/slidev) · [VHS](https://github.com/charmbracelet/vhs) · [Gource](https://github.com/acaudwell/Gource) |
| Explore niche styles | [osci-render](https://github.com/jameshball/osci-render) · [Lenia](https://github.com/Chakazul/Lenia) · [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) |

<a name="index"></a>

## Style index

Click a picture to jump to that style's table. Every thumbnail is drawn with code, and the code is in [`site/template.html`](site/template.html).

<table>
<tr><td align="center" width="33%"><a href="#math"><img src="assets/styles/math.png" alt="Math Explainer" width="260"></a><br><b><a href="#math">Math Explainer</a></b><br><sub>25 projects</sub></td><td align="center" width="33%"><a href="#mg"><img src="assets/styles/mg.png" alt="Motion Graphics" width="260"></a><br><b><a href="#mg">Motion Graphics</a></b><br><sub>103 projects</sub></td><td align="center" width="33%"><a href="#code"><img src="assets/styles/code.png" alt="Code & Terminal Demo" width="260"></a><br><b><a href="#code">Code & Terminal Demo</a></b><br><sub>17 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#type"><img src="assets/styles/type.en.png" alt="Kinetic Type & Lyrics" width="260"></a><br><b><a href="#type">Kinetic Type & Lyrics</a></b><br><sub>34 projects</sub></td><td align="center" width="33%"><a href="#short"><img src="assets/styles/short.png" alt="Shorts, Captions & Editing" width="260"></a><br><b><a href="#short">Shorts, Captions & Editing</a></b><br><sub>33 projects</sub></td><td align="center" width="33%"><a href="#hand"><img src="assets/styles/hand.png" alt="Hand-drawn & Whiteboard" width="260"></a><br><b><a href="#hand">Hand-drawn & Whiteboard</a></b><br><sub>27 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#gen"><img src="assets/styles/gen.png" alt="Generative Art" width="260"></a><br><b><a href="#gen">Generative Art</a></b><br><sub>44 projects</sub></td><td align="center" width="33%"><a href="#shader"><img src="assets/styles/shader.png" alt="Shaders & Psychedelic" width="260"></a><br><b><a href="#shader">Shaders & Psychedelic</a></b><br><sub>103 projects</sub></td><td align="center" width="33%"><a href="#live"><img src="assets/styles/live.png" alt="Live Coding & VJ" width="260"></a><br><b><a href="#live">Live Coding & VJ</a></b><br><sub>16 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#audio"><img src="assets/styles/audio.png" alt="Music Visualization" width="260"></a><br><b><a href="#audio">Music Visualization</a></b><br><sub>28 projects</sub></td><td align="center" width="33%"><a href="#3d"><img src="assets/styles/3d.png" alt="3D" width="260"></a><br><b><a href="#3d">3D</a></b><br><sub>83 projects</sub></td><td align="center" width="33%"><a href="#anime"><img src="assets/styles/anime.png" alt="Anime, MMD & VRM" width="260"></a><br><b><a href="#anime">Anime, MMD & VRM</a></b><br><sub>15 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#particle"><img src="assets/styles/particle.png" alt="Particles & Physics" width="260"></a><br><b><a href="#particle">Particles & Physics</a></b><br><sub>28 projects</sub></td><td align="center" width="33%"><a href="#glitch"><img src="assets/styles/glitch.png" alt="Glitch & Post FX" width="260"></a><br><b><a href="#glitch">Glitch & Post FX</a></b><br><sub>17 projects</sub></td><td align="center" width="33%"><a href="#pixel"><img src="assets/styles/pixel.png" alt="Pixel & Retro" width="260"></a><br><b><a href="#pixel">Pixel & Retro</a></b><br><sub>31 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#ascii"><img src="assets/styles/ascii.png" alt="ASCII & Terminal" width="260"></a><br><b><a href="#ascii">ASCII & Terminal</a></b><br><sub>26 projects</sub></td><td align="center" width="33%"><a href="#data"><img src="assets/styles/data.png" alt="Data Animation" width="260"></a><br><b><a href="#data">Data Animation</a></b><br><sub>30 projects</sub></td></tr>
</table>

### Niche styles

<table>
<tr><td align="center" width="33%"><a href="#ink"><img src="assets/styles/ink.png" alt="Ink & Watercolor" width="260"></a><br><b><a href="#ink">Ink & Watercolor</a></b><br><sub>8 projects</sub></td><td align="center" width="33%"><a href="#hanzi"><img src="assets/styles/hanzi.en.png" alt="Handwriting & Strokes" width="260"></a><br><b><a href="#hanzi">Handwriting & Strokes</a></b><br><sub>5 projects</sub></td><td align="center" width="33%"><a href="#scope"><img src="assets/styles/scope.png" alt="Oscilloscope & Vector" width="260"></a><br><b><a href="#scope">Oscilloscope & Vector</a></b><br><sub>3 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#plotter"><img src="assets/styles/plotter.png" alt="Plotter & Line Art" width="260"></a><br><b><a href="#plotter">Plotter & Line Art</a></b><br><sub>8 projects</sub></td><td align="center" width="33%"><a href="#dither"><img src="assets/styles/dither.png" alt="Dither & 1-bit" width="260"></a><br><b><a href="#dither">Dither & 1-bit</a></b><br><sub>7 projects</sub></td><td align="center" width="33%"><a href="#riso"><img src="assets/styles/riso.png" alt="Riso & Paper Collage" width="260"></a><br><b><a href="#riso">Riso & Paper Collage</a></b><br><sub>6 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#alife"><img src="assets/styles/alife.png" alt="Artificial Life & Growth" width="260"></a><br><b><a href="#alife">Artificial Life & Growth</a></b><br><sub>8 projects</sub></td><td align="center" width="33%"><a href="#procgen"><img src="assets/styles/procgen.png" alt="Procedural Generation" width="260"></a><br><b><a href="#procgen">Procedural Generation</a></b><br><sub>13 projects</sub></td><td align="center" width="33%"><a href="#fractal"><img src="assets/styles/fractal.png" alt="Fractals & Chaos" width="260"></a><br><b><a href="#fractal">Fractals & Chaos</a></b><br><sub>9 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#iso"><img src="assets/styles/iso.png" alt="Isometric & Voxel" width="260"></a><br><b><a href="#iso">Isometric & Voxel</a></b><br><sub>11 projects</sub></td><td align="center" width="33%"><a href="#scifi"><img src="assets/styles/scifi.png" alt="Sci-fi HUD" width="260"></a><br><b><a href="#scifi">Sci-fi HUD</a></b><br><sub>4 projects</sub></td><td align="center" width="33%"><a href="#map"><img src="assets/styles/map.png" alt="Map & Route" width="260"></a><br><b><a href="#map">Map & Route</a></b><br><sub>10 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#demoscene"><img src="assets/styles/demoscene.png" alt="Demoscene" width="260"></a><br><b><a href="#demoscene">Demoscene</a></b><br><sub>7 projects</sub></td><td align="center" width="33%"><a href="#sand"><img src="assets/styles/sand.png" alt="Falling Sand" width="260"></a><br><b><a href="#sand">Falling Sand</a></b><br><sub>8 projects</sub></td><td align="center" width="33%"><a href="#flow"><img src="assets/styles/flow.png" alt="Flow & Wind Fields" width="260"></a><br><b><a href="#flow">Flow & Wind Fields</a></b><br><sub>7 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#vhs"><img src="assets/styles/vhs.png" alt="VHS & Analog" width="260"></a><br><b><a href="#vhs">VHS & Analog</a></b><br><sub>13 projects</sub></td><td align="center" width="33%"><a href="#origami"><img src="assets/styles/origami.png" alt="Origami & Papercraft" width="260"></a><br><b><a href="#origami">Origami & Papercraft</a></b><br><sub>8 projects</sub></td><td align="center" width="33%"><a href="#geo"><img src="assets/styles/geo.png" alt="Geometric & Low-poly" width="260"></a><br><b><a href="#geo">Geometric & Low-poly</a></b><br><sub>7 projects</sub></td></tr>
<tr><td align="center" width="33%"><a href="#raytrace"><img src="assets/styles/raytrace.png" alt="Path Tracing" width="260"></a><br><b><a href="#raytrace">Path Tracing</a></b><br><sub>7 projects</sub></td><td align="center" width="33%"><a href="#space"><img src="assets/styles/space.png" alt="Space & Stars" width="260"></a><br><b><a href="#space">Space & Stars</a></b><br><sub>9 projects</sub></td><td align="center" width="33%"><a href="#liquid"><img src="assets/styles/liquid.en.png" alt="Liquid Glass" width="260"></a><br><b><a href="#liquid">Liquid Glass</a></b><br><sub>16 projects</sub></td></tr>
</table>

## Main styles

<a name="math"></a>

### Math Explainer

<img src="assets/styles/math.png" alt="Math Explainer sample" width="240" align="right">

> Equations, axes and geometric transforms on a 3Blue1Brown-style dark canvas

**Picks:** [Manim Community](https://github.com/ManimCommunity/manim) · [Manim (3b1b)](https://github.com/3b1b/manim) · [Motion Canvas](https://github.com/motion-canvas/motion-canvas) · [MathBox](https://github.com/unconed/mathbox) · [Code2Video](https://github.com/showlab/Code2Video)

25 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.8k | 🟢 Active | Python | The math animation engine 3Blue1Brown himself uses (ManimGL): formulas, coordinate systems, shape transforms, in the classic blue-and-black explainer style.<br><sub>Good for: Explainer videos · Also in: Data Animation</sub><br><sub>⚠️ Sparse docs; beginners should start with the community edition.</sub> |
| [Manim Community](https://github.com/ManimCommunity/manim) | 42.8k | 🟢 Active | Python | Community-maintained fork of Manim with the most complete docs and tutorials. Used for many math, physics and algorithm explainer videos on Bilibili.<br><sub>Good for: Explainer videos · Also in: Data Animation, Code & Terminal Demo</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 20.2k | 🟢 Active | TypeScript | Write animations as TypeScript generator functions, with a timeline editor and audio sync. Well suited to explainer videos and code demos.<br><sub>Good for: Explainer videos · MV · Also in: Motion Graphics, Code & Terminal Demo</sub> |
| [pywonderland](https://github.com/neozhaoliang/pywonderland) | 4.2k | 🟡 Slowing | Python | Made by a Chinese developer: math visuals in Python, including fractals, tilings, reaction-diffusion, and maze generation animations.<br><sub>Good for: Math art · Also in: Fractals & Chaos</sub> |
| [Lenia](https://github.com/Chakazul/Lenia) | 3.9k | ⚪ Dormant | Python / JS | Continuous cellular automata that grow moving, splitting "mathematical life forms", looking like organisms under a microscope.<br><sub>Good for: Artificial life · Also in: Artificial Life & Growth</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | ⚪ Dormant | Python | Machine learning concept animations built on Manim: explainer animations of neural networks, convolutions, and similar structures.<br><sub>Good for: Explainer videos · Also in: Data Animation</sub> |
| [Mafs](https://github.com/stevenpetryk/mafs) | 3.5k | 🟢 Active | React | React components for interactive math: coordinate planes, function plots, vectors. Build draggable math explainer animations.<br><sub>Good for: Interactive math</sub> |
| [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) | 2.9k | 🟢 Active | Python (Manim) | A chain of AI agents turns a math or physics concept into a storyboard, writes the Manim code and revises it after looking at the renders; it can make films up to ten minutes long.<br><sub>Good for: Math explainers · Science films · Also in: 3D</sub><br><sub>⚠️ The newer Studio pipeline renders 3D shots with Blender EEVEE; the original main pipeline uses Manim only.</sub> |
| [ManimGX](https://github.com/academa-labs/manimgx) | 2.9k | 🟢 Active | Python / Rust (wgpu) | An animation engine compatible with the Manim CE API, rebuilt on Rust and wgpu so math and 3D scenes render faster; it also runs in the browser.<br><sub>Good for: Math animation · 3D explainers · Also in: 3D</sub> |
| [Code2Video](https://github.com/showlab/Code2Video) | 2.4k | 🟢 Active | Python | Academic project: has a large language model write Manim code to automatically generate educational explainer videos, with every frame rendered by code.<br><sub>Good for: Explainer videos</sub> |
| [Animate](https://github.com/cth9191/animate) | 2.2k | 🟢 Active | JavaScript / Canvas | Claude Code skill: draws short animations procedurally on a single canvas, with 7 built-in styles: paper cut-out, hatched ink, Riso print, sketchbook, math, pixel, and isometric.<br><sub>Good for: Explainer videos · Short films · Also in: Hand-drawn & Whiteboard, Pixel & Retro, Riso & Paper Collage</sub> |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | ⚪ Dormant | JavaScript | 3D math visualization in the browser: surfaces, vector fields and coordinate grids, with clean, polished visuals.<br><sub>Good for: Explainer videos · Also in: 3D</sub> |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.4k | 🟡 Slowing | Haskell | SVG animation library written in Haskell, with LaTeX formula support and a look close to 3B1B.<br><sub>Good for: Explainer videos · Also in: Motion Graphics</sub><br><sub>⚠️ Niche language, small community.</sub> |
| [Manim Agent Skills](https://github.com/adithya-s-k/manim_skill) | 1.4k | 🟡 Slowing | Python / skill | Manim skills and best practices for making 3Blue1Brown-style animations.<br><sub>Good for: Explainer videos</sub> |
| [FieldPlay](https://github.com/anvaka/fieldplay) | 1.3k | 🟢 Active | JavaScript / GLSL | Write a vector field formula and thousands of particles flow along it, like streams of silk.<br><sub>Good for: Vector field animation · Also in: Flow & Wind Fields</sub> |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 1k | 🟢 Active | Python | Turn Manim animations into presentation slides you can play page by page. Can also export to a web page.<br><sub>Good for: Explainer videos · Talks · Also in: Code & Terminal Demo</sub> |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | 942 | 🟢 Active | Python | Describe an animation in natural language; an LLM writes the Manim code and renders it.<br><sub>Good for: Explainer videos</sub> |
| [ranim](https://github.com/AzurIce/ranim) | 662 | 🟢 Active | Rust | Animation engine written in Rust, inspired by Manim.<br><sub>Good for: Explainer videos</sub> |
| [manim-web](https://github.com/maloyan/manim-web) | 520 | 🟢 Active | TypeScript | A TypeScript port of 3Blue1Brown's Manim that renders in a browser canvas, plus molecular, chemistry, biology and map modules.<br><sub>Good for: Math animation · Web · Also in: Data Animation</sub> |
| [ManimCat](https://github.com/Wing900/ManimCat) | 513 | 🟢 Active | TypeScript / Python | Describe an animation in one sentence and AI writes the Manim code for a math animation. Supports LaTeX and auto-fixes code when rendering fails.<br><sub>Good for: Math explainer videos</sub><br><sub>⚠️ AGPL-3.0: if you use it in a network service offered to others, you must publish your modified source.</sub> |
| [manim-physics](https://github.com/Matheart/manim-physics) | 414 | 🟢 Active | Python | Physics simulation extension for Manim: rigid bodies, electromagnetic fields, waves, pendulums, and other physics animations.<br><sub>Good for: Explainer videos · Also in: Particles & Physics</sub> |
| [MathLens](https://github.com/shuyicc/MathLens) | 354 | 🟡 Slowing | Python | From a Chinese developer: paste a math problem and it analyzes it, writes a voiceover script and generates a narrated Manim explainer video.<br><sub>Good for: Math explainer videos</sub> |
| [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | 328 | 🟢 Active | Python | Adds voiceover to Manim animations, syncing animation timing to the speech automatically.<br><sub>Good for: Explainer videos</sub> |
| [manim-skill](https://github.com/Yusuke710/manim-skill) | 216 | 🟢 Active | Skill | SKILL.md that teaches AI agents to write Manim animations.<br><sub>Good for: Explainer videos</sub> |
| [Fractal Garden](https://github.com/trebeljahr/fractal-garden) | 165 | 🟢 Active | TypeScript | 62 fractals in the browser: zoom into the Mandelbrot set, fly through a Menger sponge or write your own L-systems, each with an explainer.<br><sub>Good for: Fractals · Math art · Also in: Fractals & Chaos</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="mg"></a>

### Motion Graphics

<img src="assets/styles/mg.png" alt="Motion Graphics sample" width="240" align="right">

> Flat shapes, springy easing and shape morphs

**Picks:** [GSAP](https://github.com/greensock/GSAP) · [anime.js](https://github.com/juliangarnier/anime) · [Remotion](https://github.com/remotion-dev/remotion) · [HyperFrames](https://github.com/heygen-com/hyperframes) · [mo.js](https://github.com/mojs/mojs)

103 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 88.6k | 🟢 Active | HTML / CSS / GSAP | Open-sourced by HeyGen. Write scenes in HTML/CSS, animate with GSAP, render straight to MP4. Designed for AI coding agents.<br><sub>Good for: MV · Short videos · AI generation · Also in: Kinetic Type & Lyrics, Shorts, Captions & Editing</sub><br><sub>⚠️ The official skill pack's asset skills can optionally call generation services; the rendering itself is HTML code.</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 75.1k | 🟢 Active | React / TS | Write videos as React components and render them to MP4, with batch generation. Official add-on packages cover captions, audio visualization, three.js, and more.<br><sub>Good for: MV · Short videos · Batch video rendering · Also in: Shorts, Captions & Editing, Kinetic Type & Lyrics, 3D</sub><br><sub>⚠️ Free for individuals and small companies (commercial use included); larger companies need to buy a company license.</sub> |
| [anime.js](https://github.com/juliangarnier/anime) | 75k | 🟢 Active | JavaScript | Lightweight JS animation library. Timelines, stagger, and SVG stroke animation are easy to use.<br><sub>Good for: Web animation · MV · Also in: Kinetic Type & Lyrics</sub> |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.6k | 🟢 Active | HTML / JS | Write presentations in HTML. Auto-Animate tweens elements automatically between slides.<br><sub>Good for: Explainer videos · Talks · Also in: Code & Terminal Demo</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 52.5k | 🟢 Active | React | Lots of animated React components: text effects, animated backgrounds, interactive motion. Copy and use.<br><sub>Good for: Web motion · Assets · Also in: Kinetic Type & Lyrics, Shaders & Psychedelic</sub> |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.9k | 🟢 Active | TypeScript | Fast 2D rendering engine (WebGL / WebGPU) for large numbers of sprites, filters, and 2D motion effects.<br><sub>Good for: Web animation · MV · Also in: Particles & Physics, Generative Art</sub> |
| [Motion](https://github.com/motiondivision/motion) | 35.5k | 🟢 Active | React / JS | Formerly Framer Motion. An animation library for React and JS with smooth springs, gestures, and layout transitions.<br><sub>Good for: Web motion</sub> |
| [Lottie](https://github.com/airbnb/lottie-web) | 32.6k | 🟡 Slowing | JavaScript | Plays After Effects animations exported as Bodymovin JSON in the browser. The common format for flat illustration and icon animation.<br><sub>Good for: Effect assets · Web animation</sub><br><sub>⚠️ The animation itself is usually made in AE; code handles playback and control.</sub> |
| [GSAP](https://github.com/greensock/GSAP) | 31.1k | 🟢 Active | JavaScript | Long-established JS animation engine. Plugins like SplitText and MorphSVG are now all free. Strong at split-text animation and SVG morphing.<br><sub>Good for: MV · Web animation · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ Free for commercial use, but under GreenSock's own license, not an OSI-approved open-source license.</sub> |
| [react-spring](https://github.com/pmndrs/react-spring) | 29.3k | 🟢 Active | React | React animation library built on spring physics, for natural, bouncy motion.<br><sub>Good for: Web motion</sub> |
| [Graphite](https://github.com/GraphiteEditor/Graphite) | 28k | 🟢 Active | Rust / Node graph | An open-source 2D graphics editor with a node graph under the layers: shapes, patterns and arrangements are generated procedurally with nodes and can be tweaked live.<br><sub>Good for: Vector art · Procedural design · Also in: Generative Art</sub><br><sub>⚠️ Still in alpha; motion graphics are on the roadmap, and today it is mainly for vector and procedural design.</sub> |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.5k | 🟢 Active | React | React component library with motion built in: text animations, glowing borders, particle backgrounds, and more.<br><sub>Good for: Web motion · Also in: Kinetic Type & Lyrics</sub> |
| [brag](https://github.com/latent-spaces/brag) | 22.3k | 🟢 Active | Python / skill | After you finish a project, one command makes a short promo video with music and copy, rendered with HyperFrames.<br><sub>Good for: Project promo videos</sub> |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 22.2k | 🟢 Active | React / TS | AI coding agent skill: captures screenshots of your real web pages and turns them into cinematic product promo videos with Remotion.<br><sub>Good for: Product promo videos · Also in: Shorts, Captions & Editing</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 20.2k | 🟢 Active | TypeScript | Write animations as TypeScript generator functions, with a timeline editor and audio sync. Well suited to explainer videos and code demos.<br><sub>Good for: Explainer videos · MV · Also in: Code & Terminal Demo, Math Explainer</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 20.1k | 🟢 Active | JavaScript | A toolbox of film styles made in code: 66 ready-made styles (Memphis, subway map, chalkboard, and more) that let an AI coding agent make videos in each style, all drawn with code.<br><sub>Good for: MV · Short films · Also in: Hand-drawn & Whiteboard, Pixel & Retro</sub><br><sub>⚠️ Styles are tuned for Claude; results may differ with other models.</sub> |
| [GSAP Skills](https://github.com/greensock/gsap-skills) | 18.9k | 🟢 Active | Skill | Official GSAP AI skills that teach coding agents to use GSAP and its plugins correctly.<br><sub>Good for: Web animation</sub> |
| [mo.js](https://github.com/mojs/mojs) | 18.9k | 🟢 Active | JavaScript | JS library built for motion graphics: bursts, ripples, shape pop-ins and other small MG effects.<br><sub>Good for: Effect assets</sub> |
| [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 16.3k | 🟢 Active | HTML / Canvas / three.js | 703 prompts people used to make videos with Claude Opus 5.5, each linked to the original post and a live remake. The picture is drawn in code (Canvas, SVG, three.js): mostly motion graphics, explainers and 3D scenes.<br><sub>Good for: Prompt collection · MV · Also in: 3D, Generative Art</sub><br><sub>⚠️ A few entries overlay AI-generated images or use Blender; those are labeled.</sub> |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | 🟢 Active | JavaScript | Vector graphics scripting framework with strong path operations and Bezier curves, good for vector-style generative art.<br><sub>Good for: Generative art · Also in: Generative Art</sub> |
| [Konva](https://github.com/konvajs/konva) | 15k | 🟢 Active | TypeScript | HTML5 Canvas framework with shapes, tweened animation and drag interaction. Official React and Vue wrappers.<br><sub>Good for: Canvas animation</sub> |
| [Theatre.js](https://github.com/theatre-js/theatre) | 13.1k | ⚪ Dormant | TypeScript | Visual timeline for web animation: define properties in code, drag keyframes in the UI. Often paired with three.js for 3D camera animation.<br><sub>Good for: MV · Web animation · Also in: 3D</sub> |
| [SVG.js](https://github.com/svgdotjs/svg.js) | 12k | 🟢 Active | JavaScript | Lightweight library for manipulating and animating SVG.<br><sub>Good for: Web animation</sub> |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | ⚪ Dormant | JavaScript | Pseudo-3D flat engine that draws rounded, cute flat-shaded 3D shapes.<br><sub>Good for: Web animation · Also in: 3D, Isometric & Voxel</sub><br><sub>⚠️ Not updated in years; simple and stable.</sub> |
| [EffectCraft](https://github.com/storytold/effectcraft) | 9.2k | 🟢 Active | Rust (GUI) | Open-source compositing app written from scratch, After Effects-style: layers, keyframes, expressions, 300+ effects.<br><sub>Good for: Motion graphics · Post compositing · Also in: Glitch & Post FX</sub><br><sub>⚠️ Mostly a graphical interface; the expressions part can be scripted in code.</sub> |
| [React Native Skia](https://github.com/wcandillon/react-native-skia) | 8.8k | 🟢 Active | React Native | Draw high-performance 2D graphics and animations in React Native with Skia. Supports runtime shaders.<br><sub>Good for: Mobile motion · Also in: Shaders & Psychedelic</sub> |
| [Two.js](https://github.com/jonobr1/two.js) | 8.8k | 🟢 Active | JavaScript | 2D vector drawing API. The same code outputs SVG, Canvas, or WebGL, good for flat geometric animation.<br><sub>Good for: Web animation · Also in: Generative Art</sub> |
| [Remotion Skills](https://github.com/remotion-dev/skills) | 7.8k | 🟢 Active | Markdown skill | Official Remotion skills for AI coding agents, so Claude Code and others can write Remotion videos directly.<br><sub>Good for: MV · Short videos</sub> |
| [Arwes](https://github.com/arwes/arwes) | 7.6k | 🟢 Active | TypeScript | Sci-fi web UI framework with futuristic effects: glowing borders, expanding lines, and text decoding.<br><sub>Good for: Sci-fi UI · Also in: Sci-fi HUD</sub> |
| [PAG](https://github.com/Tencent/libpag) | 5.8k | 🟢 Active | C++ / cross-platform | Tencent's open-source After Effects animation solution. Similar idea to Lottie but supports more AE features, and text and images inside can be replaced from code.<br><sub>Good for: Effect assets</sub> |
| [Lottie Skill](https://github.com/diffusionstudio/lottie) | 5.8k | 🟢 Active | TypeScript | Lets Claude Code or Codex write production-ready Lottie animation files directly.<br><sub>Good for: Lottie animation</sub> |
| [html-video](https://github.com/nexu-io/html-video) | 4.9k | 🟢 Active | HTML / CSS | Lets a local AI coding agent turn HTML/CSS into video. Ships with 21 templates, including kinetic type, Swiss grid and data cards.<br><sub>Good for: Short videos · Promo videos · Also in: Kinetic Type & Lyrics</sub> |
| [onetake](https://github.com/feitangyuan/onetake) | 4.4k | 🟢 Active | Python / HTML | Skill for single-take motion shorts: every scene grows out of the previous one instead of switching pages like a slideshow.<br><sub>Good for: Product launch videos</sub><br><sub>⚠️ A paid Pro version is also available.</sub> |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | 🟢 Active | TypeScript | Fork of Motion Canvas focused on headless rendering, so videos can be generated in bulk through an API.<br><sub>Good for: Short videos · Batch video rendering · Also in: Shorts, Captions & Editing</sub> |
| [VAP](https://github.com/Tencent/vap) | 4.2k | 🟢 Active | Cross-platform | Tencent's open-source player for videos with an alpha channel, often used for complex effects such as live-stream gifts.<br><sub>Good for: Effect assets</sub> |
| [hairline](https://github.com/lucasmarkes/hairline) | 4.1k | 🟢 Active | TypeScript | Isometric line figures and objects that turn to follow the mouse. Works with React and plain web pages.<br><sub>Good for: Web motion · Also in: Isometric & Voxel</sub> |
| [P(doom) MV (mexicat version)](https://github.com/mexicat/pdoom-video) | 4k | 🟢 Active | JavaScript | Another code-rendered music video for "I'm Upping My P(doom)", with word-by-word beat-synced lyrics.<br><sub>Good for: Lyric MV · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ AI was used only to split the audio into stems; all visuals are rendered by code.</sub> |
| [MG Styles 15](https://github.com/Vincentwei1021/mg-styles-15) | 3.9k | 🟢 Active | Python / Web | 15 motion design style demo films, each written as code by Claude Opus 5.5 from a single prompt. Prompts and source included.<br><sub>Good for: Style sample clips · Also in: 3D, Hand-drawn & Whiteboard</sub><br><sub>⚠️ Of the 15, only the 3D one uses Blender; the rest are pure code.</sub> |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | 3.6k | 🟢 Active | Markdown skill | Teaches AI agents motion design principles: timing, easing, choreography, and the Disney animation principles.<br><sub>Good for: Motion design</sub> |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3.5k | 🟢 Active | React / TS | Give it a topic and it makes a black-background motion graphics explainer video, with voiceover and captions. Every frame is rendered in code.<br><sub>Good for: Explainer videos · Also in: Data Animation</sub> |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | 🟢 Active | Rust / SVG | Write video with Rust and SVG, rendered on the GPU, with a focus on speed. Also includes a skill for AI coding agents.<br><sub>Good for: Batch video rendering · Also in: Shorts, Captions & Editing</sub> |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 3.1k | 🟢 Active | JavaScript | Has an AI coding agent make product launch films, compose its own soundtrack, and take edits by pointing at the frame.<br><sub>Good for: Product promo videos · Also in: 3D</sub> |
| [P(doom) MV](https://github.com/JohnHeibel/PDoomVideo) | 3k | 🟢 Active | JavaScript | Full source for the music video "I'm Upping My P(doom)", made by Claude Opus 5.5 writing code.<br><sub>Good for: MV · Also in: Kinetic Type & Lyrics</sub> |
| [Bang Motion](https://github.com/bangtutorial/bang-motion) | 2.9k | 🟢 Active | HTML | Browser motion graphics skill: intros, promos, transitions, and kinetic typography, in five styles.<br><sub>Good for: Intros · Promo videos · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ The optional After Effects cartoon explainer goes through a Higgsfield bridge; the default workflow is code animation in the browser.</sub> |
| [Pixel2Motion](https://github.com/nolangz/pixel2motion) | 2.7k | 🟢 Active | Python / SVG | Converts raster logos to clean SVG, then makes logo animations and video previews.<br><sub>Good for: Logo animation</sub> |
| [reanimate](https://github.com/NiazMorshed2007/reanimate) | 2.3k | 🟢 Active | JavaScript | Claude Code skill: breaks any animation down frame by frame, recreates it in code, and checks frame by frame how closely the copy matches.<br><sub>Good for: Animation recreation</sub> |
| [motion-skills](https://github.com/iart-ai/motion-skills) | 2.1k | 🟢 Active | Markdown skill | 50 AI coding agent skills: kinetic typography, data visualization, explainer videos, vertical short videos, WebGL, Manim.<br><sub>Good for: Various videos</sub> |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | 🟢 Active | TypeScript (GUI) | Motion graphics software that turns audio into visualizer videos: spectrum, waveform, text, and 3D layers can be combined and exported.<br><sub>Good for: Music visualizer · MV · Also in: Music Visualization</sub><br><sub>⚠️ Mainly a graphical interface.</sub> |
| [AI Animation Skills](https://github.com/Unclecheng-li/AI_Animation) | 1.8k | 🟢 Active | HTML / skill | 17 skills that have an AI coding agent write single-file HTML animations: PPT-style explainers, flowcharts, network protocols, animated architecture diagrams, storyboards and more.<br><sub>Good for: Explainer decks · Concept animations · Also in: Data Animation</sub> |
| [remocn](https://github.com/Remocn/remocn) | 1.8k | 🟢 Active | React / TS | Ready-made animations, transitions, backgrounds, and scene components for Remotion.<br><sub>Good for: MV · Short videos · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ Requires Remotion; Remotion's own license terms still apply.</sub> |
| [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1.8k | 🟢 Active | JavaScript (HyperFrames + GSAP) | Agent skill for launch films, product promos, brand stings and kinetic type: it captures the brand, picks one idea only that brand could own, animates with timing rules measured frame by frame from 53 professional pieces, then checks its own render.<br><sub>Good for: Launch films · Product promos · Kinetic type · Also in: Kinetic Type & Lyrics</sub> |
| [Animotion](https://github.com/animotionjs/animotion) | 1.8k | 🟢 Active | Svelte | Write animated presentations in Svelte, with smooth code highlight transitions and element tweens.<br><sub>Good for: Explainer videos · Talks · Also in: Code & Terminal Demo</sub> |
| [Liquid Logo](https://github.com/paper-design/liquid-logo) | 1.5k | 🟡 Slowing | TypeScript | Small tool from the Paper team: turns a logo into a flowing liquid-metal animation.<br><sub>Good for: Logo motion · Also in: Liquid Glass, Shaders & Psychedelic</sub> |
| [Motion Graphics Skills](https://github.com/Barty-Bart/motion-graphics) | 1.5k | 🟢 Active | HTML / skill | Collection of motion graphics skills for Claude Code and Codex.<br><sub>Good for: Motion graphics</sub> |
| [Code Animation Style Prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | 1.4k | 🟢 Active | HTML / skill | 341 code-animation style prompts and 196 reference stills, with an offline picker. Can be installed as a Claude Code / Codex skill.<br><sub>Good for: Style prompts</sub> |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.4k | 🟡 Slowing | Haskell | SVG animation library written in Haskell, with LaTeX formula support and a look close to 3B1B.<br><sub>Good for: Explainer videos · Also in: Math Explainer</sub><br><sub>⚠️ Niche language, small community.</sub> |
| [cinetic](https://github.com/Leonxlnx/cinetic) | 1.4k | 🟢 Active | TypeScript | Has an AI coding agent direct cinematic launch films and motion design from code, rendered with Remotion by default.<br><sub>Good for: Launch videos</sub> |
| [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) | 1.3k | 🟢 Active | TypeScript | Open-source skill that teaches Claude Code and Claude Desktop to write Remotion videos.<br><sub>Good for: Short videos</sub> |
| [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) | 1.2k | 🟢 Active | Prompts / HTML | A Chinese roundup of Opus 5.5 code-rendered videos: 18 full prompts and 54 public cases, including line-art animation, science explainers, launch films and lyric MVs.<br><sub>Good for: Prompt collection · Explainers · MV · Also in: Hand-drawn & Whiteboard, Shorts, Captions & Editing</sub><br><sub>⚠️ A few cases in the overview use Seedance, Runway or Blender, and the table says so; the featured prompts are all code-rendered.</sub> |
| [frame.js](https://github.com/mrdoob/frame.js) | 1.2k | 🟡 Slowing | JavaScript | JavaScript timeline editor by the author of three.js, for sequencing shots and effects in web demos.<br><sub>Good for: Web demo choreography · Also in: Demoscene</sub> |
| [Kubai Icons](https://github.com/kubai087/kubai-icons) | 1.2k | 🟢 Active | JavaScript / TypeScript (SVG) | Agent skill that draws animated SVG icons in one consistent hand: give it a product and it draws the icon set that product needs. Ships with 2,800+ ready icons for React, Vue and plain SVG.<br><sub>Good for: Animated icons</sub><br><sub>⚠️ The icon library is MIT; the skill itself is under the author's own source-available Kubai Icons License, so read the terms before using it.</sub> |
| [motion-anything](https://github.com/nexu-io/motion-anything) | 1.1k | 🟢 Active | JavaScript | Describe the feel in one sentence and AI generates motion pages and launch videos. Comes with reusable shader, Canvas, and animated text recipes.<br><sub>Good for: Motion pages · Launch videos · Also in: Shaders & Psychedelic</sub> |
| [Rive Runtime](https://github.com/rive-app/rive-wasm) | 1k | 🟢 Active | TypeScript | Web runtime for Rive animations: vector interactive animations with state machines, with state changes controlled from code.<br><sub>Good for: Interactive animation</sub><br><sub>⚠️ Animations are usually made in the Rive editor, which is not open source.</sub> |
| [Guizang Product Video](https://github.com/op7418/guizang-product-video-skill) | 968 | 🟢 Active | Python | Guizang's promo video skill: reuses a product's real components and design language to make software update promos in code, with script, music, and voiceover.<br><sub>Good for: Software promo videos</sub> |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | 957 | 🟢 Active | TypeScript | Official LottieFiles web player for Lottie / dotLottie, built on Rust + WASM for better performance.<br><sub>Good for: Effect assets · Web animation</sub> |
| [Cinematic Skill](https://github.com/Moh4696/cinematic-skill) | 932 | 🟢 Active | Python (Skia) | Agent skill for narrated cinematic films: one continuous camera over photos, maps and cards, with stamps, highlighter swipes and rolling numbers landing on the exact word of the narration. Every frame is drawn by code in Skia.<br><sub>Good for: Narrated documentaries · Explainers</sub><br><sub>⚠️ The photos in the film are public-domain images it finds, not generated ones.</sub> |
| [Rossark Motion](https://github.com/rossark0/rossark-motion-skill) | 921 | 🟢 Active | Swift / SVG | Claude Code skill: turns any SVG into a professional 60 fps animation.<br><sub>Good for: SVG animation</sub> |
| [Claude Motion Design](https://github.com/howseen-ai/claude-motion-design) | 887 | 🟢 Active | Python | Skill for pure-code motion videos: HTML + Playwright + ffmpeg, with no AI-generated imagery.<br><sub>Good for: Motion graphics video</sub> |
| [motion-web](https://github.com/feitangyuan/motion-web) | 875 | 🟢 Active | HTML / JS | Another skill set from the onetake author: motion-first creative websites built on vanilla three.js, Canvas, and WebGL.<br><sub>Good for: Motion websites · Also in: 3D</sub> |
| [genjutsu](https://github.com/AThevon/genjutsu) | 849 | 🟢 Active | Python / skill | Creative coding skills for Claude Code and claude.ai: motion, micro-interactions, and design sense.<br><sub>Good for: Creative coding · Also in: Generative Art</sub> |
| [Launch Motion Skills](https://github.com/charlie947/motion-graphics-skills) | 786 | 🟢 Active | Shell / skill | 13 Claude Code skills for making launch-quality motion graphics. Every frame is code, no After Effects.<br><sub>Good for: Launch videos</sub> |
| [Shader Lab](https://github.com/basementstudio/shader-lab) | 728 | 🟢 Active | TypeScript | Toolkit for creating, stacking, and animating shaders. Combine multiple effects like layers.<br><sub>Good for: Shader motion · Also in: Shaders & Psychedelic</sub> |
| [drawsvg](https://github.com/cduck/drawsvg) | 698 | 🟢 Active | Python | Generate SVG graphics and animations from Python, with interactive preview in Jupyter.<br><sub>Good for: SVG animation · Also in: Data Animation</sub> |
| [MotionClone](https://github.com/blixvip/MotionClone) | 685 | 🟢 Active | Python | Rebuilds a reference video as an editable HyperFrames project and compares it with the original frame by frame.<br><sub>Good for: Motion recreation</sub> |
| [Aora Bot](https://github.com/sam70361/aora-bot) | 681 | 🟢 Active | TypeScript | A web character engine drawn in code, with 46 original characters and 44 animation states.<br><sub>Good for: Character animation · Also in: Anime, MMD & VRM</sub> |
| [snapcn](https://github.com/shadcn-labs/snapcn) | 679 | 🟢 Active | TypeScript (Remotion) | A Remotion component registry for product demo videos: AI chat streams, terminal sessions, device frames and captions, installed with the shadcn CLI.<br><sub>Good for: Product demo videos · Also in: Shorts, Captions & Editing, Code & Terminal Demo</sub> |
| [Content Studio (design-agent)](https://github.com/langchain-ai/design-agent) | 674 | 🟢 Active | JavaScript / Python (HyperFrames) | LangChain's open-source design agent: ask in a chat thread and get on-brand stills, decks, diagrams, charts and motion graphics back. Video is built in HyperFrames; code renders, checks and delivers.<br><sub>Good for: Brand assets · Launch films · Also in: Data Animation</sub><br><sub>⚠️ Built on Deep Agents; full deployment runs in Slack, and it can be tried locally without keys. Image generation is optional and needs your own OpenAI or Google key.</sub> |
| [ff-tracking](https://github.com/mrsarac/ff-tracking) | 653 | 🟢 Active | Rust | Short film where a virtual camera films an AI agent's screen and tracks every glyph. Uses fframes two-pass rendering and SkSL shaders; the sound effects are also synthesized in code.<br><sub>Good for: Motion shorts · Also in: Glitch & Post FX</sub> |
| [Opus Video Skills](https://github.com/tuzhechen2005/opus-video-skills) | 559 | 🟢 Active | JavaScript | Video-making skills for Claude Opus, where every frame and every note is generated in code.<br><sub>Good for: Short films · MV · Also in: Music Visualization</sub> |
| [Code Video Showcase](https://github.com/Moessif/code-video-showcase) | 546 | 🟢 Active | HTML / Canvas / three.js | Pure-code beat-synced showcase video skill, rendered frame by frame with HTML, Canvas, SVG, and three.js.<br><sub>Good for: Beat-synced showreels · Also in: 3D</sub> |
| [Kinetograph](https://github.com/0xS4N4TG/kinetograph) | 543 | 🟢 Active | TypeScript | Fast programmatic video engine made for AI coding agents.<br><sub>Good for: Batch video rendering · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ PolyForm Small Business license: free for individuals and small companies; larger companies need a commercial license.</sub> |
| [Product Launch Motion](https://github.com/AbubakrChan/product-launch-motion) | 527 | 🟢 Active | JavaScript | Claude Code skill for Dribbble-quality product launch videos from code, with one shape carrying through without cuts.<br><sub>Good for: Product launch videos</sub> |
| [Remotion Bits](https://github.com/av/remotion-bits) | 523 | 🟢 Active | TypeScript (Remotion) | Ready-made animation components for Remotion: text effects, gradient transitions, particles, 3D scenes, charts and more; pull in only what you need.<br><sub>Good for: MG components · Short videos · Also in: Kinetic Type & Lyrics, Particles & Physics</sub><br><sub>⚠️ Not affiliated with the Remotion team.</sub> |
| [video-director](https://github.com/win4r/video-director) | 521 | 🟢 Active | Python | Claude skill: directs, builds, and checks frame by frame videos rendered from HTML / Canvas.<br><sub>Good for: Code video director</sub> |
| [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | 430 | 🟢 Active | Python | Made by a Chinese developer: Claude Opus writes code to make videos. It proposes three options with previews first, then renders the chosen one frame by frame.<br><sub>Good for: Short films · Also in: 3D</sub> |
| [fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation) | 429 | 🟢 Active | TypeScript | Turns Chinese copy, style prompts, and sound into coherent code animation (Remotion / Canvas / HTML).<br><sub>Good for: Explainer animation</sub> |
| [shipvideo](https://github.com/diggerhq/shipvideo) | 386 | 🟢 Active | TypeScript | Paste a URL or a one-line prompt: Opus writes HTML and renders it in the cloud, giving a 20 to 40 second launch video with no video model.<br><sub>Good for: Product launch videos</sub> |
| [What If Animation](https://github.com/kelano86/what-if-animation) | 386 | 🟢 Active | TypeScript | Enter a "what if..." topic and get a complete explainer animation, with no image or video models.<br><sub>Good for: Explainer shorts</sub> |
| [lemo-wake](https://github.com/lemomo-ai/lemo-wake) | 379 | 🟢 Active | Python / HTML | Give Claude Code one picture and it takes the text, objects and people apart, rebuilds them in code and makes a seamless loop of about five seconds.<br><sub>Good for: Photo loops · Logo motion · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ Code and docs are CC BY-NC 4.0 (no commercial use). Optional small local models handle cut-outs, depth and background fill (LaMa) and are only downloaded after you agree; no image generation.</sub> |
| [iso-figure](https://github.com/MrBongoC/ai-iso-skill) | 373 | 🟢 Active | SVG / skill | A Claude skill: name an object and get one HTML file with a hairline isometric drawing whose parts move, count or play notes when pressed.<br><sub>Good for: Isometric figures · Interactive animation · Also in: Isometric & Voxel</sub> |
| [motion2code](https://github.com/lovisdotio/motion2code) | 361 | 🟢 Active | HTML | Rebuilds a motion video as looping SVG + GSAP code, checked frame by frame against the source.<br><sub>Good for: Motion recreation</sub><br><sub>⚠️ The reference videos in the examples were made by a video model; this skill only handles recreating them in code.</sub> |
| [html-anime](https://github.com/blixvip/html-anime) | 273 | 🟢 Active | JavaScript | Turns a scene description into a storyboard sheet, then has a coding agent draw the whole film in HTML. No video model is called.<br><sub>Good for: Animated shorts · Also in: Anime, MMD & VRM</sub> |
| [YouTube Motion Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics) | 248 | 🟢 Active | HTML | 74 animated HTML explainer boards (charts, diagrams, flows) for YouTube explainer videos.<br><sub>Good for: Explainer video assets · Also in: Data Animation</sub> |
| [code-brand-film](https://github.com/nutllwhy/code-brand-film) | 212 | 🟢 Active | Python / JavaScript (HyperFrames + GSAP) | Agent skill for 15-second brand films made in code: one HTML page driven by a GSAP timeline and rendered frame by frame with HyperFrames, an original score synthesised in Python, and three quality gates for code, layout and rendered frames.<br><sub>Good for: 15-second brand films</sub> |
| [Vibe Knowledge Shorts](https://github.com/xiazhuo123456789/vibe-knowledge-video) | 211 | 🟢 Active | Python | Generates cinematic knowledge short videos in pure code, with bilingual captions, synthesized music, and recreated historical documents.<br><sub>Good for: Knowledge shorts · Also in: Kinetic Type & Lyrics</sub> |
| [BB-Video](https://github.com/BubbleBrainBB/BB-Video) | 211 | 🟢 Active | JavaScript | Skill for making videos in pure code: narrated explainers and product promos in 32 visual styles.<br><sub>Good for: Explainers · Promo videos · Also in: 3D</sub><br><sub>⚠️ 3D mascots can optionally be made in Blender; without Blender it falls back to three.js.</sub> |
| [RuiC Motion Reel](https://github.com/HRuiCcc/RuiC-motion-reel) | 207 | 🟢 Active | Python | One sentence generates a motion promo film, with length computed from BPM and bars; standard promos use a Remotion template.<br><sub>Good for: Promo videos</sub> |
| [HyperFrames Motion Reel](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | 207 | 🟢 Active | HTML / GSAP | A Claude Code skill that turns a one-line theme into a beat-synced motion-graphics reel with bold type, morphing transitions, particles and camera moves, rendered with HyperFrames.<br><sub>Good for: Showreels · Beat-synced MG · Also in: Kinetic Type & Lyrics</sub> |
| [persian-motion-director](https://github.com/atmirrr/persian-motion-director) | 153 | 🟢 Active | JavaScript (Remotion) | A Claude skill for Persian kinetic typography and motion films: per-letter and per-dot animation that keeps letters joined, with the music locked first and cuts on the beat.<br><sub>Good for: Persian kinetic type · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ Code is MIT; ships the Vazirmatn font (OFL).</sub> |
| [Kalem](https://github.com/leodavincs/kalem) | 119 | 🟢 Active | Python / JavaScript | Claude Code skill that splits a video into scenes and picks the engine that draws each one best (Paper.js, PixiJS, HyperFrames, three.js, Manim and more), then joins them with transitions such as a page flip and adds frame-locked sound effects.<br><sub>Good for: Scene-by-scene explainers · Also in: Hand-drawn & Whiteboard</sub><br><sub>⚠️ Docs are mainly in Turkish, with an English version. The notebook-engraving look of its plate (levha) engine uses Codex image generation for the base drawing; a flag turns that off, and the blueprint style runs entirely in code. The other engines render from code.</sub> |
| [sy-style-100](https://github.com/xiaoxiong20xx-code/sy-style-100) | 101 | 🟢 Active | HTML | Made by a Chinese developer: 100 videos where every frame is computed by code. 20 styles plus 60 industry ads, usable commercially.<br><sub>Good for: Style sample clips</sub> |
| [DeepSeek Opus Motion](https://github.com/8533502-dev/deepseek-opus-motion-skill) | 97 | 🟢 Active | TypeScript | Gets DeepSeek to make Remotion motion videos close to Claude Opus quality using the same prompts.<br><sub>Good for: Motion videos</sub> |
| [Knowledge Explainer](https://github.com/znyupup/knowledge-explainer-skill) | 74 | 🟡 Slowing | JavaScript | Automatically turns a Markdown script into an explainer animation video, rendered with Remotion.<br><sub>Good for: Explainer animation</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="code"></a>

### Code & Terminal Demo

<img src="assets/styles/code.png" alt="Code & Terminal Demo sample" width="240" align="right">

> Syntax highlighting, code appearing line by line, terminal recordings, algorithm animations

**Picks:** [Slidev](https://github.com/slidevjs/slidev) · [VHS](https://github.com/charmbracelet/vhs) · [Code Hike](https://github.com/code-hike/codehike) · [git-sim](https://github.com/initialcommit-com/git-sim) · [Animotion](https://github.com/animotionjs/animotion)

17 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.6k | 🟢 Active | HTML / JS | Write presentations in HTML. Auto-Animate tweens elements automatically between slides.<br><sub>Good for: Explainer videos · Talks · Also in: Motion Graphics</sub> |
| [Slidev](https://github.com/slidevjs/slidev) | 49.6k | 🟢 Active | Markdown / Vue | Write presentations in Markdown, with built-in code highlighting, smooth code transition animations, and recording.<br><sub>Good for: Explainer videos · Talks</sub> |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.6k | ⚪ Dormant | JavaScript | Animates how algorithms run, including sorting, graphs, and dynamic programming.<br><sub>Good for: Explainer videos · Also in: Data Animation</sub> |
| [Manim Community](https://github.com/ManimCommunity/manim) | 42.8k | 🟢 Active | Python | Community-maintained fork of Manim with the most complete docs and tutorials. Used for many math, physics and algorithm explainer videos on Bilibili.<br><sub>Good for: Explainer videos · Also in: Math Explainer, Data Animation</sub> |
| [VHS](https://github.com/charmbracelet/vhs) | 21.4k | 🟢 Active | VHS script | Script terminal actions and record them automatically as a GIF or video. The easiest way to make command-line demos.<br><sub>Good for: Explainer videos · GIF · Also in: ASCII & Terminal</sub> |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 20.2k | 🟢 Active | TypeScript | Write animations as TypeScript generator functions, with a timeline editor and audio sync. Well suited to explainer videos and code demos.<br><sub>Good for: Explainer videos · MV · Also in: Motion Graphics, Math Explainer</sub> |
| [asciinema](https://github.com/asciinema/asciinema) | 18k | 🟢 Active | Rust (CLI) | Records terminal sessions and replays them in a web player. Small files, copyable text.<br><sub>Good for: Explainer videos · Also in: ASCII & Terminal</sub> |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | ⚪ Dormant | JavaScript (CLI) | Records terminal sessions and renders them as animated GIFs with a window frame.<br><sub>Good for: GIF · Also in: ASCII & Terminal</sub> |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | 🟡 Slowing | C++ (CLI) | Renders Git commit history as a video of code "growing". A classic piece of footage for programmers.<br><sub>Good for: Developer videos · Also in: Data Animation</sub> |
| [Code Hike](https://github.com/code-hike/codehike) | 5.4k | 🟡 Slowing | React / Markdown | Code walkthroughs built with Markdown and React. Can be rendered with Remotion into code explainer videos.<br><sub>Good for: Explainer videos</sub> |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | 🟢 Active | Python | Draws the effect of Git commands as diagrams and animations (built on Manim). Good for Git teaching videos.<br><sub>Good for: Explainer videos · Also in: Data Animation</sub> |
| [doitlive](https://github.com/sloria/doitlive) | 3.6k | 🟢 Active | Python | Pre-write your commands, then mash the keyboard live and they type out character by character. Terminal demos without typos.<br><sub>Good for: Terminal demos · Also in: ASCII & Terminal</sub> |
| [Animotion](https://github.com/animotionjs/animotion) | 1.8k | 🟢 Active | Svelte | Write animated presentations in Svelte, with smooth code highlight transitions and element tweens.<br><sub>Good for: Explainer videos · Talks · Also in: Motion Graphics</sub> |
| [SeeCode](https://github.com/Aryanutkarsh/SeeCode) | 1k | 🟢 Active | JavaScript | Generates explorable animated diagrams from a short JSON spec, so coding agents like Claude can explain code structure.<br><sub>Good for: Code explainer visuals · Also in: Isometric & Voxel</sub> |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 1k | 🟢 Active | Python | Turn Manim animations into presentation slides you can play page by page. Can also export to a web page.<br><sub>Good for: Explainer videos · Talks · Also in: Math Explainer</sub> |
| [demoit](https://github.com/dgageot/demoit) | 780 | 🟢 Active | JavaScript | Tool for live code demos: slides, code and terminal on one page, so you don't switch windows.<br><sub>Good for: Live code demos</sub> |
| [snapcn](https://github.com/shadcn-labs/snapcn) | 679 | 🟢 Active | TypeScript (Remotion) | A Remotion component registry for product demo videos: AI chat streams, terminal sessions, device frames and captions, installed with the shadcn CLI.<br><sub>Good for: Product demo videos · Also in: Shorts, Captions & Editing, Motion Graphics</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="type"></a>

### Kinetic Type & Lyrics

<img src="assets/styles/type.en.png" alt="Kinetic Type & Lyrics sample" width="240" align="right">

> Morphing glyphs, word-by-word entrances, text that hits the lyrics on the beat

**Picks:** [Typed.js](https://github.com/mattboldt/typed.js) · [Splitting](https://github.com/shshaw/Splitting) · [Coldtype](https://github.com/coldtype/coldtype) · [P(doom) MV (mexicat version)](https://github.com/mexicat/pdoom-video) · [AMLL](https://github.com/amll-dev/applemusic-like-lyrics)

34 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 88.6k | 🟢 Active | HTML / CSS / GSAP | Open-sourced by HeyGen. Write scenes in HTML/CSS, animate with GSAP, render straight to MP4. Designed for AI coding agents.<br><sub>Good for: MV · Short videos · AI generation · Also in: Motion Graphics, Shorts, Captions & Editing</sub><br><sub>⚠️ The official skill pack's asset skills can optionally call generation services; the rendering itself is HTML code.</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 75.1k | 🟢 Active | React / TS | Write videos as React components and render them to MP4, with batch generation. Official add-on packages cover captions, audio visualization, three.js, and more.<br><sub>Good for: MV · Short videos · Batch video rendering · Also in: Motion Graphics, Shorts, Captions & Editing, 3D</sub><br><sub>⚠️ Free for individuals and small companies (commercial use included); larger companies need to buy a company license.</sub> |
| [anime.js](https://github.com/juliangarnier/anime) | 75k | 🟢 Active | JavaScript | Lightweight JS animation library. Timelines, stagger, and SVG stroke animation are easy to use.<br><sub>Good for: Web animation · MV · Also in: Motion Graphics</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 52.5k | 🟢 Active | React | Lots of animated React components: text effects, animated backgrounds, interactive motion. Copy and use.<br><sub>Good for: Web motion · Assets · Also in: Motion Graphics, Shaders & Psychedelic</sub> |
| [GSAP](https://github.com/greensock/GSAP) | 31.1k | 🟢 Active | JavaScript | Long-established JS animation engine. Plugins like SplitText and MorphSVG are now all free. Strong at split-text animation and SVG morphing.<br><sub>Good for: MV · Web animation · Also in: Motion Graphics</sub><br><sub>⚠️ Free for commercial use, but under GreenSock's own license, not an OSI-approved open-source license.</sub> |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.5k | 🟢 Active | React | React component library with motion built in: text animations, glowing borders, particle backgrounds, and more.<br><sub>Good for: Web motion · Also in: Motion Graphics</sub> |
| [Typed.js](https://github.com/mattboldt/typed.js) | 16.3k | 🟡 Slowing | JavaScript | Typewriter-effect text animation library.<br><sub>Good for: Web motion</sub> |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.8k | ⚪ Dormant | TypeScript | Hand-drawn annotation animations: circle, underline, and highlight text.<br><sub>Good for: Explainer videos · Web animation · Also in: Hand-drawn & Whiteboard</sub> |
| [editly](https://github.com/mifi/editly) | 5.6k | 🟡 Slowing | JSON / Node | Declarative video editing from JSON or the command line, with built-in transitions, titles, and Ken Burns pan-and-zoom.<br><sub>Good for: Fast cuts · Short videos · Also in: Shorts, Captions & Editing</sub> |
| [Hanzi Writer](https://github.com/chanind/hanzi-writer) | 5.1k | 🟡 Slowing | TypeScript | Chinese character stroke order animation and writing practice library. One line of code animates a character stroke by stroke.<br><sub>Good for: Stroke order animation · Also in: Handwriting & Strokes</sub> |
| [html-video](https://github.com/nexu-io/html-video) | 4.9k | 🟢 Active | HTML / CSS | Lets a local AI coding agent turn HTML/CSS into video. Ships with 21 templates, including kinetic type, Swiss grid and data cards.<br><sub>Good for: Short videos · Promo videos · Also in: Motion Graphics</sub> |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | 🟢 Active | Python | Terminal text effects library with dozens of text entrance animations (burn, rain, decrypt and more).<br><sub>Good for: Intros · Text effects · Also in: ASCII & Terminal</sub> |
| [P(doom) MV (mexicat version)](https://github.com/mexicat/pdoom-video) | 4k | 🟢 Active | JavaScript | Another code-rendered music video for "I'm Upping My P(doom)", with word-by-word beat-synced lyrics.<br><sub>Good for: Lyric MV · Also in: Motion Graphics</sub><br><sub>⚠️ AI was used only to split the audio into stems; all visuals are rendered by code.</sub> |
| [Tegaki](https://github.com/gkurt/tegaki) | 3.3k | 🟢 Active | TypeScript | Handwriting animation for the web: any font and any text can be turned into a pen-writing effect.<br><sub>Good for: Handwriting animation · Also in: Handwriting & Strokes, Hand-drawn & Whiteboard</sub> |
| [P(doom) MV](https://github.com/JohnHeibel/PDoomVideo) | 3k | 🟢 Active | JavaScript | Full source for the music video "I'm Upping My P(doom)", made by Claude Opus 5.5 writing code.<br><sub>Good for: MV · Also in: Motion Graphics</sub> |
| [Bang Motion](https://github.com/bangtutorial/bang-motion) | 2.9k | 🟢 Active | HTML | Browser motion graphics skill: intros, promos, transitions, and kinetic typography, in five styles.<br><sub>Good for: Intros · Promo videos · Also in: Motion Graphics</sub><br><sub>⚠️ The optional After Effects cartoon explainer goes through a Higgsfield bridge; the default workflow is code animation in the browser.</sub> |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2.5k | 🟢 Active | React / TS | Talking-head video skill: aligns to the voiceover word by word and renders animated text cards and camera moves with Remotion.<br><sub>Good for: Talking-head videos · Also in: Shorts, Captions & Editing</sub> |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | 🟢 Active | React / Vue | Apple Music-style lyrics component built by a Chinese developer: word-by-word highlighting, springy scrolling, fluid background.<br><sub>Good for: Lyric MV · Players · Also in: Music Visualization</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1.8k | 🟢 Active | JavaScript (HyperFrames + GSAP) | Agent skill for launch films, product promos, brand stings and kinetic type: it captures the brand, picks one idea only that brand could own, animates with timing rules measured frame by frame from 53 professional pieces, then checks its own render.<br><sub>Good for: Launch films · Product promos · Kinetic type · Also in: Motion Graphics</sub> |
| [Splitting](https://github.com/shshaw/Splitting) | 1.8k | ⚪ Dormant | JavaScript | Splits text into characters or words and adds CSS variables, making per-letter animation easy.<br><sub>Good for: Web motion</sub> |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | 🟢 Active | TypeScript | Add WebGL effects to images, video, and text on web pages: glitch, RGB shift, distortion, and more.<br><sub>Good for: Web effects · MV · Also in: Glitch & Post FX</sub> |
| [world.execute(me) Lyric MV](https://github.com/Nyankomintsu/world-execute-me-lyric-mv) | 586 | 🟢 Active | JavaScript | Fan-made lyric MV that plays the lyrics as a chat with Claude, rendered frame by frame from code at 4K60.<br><sub>Good for: Lyric MV · Also in: Anime, MMD & VRM</sub> |
| [Remotion Bits](https://github.com/av/remotion-bits) | 523 | 🟢 Active | TypeScript (Remotion) | Ready-made animation components for Remotion: text effects, gradient transitions, particles, 3D scenes, charts and more; pull in only what you need.<br><sub>Good for: MG components · Short videos · Also in: Motion Graphics, Particles & Physics</sub><br><sub>⚠️ Not affiliated with the Remotion team.</sub> |
| [HyperFrames Motion Director](https://github.com/geekjourneyx/hyperframes-motion-director) | 486 | 🟢 Active | Skill | Turns articles, products, websites, or READMEs into Chinese-first vertical HyperFrames motion videos, with checks before delivery.<br><sub>Good for: Vertical promo videos · Also in: Shorts, Captions & Editing</sub> |
| [animCJK](https://github.com/parsimonhi/animCJK) | 482 | 🟢 Active | SVG / HTML | SVG animations of Chinese, Japanese and Korean characters written in correct stroke order, including Japanese kana and Korean hanja.<br><sub>Good for: Stroke order animation · Also in: Handwriting & Strokes</sub> |
| [DrawBot](https://github.com/typemytype/drawbot) | 456 | 🟢 Active | Python | Draw 2D graphics in Python and export GIF/MP4; commonly used by type designers for text animation.<br><sub>Good for: Kinetic type · GIF · Also in: Generative Art</sub><br><sub>⚠️ macOS only.</sub> |
| [FredTalk](https://github.com/njrhts2kvv-star/FredTalk) | 404 | 🟢 Active | TypeScript | A talking-head video skill, a searchable motion library, and a Remotion review workflow.<br><sub>Good for: Talking-head videos · Also in: Shorts, Captions & Editing</sub> |
| [Coldtype](https://github.com/coldtype/coldtype) | 345 | 🟢 Active | Python | Python display typography and animation tool. Letterforms can follow the audio rhythm, good for lyric videos and kinetic type.<br><sub>Good for: Lyric MV · Kinetic type · Also in: Generative Art</sub> |
| [Remotion TikTok Template](https://github.com/remotion-dev/template-tiktok) | 308 | 🟢 Active | React / TS | Official Remotion template: automatic speech recognition generates short-video captions that bounce word by word.<br><sub>Good for: Short videos · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ Same license terms as Remotion.</sub> |
| [svg-text-animate](https://github.com/oubenruing/svg-text-animate) | 280 | 🟢 Active | JavaScript | Turns text in any font into an SVG stroke animation in the browser, written out stroke by stroke.<br><sub>Good for: Text stroke animation · Also in: Hand-drawn & Whiteboard</sub> |
| [Claude MV Skill](https://github.com/Joker-chichi/claude-mv-skill) | 253 | 🟢 Active | Skill | Teaches Claude to make hand-painted animation and lyric MVs: storyboard, animation, review and lyric sync, with all visuals generated procedurally.<br><sub>Good for: Hand-drawn MV · Also in: Hand-drawn & Whiteboard</sub> |
| [Vibe Knowledge Shorts](https://github.com/xiazhuo123456789/vibe-knowledge-video) | 211 | 🟢 Active | Python | Generates cinematic knowledge short videos in pure code, with bilingual captions, synthesized music, and recreated historical documents.<br><sub>Good for: Knowledge shorts · Also in: Motion Graphics</sub> |
| [HyperFrames Motion Reel](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | 207 | 🟢 Active | HTML / GSAP | A Claude Code skill that turns a one-line theme into a beat-synced motion-graphics reel with bold type, morphing transitions, particles and camera moves, rendered with HyperFrames.<br><sub>Good for: Showreels · Beat-synced MG · Also in: Motion Graphics</sub> |
| [persian-motion-director](https://github.com/atmirrr/persian-motion-director) | 153 | 🟢 Active | JavaScript (Remotion) | A Claude skill for Persian kinetic typography and motion films: per-letter and per-dot animation that keeps letters joined, with the music locked first and cuts on the beat.<br><sub>Good for: Persian kinetic type · Also in: Motion Graphics</sub><br><sub>⚠️ Code is MIT; ships the Vazirmatn font (OFL).</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="short"></a>

### Shorts, Captions & Editing

<img src="assets/styles/short.png" alt="Shorts, Captions & Editing sample" width="240" align="right">

> Auto captions, transitions, batch-editing videos with code

**Picks:** [FFmpeg](https://github.com/FFmpeg/FFmpeg) · [MoviePy](https://github.com/Zulko/moviepy) · [editly](https://github.com/mifi/editly) · [GL Transitions](https://github.com/gl-transitions/gl-transitions) · [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

33 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 88.6k | 🟢 Active | HTML / CSS / GSAP | Open-sourced by HeyGen. Write scenes in HTML/CSS, animate with GSAP, render straight to MP4. Designed for AI coding agents.<br><sub>Good for: MV · Short videos · AI generation · Also in: Motion Graphics, Kinetic Type & Lyrics</sub><br><sub>⚠️ The official skill pack's asset skills can optionally call generation services; the rendering itself is HTML code.</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 75.1k | 🟢 Active | React / TS | Write videos as React components and render them to MP4, with batch generation. Official add-on packages cover captions, audio visualization, three.js, and more.<br><sub>Good for: MV · Short videos · Batch video rendering · Also in: Motion Graphics, Kinetic Type & Lyrics, 3D</sub><br><sub>⚠️ Free for individuals and small companies (commercial use included); larger companies need to buy a company license.</sub> |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 68.1k | 🟢 Active | C (CLI) | The foundation under almost every code-to-video tool: transcoding, concatenation, filters and burned-in captions, all from the command line.<br><sub>Good for: Editing and compositing · Post-processing · Also in: Glitch & Post FX</sub><br><sub>⚠️ Mirror repository on GitHub.</sub> |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 22.2k | 🟢 Active | React / TS | AI coding agent skill: captures screenshots of your real web pages and turns them into cinematic product promo videos with Remotion.<br><sub>Good for: Product promo videos · Also in: Motion Graphics</sub> |
| [MoviePy](https://github.com/Zulko/moviepy) | 15.2k | 🟢 Active | Python | Python video editing library: cutting, concatenating, adding captions, and compositing, all in code.<br><sub>Good for: Editing and compositing</sub> |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 10k | 🟢 Active | Python | Local editing toolkit for AI coding agents: 42 FFmpeg tools, so the agent can cut, caption and color grade.<br><sub>Good for: Video editing</sub> |
| [editly](https://github.com/mifi/editly) | 5.6k | 🟡 Slowing | JSON / Node | Declarative video editing from JSON or the command line, with built-in transitions, titles, and Ken Burns pan-and-zoom.<br><sub>Good for: Fast cuts · Short videos · Also in: Kinetic Type & Lyrics</sub> |
| [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) | 4.6k | 🟢 Active | TypeScript (Remotion + three.js) | A Claude skill for ~1-minute vertical animated story shorts: 2D characters in a colourful 3D town with ink outlines, lens blur and gliding cameras, rendered with three.js inside Remotion.<br><sub>Good for: Vertical story shorts · Also in: 3D</sub> |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | 🟢 Active | TypeScript | Fork of Motion Canvas focused on headless rendering, so videos can be generated in bulk through an API.<br><sub>Good for: Short videos · Batch video rendering · Also in: Motion Graphics</sub> |
| [FFCreator](https://github.com/tnfe/FFCreator) | 3.2k | 🟡 Slowing | Node.js | Node.js library for generating short videos, open-sourced by a Tencent team. Quickly composes videos from images, text, and transitions.<br><sub>Good for: Short videos · Batch video rendering</sub> |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | 🟢 Active | Rust / SVG | Write video with Rust and SVG, rendered on the GPU, with a focus on speed. Also includes a skill for AI coding agents.<br><sub>Good for: Batch video rendering · Also in: Motion Graphics</sub> |
| [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit) | 3.1k | 🟢 Active | HTML / skill | Skill pack for editing talking-head videos, Reels, and YouTube Shorts with Codex or Claude Code.<br><sub>Good for: Video editing · Short videos</sub> |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2.5k | 🟢 Active | React / TS | Talking-head video skill: aligns to the voiceover word by word and renders animated text cards and camera moves with Remotion.<br><sub>Good for: Talking-head videos · Also in: Kinetic Type & Lyrics</sub> |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.3k | 🟢 Active | GLSL | Open collection of GLSL transitions. Plugs into editors like editly.<br><sub>Good for: Transitions · Also in: Glitch & Post FX</sub> |
| [ReelMimic](https://github.com/edenfunf/reelmimic) | 2.1k | 🟢 Active | JavaScript | Give it a video you like and an AI crew makes a new one in the same style using HyperFrames.<br><sub>Good for: Style-imitation shorts</sub><br><sub>⚠️ The repo was briefly made private in October 2026 and its stars were reset to zero, so actual interest is higher.</sub> |
| [remocn](https://github.com/Remocn/remocn) | 1.8k | 🟢 Active | React / TS | Ready-made animations, transitions, backgrounds, and scene components for Remotion.<br><sub>Good for: MV · Short videos · Also in: Motion Graphics</sub><br><sub>⚠️ Requires Remotion; Remotion's own license terms still apply.</sub> |
| [Diffusion Studio Core](https://github.com/diffusionstudio/core) | 1.2k | 🟡 Slowing | TypeScript | Browser-based video engine. Edit and composite video in code, built on WebCodecs.<br><sub>Good for: Editing and compositing</sub> |
| [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) | 1.2k | 🟢 Active | Prompts / HTML | A Chinese roundup of Opus 5.5 code-rendered videos: 18 full prompts and 54 public cases, including line-art animation, science explainers, launch films and lyric MVs.<br><sub>Good for: Prompt collection · Explainers · MV · Also in: Motion Graphics, Hand-drawn & Whiteboard</sub><br><sub>⚠️ A few cases in the overview use Seedance, Runway or Blender, and the table says so; the featured prompts are all code-rendered.</sub> |
| [Etro](https://github.com/etro-js/etro) | 1.2k | 🟢 Active | TypeScript | Composite video in the browser with TypeScript: layers, effects, keyframes, and export.<br><sub>Good for: Editing and compositing</sub> |
| [video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | 1.1k | 🟡 Slowing | JavaScript | Pushes "I want to make a video" into a storyboard script precise to the second, then hands it to HyperFrames to render.<br><sub>Good for: Storyboard scripts</sub> |
| [adu-motion-video](https://github.com/adunext/adu-motion-video) | 1k | 🟢 Active | JavaScript | By a Chinese developer: AI video editing skill with templates in the open MotionGit .motion format.<br><sub>Good for: Video editing · Short videos</sub> |
| [snapcn](https://github.com/shadcn-labs/snapcn) | 679 | 🟢 Active | TypeScript (Remotion) | A Remotion component registry for product demo videos: AI chat streams, terminal sessions, device frames and captions, installed with the shadcn CLI.<br><sub>Good for: Product demo videos · Also in: Motion Graphics, Code & Terminal Demo</sub> |
| [LiveCanvas](https://github.com/pengchujin/livecanvas) | 563 | 🟢 Active | Python | Turn one sentence into an Apple Live Photo with a cover and animation. Storyboard, Remotion animation, and export in one flow.<br><sub>Good for: Live photos</sub> |
| [Kinetograph](https://github.com/0xS4N4TG/kinetograph) | 543 | 🟢 Active | TypeScript | Fast programmatic video engine made for AI coding agents.<br><sub>Good for: Batch video rendering · Also in: Motion Graphics</sub><br><sub>⚠️ PolyForm Small Business license: free for individuals and small companies; larger companies need a commercial license.</sub> |
| [Universal Transition Shader](https://github.com/cashew-olddew/Universal-Transition-Shader) | 529 | 🟡 Slowing | Godot Shader | Packs the common transition effects into a single Godot shader.<br><sub>Good for: Transitions · Also in: Shaders & Psychedelic</sub> |
| [HyperFrames Motion Director](https://github.com/geekjourneyx/hyperframes-motion-director) | 486 | 🟢 Active | Skill | Turns articles, products, websites, or READMEs into Chinese-first vertical HyperFrames motion videos, with checks before delivery.<br><sub>Good for: Vertical promo videos · Also in: Kinetic Type & Lyrics</sub> |
| [Agentic Product Demo](https://github.com/Alexwtlf/agentic-product-demo) | 418 | 🟢 Active | TypeScript | Has an AI coding agent make product demo videos with Remotion. The UI is rebuilt in code, not screen-recorded.<br><sub>Good for: Product demo videos</sub> |
| [FredTalk](https://github.com/njrhts2kvv-star/FredTalk) | 404 | 🟢 Active | TypeScript | A talking-head video skill, a searchable motion library, and a Remotion review workflow.<br><sub>Good for: Talking-head videos · Also in: Kinetic Type & Lyrics</sub> |
| [lemo-wake](https://github.com/lemomo-ai/lemo-wake) | 379 | 🟢 Active | Python / HTML | Give Claude Code one picture and it takes the text, objects and people apart, rebuilds them in code and makes a seamless loop of about five seconds.<br><sub>Good for: Photo loops · Logo motion · Also in: Motion Graphics</sub><br><sub>⚠️ Code and docs are CC BY-NC 4.0 (no commercial use). Optional small local models handle cut-outs, depth and background fill (LaMa) and are only downloaded after you agree; no image generation.</sub> |
| [Remotion TikTok Template](https://github.com/remotion-dev/template-tiktok) | 308 | 🟢 Active | React / TS | Official Remotion template: automatic speech recognition generates short-video captions that bounce word by word.<br><sub>Good for: Short videos · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ Same license terms as Remotion.</sub> |
| [Remotion Audiogram Template](https://github.com/remotion-dev/template-audiogram) | 279 | 🟢 Active | React / TS | Official Remotion template: turns podcast audio into short videos with a waveform and captions.<br><sub>Good for: Short videos · Podcasts · Also in: Music Visualization</sub><br><sub>⚠️ Same license terms as Remotion.</sub> |
| [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) | 257 | 🟢 Active | TypeScript | Vertical cut-paper style explainer shorts: 9 skills plus Remotion templates, with backgrounds and sound effects included in the repo.<br><sub>Good for: Vertical explainers · Also in: Riso & Paper Collage</sub> |
| [Creator Style Kit](https://github.com/threeaus/creator-style-kit) | 60 | 🟢 Active | Python | 18 vertical HyperFrames video styles (fonts, colors, motion, sound effects, composition).<br><sub>Good for: Vertical shorts</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="hand"></a>

### Hand-drawn & Whiteboard

<img src="assets/styles/hand.png" alt="Hand-drawn & Whiteboard sample" width="240" align="right">

> Sketchy lines, stroke-by-stroke drawing, watercolor brushes, hand-drawn charts

**Picks:** [Rough.js](https://github.com/rough-stuff/rough) · [p5.brush](https://github.com/acamposuribe/p5.brush) · [Vivus](https://github.com/maxwellito/vivus) · [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) · [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)

27 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Rough.js](https://github.com/rough-stuff/rough) | 21.4k | ⚪ Dormant | JavaScript | Generates hand-drawn, sketchy lines and shapes. Can be combined with other animation libraries for hand-drawn style animation.<br><sub>Good for: Explainer videos · Web animation</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 20.1k | 🟢 Active | JavaScript | A toolbox of film styles made in code: 66 ready-made styles (Memphis, subway map, chalkboard, and more) that let an AI coding agent make videos in each style, all drawn with code.<br><sub>Good for: MV · Short films · Also in: Motion Graphics, Pixel & Retro</sub><br><sub>⚠️ Styles are tuned for Claude; results may differ with other models.</sub> |
| [Vivus](https://github.com/maxwellito/vivus) | 15.5k | ⚪ Dormant | JavaScript | SVG line-drawing animation that draws line art stroke by stroke.<br><sub>Good for: Web animation</sub><br><sub>⚠️ Not updated since 2022; simple and stable.</sub> |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.8k | ⚪ Dormant | TypeScript | Hand-drawn annotation animations: circle, underline, and highlight text.<br><sub>Good for: Explainer videos · Web animation · Also in: Kinetic Type & Lyrics</sub> |
| [chart.xkcd](https://github.com/timqian/chart.xkcd) | 7.9k | 🟢 Active | JavaScript | Hand-drawn chart library in the xkcd comic style, with wobbly lines and a comic font.<br><sub>Good for: Hand-drawn charts · Also in: Data Animation</sub> |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 7.5k | 🟢 Active | JavaScript | 35 art styles and 9 narration grammars, animating pictures with code. The soundtrack is also synthesized in code.<br><sub>Good for: Art animation · Also in: Ink & Watercolor</sub><br><sub>⚠️ When a real person is needed on screen, an image generation model produces the frame; everything else is drawn in code.</sub> |
| [roughViz](https://github.com/jwilber/roughViz) | 7.2k | ⚪ Dormant | JavaScript | Sketchy chart library built on Rough.js. Bar and pie charts get a hand-drawn look.<br><sub>Good for: Hand-drawn charts · Also in: Data Animation</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [MG Styles 15](https://github.com/Vincentwei1021/mg-styles-15) | 3.9k | 🟢 Active | Python / Web | 15 motion design style demo films, each written as code by Claude Opus 5.5 from a single prompt. Prompts and source included.<br><sub>Good for: Style sample clips · Also in: Motion Graphics, 3D</sub><br><sub>⚠️ Of the 15, only the 3D one uses Blender; the rest are pure code.</sub> |
| [Tegaki](https://github.com/gkurt/tegaki) | 3.3k | 🟢 Active | TypeScript | Handwriting animation for the web: any font and any text can be turned into a pen-writing effect.<br><sub>Good for: Handwriting animation · Also in: Handwriting & Strokes, Kinetic Type & Lyrics</sub> |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | 3.2k | 🟢 Active | p5.js | Starter template for having Claude make hand-painted cartoon animation: p5.js + p5.brush, with character and camera tools.<br><sub>Good for: Hand-drawn cartoons · Also in: Anime, MMD & VRM</sub> |
| [Animate](https://github.com/cth9191/animate) | 2.2k | 🟢 Active | JavaScript / Canvas | Claude Code skill: draws short animations procedurally on a single canvas, with 7 built-in styles: paper cut-out, hatched ink, Riso print, sketchbook, math, pixel, and isometric.<br><sub>Good for: Explainer videos · Short films · Also in: Pixel & Retro, Math Explainer, Riso & Paper Collage</sub> |
| [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) | 2.1k | 🟢 Active | TypeScript | Turns Excalidraw whiteboard drawings into stroke-by-stroke animations, exportable as video.<br><sub>Good for: Explainer videos</sub> |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 2k | 🟢 Active | TypeScript | AI coding agent skill: draws illustrations, loop animations, and short films with soundtracks in code, in dozens of styles, with identical results on every render.<br><sub>Good for: Illustration · Looping animation · Short films · Also in: Generative Art</sub> |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.5k | 🟢 Active | JavaScript | Adds natural brushes, watercolor fills, and hatching to p5.js for hand-drawn and watercolor textures.<br><sub>Good for: Generative art · MV · Also in: Generative Art</sub> |
| [spectral.js](https://github.com/rvanwijnen/spectral.js) | 1.3k | 🟡 Slowing | JavaScript | Mixes colors the way real paint does (Kubelka-Munk), so blue plus yellow gives green, not gray. For watercolor and oil-paint looks.<br><sub>Good for: Paint mixing</sub> |
| [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) | 1.2k | 🟢 Active | Prompts / HTML | A Chinese roundup of Opus 5.5 code-rendered videos: 18 full prompts and 54 public cases, including line-art animation, science explainers, launch films and lyric MVs.<br><sub>Good for: Prompt collection · Explainers · MV · Also in: Motion Graphics, Shorts, Captions & Editing</sub><br><sub>⚠️ A few cases in the overview use Seedance, Runway or Blender, and the table says so; the featured prompts are all code-rendered.</sub> |
| [line-art-animation](https://github.com/JDhruv14/line-art-animation) | 1.2k | 🟢 Active | TypeScript (SVG) | A Claude skill plus a small TypeScript library for ink-on-paper line-art figures that walk, ride and react to clicks, in scenes that run from day to night. Everything is drawn live in SVG, with scripts for frame-by-frame video capture.<br><sub>Good for: Line-art characters · Scene animation</sub> |
| [Pintr](https://github.com/javierbyte/pintr) | 843 | 🟢 Active | TypeScript | Turns photos into single-line illustrations drawn in one continuous stroke.<br><sub>Good for: Single-stroke drawing · Also in: Plotter & Line Art</sub> |
| [Whiteboard Teacher Video](https://github.com/liangdabiao/whiteboard-teacher-video) | 580 | 🟢 Active | Python | Made by a Chinese developer: turns an explainer script into a hand-drawn whiteboard video. Shapes are drawn stroke by stroke and text is written character by character, with zero image-generation cost.<br><sub>Good for: Knowledge shorts</sub> |
| [Claude Drawing Skill](https://github.com/cloveric/claude-drawing-skill) | 373 | 🟢 Active | Python | Claude paints stroke by stroke with code, in 77 styles including ink wash, oil painting, clay, cyanotype, stained glass, and Jiangnan gardens, with no image generation model.<br><sub>Good for: Illustration · Ink wash · Also in: Ink & Watercolor</sub> |
| [Dashi Style Explainers](https://github.com/chuspeeism/dashi-animationstyle) | 331 | 🟢 Active | HTML | By a Chinese developer: turns Chinese talking-head knowledge scripts into explainer animations in 7 styles. Claude writes HTML / Canvas code to draw each frame.<br><sub>Good for: Explainers</sub> |
| [svg-text-animate](https://github.com/oubenruing/svg-text-animate) | 280 | 🟢 Active | JavaScript | Turns text in any font into an SVG stroke animation in the browser, written out stroke by stroke.<br><sub>Good for: Text stroke animation · Also in: Kinetic Type & Lyrics</sub> |
| [weilanx Claude Videos](https://github.com/Azure12355/weilanx-claude-videos) | 277 | 🟢 Active | TypeScript | Made by a Chinese developer: hand-drawn and pixel-art explainer videos written purely in code with Remotion + React + SVG.<br><sub>Good for: Explainer videos · Also in: Pixel & Retro</sub><br><sub>⚠️ One skill's cover image used text-to-image generation; it can be swapped for a code-rendered frame.</sub> |
| [Claude MV Skill](https://github.com/Joker-chichi/claude-mv-skill) | 253 | 🟢 Active | Skill | Teaches Claude to make hand-painted animation and lyric MVs: storyboard, animation, review and lyric sync, with all visuals generated procedurally.<br><sub>Good for: Hand-drawn MV · Also in: Kinetic Type & Lyrics</sub> |
| [Kalem](https://github.com/leodavincs/kalem) | 119 | 🟢 Active | Python / JavaScript | Claude Code skill that splits a video into scenes and picks the engine that draws each one best (Paper.js, PixiJS, HyperFrames, three.js, Manim and more), then joins them with transitions such as a page flip and adds frame-locked sound effects.<br><sub>Good for: Scene-by-scene explainers · Also in: Motion Graphics</sub><br><sub>⚠️ Docs are mainly in Turkish, with an English version. The notebook-engraving look of its plate (levha) engine uses Codex image generation for the base drawing; a flag turns that off, and the blueprint style runs entirely in code. The other engines render from code.</sub> |
| [Watercolor Playground](https://github.com/msurguy/watercolor-playground) | 107 | 🟢 Active | TypeScript | Realistic watercolor simulation: paint bleeds, settles, and dries on paper.<br><sub>Good for: Watercolor painting · Also in: Ink & Watercolor</sub> |
| [wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | 68 | 🟢 Active | three.js | Real-time three.js flow-field painter that draws Bezier strokes with a wet, thick-paint look.<br><sub>Good for: Flow field drawing · Also in: Flow & Wind Fields</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="gen"></a>

### Generative Art

<img src="assets/styles/gen.png" alt="Generative Art sample" width="240" align="right">

> Algorithmic patterns, flow fields, seamless loops

**Picks:** [p5.js](https://github.com/processing/p5.js) · [Paper.js](https://github.com/paperjs/paper.js) · [nannou](https://github.com/nannou-org/nannou) · [canvas-sketch](https://github.com/mattdesl/canvas-sketch) · [css-doodle](https://github.com/css-doodle/css-doodle)

44 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.9k | 🟢 Active | TypeScript | Fast 2D rendering engine (WebGL / WebGPU) for large numbers of sprites, filters, and 2D motion effects.<br><sub>Good for: Web animation · MV · Also in: Motion Graphics, Particles & Physics</sub> |
| [raylib](https://github.com/raysan5/raylib) | 35.8k | 🟢 Active | C (many bindings) | Simple, beginner-friendly C graphics library with bindings for dozens of languages. Quick for 2D/3D animations and small demos.<br><sub>Good for: 2D/3D animation · Mini games · Also in: Pixel & Retro, 3D</sub> |
| [Graphite](https://github.com/GraphiteEditor/Graphite) | 28k | 🟢 Active | Rust / Node graph | An open-source 2D graphics editor with a node graph under the layers: shapes, patterns and arrangements are generated procedurally with nodes and can be tweaked live.<br><sub>Good for: Vector art · Procedural design · Also in: Motion Graphics</sub><br><sub>⚠️ Still in alpha; motion graphics are on the roadmap, and today it is mainly for vector and procedural design.</sub> |
| [p5.js](https://github.com/processing/p5.js) | 24.4k | 🟢 Active | JavaScript | The most popular creative coding library: draw, build interactions, and animate on the web. Plenty of Chinese tutorials too.<br><sub>Good for: Generative art · MV · Also in: Particles & Physics, Music Visualization</sub><br><sub>⚠️ Exporting video takes extra steps (save frames one by one, or screen-record).</sub> |
| [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 16.3k | 🟢 Active | HTML / Canvas / three.js | 703 prompts people used to make videos with Claude Opus 5.5, each linked to the original post and a live remake. The picture is drawn in code (Canvas, SVG, three.js): mostly motion graphics, explainers and 3D scenes.<br><sub>Good for: Prompt collection · MV · Also in: Motion Graphics, 3D</sub><br><sub>⚠️ A few entries overlay AI-generated images or use Blender; those are labeled.</sub> |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | 🟢 Active | JavaScript | Vector graphics scripting framework with strong path operations and Bezier curves, good for vector-style generative art.<br><sub>Good for: Generative art · Also in: Motion Graphics</sub> |
| [primitive](https://github.com/fogleman/primitive) | 13.6k | ⚪ Dormant | Go | Approximates a photo step by step with triangles, ellipses, and other shapes. The process can be exported as an animation.<br><sub>Good for: Geometric reconstruction · Also in: Geometric & Low-poly</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 Active | C++ | C++ creative coding framework with strong performance. Often used for interactive installations, stage visuals, and music visualization.<br><sub>Good for: Performances · Installations · MV · Also in: Music Visualization, 3D</sub> |
| [Two.js](https://github.com/jonobr1/two.js) | 8.8k | 🟢 Active | JavaScript | 2D vector drawing API. The same code outputs SVG, Canvas, or WebGL, good for flat geometric animation.<br><sub>Good for: Web animation · Also in: Motion Graphics</sub> |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.4k | ⚪ Dormant | JavaScript | A few lines of code give you animated 3D backgrounds: waves, birds, fog, grids, and more.<br><sub>Good for: Background assets · Also in: 3D</sub> |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | 🟢 Active | Rust | Rust creative coding framework with audio and OSC modules, suited to real-time audiovisual work.<br><sub>Good for: Generative art · Performances · Also in: Music Visualization</sub> |
| [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) | 6.5k | ⚪ Dormant | JavaScript | Procedurally generated, endlessly scrolling Chinese landscape painting. Mountains, rocks, trees, and pavilions are all drawn stroke by stroke by algorithms.<br><sub>Good for: Ink wash scrolls · Generative art · Also in: Ink & Watercolor</sub><br><sub>⚠️ Not updated since 2018; the work itself is complete and usable.</sub> |
| [css-doodle](https://github.com/css-doodle/css-doodle) | 6.1k | 🟢 Active | CSS | Web component that generates patterns and animations in bulk from CSS rules.<br><sub>Good for: Generative art</sub> |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | 🟡 Slowing | C++ | C++ creative coding framework geared toward professional real-time graphics and installation work.<br><sub>Good for: Performances · Installations · Also in: 3D</sub> |
| [Pts](https://github.com/williamngan/pts) | 5.4k | 🟢 Active | TypeScript | Visualization and creative coding library built around geometric relations of points, lines and shapes.<br><sub>Good for: Generative art · Also in: Data Animation</sub> |
| [canvas-sketch](https://github.com/mattdesl/canvas-sketch) | 5.3k | 🟢 Active | JavaScript | Generative art workflow that exports high-res frames, GIFs, and MP4, well suited to seamless looping animation.<br><sub>Good for: Generative art · Looping animation</sub> |
| [Tweakpane](https://github.com/cocopon/tweakpane) | 4.8k | 🟡 Slowing | TypeScript | Compact parameter panel for tweaking color, speed, and count live while creative coding.<br><sub>Good for: Parameter panels</sub> |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | 🟢 Active | TypeScript | Toolkit of over a hundred TypeScript packages for generative art and visualization, long maintained by its author.<br><sub>Good for: Generative art · Also in: Data Animation</sub> |
| [FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | 3.6k | 🟢 Active | Multiple languages | Cross-language noise function library (C#, C++, GLSL, JS, Rust, and more). Basic material for flow fields, terrain, and textures.<br><sub>Good for: Noise functions · Also in: Procedural Generation</sub> |
| [fishdraw](https://github.com/LingDong-/fishdraw) | 2.6k | ⚪ Dormant | JavaScript | Procedurally generates line drawings of fish, output as single-line SVG that a pen plotter can draw directly.<br><sub>Good for: Line art · Pen plotters · Also in: Plotter & Line Art</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [The Nature of Code](https://github.com/nature-of-code/noc-book-2) | 2k | 🟡 Slowing | p5.js | 2024 edition of The Nature of Code: simulate forces, particles, flocking, and cellular automata with p5.js. Essential reading for generative art beginners.<br><sub>Good for: Tutorials · Also in: Particles & Physics, Artificial Life & Growth</sub> |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 2k | 🟢 Active | TypeScript | AI coding agent skill: draws illustrations, loop animations, and short films with soundtracks in code, in dozens of styles, with identical results on every render.<br><sub>Good for: Illustration · Looping animation · Short films · Also in: Hand-drawn & Whiteboard</sub> |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.5k | 🟢 Active | JavaScript | Adds natural brushes, watercolor fills, and hatching to p5.js for hand-drawn and watercolor textures.<br><sub>Good for: Generative art · MV · Also in: Hand-drawn & Whiteboard</sub> |
| [Radiant](https://github.com/pbakaus/radiant) | 1.1k | 🟢 Active | GLSL / WebGL | Curated collection of generative shader art; every piece runs directly in the browser.<br><sub>Good for: Shader art · Also in: Shaders & Psychedelic</sub> |
| [Generative Design Code Package](https://github.com/generative-design/Code-Package-p5.js) | 1k | 🟢 Active | JavaScript | All the p5.js example code from the book Generative Design, a classic generative design textbook.<br><sub>Good for: Tutorials · Generative art</sub> |
| [OPENRNDR](https://github.com/openrndr/openrndr) | 988 | 🟢 Active | Kotlin | Kotlin creative coding framework, good for generative graphics and real-time visuals.<br><sub>Good for: Generative art · Performances</sub> |
| [DOjS](https://github.com/SuperIlu/DOjS) | 965 | 🟡 Slowing | JavaScript (DOS) | JavaScript creative coding environment that runs on MS-DOS, with a p5.js-like API and plenty of retro flavor.<br><sub>Good for: Retro creative coding · Also in: Pixel & Retro</sub> |
| [Fragment](https://github.com/raphaelameaume/fragment) | 951 | 🟢 Active | JavaScript | Modern creative coding toolkit with hot reload, a parameter panel, and frame sequence export built in.<br><sub>Good for: Generative art · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Still in alpha.</sub> |
| [genjutsu](https://github.com/AThevon/genjutsu) | 849 | 🟢 Active | Python / skill | Creative coding skills for Claude Code and claude.ai: motion, micro-interactions, and design sense.<br><sub>Good for: Creative coding · Also in: Motion Graphics</sub> |
| [vsketch](https://github.com/abey79/vsketch) | 615 | 🟢 Active | Python | Python generative art environment for pen plotters. Tweak parameters with live preview, export single-line SVG.<br><sub>Good for: Generative art · Pen plotters · Also in: Plotter & Line Art</sub> |
| [Bauble](https://github.com/ianthehenry/bauble) | 598 | 🟢 Active | Janet (Lisp) | Playground for making 3D art with Lisp and math, built on signed distance field ray marching.<br><sub>Good for: 3D math art · Also in: Shaders & Psychedelic, 3D</sub> |
| [Processing](https://github.com/processing/processing4) | 550 | 🟢 Active | Java | The long-standing creative coding tool; save images frame by frame and stitch them into video.<br><sub>Good for: Generative art</sub> |
| [play.core](https://github.com/ertdfgcvb/play.core) | 546 | 🟢 Active | JavaScript | Experimental platform for ASCII character animation in JS. Each character is a "pixel".<br><sub>Good for: Generative art · Also in: ASCII & Terminal</sub> |
| [Mosaic](https://github.com/d3cod3/Mosaic) | 519 | 🟢 Active | C++ | Visual patching creative coding platform built on openFrameworks, connecting nodes, code, and audio.<br><sub>Good for: Node-based creative coding · Also in: Live Coding & VJ</sub> |
| [DrawBot](https://github.com/typemytype/drawbot) | 456 | 🟢 Active | Python | Draw 2D graphics in Python and export GIF/MP4; commonly used by type designers for text animation.<br><sub>Good for: Kinetic type · GIF · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ macOS only.</sub> |
| [p5.riso](https://github.com/antiboredom/p5.riso) | 376 | 🟢 Active | JavaScript | Risograph printing library for p5.js: ink color separation, misregistration, and halftone dots for a stencil-print look.<br><sub>Good for: Riso print look · Also in: Riso & Paper Collage</sub> |
| [LUMEN](https://github.com/Leonxlnx/lumenshaders) | 369 | 🟢 Active | WebGL2 | Generative shader studio with 9 WebGL2 art modes. Blend styles and export seamless loops.<br><sub>Good for: Shader art · Also in: Shaders & Psychedelic</sub> |
| [Coldtype](https://github.com/coldtype/coldtype) | 345 | 🟢 Active | Python | Python display typography and animation tool. Letterforms can follow the audio rhythm, good for lyric videos and kinetic type.<br><sub>Good for: Lyric MV · Kinetic type · Also in: Kinetic Type & Lyrics</sub> |
| [flow-fields](https://github.com/romellogoodman/flow-fields) | 311 | 🟢 Active | JavaScript | JavaScript library for creating flow fields: lines that flow along noise.<br><sub>Good for: Flow field art · Also in: Flow & Wind Fields</sub> |
| [Space Colonization Experiments](https://github.com/jasonwebb/2d-space-colonization-experiments) | 229 | 🟡 Slowing | JavaScript | Growth animation experiments that use the space colonization algorithm to grow tree branches, leaf veins, and coral.<br><sub>Good for: Growth animation · Also in: Artificial Life & Growth</sub> |
| [Patchies](https://github.com/heypoom/patchies) | 216 | 🟢 Active | TypeScript / Web | A creative coding patcher in the browser: wire small p5.js, Hydra, GLSL and three.js programs together like modules for audio-reactive visuals.<br><sub>Good for: Live coding · Creative coding · Also in: Live Coding & VJ</sub><br><sub>⚠️ AGPL-3.0 licensed.</sub> |
| [genart](https://github.com/camilleroux/genart-skill) | 180 | 🟢 Active | JavaScript / skill | A generative art plugin for Claude Code: hash-seeded, deterministic pieces that render the same at any resolution, covering Canvas, p5.js, three.js, SVG and pen-plotter export.<br><sub>Good for: Generative art · On-chain art · Also in: Plotter & Line Art</sub> |
| [L-System Explorer](https://github.com/anvaka/lsystem) | 101 | 🟢 Active | JavaScript / WebGL | L-system explorer in WebGL. A few rules grow plants, snowflakes and fractal curves.<br><sub>Good for: Growth patterns · Also in: Artificial Life & Growth</sub> |
| [neon](https://github.com/Stanko/neon) | 44 | 🟡 Slowing | JavaScript | Generative art of neon lines made with a 2D vector field.<br><sub>Good for: Generative art · Also in: Flow & Wind Fields</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="shader"></a>

### Shaders & Psychedelic

<img src="assets/styles/shader.png" alt="Shaders & Psychedelic sample" width="240" align="right">

> Procedural light, noise, fluid gradients and abstract forms

**Picks:** [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) · [LYGIA](https://github.com/patriciogonzalezvivo/lygia) · [Paper Shaders](https://github.com/paper-design/shaders) · [ShaderGradient](https://github.com/ruucm/shadergradient) · [TypeGPU](https://github.com/software-mansion/TypeGPU)

103 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 119k | 🟢 Active | JavaScript | The de facto standard for 3D on the web: scenes, materials, particles, and post-processing, with lots of examples.<br><sub>Good for: MV · Web 3D · Also in: 3D, Particles & Physics</sub> |
| [React Bits](https://github.com/DavidHDev/react-bits) | 52.5k | 🟢 Active | React | Lots of animated React components: text effects, animated backgrounds, interactive motion. Copy and use.<br><sub>Good for: Web motion · Assets · Also in: Motion Graphics, Kinetic Type & Lyrics</sub> |
| [3D Game Shaders for Beginners](https://github.com/lettier/3d-game-shaders-for-beginners) | 20.1k | ⚪ Dormant | GLSL / C++ | Illustrated step-by-step tutorial for dozens of 3D shader effects: SSAO, depth of field, bloom, cartoon outlines, pixelation, and more.<br><sub>Good for: Tutorials · Also in: 3D</sub><br><sub>⚠️ Not updated since 2023; the tutorial content is complete.</sub> |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.9k | ⚪ Dormant | JavaScript | Real-time fluid simulation in the browser. The colorful smoke looks great on video.<br><sub>Good for: Effect assets · Also in: Particles & Physics</sub> |
| [React Native Skia](https://github.com/wcandillon/react-native-skia) | 8.8k | 🟢 Active | React Native | Draw high-performance 2D graphics and animations in React Native with Skia. Supports runtime shaders.<br><sub>Good for: Mobile motion · Also in: Motion Graphics</sub> |
| [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample) | 7.9k | 🟢 Active | Unity HLSL | Toon lighting shader example for Unity URP. A beginner reference for anime character outlines and stepped-shade shadows.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub> |
| [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | 7.1k | 🟡 Slowing | GLSL | Beginner book on shaders (a Chinese edition exists). Learn to write fragment shaders step by step.<br><sub>Good for: Tutorials</sub> |
| [Unity Shader Essentials (book source)](https://github.com/candycat1992/Unity_Shaders_Book) | 6.1k | ⚪ Dormant | Unity ShaderLab | Full source code for a classic Chinese textbook on Unity shaders, Unity Shader Essentials.<br><sub>Good for: Chinese tutorials · Also in: 3D</sub><br><sub>⚠️ Not updated since 2023; the book's content is complete.</sub> |
| [Shaders](https://github.com/shader-effects-inc/shaders) | 6k | 🟢 Active | TypeScript | WebGPU effect components for React, Vue, Svelte, Solid, and other frameworks.<br><sub>Good for: Web effects</sub> |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.5k | 🟢 Active | TypeScript | Component library that layers WebGL fluid, shader, and 3D effects over real web UI.<br><sub>Good for: Web effects · Also in: Particles & Physics</sub> |
| [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | 5.4k | 🟢 Active | GLSL / C++ | Command-line shader viewer. Can record shader pieces as frame sequences, handy for turning Shadertoy-style visuals into video.<br><sub>Good for: MV · Effect assets</sub> |
| [Orillusion](https://github.com/Orillusion/orillusion) | 5.2k | 🟢 Active | TypeScript / WebGPU | Pure WebGPU web 3D engine built by a Chinese team.<br><sub>Good for: Web 3D · Also in: 3D</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 Active | Node graph / C# | Formerly Tooll3. Open-source real-time motion graphics software with nodes and a timeline. Often used for music videos and live shows.<br><sub>Good for: MV · Live performances · Also in: Live Coding & VJ, 3D</sub> |
| [SHADERed](https://github.com/dfranx/SHADERed) | 4.8k | ⚪ Dormant | GLSL / C++ | Cross-platform shader IDE. Step-debug shaders and build multi-pass effects.<br><sub>Good for: Effect assets</sub><br><sub>⚠️ Not updated since 2023.</sub> |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | 🟢 Active | C++ | Open-source, MilkDrop-compatible visualizer engine. Embed it in a player or use it for music video backgrounds.<br><sub>Good for: Music visualizer · MV · Also in: Music Visualization</sub> |
| [Shader School](https://github.com/stackgl/shader-school) | 4.4k | ⚪ Dormant | GLSL | A level-by-level GLSL shader course: write shaders one exercise at a time in the browser.<br><sub>Good for: Tutorials</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Godot Shaders](https://github.com/gdquest-demos/godot-shaders) | 4.2k | 🟢 Active | Godot Shader | GDQuest's large collection of Godot 2D and 3D shaders: dissolve, outline, water, pixelation, and more.<br><sub>Good for: Shader collections · Also in: 3D, Pixel & Retro</sub> |
| [UnityChan Toon Shader](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) | 4.1k | ⚪ Dormant | Unity | Toon shader from Unity's official Japan team, for cel-shaded anime-look characters and scenes.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub><br><sub>⚠️ Not updated since 2024. New projects can use Unity Toon Shader.</sub> |
| [Paper Shaders](https://github.com/paper-design/shaders) | 4k | 🟢 Active | TypeScript | Shader components from the Paper team: mesh gradients, grain, metallic sheen, and more. Zero dependencies.<br><sub>Good for: Background assets · Web</sub> |
| [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | 3.5k | 🟢 Active | GLSL / HLSL / WGSL | Large shader function library: noise, lighting, color, filters. Building blocks for psychedelic visuals.<br><sub>Good for: Effect assets</sub><br><sub>⚠️ Free for non-commercial use; commercial use needs a separate license.</sub> |
| [TypeGPU](https://github.com/software-mansion/TypeGPU) | 3.3k | 🟢 Active | TypeScript / WebGPU | Toolkit for writing WebGPU shaders in TypeScript. Type-safe, works on the web and in React Native.<br><sub>Good for: WebGPU shaders</sub> |
| [ShaderGradient](https://github.com/ruucm/shadergradient) | 3.2k | 🟢 Active | TypeScript | Adjustable animated 3D gradients, the fluid-gradient style that has been popular in recent years.<br><sub>Good for: Background assets</sub> |
| [gl-react](https://github.com/gre/gl-react) | 3k | 🟢 Active | TypeScript | Write and compose WebGL shaders as React components. Also works with React Native.<br><sub>Good for: React shaders</sub> |
| [webgl-noise](https://github.com/ashima/webgl-noise) | 3k | ⚪ Dormant | GLSL | Classic GLSL procedural noise library. The noise in countless shader works comes from here.<br><sub>Good for: Noise functions · Also in: Procedural Generation</sub> |
| [Inferno](https://github.com/twostraws/Inferno) | 2.9k | 🟡 Slowing | Swift / Metal (iOS) | Collection of Metal shaders for SwiftUI: fire, water ripples, pixelation, shine sweeps, and more. Ready to use in mobile apps.<br><sub>Good for: App motion · Also in: Glitch & Post FX</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.8k | 🟡 Slowing | JavaScript | Real-time video synthesizer in the browser, modeled on analog signal synthesizers. A few lines of code give feedback, distortion, and psychedelic color visuals.<br><sub>Good for: Live VJ · MV · Also in: Live Coding & VJ, Glitch & Post FX</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [vgpu](https://github.com/vercel-labs/vgpu) | 2.7k | 🟢 Active | TypeScript / WGSL | A small WebGPU library from Vercel: import WGSL shaders like TypeScript modules and render the same code in the browser or headless Node.<br><sub>Good for: WebGPU effects · Web 3D · Also in: 3D</sub> |
| [glslEditor](https://github.com/patriciogonzalezvivo/glslEditor) | 2.6k | ⚪ Dormant | JavaScript | In-browser GLSL fragment shader editor with visual controls for colors and values.<br><sub>Good for: Shader editors</sub><br><sub>⚠️ Not updated since 2023.</sub> |
| [glslify](https://github.com/glslify/glslify) | 2.3k | ⚪ Dormant | JavaScript | Import modules into GLSL shaders the way npm does, so functions like noise and blend modes can be reused directly.<br><sub>Good for: Shader modules</sub><br><sub>⚠️ Not updated since 2022.</sub> |
| [glslCanvas](https://github.com/patriciogonzalezvivo/glslCanvas) | 2.3k | ⚪ Dormant | JavaScript | Small tool that runs GLSL shaders on a web page canvas. Used by The Book of Shaders.<br><sub>Good for: Web shaders</sub><br><sub>⚠️ Not updated since 2023.</sub> |
| [GLSL-PathTracer](https://github.com/knightcrawler25/GLSL-PathTracer) | 2.1k | ⚪ Dormant | C++ / GLSL | Small GPU physically based path tracer, good for learning and for rendering material showcases.<br><sub>Good for: Realistic rendering · Also in: Path Tracing</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | 🟡 Slowing | JavaScript | MilkDrop music visualizer for WebGL, with many classic psychedelic presets built in.<br><sub>Good for: Music visualizer · MV · Also in: Music Visualization</sub> |
| [GLSL Sandbox](https://github.com/mrdoob/glsl-sandbox) | 1.7k | 🟢 Active | JavaScript | Shader editor and gallery from the author of three.js. Open a shader, edit the code and see the result right away.<br><sub>Good for: Shader gallery · Also in: Live Coding & VJ</sub> |
| [Poiyomi Toon Shader](https://github.com/poiyomi/PoiyomiToonShader) | 1.7k | 🟢 Active | Unity | Full-featured Unity toon shader, commonly used for VRChat avatars.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub> |
| [Dither3D](https://github.com/runevision/Dither3D) | 1.6k | 🟡 Slowing | Unity Shader | Fractal dithering shader that sticks to object surfaces and doesn't flicker when the camera moves. For 1-bit style 3D visuals.<br><sub>Good for: 1-bit 3D · Also in: Dither & 1-bit, 3D</sub><br><sub>⚠️ Unity shader; not updated since early 2025.</sub> |
| [Unity Toon Shader](https://github.com/Unity-Technologies/com.unity.toonshader) | 1.6k | 🟢 Active | Unity | Unity's official toon shader for Japanese anime-style characters and scenes.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub> |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.6k | 🟢 Active | C++ (Windows) | A continuation of MilkDrop, with new features such as any audio source and double-preset blending.<br><sub>Good for: Music visualizer · Also in: Music Visualization</sub> |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | 🟡 Slowing | GLSL | Live shader coding tool used in the demoscene Shader Showdown contest. Write code live and see the picture live.<br><sub>Good for: Live performances · Also in: Live Coding & VJ, Demoscene</sub> |
| [Liquid Logo](https://github.com/paper-design/liquid-logo) | 1.5k | 🟡 Slowing | TypeScript | Small tool from the Paper team: turns a logo into a flowing liquid-metal animation.<br><sub>Good for: Logo motion · Also in: Liquid Glass, Motion Graphics</sub> |
| [ShaderMan](https://github.com/smkplus/ShaderMan) | 1.5k | ⚪ Dormant | C# (Unity) | Converts Shadertoy shaders into HLSL / CG that Unity can use.<br><sub>Good for: Shader ports</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [GLSL Primer Cards](https://github.com/wshxbqq/GLSL-Card) | 1.5k | ⚪ Dormant | GLSL | GLSL shader language primer compiled by a Chinese developer, with functions and usage laid out as cards.<br><sub>Good for: Chinese tutorials</sub><br><sub>⚠️ Not updated since 2019.</sub> |
| [NoiseShader](https://github.com/keijiro/NoiseShader) | 1.4k | 🟡 Slowing | Unity HLSL | Keijiro's Unity noise shader library, with simplex noise, Perlin noise and more.<br><sub>Good for: Noise functions · Also in: Procedural Generation</sub> |
| [CustomShaderMaterial](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial) | 1.4k | 🟡 Slowing | TypeScript | Layer your own shaders on top of three.js standard materials while keeping lighting and shadows.<br><sub>Good for: three.js shaders · Also in: 3D</sub> |
| [URP_Toon](https://github.com/ChiliMilk/URP_Toon) | 1.4k | ⚪ Dormant | Unity | Toon shader for Unity URP with outlines, stepped shading, and rim light.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | 🟢 Active | GLSL | RetroArch shader collection: CRT scanlines, pixel upscaling, and other retro display effects.<br><sub>Good for: Retro post-processing · Also in: Pixel & Retro, VHS & Analog</sub> |
| [shuding/liquid-glass](https://github.com/shuding/liquid-glass) | 1.2k | 🟡 Slowing | SVG / JS | Copy-and-paste liquid glass shader, built with SVG filters.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub> |
| [PixiJS Filters](https://github.com/pixijs/filters) | 1.2k | 🟡 Slowing | TypeScript | Community filter collection for PixiJS: glitch, glow, pixelate, CRT, and dozens more effects.<br><sub>Good for: 2D effects · Also in: Glitch & Post FX</sub> |
| [motion-anything](https://github.com/nexu-io/motion-anything) | 1.1k | 🟢 Active | JavaScript | Describe the feel in one sentence and AI generates motion pages and launch videos. Comes with reusable shader, Canvas, and animated text recipes.<br><sub>Good for: Motion pages · Launch videos · Also in: Motion Graphics</sub> |
| [glsl-blend](https://github.com/jamieowen/glsl-blend) | 1.1k | ⚪ Dormant | GLSL | GLSL implementations of the full set of Photoshop layer blend modes.<br><sub>Good for: Blend modes</sub><br><sub>⚠️ Not updated since 2022.</sub> |
| [twigl](https://github.com/doxas/twigl) | 1.1k | 🟡 Slowing | GLSL | Minimal online GLSL editor popular in Japan's tweet-sized GLSL scene. Exports GIFs and videos.<br><sub>Good for: Short films · GIF · Also in: Live Coding & VJ</sub> |
| [Shader Editor](https://github.com/markusfisch/ShaderEditor) | 1.1k | 🟢 Active | Java (Android) | Write GLSL shaders on an Android phone and set them directly as live wallpaper.<br><sub>Good for: Phone shader coding</sub> |
| [liquidGL](https://github.com/naughtyduk/liquidGL) | 1.1k | 🟢 Active | WebGL / WebGPU | Liquid glass effect for the web, implemented in WebGL and WebGPU.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub> |
| [Radiant](https://github.com/pbakaus/radiant) | 1.1k | 🟢 Active | GLSL / WebGL | Curated collection of generative shader art; every piece runs directly in the browser.<br><sub>Good for: Shader art · Also in: Generative Art</sub> |
| [Raymarching Workshop](https://github.com/electricsquare/raymarching-workshop) | 1k | ⚪ Dormant | GLSL | Beginner raymarching workshop: build up 3D shapes step by step with signed distance fields.<br><sub>Good for: Tutorials · Also in: 3D</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Godot Realistic Water](https://github.com/godot-extended-libraries/godot-realistic-water) | 985 | 🟡 Slowing | Godot Shader | Realistic water surface shader for Godot.<br><sub>Good for: Water surfaces · Also in: 3D</sub> |
| [Fragment](https://github.com/raphaelameaume/fragment) | 951 | 🟢 Active | JavaScript | Modern creative coding toolkit with hot reload, a parameter panel, and frame sequence export built in.<br><sub>Good for: Generative art · Also in: Generative Art</sub><br><sub>⚠️ Still in alpha.</sub> |
| [Liquid Glass Studio](https://github.com/iyinchao/liquid-glass-studio) | 850 | 🟢 Active | WebGL2 / WebGPU | By a Chinese developer: recreates Apple's liquid glass interface on the web, with real-time control of refraction, dispersion, and highlights.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub> |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 833 | 🟢 Active | JavaScript | Write SDF shaders in JS-like syntax to make sculptural 3D abstract forms.<br><sub>Good for: MV · Generative art · Also in: 3D</sub> |
| [GodotRetro](https://github.com/ahopness/GodotRetro) | 824 | 🟢 Active | Godot Shader | Retro post-processing effects pack for Godot: CRT, VHS, dithering, pixelation.<br><sub>Good for: Retro post-processing · Also in: Pixel & Retro, VHS & Analog</sub> |
| [orb](https://github.com/LerSent001/orb) | 760 | 🟢 Active | WebGPU | From a Chinese developer: real-time WebGPU liquid glass orb editor, exportable to the web or SwiftUI / Metal.<br><sub>Good for: Liquid glass orbs · Also in: Liquid Glass</sub> |
| [Shader Lab](https://github.com/basementstudio/shader-lab) | 728 | 🟢 Active | TypeScript | Toolkit for creating, stacking, and animating shaders. Combine multiple effects like layers.<br><sub>Good for: Shader motion · Also in: Motion Graphics</sub> |
| [shadplay](https://github.com/alphastrata/shadplay) | 727 | 🟢 Active | Rust / WGSL | Real-time WGSL shader visualization tool: write and see the result live, handy for learning shaders.<br><sub>Good for: Shader practice · Also in: Live Coding & VJ</sub> |
| [Shader Toy for VS Code](https://github.com/stevensona/shader-toy) | 723 | 🟢 Active | TypeScript | Live preview of Shadertoy-style GLSL shaders inside VS Code.<br><sub>Good for: Shader development</sub> |
| [LiquidGlass](https://github.com/ybouane/liquidglass) | 656 | 🟢 Active | TypeScript / WebGL | A liquid glass effect library for the web: WebGL shaders add refraction, blur, chromatic aberration and lighting to any HTML element.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub> |
| [Godot Ocean FFT](https://github.com/tessarakkt/godot4-oceanfft) | 614 | 🟡 Slowing | Godot | Ocean waves and buoyancy based on Tessendorf FFT, implemented with compute shaders in Godot 4.<br><sub>Good for: Ocean · Also in: 3D, Particles & Physics</sub> |
| [Fabric](https://github.com/Fabric-Project/Fabric) | 613 | 🟢 Active | Swift (Metal) | A node-based creative coding tool in the spirit of Quartz Composer, rendering 3D, image effects and audio-reactive scenes with Metal.<br><sub>Good for: Real-time visuals · Node-based creation · Also in: Live Coding & VJ, 3D</sub><br><sub>⚠️ macOS 15+ only.</sub> |
| [LiliumToonGraph](https://github.com/you-ri/LiliumToonGraph) | 609 | 🟢 Active | Unity Shader Graph | Unity URP toon shader built with Shader Graph.<br><sub>Good for: Anime rendering · Also in: Anime, MMD & VRM</sub> |
| [Bauble](https://github.com/ianthehenry/bauble) | 598 | 🟢 Active | Janet (Lisp) | Playground for making 3D art with Lisp and math, built on signed distance field ray marching.<br><sub>Good for: 3D math art · Also in: 3D, Generative Art</sub> |
| [shader-doodle](https://github.com/mmmerl/shader-doodle) | 590 | 🟢 Active | Web Component | Web component for writing and displaying shaders. One tag puts Shadertoy-style code on a page.<br><sub>Good for: Web shaders</sub> |
| [Shader Minifier](https://github.com/laurentlb/shader-minifier) | 587 | 🟢 Active | F# | Shrinks GLSL / HLSL code to the minimum. A must for 4KB and 64KB demos.<br><sub>Good for: Demoscene · Also in: Demoscene</sub> |
| [cables](https://github.com/cables-gl/cables) | 576 | 🟢 Active | Node graph / JS | Node-based visual programming platform. Wire up real-time WebGL visuals in the browser, often used for music videos and live show visuals.<br><sub>Good for: MV · Live performances · Also in: Live Coding & VJ, 3D</sub> |
| [Glass SDK Liquid Glass](https://github.com/Glass-HQ/liquid-glass) | 549 | 🟢 Active | TypeScript / WebGPU | Liquid glass materials and controls for React, the web and Electron that refract live content with WebGPU, in light and dark appearances.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub><br><sub>⚠️ Requires WebGPU; Safari has known rendering issues.</sub> |
| [Shader Skills](https://github.com/gokayfem/shader-skills) | 548 | 🟢 Active | GLSL | GLSL and Shadertoy skills for AI coding agents, with 186 shader functions.<br><sub>Good for: Shaders</sub> |
| [Universal Transition Shader](https://github.com/cashew-olddew/Universal-Transition-Shader) | 529 | 🟡 Slowing | Godot Shader | Packs the common transition effects into a single Godot shader.<br><sub>Good for: Transitions · Also in: Shorts, Captions & Editing</sub> |
| [Beam](https://github.com/doodlewind/beam) | 527 | 🟢 Active | JavaScript / WebGPU | Lightweight WebGPU library by a Chinese developer. Builds shader rendering pipelines with very little code.<br><sub>Good for: Shader rendering</sub> |
| [Learn wgpu (Chinese edition)](https://github.com/jinleili/learn-wgpu-zh) | 510 | 🟢 Active | Rust / WGSL | Chinese edition of the wgpu graphics programming tutorial, from the first triangle to shaders and compute pipelines.<br><sub>Good for: Chinese tutorials · Also in: 3D</sub> |
| [ShaderKit](https://github.com/jamesrochabrun/ShaderKit) | 491 | 🟢 Active | Swift / Metal (iOS) | Composable Metal shaders and holographic UI effects for SwiftUI.<br><sub>Good for: App motion · Also in: Liquid Glass</sub> |
| [Retro Crisis Shaders](https://github.com/RetroCrisis/Retro-Crisis-GDV-NTSC) | 482 | 🟢 Active | Slang Shader | Collection of CRT shader presets for RetroArch, based on Guest Advanced NTSC. Recreates the look of various old TVs.<br><sub>Good for: CRT post-processing · Also in: VHS & Analog, Pixel & Retro</sub> |
| [Svader](https://github.com/sockmaster27/svader) | 464 | 🟢 Active | Svelte | Svelte components rendered with GPU shaders.<br><sub>Good for: Web shaders</sub> |
| [liquid_glass_renderer](https://github.com/whynotmake-it/flutter_liquid_glass) | 462 | 🟢 Active | Dart (Flutter) | A Flutter package that renders liquid glass with fragment shaders (refraction, blending and lighting); several Flutter glass widget kits build on it.<br><sub>Good for: Liquid glass · Also in: Liquid Glass</sub> |
| [react-native-effects](https://github.com/blazejkustra/react-native-effects) | 394 | 🟢 Active | TypeScript / WGSL | WebGPU shader effect components for React Native: aurora, liquid chrome, lava lamp, CRT-off and more, or write your own in WGSL.<br><sub>Good for: App effect backgrounds</sub><br><sub>⚠️ Experimental; the API may change.</sub> |
| [AquaInkGL](https://github.com/WishMelz/AquaInkGL) | 387 | 🟡 Slowing | WebGL | WebGL ink-wash background effect, with ink bleeding and flowing across rice paper.<br><sub>Good for: Ink wash backgrounds · Also in: Ink & Watercolor</sub> |
| [LUMEN](https://github.com/Leonxlnx/lumenshaders) | 369 | 🟢 Active | WebGL2 | Generative shader studio with 9 WebGL2 art modes. Blend styles and export seamless loops.<br><sub>Good for: Shader art · Also in: Generative Art</sub> |
| [RayTK](https://github.com/t3kt/raytk) | 359 | 🟡 Slowing | TouchDesigner | Raymarching shader toolkit for TouchDesigner; build SDF scenes with nodes.<br><sub>Good for: Ray marching · Also in: Live Coding & VJ, 3D</sub><br><sub>⚠️ Requires TouchDesigner (commercial software, with a free version).</sub> |
| [Godot VFX Library](https://github.com/haowg/GODOT-VFX-LIBRARY) | 359 | 🟡 Slowing | Godot | Collection of particle effects and shaders for Godot 4.<br><sub>Good for: Effect assets · Also in: Particles & Physics</sub> |
| [SwiftUI Shaders](https://github.com/krispuckett/SwiftUIShaders) | 353 | 🟢 Active | Swift (iOS) | 41 Metal shaders ready to drop into SwiftUI: holographic foil, kaleidoscope, magnetic distortion, and more. Good for mobile app motion.<br><sub>Good for: App motion · Also in: Glitch & Post FX</sub> |
| [ShaderMania](https://github.com/markusmoenig/ShaderMania) | 349 | 🟡 Slowing | Swift (macOS / iPad) | Metal fragment shader editor for macOS and iPadOS.<br><sub>Good for: Shader editors</sub> |
| [Ultimate Retro Shaders](https://github.com/Zorochase/ultimate-retro-shader-collection) | 344 | 🟢 Active | Godot Shader | Retro shader collection for Godot 4, giving the dithering, low-poly, and texture-wobble look of the PS1 and N64 era.<br><sub>Good for: PS1 retro 3D · Also in: Pixel & Retro, 3D</sub> |
| [Plasma UI](https://github.com/CruxGarden/plasma-ui) | 339 | 🟢 Active | TypeScript (React / WebGL) | Liquid React panels rendered in WebGL: they fuse like droplets when they touch and refract whatever is behind them.<br><sub>Good for: Liquid glass · Interfaces · Also in: Liquid Glass</sub><br><sub>⚠️ Pre-1.0 and GPU-heavy; does not run well on mobile.</sub> |
| [Poseidon](https://github.com/owenyuwono/poseidon) | 325 | 🟢 Active | three.js / TSL | GPU-driven real-time FFT ocean, in three.js with WebGPU.<br><sub>Good for: Ocean · Also in: 3D</sub> |
| [Singularity](https://github.com/MisterPrada/singularity) | 319 | 🟡 Slowing | three.js / TSL | Black hole written in TSL, the three.js shading language. Runs on WebGPU and WebGL.<br><sub>Good for: Space effects · Also in: Space & Stars</sub> |
| [ShaderToy Browser Extension](https://github.com/patuwwy/ShaderToy-Chrome-Plugin) | 313 | 🟢 Active | JavaScript | Browser extension that adds features to shadertoy.com: resolution control, recording, slow motion, and more.<br><sub>Good for: Shadertoy tools</sub> |
| [AGSL Shader Playground](https://github.com/mejdi14/Android-AGSL-Shader-Playground) | 310 | 🟢 Active | Kotlin (Android) | Android AGSL shader effect library. Adds glow, ripple, gradient, and similar effects to apps.<br><sub>Good for: App motion</sub> |
| [Natural Disasters](https://github.com/Token-Gremlin/natural-disasters) | 307 | 🟢 Active | WebGPU | Fully procedural cinematic ocean and extreme weather simulation in the browser: storms, waves, tornadoes.<br><sub>Good for: Weather effects · Also in: Particles & Physics, 3D</sub> |
| [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | 298 | 🟢 Active | React / TS | Real-time Bayer dithering post-processing effect for React Three Fiber, turning 3D scenes into a retro dithered look.<br><sub>Good for: 3D post-processing · Also in: Dither & 1-bit, 3D</sub> |
| [TSL Textures](https://github.com/boytchev/tsl-textures) | 275 | 🟢 Active | three.js / TSL | Procedural textures for three.js's shading language TSL: marble, wood grain, clouds, starfields.<br><sub>Good for: Procedural textures · Also in: Procedural Generation</sub> |
| [Radiance](https://github.com/zbanks/radiance) | 250 | 🟡 Slowing | C++ | Video art software for VJs: beat detection, shader effect chains, and mixing of GIF and video clips.<br><sub>Good for: VJ · Also in: Live Coding & VJ, Music Visualization</sub> |
| [three-good-godrays](https://github.com/Ameobea/three-good-godrays) | 238 | 🟢 Active | TypeScript | Screen-space ray-marched volumetric light (god rays) for three.js.<br><sub>Good for: 3D post-processing · Also in: 3D</sub> |
| [retrace.gl](https://github.com/stasilo/retrace.gl) | 196 | 🟢 Active | JavaScript | Define signed distance field CSG shapes in code, ray trace them, and export the result.<br><sub>Good for: Ray-traced 3D · Also in: Path Tracing, 3D</sub> |
| [WebGL CRT Shader](https://github.com/gingerbeardman/webgl-crt-shader) | 188 | 🟡 Slowing | WebGL | Adjustable CRT shader for web canvas: scanlines, screen curvature, phosphor ghosting.<br><sub>Good for: CRT post-processing · Also in: VHS & Analog</sub> |
| [Black Hole](https://github.com/ibra-kdbra/black-hole) | 113 | 🟢 Active | three.js / GLSL | Black hole and accretion disk made with three.js and GLSL shaders.<br><sub>Good for: Space effects · Also in: Space & Stars</sub> |
| [ditherwave](https://github.com/sahilsaini5/ditherwave) | 90 | 🟡 Slowing | React / WebGL2 | WebGL2 dithering component under 8KB: Bayer, halftone, ASCII, and error diffusion.<br><sub>Good for: Web effects · Also in: Dither & 1-bit</sub> |
| [Galaxy Shader](https://github.com/AmitDigga/threejs-galaxy-shader) | 73 | 🟡 Slowing | three.js | High-performance three.js galaxy shader with adjustable colors, spiral arms, and black hole effects.<br><sub>Good for: Galaxy effects · Also in: Space & Stars, Particles & Physics</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="live"></a>

### Live Coding & VJ

<img src="assets/styles/live.png" alt="Live Coding & VJ sample" width="240" align="right">

> Writing code live to make the picture, with a video-synth feel

**Picks:** [Hydra](https://github.com/hydra-synth/hydra) · [TiXL](https://github.com/tixl3d/tixl) · [cables](https://github.com/cables-gl/cables) · [Bonzomatic](https://github.com/Gargaj/Bonzomatic) · [ossia score](https://github.com/ossia/score)

16 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | 🟢 Active | Lua / JS and more | Fantasy console (240x136 pixels, 16 colors), popular for tiny demoscene pieces and live Byte Jam streams.<br><sub>Good for: Pixel animation · Live · Also in: Pixel & Retro, Demoscene</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 Active | Node graph / C# | Formerly Tooll3. Open-source real-time motion graphics software with nodes and a timeline. Often used for music videos and live shows.<br><sub>Good for: MV · Live performances · Also in: Shaders & Psychedelic, 3D</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.8k | 🟡 Slowing | JavaScript | Real-time video synthesizer in the browser, modeled on analog signal synthesizers. A few lines of code give feedback, distortion, and psychedelic color visuals.<br><sub>Good for: Live VJ · MV · Also in: Glitch & Post FX, Shaders & Psychedelic</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [ossia score](https://github.com/ossia/score) | 2.1k | 🟢 Active | C++ (GUI) | Multimedia timeline sequencer that syncs audio, video, lighting, and shaders.<br><sub>Good for: Performances · Installations</sub> |
| [GLSL Sandbox](https://github.com/mrdoob/glsl-sandbox) | 1.7k | 🟢 Active | JavaScript | Shader editor and gallery from the author of three.js. Open a shader, edit the code and see the result right away.<br><sub>Good for: Shader gallery · Also in: Shaders & Psychedelic</sub> |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | 🟡 Slowing | GLSL | Live shader coding tool used in the demoscene Shader Showdown contest. Write code live and see the picture live.<br><sub>Good for: Live performances · Also in: Shaders & Psychedelic, Demoscene</sub> |
| [twigl](https://github.com/doxas/twigl) | 1.1k | 🟡 Slowing | GLSL | Minimal online GLSL editor popular in Japan's tweet-sized GLSL scene. Exports GIFs and videos.<br><sub>Good for: Short films · GIF · Also in: Shaders & Psychedelic</sub> |
| [shadplay](https://github.com/alphastrata/shadplay) | 727 | 🟢 Active | Rust / WGSL | Real-time WGSL shader visualization tool: write and see the result live, handy for learning shaders.<br><sub>Good for: Shader practice · Also in: Shaders & Psychedelic</sub> |
| [Fabric](https://github.com/Fabric-Project/Fabric) | 613 | 🟢 Active | Swift (Metal) | A node-based creative coding tool in the spirit of Quartz Composer, rendering 3D, image effects and audio-reactive scenes with Metal.<br><sub>Good for: Real-time visuals · Node-based creation · Also in: 3D, Shaders & Psychedelic</sub><br><sub>⚠️ macOS 15+ only.</sub> |
| [cables](https://github.com/cables-gl/cables) | 576 | 🟢 Active | Node graph / JS | Node-based visual programming platform. Wire up real-time WebGL visuals in the browser, often used for music videos and live show visuals.<br><sub>Good for: MV · Live performances · Also in: Shaders & Psychedelic, 3D</sub> |
| [Mosaic](https://github.com/d3cod3/Mosaic) | 519 | 🟢 Active | C++ | Visual patching creative coding platform built on openFrameworks, connecting nodes, code, and audio.<br><sub>Good for: Node-based creative coding · Also in: Generative Art</sub> |
| [modV](https://github.com/vcync/modV) | 498 | 🟡 Slowing | JavaScript | Modular music visualizer and VJ tool. Write modules in JavaScript and shaders.<br><sub>Good for: VJ · Music visualizer · Also in: Music Visualization</sub> |
| [RayTK](https://github.com/t3kt/raytk) | 359 | 🟡 Slowing | TouchDesigner | Raymarching shader toolkit for TouchDesigner; build SDF scenes with nodes.<br><sub>Good for: Ray marching · Also in: Shaders & Psychedelic, 3D</sub><br><sub>⚠️ Requires TouchDesigner (commercial software, with a free version).</sub> |
| [Infinite](https://github.com/n1m21n/Infinite) | 341 | 🟢 Active | C++ / Node graph | An open-source audiovisual workstation: visuals, music and code share one node canvas, with GPU compositing, procedural 3D and a synth rack that modulate each other.<br><sub>Good for: Audiovisual live · MV · Also in: Music Visualization, 3D</sub> |
| [Radiance](https://github.com/zbanks/radiance) | 250 | 🟡 Slowing | C++ | Video art software for VJs: beat detection, shader effect chains, and mixing of GIF and video clips.<br><sub>Good for: VJ · Also in: Shaders & Psychedelic, Music Visualization</sub> |
| [Patchies](https://github.com/heypoom/patchies) | 216 | 🟢 Active | TypeScript / Web | A creative coding patcher in the browser: wire small p5.js, Hydra, GLSL and three.js programs together like modules for audio-reactive visuals.<br><sub>Good for: Live coding · Creative coding · Also in: Generative Art</sub><br><sub>⚠️ AGPL-3.0 licensed.</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="audio"></a>

### Music Visualization

<img src="assets/styles/audio.png" alt="Music Visualization sample" width="240" align="right">

> Spectrums, waveforms and MilkDrop-style visuals that move with the music

**Picks:** [Butterchurn](https://github.com/jberg/butterchurn) · [projectM](https://github.com/projectM-visualizer/projectm) · [CAVA](https://github.com/karlstav/cava) · [Astrofox](https://github.com/astrofox-io/astrofox) · [audioMotion](https://github.com/hvianna/audioMotion-analyzer)

28 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [p5.js](https://github.com/processing/p5.js) | 24.4k | 🟢 Active | JavaScript | The most popular creative coding library: draw, build interactions, and animate on the web. Plenty of Chinese tutorials too.<br><sub>Good for: Generative art · MV · Also in: Generative Art, Particles & Physics</sub><br><sub>⚠️ Exporting video takes extra steps (save frames one by one, or screen-record).</sub> |
| [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js) | 10.5k | 🟢 Active | TypeScript | Draws and plays audio waveforms on the web. Can be used for waveform animation and audio editing interfaces.<br><sub>Good for: Audio waveforms</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 Active | C++ | C++ creative coding framework with strong performance. Often used for interactive installations, stage visuals, and music visualization.<br><sub>Good for: Performances · Installations · MV · Also in: Generative Art, 3D</sub> |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | 🟢 Active | Rust | Rust creative coding framework with audio and OSC modules, suited to real-time audiovisual work.<br><sub>Good for: Generative art · Performances · Also in: Generative Art</sub> |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | 🟢 Active | C (CLI) | Audio spectrum visualizer for the terminal.<br><sub>Good for: Music visualizer · Also in: ASCII & Terminal</sub> |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | 🟢 Active | C++ | Open-source, MilkDrop-compatible visualizer engine. Embed it in a player or use it for music video backgrounds.<br><sub>Good for: Music visualizer · MV · Also in: Shaders & Psychedelic</sub> |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | 🟢 Active | React / Vue | Apple Music-style lyrics component built by a Chinese developer: word-by-word highlighting, springy scrolling, fluid background.<br><sub>Good for: Lyric MV · Players · Also in: Kinetic Type & Lyrics</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | 🟢 Active | TypeScript (GUI) | Motion graphics software that turns audio into visualizer videos: spectrum, waveform, text, and 3D layers can be combined and exported.<br><sub>Good for: Music visualizer · MV · Also in: Motion Graphics</sub><br><sub>⚠️ Mainly a graphical interface.</sub> |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | 🟡 Slowing | JavaScript | MilkDrop music visualizer for WebGL, with many classic psychedelic presets built in.<br><sub>Good for: Music visualizer · MV · Also in: Shaders & Psychedelic</sub> |
| [Meyda](https://github.com/meyda/meyda) | 1.7k | ⚪ Dormant | TypeScript | JavaScript audio feature extraction (loudness, spectral centroid, and more), used to drive visuals that react to music.<br><sub>Good for: Audio analysis</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.6k | 🟢 Active | C++ (Windows) | A continuation of MilkDrop, with new features such as any audio source and double-preset blending.<br><sub>Good for: Music visualizer · Also in: Shaders & Psychedelic</sub> |
| [Musializer](https://github.com/tsoding/musializer) | 1.5k | 🟢 Active | C | Music visualizer written in C that can render straight to video.<br><sub>Good for: Music visualizer · MV</sub> |
| [Fractal Sound Explorer](https://github.com/HackerPoet/FractalSoundExplorer) | 1.3k | ⚪ Dormant | C++ | Click in a fractal and the path turns into sound; visuals and audio evolve together.<br><sub>Good for: Fractals · Audio-visual · Also in: Fractals & Chaos</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Realtime PyAudio FFT](https://github.com/aiXander/Realtime_PyAudio_FFT) | 1.1k | 🟢 Active | Python | Analyzes audio in real time and sends the results to other programs over OSC, to drive visuals that react to music.<br><sub>Good for: Audio analysis</sub> |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 983 | 🟢 Active | JavaScript | High-resolution real-time spectrum analyzer with adjustable bar, radial, and other styles.<br><sub>Good for: Music visualizer · Also in: Data Animation</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [HaloFlux](https://github.com/Ryder191/haloflux) | 830 | 🟢 Active | Canvas | Sci-fi light-ring visualization that pulses to the beat. Pure Canvas in a single HTML file, no dependencies.<br><sub>Good for: Music visualizer · Also in: Sci-fi HUD</sub><br><sub>⚠️ Noncommercial use only.</sub> |
| [party-mode](https://github.com/preziotte/party-mode) | 807 | 🟢 Active | JavaScript | Experimental D3-based music visualizer with several rhythmic geometric patterns.<br><sub>Good for: Music visualizer · Also in: Data Animation</sub> |
| [scope-tui](https://github.com/alemidev/scope-tui) | 763 | 🟢 Active | Rust (CLI) | Oscilloscope, vectorscope, and spectroscope in your terminal, drawing waveforms with characters.<br><sub>Good for: Terminal oscilloscope · Also in: Oscilloscope & Vector, ASCII & Terminal</sub> |
| [osci-render](https://github.com/jameshball/osci-render) | 744 | 🟢 Active | C++ / Lua | Synthesizer plugin that draws shapes on an oscilloscope: shapes become sound, and the sound turns back into glowing vector lines on the scope.<br><sub>Good for: Oscilloscope music · MV · Also in: Oscilloscope & Vector</sub> |
| [Waveform for OBS](https://github.com/phandasm/waveform) | 722 | 🟢 Active | C++ | Audio spectrum plugin for OBS that shows a live spectrum while streaming or recording.<br><sub>Good for: Live audio visualizer</sub> |
| [audioMotion Player](https://github.com/hvianna/audioMotion.js) | 646 | 🟢 Active | JavaScript | Web music player with real-time spectrum analysis, from the author of audioMotion-analyzer.<br><sub>Good for: Music visualizer</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [Opus Video Skills](https://github.com/tuzhechen2005/opus-video-skills) | 559 | 🟢 Active | JavaScript | Video-making skills for Claude Opus, where every frame and every note is generated in code.<br><sub>Good for: Short films · MV · Also in: Motion Graphics</sub> |
| [modV](https://github.com/vcync/modV) | 498 | 🟡 Slowing | JavaScript | Modular music visualizer and VJ tool. Write modules in JavaScript and shaders.<br><sub>Good for: VJ · Music visualizer · Also in: Live Coding & VJ</sub> |
| [Open Cubic Player](https://github.com/mywave82/opencubicplayer) | 453 | 🟢 Active | C | Unix version of the classic DOS player. Plays tracker music such as MOD and S3M, with retro visualizations.<br><sub>Good for: Retro music visualizer · Also in: Demoscene, ASCII & Terminal</sub> |
| [Infinite](https://github.com/n1m21n/Infinite) | 341 | 🟢 Active | C++ / Node graph | An open-source audiovisual workstation: visuals, music and code share one node canvas, with GPU compositing, procedural 3D and a synth rack that modulate each other.<br><sub>Good for: Audiovisual live · MV · Also in: Live Coding & VJ, 3D</sub> |
| [Remotion Audiogram Template](https://github.com/remotion-dev/template-audiogram) | 279 | 🟢 Active | React / TS | Official Remotion template: turns podcast audio into short videos with a waveform and captions.<br><sub>Good for: Short videos · Podcasts · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ Same license terms as Remotion.</sub> |
| [Radiance](https://github.com/zbanks/radiance) | 250 | 🟡 Slowing | C++ | Video art software for VJs: beat detection, shader effect chains, and mixing of GIF and video clips.<br><sub>Good for: VJ · Also in: Live Coding & VJ, Shaders & Psychedelic</sub> |
| [Oscillody](https://github.com/Akosmo/Oscillody) | 56 | 🟢 Active | GDScript (Godot) | An oscilloscope-style audio visualizer: import up to four stems, draw their waveforms in real time, style them and export a video.<br><sub>Good for: Oscilloscope waveforms · Music visualization · Also in: Oscilloscope & Vector</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="3d"></a>

### 3D

<img src="assets/styles/3d.png" alt="3D sample" width="240" align="right">

> 3D scenes, camera moves, materials and lighting

**Picks:** [three.js](https://github.com/mrdoob/three.js) · [React Three Fiber](https://github.com/pmndrs/react-three-fiber) · [Babylon.js](https://github.com/BabylonJS/Babylon.js) · [PlayCanvas](https://github.com/playcanvas/engine)

83 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 119k | 🟢 Active | JavaScript | The de facto standard for 3D on the web: scenes, materials, particles, and post-processing, with lots of examples.<br><sub>Good for: MV · Web 3D · Also in: Particles & Physics, Shaders & Psychedelic</sub> |
| [Remotion](https://github.com/remotion-dev/remotion) | 75.1k | 🟢 Active | React / TS | Write videos as React components and render them to MP4, with batch generation. Official add-on packages cover captions, audio visualization, three.js, and more.<br><sub>Good for: MV · Short videos · Batch video rendering · Also in: Motion Graphics, Shorts, Captions & Editing, Kinetic Type & Lyrics</sub><br><sub>⚠️ Free for individuals and small companies (commercial use included); larger companies need to buy a company license.</sub> |
| [raylib](https://github.com/raysan5/raylib) | 35.8k | 🟢 Active | C (many bindings) | Simple, beginner-friendly C graphics library with bindings for dozens of languages. Quick for 2D/3D animations and small demos.<br><sub>Good for: 2D/3D animation · Mini games · Also in: Pixel & Retro, Generative Art</sub> |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | 33.9k | 🟢 Active | React / TS | Write three.js scenes in React; pairs with Remotion to render 3D videos.<br><sub>Good for: MV · Web 3D</sub> |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | 🟢 Active | Python | High-performance parallel computing in Python, often used for physics simulations such as fluids, elastic bodies, and particles.<br><sub>Good for: Physics simulation · Also in: Particles & Physics</sub> |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | 26.4k | 🟢 Active | TypeScript | Web 3D engine maintained by a Microsoft team, with a wide feature set and built-in online editing tools.<br><sub>Good for: Web 3D · MV</sub> |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 21.8k | 🟢 Active | Python / three.js | AI coding agent skill: rebuilds a reference image as a procedural three.js 3D model in pure code, ready to animate.<br><sub>Good for: 3D assets</sub><br><sub>⚠️ Includes an optional Blender export bridge; the core is a pure-code three.js model.</sub> |
| [3D Game Shaders for Beginners](https://github.com/lettier/3d-game-shaders-for-beginners) | 20.1k | ⚪ Dormant | GLSL / C++ | Illustrated step-by-step tutorial for dozens of 3D shader effects: SSAO, depth of field, bloom, cartoon outlines, pixelation, and more.<br><sub>Good for: Tutorials · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2023; the tutorial content is complete.</sub> |
| [PlayCanvas](https://github.com/playcanvas/engine) | 17.4k | 🟢 Active | JavaScript | Web 3D engine supporting WebGL, WebGPU, and Gaussian splatting.<br><sub>Good for: Web 3D</sub> |
| [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 16.3k | 🟢 Active | HTML / Canvas / three.js | 703 prompts people used to make videos with Claude Opus 5.5, each linked to the original post and a live remake. The picture is drawn in code (Canvas, SVG, three.js): mostly motion graphics, explainers and 3D scenes.<br><sub>Good for: Prompt collection · MV · Also in: Motion Graphics, Generative Art</sub><br><sub>⚠️ A few entries overlay AI-generated images or use Blender; those are labeled.</sub> |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.8k | 🟢 Active | TypeScript | Large-scale geospatial data visualization: animated trajectories, 3D column maps, and more.<br><sub>Good for: Map animation · Also in: Data Animation, Map & Route</sub> |
| [Theatre.js](https://github.com/theatre-js/theatre) | 13.1k | ⚪ Dormant | TypeScript | Visual timeline for web animation: define properties in code, drag keyframes in the UI. Often paired with three.js for 3D camera animation.<br><sub>Good for: MV · Web animation · Also in: Motion Graphics</sub> |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | ⚪ Dormant | JavaScript | Pseudo-3D flat engine that draws rounded, cute flat-shaded 3D shapes.<br><sub>Good for: Web animation · Also in: Motion Graphics, Isometric & Voxel</sub><br><sub>⚠️ Not updated in years; simple and stable.</sub> |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | 🟢 Active | C++ | C++ creative coding framework with strong performance. Often used for interactive installations, stage visuals, and music visualization.<br><sub>Good for: Performances · Installations · MV · Also in: Generative Art, Music Visualization</sub> |
| [ThreeUI](https://github.com/MengTo/threeui) | 7.4k | 🟢 Active | three.js | Directory of interactive three.js components, each with adjustable parameters and source code.<br><sub>Good for: Web 3D · Assets</sub> |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.4k | ⚪ Dormant | JavaScript | A few lines of code give you animated 3D backgrounds: waves, birds, fog, grids, and more.<br><sub>Good for: Background assets · Also in: Generative Art</sub> |
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | 6.8k | ⚪ Dormant | C / JS | Recreates the 90s game Comanche's voxel terrain flight view in under 20 lines of code, with an explanation of how it works.<br><sub>Good for: Retro voxel terrain · Also in: Isometric & Voxel, Pixel & Retro</sub> |
| [Unity Shader Essentials (book source)](https://github.com/candycat1992/Unity_Shaders_Book) | 6.1k | ⚪ Dormant | Unity ShaderLab | Full source code for a classic Chinese textbook on Unity shaders, Unity Shader Essentials.<br><sub>Good for: Chinese tutorials · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2023; the book's content is complete.</sub> |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | 🟢 Active | TypeScript | Web graphics engine open-sourced by Ant Group, covering 2D, 3D, particles, and Lottie.<br><sub>Good for: Web 3D · Interactive · Also in: Particles & Physics</sub> |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | 🟡 Slowing | C++ | C++ creative coding framework geared toward professional real-time graphics and installation work.<br><sub>Good for: Performances · Installations · Also in: Generative Art</sub> |
| [Orillusion](https://github.com/Orillusion/orillusion) | 5.2k | 🟢 Active | TypeScript / WebGPU | Pure WebGPU web 3D engine built by a Chinese team.<br><sub>Good for: Web 3D · Also in: Shaders & Psychedelic</sub> |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | 🟢 Active | Node graph / C# | Formerly Tooll3. Open-source real-time motion graphics software with nodes and a timeline. Often used for music videos and live shows.<br><sub>Good for: MV · Live performances · Also in: Live Coding & VJ, Shaders & Psychedelic</sub> |
| [WFC Infinite City](https://github.com/marian42/wavefunctioncollapse) | 4.9k | ⚪ Dormant | C# (Unity) | Uses wave function collapse to generate an endless 3D city in real time that you can keep walking through.<br><sub>Good for: Procedural generation · Also in: Procedural Generation</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) | 4.6k | 🟢 Active | TypeScript (Remotion + three.js) | A Claude skill for ~1-minute vertical animated story shorts: 2D characters in a colourful 3D town with ink outlines, lens blur and gliding cameras, rendered with three.js inside Remotion.<br><sub>Good for: Vertical story shorts · Also in: Shorts, Captions & Editing</sub> |
| [Godot Shaders](https://github.com/gdquest-demos/godot-shaders) | 4.2k | 🟢 Active | Godot Shader | GDQuest's large collection of Godot 2D and 3D shaders: dissolve, outline, water, pixelation, and more.<br><sub>Good for: Shader collections · Also in: Shaders & Psychedelic, Pixel & Retro</sub> |
| [MG Styles 15](https://github.com/Vincentwei1021/mg-styles-15) | 3.9k | 🟢 Active | Python / Web | 15 motion design style demo films, each written as code by Claude Opus 5.5 from a single prompt. Prompts and source included.<br><sub>Good for: Style sample clips · Also in: Motion Graphics, Hand-drawn & Whiteboard</sub><br><sub>⚠️ Of the 15, only the 3D one uses Blender; the rest are pure code.</sub> |
| [farbrausch Tools](https://github.com/farbrausch/fr_public) | 3.8k | ⚪ Dormant | C++ | Tool source code from the legendary demo group farbrausch, 2001-2011, including .werkkzeug, which made their 64KB 3D shorts.<br><sub>Good for: Demoscene · Also in: Demoscene</sub><br><sub>⚠️ Historical source archive; hard to compile and use.</sub> |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 3.1k | 🟢 Active | JavaScript | Has an AI coding agent make product launch films, compose its own soundtrack, and take edits by pointing at the frame.<br><sub>Good for: Product promo videos · Also in: Motion Graphics</sub> |
| [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) | 3k | 🟢 Active | C++ / Python | Research-grade physically based renderer. Build scenes and render frame-by-frame animation with Python scripts.<br><sub>Good for: Realistic rendering · Also in: Path Tracing</sub> |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 3k | 🟢 Active | JavaScript | Post-processing library for three.js: bloom, chromatic aberration, glitch, depth of field, and more.<br><sub>Good for: 3D post-processing · Also in: Glitch & Post FX</sub> |
| [Yocto/GL](https://github.com/xelatihy/yocto-gl) | 2.9k | ⚪ Dormant | C++ | Small C++ libraries for data-driven physically based rendering, common in academia.<br><sub>Good for: Realistic rendering · Also in: Path Tracing</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) | 2.9k | 🟢 Active | Python (Manim) | A chain of AI agents turns a math or physics concept into a storyboard, writes the Manim code and revises it after looking at the renders; it can make films up to ten minutes long.<br><sub>Good for: Math explainers · Science films · Also in: Math Explainer</sub><br><sub>⚠️ The newer Studio pipeline renders 3D shots with Blender EEVEE; the original main pipeline uses Manim only.</sub> |
| [ManimGX](https://github.com/academa-labs/manimgx) | 2.9k | 🟢 Active | Python / Rust (wgpu) | An animation engine compatible with the Manim CE API, rebuilt on Rust and wgpu so math and 3D scenes render faster; it also runs in the browser.<br><sub>Good for: Math animation · 3D explainers · Also in: Math Explainer</sub> |
| [vgpu](https://github.com/vercel-labs/vgpu) | 2.7k | 🟢 Active | TypeScript / WGSL | A small WebGPU library from Vercel: import WGSL shaders like TypeScript modules and render the same code in the browser or headless Node.<br><sub>Good for: WebGPU effects · Web 3D · Also in: Shaders & Psychedelic</sub> |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | 🟢 Active | TypeScript | 3D renderer written in JavaScript that draws 3D scenes directly in the terminal.<br><sub>Good for: Terminal animation · Also in: ASCII & Terminal</sub> |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | 🟢 Active | TypeScript | From pixiv: use VRM anime avatars in three.js.<br><sub>Good for: Anime MV · Avatars · Also in: Anime, MMD & VRM</sub> |
| [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) | 2.1k | 🟢 Active | JavaScript | GPU path tracing renderer for three.js, giving web 3D scenes realistic lighting, reflections, and depth of field.<br><sub>Good for: Realistic rendering · Also in: Path Tracing</sub> |
| [Dither3D](https://github.com/runevision/Dither3D) | 1.6k | 🟡 Slowing | Unity Shader | Fractal dithering shader that sticks to object surfaces and doesn't flicker when the camera moves. For 1-bit style 3D visuals.<br><sub>Good for: 1-bit 3D · Also in: Dither & 1-bit, Shaders & Psychedelic</sub><br><sub>⚠️ Unity shader; not updated since early 2025.</sub> |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | ⚪ Dormant | JavaScript | 3D math visualization in the browser: surfaces, vector fields and coordinate grids, with clean, polished visuals.<br><sub>Good for: Explainer videos · Also in: Math Explainer</sub> |
| [Bonsai](https://github.com/scallyw4g/bonsai) | 1.5k | 🟢 Active | C | Procedurally generated voxel engine. Terrain and buildings are grown from code.<br><sub>Good for: Procedural voxels · Also in: Procedural Generation, Isometric & Voxel</sub> |
| [Origami Simulator](https://github.com/amandaghassaei/OrigamiSimulator) | 1.4k | 🟢 Active | JavaScript / WebGL | Real-time WebGL origami simulator. Import a crease pattern and watch a sheet of paper fold itself into a crane.<br><sub>Good for: Origami animation · Also in: Origami & Papercraft</sub> |
| [CustomShaderMaterial](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial) | 1.4k | 🟡 Slowing | TypeScript | Layer your own shaders on top of three.js standard materials while keeping lighting and shadows.<br><sub>Good for: three.js shaders · Also in: Shaders & Psychedelic</sub> |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.3k | 🟢 Active | TypeScript | Particle effects system for three.js: fire, explosions, magic, and other VFX.<br><sub>Good for: 3D effects · Also in: Particles & Physics</sub> |
| [TerraForge3D](https://github.com/Jaysmito101/TerraForge3D) | 1.3k | 🟢 Active | C++ | Procedural terrain generation and texturing tool with node-based editing.<br><sub>Good for: Procedural terrain · Also in: Procedural Generation</sub><br><sub>⚠️ Mostly a graphical interface.</sub> |
| [three-nebula](https://github.com/creativelifeform/three-nebula) | 1.3k | 🟢 Active | JavaScript | WebGL particle system engine for three.js, with a visual editor.<br><sub>Good for: 3D particles · Also in: Particles & Physics</sub> |
| [Claude Animation Skills](https://github.com/artemnovitckii/claude-animation-skills) | 1.1k | 🟢 Active | JavaScript | Six Claude skills for short-video animation: 3D cartoon explainers in three.js, stick figures, map routes, exploded-view diagrams and more.<br><sub>Good for: Vertical shorts · Also in: Map & Route</sub> |
| [Mandelbulber](https://github.com/buddhi1980/mandelbulber2) | 1.1k | 🟢 Active | C++ | 3D fractal renderer. Fractals like the Mandelbulb can be keyframed for fly-through animations.<br><sub>Good for: 3D fractal animation · Also in: Fractals & Chaos</sub><br><sub>⚠️ Mainly a graphical app; also supports batch rendering from the command line.</sub> |
| [Raymarching Workshop](https://github.com/electricsquare/raymarching-workshop) | 1k | ⚪ Dormant | GLSL | Beginner raymarching workshop: build up 3D shapes step by step with signed distance fields.<br><sub>Good for: Tutorials · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Godot Realistic Water](https://github.com/godot-extended-libraries/godot-realistic-water) | 985 | 🟡 Slowing | Godot Shader | Realistic water surface shader for Godot.<br><sub>Good for: Water surfaces · Also in: Shaders & Psychedelic</sub> |
| [THREE.Terrain](https://github.com/IceCreamYou/THREE.Terrain) | 926 | 🟢 Active | JavaScript | Procedural terrain generation engine for three.js.<br><sub>Good for: Procedural terrain · Also in: Procedural Generation</sub> |
| [motion-web](https://github.com/feitangyuan/motion-web) | 875 | 🟢 Active | HTML / JS | Another skill set from the onetake author: motion-first creative websites built on vanilla three.js, Canvas, and WebGL.<br><sub>Good for: Motion websites · Also in: Motion Graphics</sub> |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 833 | 🟢 Active | JavaScript | Write SDF shaders in JS-like syntax to make sculptural 3D abstract forms.<br><sub>Good for: MV · Generative art · Also in: Shaders & Psychedelic</sub> |
| [Solar Wanderer](https://github.com/hyqzz/Solar-Wanderer) | 777 | 🟢 Active | three.js | A 1:1 real-time solar system in the browser using NASA JPL ephemeris data. Fly to any planet.<br><sub>Good for: Solar system animation · Also in: Space & Stars</sub> |
| [Machine Skill](https://github.com/AirsupHQ/machine-skill) | 738 | 🟢 Active | JavaScript | Describe a machine in one line and Claude builds a realistic, physics-based interactive 3D simulation and teardown animation in code.<br><sub>Good for: 3D mechanical animation</sub> |
| [Athenaion](https://github.com/Leonxlnx/athenaion) | 733 | 🟢 Active | three.js | Ancient Greek city-state world built purely in code with three.js. Zero assets, made by Claude.<br><sub>Good for: 3D worlds</sub> |
| [Diorama](https://github.com/sloemo01/diorama) | 715 | 🟢 Active | JavaScript (three.js) | A playbook for AI coding agents to build three.js dioramas: tiny people with joint animation, a 64-colour ordered-dither pixel look by default, or stroked toon.<br><sub>Good for: Miniature scene clips · Also in: Pixel & Retro, Dither & 1-bit</sub><br><sub>⚠️ By default mixes commercially licensed 3D assets with hand-built geometry; sources are recorded in the repo.</sub> |
| [Procedural Terrains](https://github.com/ZyFou/ProceduralTerrains) | 701 | 🟢 Active | JavaScript (three.js) | A three.js procedural terrain studio: height and biomes are computed on the GPU for tiles, infinite worlds, planets and dioramas, with water and volumetric clouds.<br><sub>Good for: Terrain · Dioramas · Also in: Procedural Generation</sub><br><sub>⚠️ Ships optional Unity and Blender export plugins; the rendering itself is three.js.</sub> |
| [heerich](https://github.com/meodai/heerich) | 637 | 🟢 Active | JavaScript | Small engine that renders 3D voxel scenes to SVG. Supports boolean operations and oblique and perspective cameras. No WebGL.<br><sub>Good for: Voxel illustration · Also in: Isometric & Voxel</sub> |
| [Godot Ocean FFT](https://github.com/tessarakkt/godot4-oceanfft) | 614 | 🟡 Slowing | Godot | Ocean waves and buoyancy based on Tessendorf FFT, implemented with compute shaders in Godot 4.<br><sub>Good for: Ocean · Also in: Shaders & Psychedelic, Particles & Physics</sub> |
| [Fabric](https://github.com/Fabric-Project/Fabric) | 613 | 🟢 Active | Swift (Metal) | A node-based creative coding tool in the spirit of Quartz Composer, rendering 3D, image effects and audio-reactive scenes with Metal.<br><sub>Good for: Real-time visuals · Node-based creation · Also in: Live Coding & VJ, Shaders & Psychedelic</sub><br><sub>⚠️ macOS 15+ only.</sub> |
| [Bauble](https://github.com/ianthehenry/bauble) | 598 | 🟢 Active | Janet (Lisp) | Playground for making 3D art with Lisp and math, built on signed distance field ray marching.<br><sub>Good for: 3D math art · Also in: Shaders & Psychedelic, Generative Art</sub> |
| [cables](https://github.com/cables-gl/cables) | 576 | 🟢 Active | Node graph / JS | Node-based visual programming platform. Wire up real-time WebGL visuals in the browser, often used for music videos and live show visuals.<br><sub>Good for: MV · Live performances · Also in: Live Coding & VJ, Shaders & Psychedelic</sub> |
| [Code Video Showcase](https://github.com/Moessif/code-video-showcase) | 546 | 🟢 Active | HTML / Canvas / three.js | Pure-code beat-synced showcase video skill, rendered frame by frame with HTML, Canvas, SVG, and three.js.<br><sub>Good for: Beat-synced showreels · Also in: Motion Graphics</sub> |
| [Learn wgpu (Chinese edition)](https://github.com/jinleili/learn-wgpu-zh) | 510 | 🟢 Active | Rust / WGSL | Chinese edition of the wgpu graphics programming tutorial, from the first triangle to shaders and compute pipelines.<br><sub>Good for: Chinese tutorials · Also in: Shaders & Psychedelic</sub> |
| [godot-vrm](https://github.com/V-Sekai/godot-vrm) | 486 | 🟢 Active | Godot | VRM avatar import and export for Godot, with a built-in MToon toon shader.<br><sub>Good for: Anime 3D · Also in: Anime, MMD & VRM</sub> |
| [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | 430 | 🟢 Active | Python | Made by a Chinese developer: Claude Opus writes code to make videos. It proposes three options with previews first, then renders the chosen one frame by frame.<br><sub>Good for: Short films · Also in: Motion Graphics</sub> |
| [RayTK](https://github.com/t3kt/raytk) | 359 | 🟡 Slowing | TouchDesigner | Raymarching shader toolkit for TouchDesigner; build SDF scenes with nodes.<br><sub>Good for: Ray marching · Also in: Shaders & Psychedelic, Live Coding & VJ</sub><br><sub>⚠️ Requires TouchDesigner (commercial software, with a free version).</sub> |
| [Ultimate Retro Shaders](https://github.com/Zorochase/ultimate-retro-shader-collection) | 344 | 🟢 Active | Godot Shader | Retro shader collection for Godot 4, giving the dithering, low-poly, and texture-wobble look of the PS1 and N64 era.<br><sub>Good for: PS1 retro 3D · Also in: Pixel & Retro, Shaders & Psychedelic</sub> |
| [Infinite](https://github.com/n1m21n/Infinite) | 341 | 🟢 Active | C++ / Node graph | An open-source audiovisual workstation: visuals, music and code share one node canvas, with GPU compositing, procedural 3D and a synth rack that modulate each other.<br><sub>Good for: Audiovisual live · MV · Also in: Live Coding & VJ, Music Visualization</sub> |
| [Poseidon](https://github.com/owenyuwono/poseidon) | 325 | 🟢 Active | three.js / TSL | GPU-driven real-time FFT ocean, in three.js with WebGPU.<br><sub>Good for: Ocean · Also in: Shaders & Psychedelic</sub> |
| [Natural Disasters](https://github.com/Token-Gremlin/natural-disasters) | 307 | 🟢 Active | WebGPU | Fully procedural cinematic ocean and extreme weather simulation in the browser: storms, waves, tornadoes.<br><sub>Good for: Weather effects · Also in: Shaders & Psychedelic, Particles & Physics</sub> |
| [OriSim3D](https://github.com/RemiKoutcherawy/OriSim3D-Android) | 304 | 🟢 Active | Kotlin (Android) | OpenGL origami folding simulation on Android that can demonstrate folds step by step.<br><sub>Good for: Mobile origami animation · Also in: Origami & Papercraft</sub> |
| [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | 298 | 🟢 Active | React / TS | Real-time Bayer dithering post-processing effect for React Three Fiber, turning 3D scenes into a retro dithered look.<br><sub>Good for: 3D post-processing · Also in: Dither & 1-bit, Shaders & Psychedelic</sub> |
| [Papercraft](https://github.com/rodrigorc/papercraft) | 291 | 🟢 Active | Rust | Unfolds 3D models into paper models you can print, cut out, and glue together.<br><sub>Good for: Paper model unfolding · Also in: Origami & Papercraft</sub> |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 267 | 🟢 Active | TypeScript | Loads and plays MMD models and motions in Babylon.js, for anime character dance MVs.<br><sub>Good for: Anime MV · Also in: Anime, MMD & VRM</sub> |
| [Krbn](https://github.com/vpalos/Krbn) | 253 | 🟢 Active | TypeScript | Renders 3D scenes as pencil-sketch SVG: exact outlines, hidden lines, hatched shading.<br><sub>Good for: 3D line art · Also in: Plotter & Line Art</sub> |
| [three-good-godrays](https://github.com/Ameobea/three-good-godrays) | 238 | 🟢 Active | TypeScript | Screen-space ray-marched volumetric light (god rays) for three.js.<br><sub>Good for: 3D post-processing · Also in: Shaders & Psychedelic</sub> |
| [BB-Video](https://github.com/BubbleBrainBB/BB-Video) | 211 | 🟢 Active | JavaScript | Skill for making videos in pure code: narrated explainers and product promos in 32 visual styles.<br><sub>Good for: Explainers · Promo videos · Also in: Motion Graphics</sub><br><sub>⚠️ 3D mascots can optionally be made in Blender; without Blender it falls back to three.js.</sub> |
| [Papercraft World](https://github.com/andrewwoan/aimee-xus-papercraft-world) | 201 | 🟢 Active | three.js | Papercraft-style seasonal 3D portfolio site. Useful as a three.js reference for the papercraft style.<br><sub>Good for: Papercraft 3D web · Also in: Origami & Papercraft</sub> |
| [mutracer](https://github.com/pissang/mutracer) | 198 | 🟢 Active | TypeScript / WebGPU | WebGPU physically based path tracer, written by one of the ECharts authors.<br><sub>Good for: Realistic rendering · Also in: Path Tracing</sub> |
| [retrace.gl](https://github.com/stasilo/retrace.gl) | 196 | 🟢 Active | JavaScript | Define signed distance field CSG shapes in code, ray trace them, and export the result.<br><sub>Good for: Ray-traced 3D · Also in: Path Tracing, Shaders & Psychedelic</sub> |
| [I, Voyager Planetarium](https://github.com/ivoyager/planetarium) | 162 | 🟢 Active | Godot | Open-source solar system simulation built on Godot.<br><sub>Good for: Solar system · Also in: Space & Stars</sub> |
| [Cyber Ocean](https://github.com/SahilK-027/Cyber-Ocean) | 82 | 🟢 Active | three.js | 3D flow-field particle ocean built with three.js, with custom post-processing.<br><sub>Good for: 3D particles · Also in: Flow & Wind Fields, Particles & Physics</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="anime"></a>

### Anime, MMD & VRM

<img src="assets/styles/anime.png" alt="Anime, MMD & VRM sample" width="240" align="right">

> Anime characters, avatars and dance music videos

**Picks:** [three-vrm](https://github.com/pixiv/three-vrm) · [Kalidokit](https://github.com/yeemachine/kalidokit) · [babylon-mmd](https://github.com/noname0310/babylon-mmd) · [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) · [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample)

15 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample) | 7.9k | 🟢 Active | Unity HLSL | Toon lighting shader example for Unity URP. A beginner reference for anime character outlines and stepped-shade shadows.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub> |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | 5.7k | 🟡 Slowing | TypeScript | Captures face and body motion from a webcam to drive VRM / Live2D characters.<br><sub>Good for: Avatars</sub> |
| [UnityChan Toon Shader](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) | 4.1k | ⚪ Dormant | Unity | Toon shader from Unity's official Japan team, for cel-shaded anime-look characters and scenes.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2024. New projects can use Unity Toon Shader.</sub> |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | 3.2k | 🟢 Active | p5.js | Starter template for having Claude make hand-painted cartoon animation: p5.js + p5.brush, with character and camera tools.<br><sub>Good for: Hand-drawn cartoons · Also in: Hand-drawn & Whiteboard</sub> |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | 🟢 Active | TypeScript | From pixiv: use VRM anime avatars in three.js.<br><sub>Good for: Anime MV · Avatars · Also in: 3D</sub> |
| [Poiyomi Toon Shader](https://github.com/poiyomi/PoiyomiToonShader) | 1.7k | 🟢 Active | Unity | Full-featured Unity toon shader, commonly used for VRChat avatars.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub> |
| [Unity Toon Shader](https://github.com/Unity-Technologies/com.unity.toonshader) | 1.6k | 🟢 Active | Unity | Unity's official toon shader for Japanese anime-style characters and scenes.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub> |
| [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | 1.5k | ⚪ Dormant | TypeScript | Displays and drives Live2D models in PixiJS, for 2D anime character animation.<br><sub>Good for: Anime animation</sub> |
| [URP_Toon](https://github.com/ChiliMilk/URP_Toon) | 1.4k | ⚪ Dormant | Unity | Toon shader for Unity URP with outlines, stepped shading, and rim light.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Aora Bot](https://github.com/sam70361/aora-bot) | 681 | 🟢 Active | TypeScript | A web character engine drawn in code, with 46 original characters and 44 animation states.<br><sub>Good for: Character animation · Also in: Motion Graphics</sub> |
| [LiliumToonGraph](https://github.com/you-ri/LiliumToonGraph) | 609 | 🟢 Active | Unity Shader Graph | Unity URP toon shader built with Shader Graph.<br><sub>Good for: Anime rendering · Also in: Shaders & Psychedelic</sub> |
| [world.execute(me) Lyric MV](https://github.com/Nyankomintsu/world-execute-me-lyric-mv) | 586 | 🟢 Active | JavaScript | Fan-made lyric MV that plays the lyrics as a chat with Claude, rendered frame by frame from code at 4K60.<br><sub>Good for: Lyric MV · Also in: Kinetic Type & Lyrics</sub> |
| [godot-vrm](https://github.com/V-Sekai/godot-vrm) | 486 | 🟢 Active | Godot | VRM avatar import and export for Godot, with a built-in MToon toon shader.<br><sub>Good for: Anime 3D · Also in: 3D</sub> |
| [html-anime](https://github.com/blixvip/html-anime) | 273 | 🟢 Active | JavaScript | Turns a scene description into a storyboard sheet, then has a coding agent draw the whole film in HTML. No video model is called.<br><sub>Good for: Animated shorts · Also in: Motion Graphics</sub> |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 267 | 🟢 Active | TypeScript | Loads and plays MMD models and motions in Babylon.js, for anime character dance MVs.<br><sub>Good for: Anime MV · Also in: 3D</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="particle"></a>

### Particles & Physics

<img src="assets/styles/particle.png" alt="Particles & Physics sample" width="240" align="right">

> Smoke, fluid, fireworks and collision simulations

**Picks:** [Taichi](https://github.com/taichi-dev/taichi) · [Matter.js](https://github.com/liabru/matter-js) · [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) · [tsParticles](https://github.com/tsparticles/tsparticles) · [three.quarks](https://github.com/Alchemist0823/three.quarks)

28 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [three.js](https://github.com/mrdoob/three.js) | 119k | 🟢 Active | JavaScript | The de facto standard for 3D on the web: scenes, materials, particles, and post-processing, with lots of examples.<br><sub>Good for: MV · Web 3D · Also in: 3D, Shaders & Psychedelic</sub> |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.9k | 🟢 Active | TypeScript | Fast 2D rendering engine (WebGL / WebGPU) for large numbers of sprites, filters, and 2D motion effects.<br><sub>Good for: Web animation · MV · Also in: Motion Graphics, Generative Art</sub> |
| [particles.js](https://github.com/VincentGarreau/particles.js) | 30.2k | ⚪ Dormant | JavaScript | Classic particle background library for web pages.<br><sub>Good for: Background assets</sub><br><sub>⚠️ Not updated in years. For new projects, use tsParticles.</sub> |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | 🟢 Active | Python | High-performance parallel computing in Python, often used for physics simulations such as fluids, elastic bodies, and particles.<br><sub>Good for: Physics simulation · Also in: 3D</sub> |
| [p5.js](https://github.com/processing/p5.js) | 24.4k | 🟢 Active | JavaScript | The most popular creative coding library: draw, build interactions, and animate on the web. Plenty of Chinese tutorials too.<br><sub>Good for: Generative art · MV · Also in: Generative Art, Music Visualization</sub><br><sub>⚠️ Exporting video takes extra steps (save frames one by one, or screen-record).</sub> |
| [Matter.js](https://github.com/liabru/matter-js) | 18.7k | 🟢 Active | JavaScript | 2D physics engine for collisions, bouncing, stacking, and similar physics animation.<br><sub>Good for: Physics animation</sub> |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.9k | ⚪ Dormant | JavaScript | Real-time fluid simulation in the browser. The colorful smoke looks great on video.<br><sub>Good for: Effect assets · Also in: Shaders & Psychedelic</sub> |
| [canvas-confetti](https://github.com/catdad/canvas-confetti) | 12.9k | 🟡 Slowing | JavaScript | Confetti and fireworks effects in one line of code.<br><sub>Good for: Web effects</sub> |
| [tsParticles](https://github.com/tsparticles/tsparticles) | 9.1k | 🟢 Active | TypeScript | Library of particle, confetti, and fireworks effects. Change the config and it works.<br><sub>Good for: Web effects</sub> |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | 🟢 Active | TypeScript | Web graphics engine open-sourced by Ant Group, covering 2D, 3D, particles, and Lottie.<br><sub>Good for: Web 3D · Interactive · Also in: 3D</sub> |
| [ALIEN](https://github.com/chrxh/alien) | 5.6k | 🟢 Active | C++ / CUDA | GPU-accelerated artificial life simulation where thousands of particles form evolving organisms.<br><sub>Good for: Artificial life · Also in: Artificial Life & Growth</sub><br><sub>⚠️ Requires an NVIDIA GPU.</sub> |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.5k | 🟢 Active | TypeScript | Component library that layers WebGL fluid, shader, and 3D effects over real web UI.<br><sub>Good for: Web effects · Also in: Shaders & Psychedelic</sub> |
| [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) | 5.4k | 🟢 Active | C++ | Classic falling-sand physics sandbox: simulates air pressure, temperature, electricity, and reactions among hundreds of elements.<br><sub>Good for: Particle sandbox · Also in: Falling Sand</sub><br><sub>⚠️ Mainly a game; good for recording physics reactions.</sub> |
| [Particle Life](https://github.com/hunar4321/particle-life) | 3.4k | ⚪ Dormant | JS / C++ / Python | Set attraction and repulsion between a few kinds of particles and cell-like group motion emerges. Very short code.<br><sub>Good for: Artificial life · Also in: Artificial Life & Growth</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Proton](https://github.com/drawcall/Proton) | 2.5k | 🟡 Slowing | JavaScript | JavaScript particle animation engine. Renders to Canvas, WebGL or the DOM, and can plug into three.js and PixiJS.<br><sub>Good for: Particle animation</sub> |
| [The Nature of Code](https://github.com/nature-of-code/noc-book-2) | 2k | 🟡 Slowing | p5.js | 2024 edition of The Nature of Code: simulate forces, particles, flocking, and cellular automata with p5.js. Essential reading for generative art beginners.<br><sub>Good for: Tutorials · Also in: Generative Art, Artificial Life & Growth</sub> |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.3k | 🟢 Active | TypeScript | Particle effects system for three.js: fire, explosions, magic, and other VFX.<br><sub>Good for: 3D effects · Also in: 3D</sub> |
| [three-nebula](https://github.com/creativelifeform/three-nebula) | 1.3k | 🟢 Active | JavaScript | WebGL particle system engine for three.js, with a visual editor.<br><sub>Good for: 3D particles · Also in: 3D</sub> |
| [Particle Life App](https://github.com/tom-mohr/particle-life-app) | 1k | 🟡 Slowing | Java | Particle life simulator with a graphical interface. Tweak the rules and record the emergent behavior.<br><sub>Good for: Artificial life · Also in: Artificial Life & Growth</sub> |
| [Godot Ocean FFT](https://github.com/tessarakkt/godot4-oceanfft) | 614 | 🟡 Slowing | Godot | Ocean waves and buoyancy based on Tessendorf FFT, implemented with compute shaders in Godot 4.<br><sub>Good for: Ocean · Also in: Shaders & Psychedelic, 3D</sub> |
| [Remotion Bits](https://github.com/av/remotion-bits) | 523 | 🟢 Active | TypeScript (Remotion) | Ready-made animation components for Remotion: text effects, gradient transitions, particles, 3D scenes, charts and more; pull in only what you need.<br><sub>Good for: MG components · Short videos · Also in: Motion Graphics, Kinetic Type & Lyrics</sub><br><sub>⚠️ Not affiliated with the Remotion team.</sub> |
| [manim-physics](https://github.com/Matheart/manim-physics) | 414 | 🟢 Active | Python | Physics simulation extension for Manim: rigid bodies, electromagnetic fields, waves, pendulums, and other physics animations.<br><sub>Good for: Explainer videos · Also in: Math Explainer</sub> |
| [Godot VFX Library](https://github.com/haowg/GODOT-VFX-LIBRARY) | 359 | 🟡 Slowing | Godot | Collection of particle effects and shaders for Godot 4.<br><sub>Good for: Effect assets · Also in: Shaders & Psychedelic</sub> |
| [cbirds](https://github.com/clainstone/cbirds) | 320 | 🟢 Active | C (CLI) | A flock of birds in your terminal: the Boids flocking algorithm drawn with braille dots, also exportable as sprites.<br><sub>Good for: Terminal animation · Also in: ASCII & Terminal</sub> |
| [Natural Disasters](https://github.com/Token-Gremlin/natural-disasters) | 307 | 🟢 Active | WebGPU | Fully procedural cinematic ocean and extreme weather simulation in the browser: storms, waves, tornadoes.<br><sub>Good for: Weather effects · Also in: Shaders & Psychedelic, 3D</sub> |
| [Galaxy Simulation](https://github.com/N0rvel/galaxy_sim) | 162 | 🟢 Active | JavaScript (three.js) | Simulates gravity between thousands of particles with three.js and shaders: a single galaxy, two colliding galaxies or an expanding universe.<br><sub>Good for: Galaxies · Particles · Also in: Space & Stars</sub> |
| [Cyber Ocean](https://github.com/SahilK-027/Cyber-Ocean) | 82 | 🟢 Active | three.js | 3D flow-field particle ocean built with three.js, with custom post-processing.<br><sub>Good for: 3D particles · Also in: Flow & Wind Fields, 3D</sub> |
| [Galaxy Shader](https://github.com/AmitDigga/threejs-galaxy-shader) | 73 | 🟡 Slowing | three.js | High-performance three.js galaxy shader with adjustable colors, spiral arms, and black hole effects.<br><sub>Good for: Galaxy effects · Also in: Space & Stars, Shaders & Psychedelic</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="glitch"></a>

### Glitch & Post FX

<img src="assets/styles/glitch.png" alt="Glitch & Post FX sample" width="240" align="right">

> RGB shift, distortion, bloom, pixel sorting and compositing

**Picks:** [postprocessing](https://github.com/pmndrs/postprocessing) · [VFX-JS](https://github.com/fand/vfx-js) · [pixelsort](https://github.com/satyarth/pixelsort) · [PixiJS Filters](https://github.com/pixijs/filters) · [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs)

17 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 68.1k | 🟢 Active | C (CLI) | The foundation under almost every code-to-video tool: transcoding, concatenation, filters and burned-in captions, all from the command line.<br><sub>Good for: Editing and compositing · Post-processing · Also in: Shorts, Captions & Editing</sub><br><sub>⚠️ Mirror repository on GitHub.</sub> |
| [EffectCraft](https://github.com/storytold/effectcraft) | 9.2k | 🟢 Active | Rust (GUI) | Open-source compositing app written from scratch, After Effects-style: layers, keyframes, expressions, 300+ effects.<br><sub>Good for: Motion graphics · Post compositing · Also in: Motion Graphics</sub><br><sub>⚠️ Mostly a graphical interface; the expressions part can be scripted in code.</sub> |
| [Natron](https://github.com/NatronGitHub/Natron) | 5.8k | 🟢 Active | C++ / Python | Open-source node-based compositing software, scriptable with Python, for post-production compositing and effects.<br><sub>Good for: Post compositing</sub> |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | 🟢 Active | C++ (Windows) | Overlays retro shaders (CRT, pixel, and others) on the Windows desktop; screen-record to get a retro look.<br><sub>Good for: Retro post-processing · Also in: Pixel & Retro, VHS & Analog</sub> |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 3k | 🟢 Active | JavaScript | Post-processing library for three.js: bloom, chromatic aberration, glitch, depth of field, and more.<br><sub>Good for: 3D post-processing · Also in: 3D</sub> |
| [Inferno](https://github.com/twostraws/Inferno) | 2.9k | 🟡 Slowing | Swift / Metal (iOS) | Collection of Metal shaders for SwiftUI: fire, water ripples, pixelation, shine sweeps, and more. Ready to use in mobile apps.<br><sub>Good for: App motion · Also in: Shaders & Psychedelic</sub> |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.8k | 🟡 Slowing | JavaScript | Real-time video synthesizer in the browser, modeled on analog signal synthesizers. A few lines of code give feedback, distortion, and psychedelic color visuals.<br><sub>Good for: Live VJ · MV · Also in: Live Coding & VJ, Shaders & Psychedelic</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) | 2.7k | 🟢 Active | Rust | Open-source VHS effect: simulates NTSC signal and tape color bleed, jitter, and snow. Works standalone and as an AE, PR, and OFX plugin.<br><sub>Good for: VHS post-processing · Also in: VHS & Analog</sub> |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.3k | 🟢 Active | GLSL | Open collection of GLSL transitions. Plugs into editors like editly.<br><sub>Good for: Transitions · Also in: Shorts, Captions & Editing</sub> |
| [glitch-this](https://github.com/TotallyNotChase/glitch-this) | 1.8k | ⚪ Dormant | Python | Adds glitch effects to images and GIFs with adjustable parameters, and can output glitched GIFs directly.<br><sub>Good for: Glitch GIFs</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | 🟢 Active | TypeScript | Add WebGL effects to images, video, and text on web pages: glitch, RGB shift, distortion, and more.<br><sub>Good for: Web effects · MV · Also in: Kinetic Type & Lyrics</sub> |
| [ntscqt](https://github.com/JargeZ/ntscqt) | 1.2k | ⚪ Dormant | Python | GUI for a VHS video simulator, giving video an old videotape look.<br><sub>Good for: VHS post-processing · Also in: VHS & Analog</sub><br><sub>⚠️ Not updated since 2024; use ntsc-rs for new projects.</sub> |
| [PixiJS Filters](https://github.com/pixijs/filters) | 1.2k | 🟡 Slowing | TypeScript | Community filter collection for PixiJS: glitch, glow, pixelate, CRT, and dozens more effects.<br><sub>Good for: 2D effects · Also in: Shaders & Psychedelic</sub> |
| [pixelsort](https://github.com/satyarth/pixelsort) | 876 | 🟢 Active | Python | Pixel sorting glitch art: rearranges pixels by rules such as brightness.<br><sub>Good for: Glitch art</sub> |
| [ff-tracking](https://github.com/mrsarac/ff-tracking) | 653 | 🟢 Active | Rust | Short film where a virtual camera films an AI agent's screen and tracks every glyph. Uses fframes two-pass rendering and SkSL shaders; the sound effects are also synthesized in code.<br><sub>Good for: Motion shorts · Also in: Motion Graphics</sub> |
| [SwiftUI Shaders](https://github.com/krispuckett/SwiftUIShaders) | 353 | 🟢 Active | Swift (iOS) | 41 Metal shaders ready to drop into SwiftUI: holographic foil, kaleidoscope, magnetic distortion, and more. Good for mobile app motion.<br><sub>Good for: App motion · Also in: Shaders & Psychedelic</sub> |
| [VhsFx](https://github.com/NullTale/VhsFx) | 90 | 🟡 Slowing | Unity | VHS post-processing effect for Unity URP.<br><sub>Good for: VHS post-processing · Also in: VHS & Analog</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="pixel"></a>

### Pixel & Retro

<img src="assets/styles/pixel.png" alt="Pixel & Retro sample" width="240" align="right">

> Low resolution, limited palettes, CRT scanlines, PS1 texture

**Picks:** [Pyxel](https://github.com/kitao/pyxel) · [TIC-80](https://github.com/nesbox/TIC-80) · [raylib](https://github.com/raysan5/raylib) · [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) · [pixelfx](https://github.com/patch-gg/pixelfx)

31 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [raylib](https://github.com/raysan5/raylib) | 35.8k | 🟢 Active | C (many bindings) | Simple, beginner-friendly C graphics library with bindings for dozens of languages. Quick for 2D/3D animations and small demos.<br><sub>Good for: 2D/3D animation · Mini games · Also in: 3D, Generative Art</sub> |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | 26.6k | 🟢 Active | QML / C++ | Terminal that imitates an old CRT monitor: scanlines, glow, screen curvature. Screen recordings come out looking retro.<br><sub>Good for: Retro terminals · Also in: ASCII & Terminal, VHS & Analog</sub> |
| [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | 25.6k | 🟢 Active | C# | Wave Function Collapse algorithm: generates endless variations of pixel images and maps from one small sample. The generation process itself is fun to watch.<br><sub>Good for: Procedural generation · Also in: Procedural Generation</sub> |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 20.1k | 🟢 Active | JavaScript | A toolbox of film styles made in code: 66 ready-made styles (Memphis, subway map, chalkboard, and more) that let an AI coding agent make videos in each style, all drawn with code.<br><sub>Good for: MV · Short films · Also in: Motion Graphics, Hand-drawn & Whiteboard</sub><br><sub>⚠️ Styles are tuned for Claude; results may differ with other models.</sub> |
| [Pyxel](https://github.com/kitao/pyxel) | 18.7k | 🟢 Active | Python | Retro game engine for Python with a 16-color pixel display. Also good for small pixel-art animations.<br><sub>Good for: Pixel animation</sub> |
| [LÖVE](https://github.com/love2d/love) | 9k | 🟢 Active | Lua | Framework for making 2D games and animations in Lua. Lots of pixel-art work.<br><sub>Good for: Pixel animation · Mini games</sub> |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 8.8k | 🟢 Active | JavaScript | 244 pixel effect animations written in code: fire, explosions, magic, weather, and more. Exports sprite sheets. Includes an AI coding agent skill.<br><sub>Good for: Pixel effect assets</sub> |
| [MarkovJunior](https://github.com/mxgmn/MarkovJunior) | 8.5k | 🟡 Slowing | C# | From the same author: a procedural generation language that uses rewrite rules to grow mazes, cities, and voxel buildings step by step. Comes with 153 example animations.<br><sub>Good for: Procedural generation · Also in: Procedural Generation, Isometric & Voxel</sub> |
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | 6.8k | ⚪ Dormant | C / JS | Recreates the 90s game Comanche's voxel terrain flight view in under 20 lines of code, with an explanation of how it works.<br><sub>Good for: Retro voxel terrain · Also in: Isometric & Voxel, 3D</sub> |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | 🟢 Active | Lua / JS and more | Fantasy console (240x136 pixels, 16 colors), popular for tiny demoscene pieces and live Byte Jam streams.<br><sub>Good for: Pixel animation · Live · Also in: Live Coding & VJ, Demoscene</sub> |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | 🟢 Active | C++ (Windows) | Overlays retro shaders (CRT, pixel, and others) on the Windows desktop; screen-record to get a retro look.<br><sub>Good for: Retro post-processing · Also in: Glitch & Post FX, VHS & Analog</sub> |
| [Godot Shaders](https://github.com/gdquest-demos/godot-shaders) | 4.2k | 🟢 Active | Godot Shader | GDQuest's large collection of Godot 2D and 3D shaders: dissolve, outline, water, pixelation, and more.<br><sub>Good for: Shader collections · Also in: Shaders & Psychedelic, 3D</sub> |
| [Sandspiel](https://github.com/MaxBittker/sandspiel) | 3.2k | 🟢 Active | Rust / WASM | Falling-sand sandbox in the browser: sand, water, fire, and plants interact by cellular automata rules, like flowing pixel art.<br><sub>Good for: Falling sand visuals · Also in: Falling Sand</sub> |
| [timg](https://github.com/hzeller/timg) | 2.8k | 🟢 Active | C++ (CLI) | Shows images and plays video in the terminal, using character blocks and terminal graphics protocols.<br><sub>Good for: Terminal playback · Also in: ASCII & Terminal</sub> |
| [obelisk.js](https://github.com/nosir/obelisk.js) | 2.3k | ⚪ Dormant | JavaScript | Builds pixel-style isometric graphics on Canvas, stacking pixel blocks one by one.<br><sub>Good for: Pixel isometric · Also in: Isometric & Voxel</sub><br><sub>⚠️ Not updated since 2019.</sub> |
| [Animate](https://github.com/cth9191/animate) | 2.2k | 🟢 Active | JavaScript / Canvas | Claude Code skill: draws short animations procedurally on a single canvas, with 7 built-in styles: paper cut-out, hatched ink, Riso print, sketchbook, math, pixel, and isometric.<br><sub>Good for: Explainer videos · Short films · Also in: Hand-drawn & Whiteboard, Math Explainer, Riso & Paper Collage</sub> |
| [WASM-4](https://github.com/aduros/wasm4) | 1.5k | 🟢 Active | Multiple languages | Minimal fantasy console (160x160 pixels, 4 colors). Write small pixel-art pieces in many languages.<br><sub>Good for: Pixel animation</sub> |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | 🟢 Active | GLSL | RetroArch shader collection: CRT scanlines, pixel upscaling, and other retro display effects.<br><sub>Good for: Retro post-processing · Also in: Shaders & Psychedelic, VHS & Analog</sub> |
| [DOjS](https://github.com/SuperIlu/DOjS) | 965 | 🟡 Slowing | JavaScript (DOS) | JavaScript creative coding environment that runs on MS-DOS, with a p5.js-like API and plenty of retro flavor.<br><sub>Good for: Retro creative coding · Also in: Generative Art</sub> |
| [GodotRetro](https://github.com/ahopness/GodotRetro) | 824 | 🟢 Active | Godot Shader | Retro post-processing effects pack for Godot: CRT, VHS, dithering, pixelation.<br><sub>Good for: Retro post-processing · Also in: Shaders & Psychedelic, VHS & Analog</sub> |
| [Diorama](https://github.com/sloemo01/diorama) | 715 | 🟢 Active | JavaScript (three.js) | A playbook for AI coding agents to build three.js dioramas: tiny people with joint animation, a 64-colour ordered-dither pixel look by default, or stroked toon.<br><sub>Good for: Miniature scene clips · Also in: 3D, Dither & 1-bit</sub><br><sub>⚠️ By default mixes commercially licensed 3D assets with hand-built geometry; sources are recorded in the repo.</sub> |
| [NTSC-CRT](https://github.com/LMP88959/NTSC-CRT) | 578 | 🟢 Active | C | NTSC encoding/decoding simulation using only integer math, able to recreate how old consoles like the NES looked on a TV.<br><sub>Good for: CRT simulation · Also in: VHS & Analog</sub> |
| [Sandboxels](https://github.com/R74nCom/sandboxels) | 487 | 🟢 Active | JavaScript | Browser falling-sand simulation with 500+ elements and thousands of reactions. You can write your own elements as mods.<br><sub>Good for: Falling sand visuals · Also in: Falling Sand</sub> |
| [Retro Crisis Shaders](https://github.com/RetroCrisis/Retro-Crisis-GDV-NTSC) | 482 | 🟢 Active | Slang Shader | Collection of CRT shader presets for RetroArch, based on Guest Advanced NTSC. Recreates the look of various old TVs.<br><sub>Good for: CRT post-processing · Also in: VHS & Analog, Shaders & Psychedelic</sub> |
| [Ultimate Retro Shaders](https://github.com/Zorochase/ultimate-retro-shader-collection) | 344 | 🟢 Active | Godot Shader | Retro shader collection for Godot 4, giving the dithering, low-poly, and texture-wobble look of the PS1 and N64 era.<br><sub>Good for: PS1 retro 3D · Also in: 3D, Shaders & Psychedelic</sub> |
| [weilanx Claude Videos](https://github.com/Azure12355/weilanx-claude-videos) | 277 | 🟢 Active | TypeScript | Made by a Chinese developer: hand-drawn and pixel-art explainer videos written purely in code with Remotion + React + SVG.<br><sub>Good for: Explainer videos · Also in: Hand-drawn & Whiteboard</sub><br><sub>⚠️ One skill's cover image used text-to-image generation; it can be swapped for a code-rendered frame.</sub> |
| [hitherdither](https://github.com/hbldh/hitherdither) | 260 | 🟢 Active | Python | Python dithering algorithm library with support for arbitrary palettes. For limited-color pixel looks and retro print textures.<br><sub>Good for: Dithering assets · Also in: Dither & 1-bit</sub> |
| [Dither Guy](https://github.com/manoelpiovesan/dither-guy) | 254 | 🟢 Active | Python | An open-source alternative to Dither Boy: applies Bayer, Floyd-Steinberg and other dithering to images and video for a low-colour retro display look.<br><sub>Good for: Dithering · Retro look · Also in: Dither & 1-bit</sub> |
| [Codixel](https://github.com/mankidev/codixel) | 244 | 🟢 Active | JavaScript / skill | Teaches Claude Code to make pixel animation in code: assemble a character from reference images, rig it, then pixelate it; also covers fire, smoke and beam effects.<br><sub>Good for: Pixel sprites · Game effects</sub><br><sub>⚠️ You supply the reference images (your own or suitably licensed); no image generation is used.</sub> |
| [Sand Slide](https://github.com/kiwijuice56/sand-slide) | 143 | 🟢 Active | Godot / C++ | Fast falling sand game built with Godot and GDExtension, with many element types.<br><sub>Good for: Falling sand visuals · Also in: Falling Sand</sub> |
| [FallingSandEngine](https://github.com/PieKing1215/FallingSandEngine) | 76 | 🟡 Slowing | Rust | Experimental 2D falling sand engine in Rust, where every pixel takes part in physics like in Noita.<br><sub>Good for: Falling sand engines · Also in: Falling Sand</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="ascii"></a>

### ASCII & Terminal

<img src="assets/styles/ascii.png" alt="ASCII & Terminal sample" width="240" align="right">

> Text art, Braille dots and text effects in the terminal

**Picks:** [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) · [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) · [Chafa](https://github.com/hpjansson/chafa) · [asciimatics](https://github.com/peterbrittain/asciimatics) · [play.core](https://github.com/ertdfgcvb/play.core)

26 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | 26.6k | 🟢 Active | QML / C++ | Terminal that imitates an old CRT monitor: scanlines, glow, screen curvature. Screen recordings come out looking retro.<br><sub>Good for: Retro terminals · Also in: Pixel & Retro, VHS & Analog</sub> |
| [VHS](https://github.com/charmbracelet/vhs) | 21.4k | 🟢 Active | VHS script | Script terminal actions and record them automatically as a GIF or video. The easiest way to make command-line demos.<br><sub>Good for: Explainer videos · GIF · Also in: Code & Terminal Demo</sub> |
| [asciinema](https://github.com/asciinema/asciinema) | 18k | 🟢 Active | Rust (CLI) | Records terminal sessions and replays them in a web player. Small files, copyable text.<br><sub>Good for: Explainer videos · Also in: Code & Terminal Demo</sub> |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | ⚪ Dormant | JavaScript (CLI) | Records terminal sessions and renders them as animated GIFs with a window frame.<br><sub>Good for: GIF · Also in: Code & Terminal Demo</sub> |
| [MapSCII](https://github.com/rastapasta/mapscii) | 9.3k | ⚪ Dormant | JavaScript | Renders a world map in the terminal with Braille dots and characters; you can zoom and drag.<br><sub>Good for: Terminal maps · Also in: Map & Route</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | 🟢 Active | C (CLI) | Audio spectrum visualizer for the terminal.<br><sub>Good for: Music visualizer · Also in: Music Visualization</sub> |
| [Chafa](https://github.com/hpjansson/chafa) | 5.4k | 🟢 Active | C (CLI) | Converts images and animations to terminal character art, with many character sets and color modes.<br><sub>Good for: Text art assets</sub> |
| [CMatrix](https://github.com/abishekvashok/cmatrix) | 5.3k | ⚪ Dormant | C (CLI) | The Matrix code rain in your terminal.<br><sub>Good for: Terminal animation</sub> |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | 🟢 Active | Python | Terminal text effects library with dozens of text entrance animations (burn, rain, decrypt and more).<br><sub>Good for: Intros · Text effects · Also in: Kinetic Type & Lyrics</sub> |
| [asciimatics](https://github.com/peterbrittain/asciimatics) | 4.3k | 🟢 Active | Python | Python library for terminal animation and text UIs. Can build ASCII-art effect scenes.<br><sub>Good for: Terminal animation</sub> |
| [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | 3.6k | ⚪ Dormant | Go (CLI) | Command-line tool that converts images and GIFs into colored ASCII art.<br><sub>Good for: Text art assets</sub> |
| [doitlive](https://github.com/sloria/doitlive) | 3.6k | 🟢 Active | Python | Pre-write your commands, then mash the keyboard live and they type out character by character. Terminal demos without typos.<br><sub>Good for: Terminal demos · Also in: Code & Terminal Demo</sub> |
| [timg](https://github.com/hzeller/timg) | 2.8k | 🟢 Active | C++ (CLI) | Shows images and plays video in the terminal, using character blocks and terminal graphics protocols.<br><sub>Good for: Terminal playback · Also in: Pixel & Retro</sub> |
| [astroterm](https://github.com/da-luce/astroterm) | 2.6k | 🟢 Active | C (CLI) | Planetarium in your terminal. Renders stars, planets, and constellations live as characters.<br><sub>Good for: Terminal starfields · Also in: Space & Stars</sub> |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | 🟢 Active | TypeScript | 3D renderer written in JavaScript that draws 3D scenes directly in the terminal.<br><sub>Good for: Terminal animation · Also in: 3D</sub> |
| [video-to-ascii](https://github.com/joelibaceta/video-to-ascii) | 1.9k | 🟡 Slowing | Python | Plays video in the terminal as character art.<br><sub>Good for: Effect assets</sub> |
| [Durdraw](https://github.com/durdraw/durdraw) | 1.9k | 🟢 Active | Python (terminal) | ASCII/ANSI art editor for the terminal, with frame-by-frame character animation.<br><sub>Good for: ANSI text animation</sub> |
| [scope-tui](https://github.com/alemidev/scope-tui) | 763 | 🟢 Active | Rust (CLI) | Oscilloscope, vectorscope, and spectroscope in your terminal, drawing waveforms with characters.<br><sub>Good for: Terminal oscilloscope · Also in: Oscilloscope & Vector, Music Visualization</sub> |
| [linecast](https://github.com/ashuttl/linecast) | 698 | 🟢 Active | CLI | Weather, tides, sun, moon, and stars in the terminal, in a retro almanac style.<br><sub>Good for: Terminal sky charts · Also in: Space & Stars</sub> |
| [play.core](https://github.com/ertdfgcvb/play.core) | 546 | 🟢 Active | JavaScript | Experimental platform for ASCII character animation in JS. Each character is a "pixel".<br><sub>Good for: Generative art · Also in: Generative Art</sub> |
| [ASCII Magic](https://github.com/kailashsr38/ascii-magic-art) | 480 | 🟢 Active | JavaScript | 734 animated ASCII pieces in 24 categories. Preview them in the terminal, switch looks (halftone, binary, dither), then hand one to an AI coding agent to add to a page.<br><sub>Good for: ASCII animation assets</sub> |
| [Open Cubic Player](https://github.com/mywave82/opencubicplayer) | 453 | 🟢 Active | C | Unix version of the classic DOS player. Plays tracker music such as MOD and S3M, with retro visualizations.<br><sub>Good for: Retro music visualizer · Also in: Music Visualization, Demoscene</sub> |
| [cbirds](https://github.com/clainstone/cbirds) | 320 | 🟢 Active | C (CLI) | A flock of birds in your terminal: the Boids flocking algorithm drawn with braille dots, also exportable as sprites.<br><sub>Good for: Terminal animation · Also in: Particles & Physics</sub> |
| [termsand](https://github.com/cgsdev0/termsand) | 318 | 🟢 Active | Shell / tmux | Falling sand simulation that runs in tmux. Click with the mouse and sand falls from the top of the terminal.<br><sub>Good for: Terminal animation · Also in: Falling Sand</sub> |
| [proof-engine](https://github.com/Mattbusel/proof-engine) | 32 | 🟢 Active | Rust | Rendering engine where every visual is math: glyphs and particles driven by strange attractors.<br><sub>Good for: Math visuals · Also in: Fractals & Chaos</sub> |
| [TermiSand](https://github.com/BobdaProgrammer/TermiSand) | 22 | 🟡 Slowing | CLI | Falling-sand simulator in your terminal, drawing sand and water with characters.<br><sub>Good for: Terminal animation · Also in: Falling Sand</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="data"></a>

### Data Animation

<img src="assets/styles/data.png" alt="Data Animation sample" width="240" align="right">

> Growing charts, bar chart races, Git history animations

**Picks:** [D3](https://github.com/d3/d3) · [Apache ECharts](https://github.com/apache/echarts) · [Gource](https://github.com/acaudwell/Gource) · [Vizzu](https://github.com/vizzuhq/vizzu-lib) · [deck.gl](https://github.com/visgl/deck.gl)

30 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [D3](https://github.com/d3/d3) | 114k | 🟢 Active | JavaScript | Low-level data visualization library with strong transition animation, often used for data journalism animations.<br><sub>Good for: Data videos · Web</sub> |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.8k | 🟢 Active | Python | The math animation engine 3Blue1Brown himself uses (ManimGL): formulas, coordinate systems, shape transforms, in the classic blue-and-black explainer style.<br><sub>Good for: Explainer videos · Also in: Math Explainer</sub><br><sub>⚠️ Sparse docs; beginners should start with the community edition.</sub> |
| [Apache ECharts](https://github.com/apache/echarts) | 67.8k | 🟢 Active | TypeScript | One of the most widely used chart libraries in China, with rich built-in transition animations and timeline playback.<br><sub>Good for: Data videos · Web</sub> |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.6k | ⚪ Dormant | JavaScript | Animates how algorithms run, including sorting, graphs, and dynamic programming.<br><sub>Good for: Explainer videos · Also in: Code & Terminal Demo</sub> |
| [Manim Community](https://github.com/ManimCommunity/manim) | 42.8k | 🟢 Active | Python | Community-maintained fork of Manim with the most complete docs and tutorials. Used for many math, physics and algorithm explainer videos on Bilibili.<br><sub>Good for: Explainer videos · Also in: Math Explainer, Code & Terminal Demo</sub> |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | 23.5k | 🟢 Active | Python | The basic Python plotting library. FuncAnimation makes data animations that export to video.<br><sub>Good for: Data videos</sub> |
| [Plotly](https://github.com/plotly/plotly.py) | 18.9k | 🟢 Active | Python | Interactive charting library for Python, with frame-by-frame animated charts.<br><sub>Good for: Data animation</sub> |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.8k | 🟢 Active | TypeScript | Large-scale geospatial data visualization: animated trajectories, 3D column maps, and more.<br><sub>Good for: Map animation · Also in: 3D, Map & Route</sub> |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | 🟡 Slowing | C++ (CLI) | Renders Git commit history as a video of code "growing". A classic piece of footage for programmers.<br><sub>Good for: Developer videos · Also in: Code & Terminal Demo</sub> |
| [AntV G2](https://github.com/antvis/G2) | 12.7k | 🟢 Active | TypeScript | Visualization grammar library from Ant Group's AntV. Charts come with built-in enter and update animations.<br><sub>Good for: Data animation</sub> |
| [chart.xkcd](https://github.com/timqian/chart.xkcd) | 7.9k | 🟢 Active | JavaScript | Hand-drawn chart library in the xkcd comic style, with wobbly lines and a comic font.<br><sub>Good for: Hand-drawn charts · Also in: Hand-drawn & Whiteboard</sub> |
| [roughViz](https://github.com/jwilber/roughViz) | 7.2k | ⚪ Dormant | JavaScript | Sketchy chart library built on Rough.js. Bar and pie charts get a hand-drawn look.<br><sub>Good for: Hand-drawn charts · Also in: Hand-drawn & Whiteboard</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [earth](https://github.com/cambecc/earth) | 6.6k | ⚪ Dormant | JavaScript | Famous global weather animation: wind, ocean currents, and temperature flowing over the globe in real time.<br><sub>Good for: Global wind maps · Also in: Flow & Wind Fields, Map & Route</sub><br><sub>⚠️ Not updated since 2022; the look and the code are still a classic reference.</sub> |
| [Pts](https://github.com/williamngan/pts) | 5.4k | 🟢 Active | TypeScript | Visualization and creative coding library built around geometric relations of points, lines and shapes.<br><sub>Good for: Generative art · Also in: Generative Art</sub> |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | 🟢 Active | Python | Draws the effect of Git commands as diagrams and animations (built on Manim). Good for Git teaching videos.<br><sub>Good for: Explainer videos · Also in: Code & Terminal Demo</sub> |
| [AntV L7](https://github.com/antvis/L7) | 4.1k | 🟢 Active | TypeScript | Large-scale geospatial visualization engine from Ant Group's AntV. Map animations such as flying lines, trajectories, and heatmaps.<br><sub>Good for: Map animation · Also in: Map & Route</sub> |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | 🟢 Active | TypeScript | Toolkit of over a hundred TypeScript packages for generative art and visualization, long maintained by its author.<br><sub>Good for: Generative art · Also in: Generative Art</sub> |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3.5k | 🟢 Active | React / TS | Give it a topic and it makes a black-background motion graphics explainer video, with voiceover and captions. Every frame is rendered in code.<br><sub>Good for: Explainer videos · Also in: Motion Graphics</sub> |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | ⚪ Dormant | Python | Machine learning concept animations built on Manim: explainer animations of neural networks, convolutions, and similar structures.<br><sub>Good for: Explainer videos · Also in: Math Explainer</sub> |
| [Vizzu](https://github.com/vizzuhq/vizzu-lib) | 2k | 🟡 Slowing | JavaScript | Chart library built for data animation. Charts morph smoothly into one another, good for data storytelling.<br><sub>Good for: Data story animation</sub> |
| [gganimate](https://github.com/thomasp85/gganimate) | 2k | 🟡 Slowing | R | Animation extension for R's ggplot2. Turns static charts into animations.<br><sub>Good for: Data videos</sub> |
| [AI Animation Skills](https://github.com/Unclecheng-li/AI_Animation) | 1.8k | 🟢 Active | HTML / skill | 17 skills that have an AI coding agent write single-file HTML animations: PPT-style explainers, flowcharts, network protocols, animated architecture diagrams, storyboards and more.<br><sub>Good for: Explainer decks · Concept animations · Also in: Motion Graphics</sub> |
| [Logstalgia](https://github.com/acaudwell/Logstalgia) | 1.8k | 🟡 Slowing | C++ (CLI) | Turns website access logs into a Pong-style animation.<br><sub>Good for: Playful visualization</sub> |
| [bar_chart_race](https://github.com/dexplo/bar_chart_race) | 1.5k | ⚪ Dormant | Python | Generate bar chart race animation videos in a few lines of Python.<br><sub>Good for: Data videos</sub> |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 983 | 🟢 Active | JavaScript | High-resolution real-time spectrum analyzer with adjustable bar, radial, and other styles.<br><sub>Good for: Music visualizer · Also in: Music Visualization</sub><br><sub>⚠️ AGPL-3.0: if used in a network service offered to others, you must publish your modified source.</sub> |
| [party-mode](https://github.com/preziotte/party-mode) | 807 | 🟢 Active | JavaScript | Experimental D3-based music visualizer with several rhythmic geometric patterns.<br><sub>Good for: Music visualizer · Also in: Music Visualization</sub> |
| [drawsvg](https://github.com/cduck/drawsvg) | 698 | 🟢 Active | Python | Generate SVG graphics and animations from Python, with interactive preview in Jupyter.<br><sub>Good for: SVG animation · Also in: Motion Graphics</sub> |
| [Content Studio (design-agent)](https://github.com/langchain-ai/design-agent) | 674 | 🟢 Active | JavaScript / Python (HyperFrames) | LangChain's open-source design agent: ask in a chat thread and get on-brand stills, decks, diagrams, charts and motion graphics back. Video is built in HyperFrames; code renders, checks and delivers.<br><sub>Good for: Brand assets · Launch films · Also in: Motion Graphics</sub><br><sub>⚠️ Built on Deep Agents; full deployment runs in Slack, and it can be tried locally without keys. Image generation is optional and needs your own OpenAI or Google key.</sub> |
| [manim-web](https://github.com/maloyan/manim-web) | 520 | 🟢 Active | TypeScript | A TypeScript port of 3Blue1Brown's Manim that renders in a browser canvas, plus molecular, chemistry, biology and map modules.<br><sub>Good for: Math animation · Web · Also in: Math Explainer</sub> |
| [YouTube Motion Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics) | 248 | 🟢 Active | HTML | 74 animated HTML explainer boards (charts, diagrams, flows) for YouTube explainer videos.<br><sub>Good for: Explainer video assets · Also in: Motion Graphics</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="niche"></a>

## Niche styles

Fewer people use these, but you'd recognize them anywhere. The bar is lower here, at 20+ stars with a push in the last year. 165 projects in all.

<a name="ink"></a>

### Ink & Watercolor

<img src="assets/styles/ink.png" alt="Ink & Watercolor sample" width="240" align="right">

> Procedural landscape scrolls, ink bleeds, watercolor pigment and empty space

**Picks:** [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) · [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) · [AquaInkGL](https://github.com/WishMelz/AquaInkGL) · [Watercolor Playground](https://github.com/msurguy/watercolor-playground)

8 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 7.5k | 🟢 Active | JavaScript | 35 art styles and 9 narration grammars, animating pictures with code. The soundtrack is also synthesized in code.<br><sub>Good for: Art animation · Also in: Hand-drawn & Whiteboard</sub><br><sub>⚠️ When a real person is needed on screen, an image generation model produces the frame; everything else is drawn in code.</sub> |
| [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) | 6.5k | ⚪ Dormant | JavaScript | Procedurally generated, endlessly scrolling Chinese landscape painting. Mountains, rocks, trees, and pavilions are all drawn stroke by stroke by algorithms.<br><sub>Good for: Ink wash scrolls · Generative art · Also in: Generative Art</sub><br><sub>⚠️ Not updated since 2018; the work itself is complete and usable.</sub> |
| [Shuimo UI](https://github.com/shuimo-design/shuimo-ui) | 401 | 🟢 Active | Vue / TypeScript | From a Chinese team: ink wash style UI component library, with buttons and dialogs drawn as ink brush strokes.<br><sub>Good for: Ink wash UI</sub> |
| [AquaInkGL](https://github.com/WishMelz/AquaInkGL) | 387 | 🟡 Slowing | WebGL | WebGL ink-wash background effect, with ink bleeding and flowing across rice paper.<br><sub>Good for: Ink wash backgrounds · Also in: Shaders & Psychedelic</sub> |
| [Claude Drawing Skill](https://github.com/cloveric/claude-drawing-skill) | 373 | 🟢 Active | Python | Claude paints stroke by stroke with code, in 77 styles including ink wash, oil painting, clay, cyanotype, stained glass, and Jiangnan gardens, with no image generation model.<br><sub>Good for: Illustration · Ink wash · Also in: Hand-drawn & Whiteboard</sub> |
| [Watercolor Playground](https://github.com/msurguy/watercolor-playground) | 107 | 🟢 Active | TypeScript | Realistic watercolor simulation: paint bleeds, settles, and dries on paper.<br><sub>Good for: Watercolor painting · Also in: Hand-drawn & Whiteboard</sub> |
| [code-poem-film](https://github.com/bangbuilds/code-poem-film) | 66 | 🟢 Active | JavaScript | Speak a poem and get an ink-wash hand-drawn 2D animation: frames drawn by code, recitation aligned word by word, soundtrack synthesized with numpy.<br><sub>Good for: Poetry animation</sub> |
| [Chinese-Style Paper Animation](https://github.com/AllenAI2014/remotion-guofeng-starter) | 37 | 🟢 Active | React / Remotion | Asset library and production skill for Chinese-style paper collage animation. Give an AI a poem or idiom and it renders the video entirely in code.<br><sub>Good for: Poetry animation · Also in: Riso & Paper Collage</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="hanzi"></a>

### Handwriting & Strokes

<img src="assets/styles/hanzi.en.png" alt="Handwriting & Strokes sample" width="240" align="right">

> Chinese characters and handwriting written out stroke by stroke

**Picks:** [Hanzi Writer](https://github.com/chanind/hanzi-writer) · [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) · [animCJK](https://github.com/parsimonhi/animCJK) · [Tegaki](https://github.com/gkurt/tegaki)

5 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Hanzi Writer](https://github.com/chanind/hanzi-writer) | 5.1k | 🟡 Slowing | TypeScript | Chinese character stroke order animation and writing practice library. One line of code animates a character stroke by stroke.<br><sub>Good for: Stroke order animation · Also in: Kinetic Type & Lyrics</sub> |
| [Tegaki](https://github.com/gkurt/tegaki) | 3.3k | 🟢 Active | TypeScript | Handwriting animation for the web: any font and any text can be turned into a pen-writing effect.<br><sub>Good for: Handwriting animation · Also in: Kinetic Type & Lyrics, Hand-drawn & Whiteboard</sub> |
| [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) | 2.8k | 🟡 Slowing | Data / JS | Open-source Chinese character stroke and component data. Stroke order animations such as Hanzi Writer use its data.<br><sub>Good for: Stroke data</sub> |
| [animCJK](https://github.com/parsimonhi/animCJK) | 482 | 🟢 Active | SVG / HTML | SVG animations of Chinese, Japanese and Korean characters written in correct stroke order, including Japanese kana and Korean hanja.<br><sub>Good for: Stroke order animation · Also in: Kinetic Type & Lyrics</sub> |
| [Stroke Order Animator](https://github.com/chill-chinese/stroke-order-animator) | 112 | 🟡 Slowing | Dart (Flutter) | Flutter stroke-order animations and writing quizzes for Chinese characters, using stroke data from Make Me a Hanzi.<br><sub>Good for: Stroke order animation</sub><br><sub>⚠️ Stroke data is under the Arphic Public License.</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="scope"></a>

### Oscilloscope & Vector

<img src="assets/styles/scope.png" alt="Oscilloscope & Vector sample" width="240" align="right">

> Glowing vector lines on an oscilloscope, where pictures and sound turn into each other

**Picks:** [osci-render](https://github.com/jameshball/osci-render) · [scope-tui](https://github.com/alemidev/scope-tui) · [Oscillody](https://github.com/Akosmo/Oscillody)

3 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [scope-tui](https://github.com/alemidev/scope-tui) | 763 | 🟢 Active | Rust (CLI) | Oscilloscope, vectorscope, and spectroscope in your terminal, drawing waveforms with characters.<br><sub>Good for: Terminal oscilloscope · Also in: ASCII & Terminal, Music Visualization</sub> |
| [osci-render](https://github.com/jameshball/osci-render) | 744 | 🟢 Active | C++ / Lua | Synthesizer plugin that draws shapes on an oscilloscope: shapes become sound, and the sound turns back into glowing vector lines on the scope.<br><sub>Good for: Oscilloscope music · MV · Also in: Music Visualization</sub> |
| [Oscillody](https://github.com/Akosmo/Oscillody) | 56 | 🟢 Active | GDScript (Godot) | An oscilloscope-style audio visualizer: import up to four stems, draw their waveforms in real time, style them and export a video.<br><sub>Good for: Oscilloscope waveforms · Music visualization · Also in: Music Visualization</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="plotter"></a>

### Plotter & Line Art

<img src="assets/styles/plotter.png" alt="Plotter & Line Art sample" width="240" align="right">

> Single lines, hatching and line art drawn by a pen plotter

**Picks:** [vpype](https://github.com/abey79/vpype) · [vsketch](https://github.com/abey79/vsketch) · [fishdraw](https://github.com/LingDong-/fishdraw) · [p5.plotSvg](https://github.com/golanlevin/p5.plotSvg)

8 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [fishdraw](https://github.com/LingDong-/fishdraw) | 2.6k | ⚪ Dormant | JavaScript | Procedurally generates line drawings of fish, output as single-line SVG that a pen plotter can draw directly.<br><sub>Good for: Line art · Pen plotters · Also in: Generative Art</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [vpype](https://github.com/abey79/vpype) | 986 | 🟢 Active | Python (CLI) | Swiss Army knife for plotter vector graphics: merge, sort, crop, and layer line art before sending it to the plotter.<br><sub>Good for: Plotter line art</sub> |
| [Pintr](https://github.com/javierbyte/pintr) | 843 | 🟢 Active | TypeScript | Turns photos into single-line illustrations drawn in one continuous stroke.<br><sub>Good for: Single-stroke drawing · Also in: Hand-drawn & Whiteboard</sub> |
| [vsketch](https://github.com/abey79/vsketch) | 615 | 🟢 Active | Python | Python generative art environment for pen plotters. Tweak parameters with live preview, export single-line SVG.<br><sub>Good for: Generative art · Pen plotters · Also in: Generative Art</sub> |
| [Krbn](https://github.com/vpalos/Krbn) | 253 | 🟢 Active | TypeScript | Renders 3D scenes as pencil-sketch SVG: exact outlines, hidden lines, hatched shading.<br><sub>Good for: 3D line art · Also in: 3D</sub> |
| [p5.plotSvg](https://github.com/golanlevin/p5.plotSvg) | 220 | 🟢 Active | JavaScript | Exports p5.js work as line-art SVG suited to pen plotters.<br><sub>Good for: Pen plotters · p5.js</sub> |
| [genart](https://github.com/camilleroux/genart-skill) | 180 | 🟢 Active | JavaScript / skill | A generative art plugin for Claude Code: hash-seeded, deterministic pieces that render the same at any resolution, covering Canvas, p5.js, three.js, SVG and pen-plotter export.<br><sub>Good for: Generative art · On-chain art · Also in: Generative Art</sub> |
| [Delaunay Stippler](https://github.com/NHasan143/delaunay-stippler) | 68 | 🟢 Active | JavaScript | Web tool that turns images into stipple art, placing dots with a weighted Voronoi algorithm.<br><sub>Good for: Pointillism · Also in: Geometric & Low-poly</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="dither"></a>

### Dither & 1-bit

<img src="assets/styles/dither.png" alt="Dither & 1-bit sample" width="240" align="right">

> Black-and-white dither dots, with an old Mac and Return of the Obra Dinn feel

**Picks:** [Dither3D](https://github.com/runevision/Dither3D) · [Dithering Shader](https://github.com/niccolofanton/dithering-shader) · [hitherdither](https://github.com/hbldh/hitherdither) · [ditherwave](https://github.com/sahilsaini5/ditherwave)

7 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Dither3D](https://github.com/runevision/Dither3D) | 1.6k | 🟡 Slowing | Unity Shader | Fractal dithering shader that sticks to object surfaces and doesn't flicker when the camera moves. For 1-bit style 3D visuals.<br><sub>Good for: 1-bit 3D · Also in: Shaders & Psychedelic, 3D</sub><br><sub>⚠️ Unity shader; not updated since early 2025.</sub> |
| [Diorama](https://github.com/sloemo01/diorama) | 715 | 🟢 Active | JavaScript (three.js) | A playbook for AI coding agents to build three.js dioramas: tiny people with joint animation, a 64-colour ordered-dither pixel look by default, or stroked toon.<br><sub>Good for: Miniature scene clips · Also in: 3D, Pixel & Retro</sub><br><sub>⚠️ By default mixes commercially licensed 3D assets with hand-built geometry; sources are recorded in the repo.</sub> |
| [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | 298 | 🟢 Active | React / TS | Real-time Bayer dithering post-processing effect for React Three Fiber, turning 3D scenes into a retro dithered look.<br><sub>Good for: 3D post-processing · Also in: 3D, Shaders & Psychedelic</sub> |
| [hitherdither](https://github.com/hbldh/hitherdither) | 260 | 🟢 Active | Python | Python dithering algorithm library with support for arbitrary palettes. For limited-color pixel looks and retro print textures.<br><sub>Good for: Dithering assets · Also in: Pixel & Retro</sub> |
| [Dither Guy](https://github.com/manoelpiovesan/dither-guy) | 254 | 🟢 Active | Python | An open-source alternative to Dither Boy: applies Bayer, Floyd-Steinberg and other dithering to images and video for a low-colour retro display look.<br><sub>Good for: Dithering · Retro look · Also in: Pixel & Retro</sub> |
| [ditherwave](https://github.com/sahilsaini5/ditherwave) | 90 | 🟡 Slowing | React / WebGL2 | WebGL2 dithering component under 8KB: Bayer, halftone, ASCII, and error diffusion.<br><sub>Good for: Web effects · Also in: Shaders & Psychedelic</sub> |
| [gbro Collage Info Animation](https://github.com/pyang5166/gbro-collage-info) | 58 | 🟢 Active | HTML / CSS / GSAP | Skill for halftone paper-collage infographic animations, generated segment by segment from a talking-head script. No image models.<br><sub>Good for: Infographic animation · Also in: Riso & Paper Collage</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="riso"></a>

### Riso & Paper Collage

<img src="assets/styles/riso.png" alt="Riso & Paper Collage sample" width="240" align="right">

> Misregistered risograph colors, halftone dots and paper collage

**Picks:** [p5.riso](https://github.com/antiboredom/p5.riso) · [Animate](https://github.com/cth9191/animate) · [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) · [Riso Window Seat](https://github.com/sevenevesai/riso-windowseat)

6 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Animate](https://github.com/cth9191/animate) | 2.2k | 🟢 Active | JavaScript / Canvas | Claude Code skill: draws short animations procedurally on a single canvas, with 7 built-in styles: paper cut-out, hatched ink, Riso print, sketchbook, math, pixel, and isometric.<br><sub>Good for: Explainer videos · Short films · Also in: Hand-drawn & Whiteboard, Pixel & Retro, Math Explainer</sub> |
| [p5.riso](https://github.com/antiboredom/p5.riso) | 376 | 🟢 Active | JavaScript | Risograph printing library for p5.js: ink color separation, misregistration, and halftone dots for a stencil-print look.<br><sub>Good for: Riso print look · Also in: Generative Art</sub> |
| [Riso Window Seat](https://github.com/sevenevesai/riso-windowseat) | 324 | 🟢 Active | HTML | Procedurally generated Riso print style short films, each a single HTML file, with Claude prompts included.<br><sub>Good for: Riso short films</sub> |
| [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) | 257 | 🟢 Active | TypeScript | Vertical cut-paper style explainer shorts: 9 skills plus Remotion templates, with backgrounds and sound effects included in the repo.<br><sub>Good for: Vertical explainers · Also in: Shorts, Captions & Editing</sub> |
| [gbro Collage Info Animation](https://github.com/pyang5166/gbro-collage-info) | 58 | 🟢 Active | HTML / CSS / GSAP | Skill for halftone paper-collage infographic animations, generated segment by segment from a talking-head script. No image models.<br><sub>Good for: Infographic animation · Also in: Dither & 1-bit</sub> |
| [Chinese-Style Paper Animation](https://github.com/AllenAI2014/remotion-guofeng-starter) | 37 | 🟢 Active | React / Remotion | Asset library and production skill for Chinese-style paper collage animation. Give an AI a poem or idiom and it renders the video entirely in code.<br><sub>Good for: Poetry animation · Also in: Ink & Watercolor</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="alife"></a>

### Artificial Life & Growth

<img src="assets/styles/alife.png" alt="Artificial Life & Growth sample" width="240" align="right">

> Patterns that emerge and grow from simple rules: cellular automata, particle life, space colonization, L-systems

**Picks:** [ALIEN](https://github.com/chrxh/alien) · [Lenia](https://github.com/Chakazul/Lenia) · [Particle Life](https://github.com/hunar4321/particle-life) · [algovivo](https://github.com/juniorrojas/algovivo)

8 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [ALIEN](https://github.com/chrxh/alien) | 5.6k | 🟢 Active | C++ / CUDA | GPU-accelerated artificial life simulation where thousands of particles form evolving organisms.<br><sub>Good for: Artificial life · Also in: Particles & Physics</sub><br><sub>⚠️ Requires an NVIDIA GPU.</sub> |
| [Lenia](https://github.com/Chakazul/Lenia) | 3.9k | ⚪ Dormant | Python / JS | Continuous cellular automata that grow moving, splitting "mathematical life forms", looking like organisms under a microscope.<br><sub>Good for: Artificial life · Also in: Math Explainer</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Particle Life](https://github.com/hunar4321/particle-life) | 3.4k | ⚪ Dormant | JS / C++ / Python | Set attraction and repulsion between a few kinds of particles and cell-like group motion emerges. Very short code.<br><sub>Good for: Artificial life · Also in: Particles & Physics</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [The Nature of Code](https://github.com/nature-of-code/noc-book-2) | 2k | 🟡 Slowing | p5.js | 2024 edition of The Nature of Code: simulate forces, particles, flocking, and cellular automata with p5.js. Essential reading for generative art beginners.<br><sub>Good for: Tutorials · Also in: Generative Art, Particles & Physics</sub> |
| [Particle Life App](https://github.com/tom-mohr/particle-life-app) | 1k | 🟡 Slowing | Java | Particle life simulator with a graphical interface. Tweak the rules and record the emergent behavior.<br><sub>Good for: Artificial life · Also in: Particles & Physics</sub> |
| [algovivo](https://github.com/juniorrojas/algovivo) | 393 | 🟢 Active | JavaScript / WASM | Energy-based soft-bodied virtual creatures that learn to crawl on their own. Runs in the browser.<br><sub>Good for: Soft-body creature animation</sub> |
| [Space Colonization Experiments](https://github.com/jasonwebb/2d-space-colonization-experiments) | 229 | 🟡 Slowing | JavaScript | Growth animation experiments that use the space colonization algorithm to grow tree branches, leaf veins, and coral.<br><sub>Good for: Growth animation · Also in: Generative Art</sub> |
| [L-System Explorer](https://github.com/anvaka/lsystem) | 101 | 🟢 Active | JavaScript / WebGL | L-system explorer in WebGL. A few rules grow plants, snowflakes and fractal curves.<br><sub>Good for: Growth patterns · Also in: Generative Art</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="procgen"></a>

### Procedural Generation

<img src="assets/styles/procgen.png" alt="Procedural Generation sample" width="240" align="right">

> Maps, cities and mazes grown from small samples, where the generating itself is the animation

**Picks:** [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) · [MarkovJunior](https://github.com/mxgmn/MarkovJunior) · [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) · [mapgen4](https://github.com/redblobgames/mapgen4)

13 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | 25.6k | 🟢 Active | C# | Wave Function Collapse algorithm: generates endless variations of pixel images and maps from one small sample. The generation process itself is fun to watch.<br><sub>Good for: Procedural generation · Also in: Pixel & Retro</sub> |
| [MarkovJunior](https://github.com/mxgmn/MarkovJunior) | 8.5k | 🟡 Slowing | C# | From the same author: a procedural generation language that uses rewrite rules to grow mazes, cities, and voxel buildings step by step. Comes with 153 example animations.<br><sub>Good for: Procedural generation · Also in: Pixel & Retro, Isometric & Voxel</sub> |
| [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) | 6.2k | 🟢 Active | JavaScript | Procedurally generates interactive fantasy world maps. Continents, rivers, states and towns are all adjustable.<br><sub>Good for: Fantasy maps · Also in: Map & Route</sub> |
| [WFC Infinite City](https://github.com/marian42/wavefunctioncollapse) | 4.9k | ⚪ Dormant | C# (Unity) | Uses wave function collapse to generate an endless 3D city in real time that you can keep walking through.<br><sub>Good for: Procedural generation · Also in: 3D</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | 3.6k | 🟢 Active | Multiple languages | Cross-language noise function library (C#, C++, GLSL, JS, Rust, and more). Basic material for flow fields, terrain, and textures.<br><sub>Good for: Noise functions · Also in: Generative Art</sub> |
| [webgl-noise](https://github.com/ashima/webgl-noise) | 3k | ⚪ Dormant | GLSL | Classic GLSL procedural noise library. The noise in countless shader works comes from here.<br><sub>Good for: Noise functions · Also in: Shaders & Psychedelic</sub> |
| [Bonsai](https://github.com/scallyw4g/bonsai) | 1.5k | 🟢 Active | C | Procedurally generated voxel engine. Terrain and buildings are grown from code.<br><sub>Good for: Procedural voxels · Also in: Isometric & Voxel, 3D</sub> |
| [NoiseShader](https://github.com/keijiro/NoiseShader) | 1.4k | 🟡 Slowing | Unity HLSL | Keijiro's Unity noise shader library, with simplex noise, Perlin noise and more.<br><sub>Good for: Noise functions · Also in: Shaders & Psychedelic</sub> |
| [TerraForge3D](https://github.com/Jaysmito101/TerraForge3D) | 1.3k | 🟢 Active | C++ | Procedural terrain generation and texturing tool with node-based editing.<br><sub>Good for: Procedural terrain · Also in: 3D</sub><br><sub>⚠️ Mostly a graphical interface.</sub> |
| [mapgen4](https://github.com/redblobgames/mapgen4) | 954 | 🟡 Slowing | TypeScript | Red Blob Games' procedural wilderness map generator, with hand-drawn style contours and rivers.<br><sub>Good for: Procedural maps · Also in: Map & Route</sub> |
| [THREE.Terrain](https://github.com/IceCreamYou/THREE.Terrain) | 926 | 🟢 Active | JavaScript | Procedural terrain generation engine for three.js.<br><sub>Good for: Procedural terrain · Also in: 3D</sub> |
| [Procedural Terrains](https://github.com/ZyFou/ProceduralTerrains) | 701 | 🟢 Active | JavaScript (three.js) | A three.js procedural terrain studio: height and biomes are computed on the GPU for tiles, infinite worlds, planets and dioramas, with water and volumetric clouds.<br><sub>Good for: Terrain · Dioramas · Also in: 3D</sub><br><sub>⚠️ Ships optional Unity and Blender export plugins; the rendering itself is three.js.</sub> |
| [TSL Textures](https://github.com/boytchev/tsl-textures) | 275 | 🟢 Active | three.js / TSL | Procedural textures for three.js's shading language TSL: marble, wood grain, clouds, starfields.<br><sub>Good for: Procedural textures · Also in: Shaders & Psychedelic</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="fractal"></a>

### Fractals & Chaos

<img src="assets/styles/fractal.png" alt="Fractals & Chaos sample" width="240" align="right">

> Endless fractal zooms, chaotic strange attractors and mathematical tilings

**Picks:** [Mandelbulber](https://github.com/buddhi1980/mandelbulber2) · [XaoS](https://github.com/xaos-project/XaoS) · [pywonderland](https://github.com/neozhaoliang/pywonderland) · [Fractal Sound Explorer](https://github.com/HackerPoet/FractalSoundExplorer)

9 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [pywonderland](https://github.com/neozhaoliang/pywonderland) | 4.2k | 🟡 Slowing | Python | Made by a Chinese developer: math visuals in Python, including fractals, tilings, reaction-diffusion, and maze generation animations.<br><sub>Good for: Math art · Also in: Math Explainer</sub> |
| [Fractal Sound Explorer](https://github.com/HackerPoet/FractalSoundExplorer) | 1.3k | ⚪ Dormant | C++ | Click in a fractal and the path turns into sound; visuals and audio evolve together.<br><sub>Good for: Fractals · Audio-visual · Also in: Music Visualization</sub><br><sub>⚠️ Not updated since 2021.</sub> |
| [Mandelbulber](https://github.com/buddhi1980/mandelbulber2) | 1.1k | 🟢 Active | C++ | 3D fractal renderer. Fractals like the Mandelbulb can be keyframed for fly-through animations.<br><sub>Good for: 3D fractal animation · Also in: 3D</sub><br><sub>⚠️ Mainly a graphical app; also supports batch rendering from the command line.</sub> |
| [XaoS](https://github.com/xaos-project/XaoS) | 628 | 🟢 Active | C++ | Real-time interactive fractal zoomer. Can record infinite-zoom fractal animations.<br><sub>Good for: Fractal zoom</sub> |
| [Fractal Garden](https://github.com/trebeljahr/fractal-garden) | 165 | 🟢 Active | TypeScript | 62 fractals in the browser: zoom into the Mandelbrot set, fly through a Menger sponge or write your own L-systems, each with an explainer.<br><sub>Good for: Fractals · Math art · Also in: Math Explainer</sub> |
| [Strange Attractor Renderer](https://github.com/Icelk/strange-attractor-renderer) | 90 | 🟡 Slowing | Rust | Multithreaded strange attractor renderer that draws silky chaotic trajectories.<br><sub>Good for: Chaos art</sub> |
| [Hopalong Attractor](https://github.com/ratwolfzero/hopalong_python) | 42 | 🟢 Active | Python | Density visualization of the Hopalong attractor, drawing nebula-like patterns.<br><sub>Good for: Chaos art</sub> |
| [proof-engine](https://github.com/Mattbusel/proof-engine) | 32 | 🟢 Active | Rust | Rendering engine where every visual is math: glyphs and particles driven by strange attractors.<br><sub>Good for: Math visuals · Also in: ASCII & Terminal</sub> |
| [attractors](https://github.com/vdesmond/attractors) | 23 | 🟡 Slowing | Python | Python package for simulating and visualizing strange attractors, with direct animation export.<br><sub>Good for: Chaos animation</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="iso"></a>

### Isometric & Voxel

<img src="assets/styles/iso.png" alt="Isometric & Voxel sample" width="240" align="right">

> Isometric blocks, voxel terrain and little figures

**Picks:** [Zdog](https://github.com/metafizzy/zdog) · [VoxelSpace](https://github.com/s-macke/VoxelSpace) · [Isomer](https://github.com/jdan/isomer) · [heerich](https://github.com/meodai/heerich)

11 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | ⚪ Dormant | JavaScript | Pseudo-3D flat engine that draws rounded, cute flat-shaded 3D shapes.<br><sub>Good for: Web animation · Also in: Motion Graphics, 3D</sub><br><sub>⚠️ Not updated in years; simple and stable.</sub> |
| [MarkovJunior](https://github.com/mxgmn/MarkovJunior) | 8.5k | 🟡 Slowing | C# | From the same author: a procedural generation language that uses rewrite rules to grow mazes, cities, and voxel buildings step by step. Comes with 153 example animations.<br><sub>Good for: Procedural generation · Also in: Procedural Generation, Pixel & Retro</sub> |
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | 6.8k | ⚪ Dormant | C / JS | Recreates the 90s game Comanche's voxel terrain flight view in under 20 lines of code, with an explanation of how it works.<br><sub>Good for: Retro voxel terrain · Also in: Pixel & Retro, 3D</sub> |
| [hairline](https://github.com/lucasmarkes/hairline) | 4.1k | 🟢 Active | TypeScript | Isometric line figures and objects that turn to follow the mouse. Works with React and plain web pages.<br><sub>Good for: Web motion · Also in: Motion Graphics</sub> |
| [Isomer](https://github.com/jdan/isomer) | 2.9k | ⚪ Dormant | JavaScript | Simple isometric graphics library. Draw isometric blocks and buildings in a few lines of code.<br><sub>Good for: Isometric graphics</sub><br><sub>⚠️ Not updated since 2022.</sub> |
| [obelisk.js](https://github.com/nosir/obelisk.js) | 2.3k | ⚪ Dormant | JavaScript | Builds pixel-style isometric graphics on Canvas, stacking pixel blocks one by one.<br><sub>Good for: Pixel isometric · Also in: Pixel & Retro</sub><br><sub>⚠️ Not updated since 2019.</sub> |
| [Bonsai](https://github.com/scallyw4g/bonsai) | 1.5k | 🟢 Active | C | Procedurally generated voxel engine. Terrain and buildings are grown from code.<br><sub>Good for: Procedural voxels · Also in: Procedural Generation, 3D</sub> |
| [SeeCode](https://github.com/Aryanutkarsh/SeeCode) | 1k | 🟢 Active | JavaScript | Generates explorable animated diagrams from a short JSON spec, so coding agents like Claude can explain code structure.<br><sub>Good for: Code explainer visuals · Also in: Code & Terminal Demo</sub> |
| [heerich](https://github.com/meodai/heerich) | 637 | 🟢 Active | JavaScript | Small engine that renders 3D voxel scenes to SVG. Supports boolean operations and oblique and perspective cameras. No WebGL.<br><sub>Good for: Voxel illustration · Also in: 3D</sub> |
| [iso-figure](https://github.com/MrBongoC/ai-iso-skill) | 373 | 🟢 Active | SVG / skill | A Claude skill: name an object and get one HTML file with a hairline isometric drawing whose parts move, count or play notes when pressed.<br><sub>Good for: Isometric figures · Interactive animation · Also in: Motion Graphics</sub> |
| [isometric](https://github.com/elchininet/isometric) | 247 | 🟢 Active | TypeScript | A lightweight library for isometric projections in SVG: rectangles, circles, paths and text on isometric planes, with SVG animation support.<br><sub>Good for: Isometric art · SVG animation</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="scifi"></a>

### Sci-fi HUD

<img src="assets/styles/scifi.png" alt="Sci-fi HUD sample" width="240" align="right">

> Glowing wireframes, chamfered frames and futuristic interfaces with decoding text

**Picks:** [Arwes](https://github.com/arwes/arwes) · [augmented-ui](https://github.com/propjockey/augmented-ui) · [Cosmic UI](https://github.com/rizznme/cosmic-ui) · [HaloFlux](https://github.com/Ryder191/haloflux)

4 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Arwes](https://github.com/arwes/arwes) | 7.6k | 🟢 Active | TypeScript | Sci-fi web UI framework with futuristic effects: glowing borders, expanding lines, and text decoding.<br><sub>Good for: Sci-fi UI · Also in: Motion Graphics</sub> |
| [augmented-ui](https://github.com/propjockey/augmented-ui) | 1.4k | ⚪ Dormant | CSS | Cyberpunk-style UI borders with cut corners and notches, in pure CSS.<br><sub>Good for: Cyberpunk UI</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [HaloFlux](https://github.com/Ryder191/haloflux) | 830 | 🟢 Active | Canvas | Sci-fi light-ring visualization that pulses to the beat. Pure Canvas in a single HTML file, no dependencies.<br><sub>Good for: Music visualizer · Also in: Music Visualization</sub><br><sub>⚠️ Noncommercial use only.</sub> |
| [Cosmic UI](https://github.com/rizznme/cosmic-ui) | 766 | 🟢 Active | Astro / CSS | Sci-fi themed component collection for building spaceship-console style interfaces.<br><sub>Good for: Sci-fi UI</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="map"></a>

### Map & Route

<img src="assets/styles/map.png" alt="Map & Route sample" width="240" align="right">

> Flight arcs, traced routes, dives toward the globe and travel paths

**Picks:** [AntV L7](https://github.com/antvis/L7) · [deck.gl](https://github.com/visgl/deck.gl) · [MapSCII](https://github.com/rastapasta/mapscii) · [map-motion](https://github.com/SpaceZephyr/map-motion)

10 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.8k | 🟢 Active | TypeScript | Large-scale geospatial data visualization: animated trajectories, 3D column maps, and more.<br><sub>Good for: Map animation · Also in: Data Animation, 3D</sub> |
| [MapSCII](https://github.com/rastapasta/mapscii) | 9.3k | ⚪ Dormant | JavaScript | Renders a world map in the terminal with Braille dots and characters; you can zoom and drag.<br><sub>Good for: Terminal maps · Also in: ASCII & Terminal</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [earth](https://github.com/cambecc/earth) | 6.6k | ⚪ Dormant | JavaScript | Famous global weather animation: wind, ocean currents, and temperature flowing over the globe in real time.<br><sub>Good for: Global wind maps · Also in: Flow & Wind Fields, Data Animation</sub><br><sub>⚠️ Not updated since 2022; the look and the code are still a classic reference.</sub> |
| [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) | 6.2k | 🟢 Active | JavaScript | Procedurally generates interactive fantasy world maps. Continents, rivers, states and towns are all adjustable.<br><sub>Good for: Fantasy maps · Also in: Procedural Generation</sub> |
| [AntV L7](https://github.com/antvis/L7) | 4.1k | 🟢 Active | TypeScript | Large-scale geospatial visualization engine from Ant Group's AntV. Map animations such as flying lines, trajectories, and heatmaps.<br><sub>Good for: Map animation · Also in: Data Animation</sub> |
| [Claude Animation Skills](https://github.com/artemnovitckii/claude-animation-skills) | 1.1k | 🟢 Active | JavaScript | Six Claude skills for short-video animation: 3D cartoon explainers in three.js, stick figures, map routes, exploded-view diagrams and more.<br><sub>Good for: Vertical shorts · Also in: 3D</sub> |
| [webgl-wind](https://github.com/mapbox/webgl-wind) | 1.1k | 🟢 Active | JavaScript / WebGL | Mapbox's WebGL wind particle visualization: hundreds of thousands of particles flow with the wind across a map.<br><sub>Good for: Wind field animation · Also in: Flow & Wind Fields</sub> |
| [mapgen4](https://github.com/redblobgames/mapgen4) | 954 | 🟡 Slowing | TypeScript | Red Blob Games' procedural wilderness map generator, with hand-drawn style contours and rivers.<br><sub>Good for: Procedural maps · Also in: Procedural Generation</sub> |
| [Trail](https://github.com/amalChandran/trail-android) | 517 | 🟢 Active | Kotlin (Android) | Smooth route line drawing animation on Google Maps for Android.<br><sub>Good for: Route animation</sub> |
| [map-motion](https://github.com/SpaceZephyr/map-motion) | 126 | 🟢 Active | Python | Map animation videos from real Amap routes and satellite basemaps, such as earth zoom-ins, travel routes, and hiking elevation.<br><sub>Good for: Map motion videos</sub><br><sub>⚠️ The optional cartoon character calls an image generation API; the built-in figure is drawn in code.</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="demoscene"></a>

### Demoscene

<img src="assets/styles/demoscene.png" alt="Demoscene sample" width="240" align="right">

> Real-time shorts from a few KB of code, sine scrollers and rainbow bars

**Picks:** [TIC-80](https://github.com/nesbox/TIC-80) · [farbrausch Tools](https://github.com/farbrausch/fr_public) · [Shader Minifier](https://github.com/laurentlb/shader-minifier) · [Teach Yourself Demoscene in 14 Days](https://github.com/psenough/teach_yourself_demoscene_in_14_days)

7 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | 🟢 Active | Lua / JS and more | Fantasy console (240x136 pixels, 16 colors), popular for tiny demoscene pieces and live Byte Jam streams.<br><sub>Good for: Pixel animation · Live · Also in: Pixel & Retro, Live Coding & VJ</sub> |
| [farbrausch Tools](https://github.com/farbrausch/fr_public) | 3.8k | ⚪ Dormant | C++ | Tool source code from the legendary demo group farbrausch, 2001-2011, including .werkkzeug, which made their 64KB 3D shorts.<br><sub>Good for: Demoscene · Also in: 3D</sub><br><sub>⚠️ Historical source archive; hard to compile and use.</sub> |
| [Teach Yourself Demoscene in 14 Days](https://github.com/psenough/teach_yourself_demoscene_in_14_days) | 2.3k | ⚪ Dormant | Guide | Two-week beginner's guide to the demoscene: what a demo is, how to start writing one, and where to compete.<br><sub>Good for: Tutorials</sub> |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | 🟡 Slowing | GLSL | Live shader coding tool used in the demoscene Shader Showdown contest. Write code live and see the picture live.<br><sub>Good for: Live performances · Also in: Shaders & Psychedelic, Live Coding & VJ</sub> |
| [frame.js](https://github.com/mrdoob/frame.js) | 1.2k | 🟡 Slowing | JavaScript | JavaScript timeline editor by the author of three.js, for sequencing shots and effects in web demos.<br><sub>Good for: Web demo choreography · Also in: Motion Graphics</sub> |
| [Shader Minifier](https://github.com/laurentlb/shader-minifier) | 587 | 🟢 Active | F# | Shrinks GLSL / HLSL code to the minimum. A must for 4KB and 64KB demos.<br><sub>Good for: Demoscene · Also in: Shaders & Psychedelic</sub> |
| [Open Cubic Player](https://github.com/mywave82/opencubicplayer) | 453 | 🟢 Active | C | Unix version of the classic DOS player. Plays tracker music such as MOD and S3M, with retro visualizations.<br><sub>Good for: Retro music visualizer · Also in: Music Visualization, ASCII & Terminal</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="sand"></a>

### Falling Sand

<img src="assets/styles/sand.png" alt="Falling Sand sample" width="240" align="right">

> Every pixel is a grain of sand or a drop of water, flowing, burning and growing by rules

**Picks:** [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) · [Sandspiel](https://github.com/MaxBittker/sandspiel) · [Sandboxels](https://github.com/R74nCom/sandboxels) · [termsand](https://github.com/cgsdev0/termsand)

8 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) | 5.4k | 🟢 Active | C++ | Classic falling-sand physics sandbox: simulates air pressure, temperature, electricity, and reactions among hundreds of elements.<br><sub>Good for: Particle sandbox · Also in: Particles & Physics</sub><br><sub>⚠️ Mainly a game; good for recording physics reactions.</sub> |
| [Sandspiel](https://github.com/MaxBittker/sandspiel) | 3.2k | 🟢 Active | Rust / WASM | Falling-sand sandbox in the browser: sand, water, fire, and plants interact by cellular automata rules, like flowing pixel art.<br><sub>Good for: Falling sand visuals · Also in: Pixel & Retro</sub> |
| [Sandboxels](https://github.com/R74nCom/sandboxels) | 487 | 🟢 Active | JavaScript | Browser falling-sand simulation with 500+ elements and thousands of reactions. You can write your own elements as mods.<br><sub>Good for: Falling sand visuals · Also in: Pixel & Retro</sub> |
| [termsand](https://github.com/cgsdev0/termsand) | 318 | 🟢 Active | Shell / tmux | Falling sand simulation that runs in tmux. Click with the mouse and sand falls from the top of the terminal.<br><sub>Good for: Terminal animation · Also in: ASCII & Terminal</sub> |
| [Sand Slide](https://github.com/kiwijuice56/sand-slide) | 143 | 🟢 Active | Godot / C++ | Fast falling sand game built with Godot and GDExtension, with many element types.<br><sub>Good for: Falling sand visuals · Also in: Pixel & Retro</sub> |
| [FallingSandEngine](https://github.com/PieKing1215/FallingSandEngine) | 76 | 🟡 Slowing | Rust | Experimental 2D falling sand engine in Rust, where every pixel takes part in physics like in Noita.<br><sub>Good for: Falling sand engines · Also in: Pixel & Retro</sub> |
| [VSand](https://github.com/Ealrann/VSand) | 31 | 🟢 Active | Vulkan / C++ | The classic Falling Sand game rewritten in Vulkan, running large-scale pixel simulation on the GPU.<br><sub>Good for: Falling sand visuals</sub> |
| [TermiSand](https://github.com/BobdaProgrammer/TermiSand) | 22 | 🟡 Slowing | CLI | Falling-sand simulator in your terminal, drawing sand and water with characters.<br><sub>Good for: Terminal animation · Also in: ASCII & Terminal</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="flow"></a>

### Flow & Wind Fields

<img src="assets/styles/flow.png" alt="Flow & Wind Fields sample" width="240" align="right">

> Thousands of particles following a vector field, like silk threads or wind

**Picks:** [earth](https://github.com/cambecc/earth) · [webgl-wind](https://github.com/mapbox/webgl-wind) · [FieldPlay](https://github.com/anvaka/fieldplay) · [flow-fields](https://github.com/romellogoodman/flow-fields)

7 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [earth](https://github.com/cambecc/earth) | 6.6k | ⚪ Dormant | JavaScript | Famous global weather animation: wind, ocean currents, and temperature flowing over the globe in real time.<br><sub>Good for: Global wind maps · Also in: Map & Route, Data Animation</sub><br><sub>⚠️ Not updated since 2022; the look and the code are still a classic reference.</sub> |
| [FieldPlay](https://github.com/anvaka/fieldplay) | 1.3k | 🟢 Active | JavaScript / GLSL | Write a vector field formula and thousands of particles flow along it, like streams of silk.<br><sub>Good for: Vector field animation · Also in: Math Explainer</sub> |
| [webgl-wind](https://github.com/mapbox/webgl-wind) | 1.1k | 🟢 Active | JavaScript / WebGL | Mapbox's WebGL wind particle visualization: hundreds of thousands of particles flow with the wind across a map.<br><sub>Good for: Wind field animation · Also in: Map & Route</sub> |
| [flow-fields](https://github.com/romellogoodman/flow-fields) | 311 | 🟢 Active | JavaScript | JavaScript library for creating flow fields: lines that flow along noise.<br><sub>Good for: Flow field art · Also in: Generative Art</sub> |
| [Cyber Ocean](https://github.com/SahilK-027/Cyber-Ocean) | 82 | 🟢 Active | three.js | 3D flow-field particle ocean built with three.js, with custom post-processing.<br><sub>Good for: 3D particles · Also in: 3D, Particles & Physics</sub> |
| [wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | 68 | 🟢 Active | three.js | Real-time three.js flow-field painter that draws Bezier strokes with a wet, thick-paint look.<br><sub>Good for: Flow field drawing · Also in: Hand-drawn & Whiteboard</sub> |
| [neon](https://github.com/Stanko/neon) | 44 | 🟡 Slowing | JavaScript | Generative art of neon lines made with a 2D vector field.<br><sub>Good for: Generative art · Also in: Generative Art</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="vhs"></a>

### VHS & Analog

<img src="assets/styles/vhs.png" alt="VHS & Analog sample" width="240" align="right">

> Tape color bleed, signal jitter, scanlines and old TV texture

**Picks:** [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) · [NTSC-CRT](https://github.com/LMP88959/NTSC-CRT) · [WebGL CRT Shader](https://github.com/gingerbeardman/webgl-crt-shader) · [ShaderGlass](https://github.com/mausimus/ShaderGlass)

13 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | 26.6k | 🟢 Active | QML / C++ | Terminal that imitates an old CRT monitor: scanlines, glow, screen curvature. Screen recordings come out looking retro.<br><sub>Good for: Retro terminals · Also in: ASCII & Terminal, Pixel & Retro</sub> |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | 🟢 Active | C++ (Windows) | Overlays retro shaders (CRT, pixel, and others) on the Windows desktop; screen-record to get a retro look.<br><sub>Good for: Retro post-processing · Also in: Pixel & Retro, Glitch & Post FX</sub> |
| [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) | 2.7k | 🟢 Active | Rust | Open-source VHS effect: simulates NTSC signal and tape color bleed, jitter, and snow. Works standalone and as an AE, PR, and OFX plugin.<br><sub>Good for: VHS post-processing · Also in: Glitch & Post FX</sub> |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | 🟢 Active | GLSL | RetroArch shader collection: CRT scanlines, pixel upscaling, and other retro display effects.<br><sub>Good for: Retro post-processing · Also in: Pixel & Retro, Shaders & Psychedelic</sub> |
| [ntscqt](https://github.com/JargeZ/ntscqt) | 1.2k | ⚪ Dormant | Python | GUI for a VHS video simulator, giving video an old videotape look.<br><sub>Good for: VHS post-processing · Also in: Glitch & Post FX</sub><br><sub>⚠️ Not updated since 2024; use ntsc-rs for new projects.</sub> |
| [GodotRetro](https://github.com/ahopness/GodotRetro) | 824 | 🟢 Active | Godot Shader | Retro post-processing effects pack for Godot: CRT, VHS, dithering, pixelation.<br><sub>Good for: Retro post-processing · Also in: Shaders & Psychedelic, Pixel & Retro</sub> |
| [NTSCRT](https://github.com/finnmckenty/NTSCRT) | 710 | 🟢 Active | Swift (macOS) | Retro TV / VHS image tool for macOS: ntsc-rs signal emulation plus RetroArch CRT shaders.<br><sub>Good for: Old TV look</sub> |
| [NTSC-CRT](https://github.com/LMP88959/NTSC-CRT) | 578 | 🟢 Active | C | NTSC encoding/decoding simulation using only integer math, able to recreate how old consoles like the NES looked on a TV.<br><sub>Good for: CRT simulation · Also in: Pixel & Retro</sub> |
| [Retro Crisis Shaders](https://github.com/RetroCrisis/Retro-Crisis-GDV-NTSC) | 482 | 🟢 Active | Slang Shader | Collection of CRT shader presets for RetroArch, based on Guest Advanced NTSC. Recreates the look of various old TVs.<br><sub>Good for: CRT post-processing · Also in: Pixel & Retro, Shaders & Psychedelic</sub> |
| [WebGL CRT Shader](https://github.com/gingerbeardman/webgl-crt-shader) | 188 | 🟡 Slowing | WebGL | Adjustable CRT shader for web canvas: scanlines, screen curvature, phosphor ghosting.<br><sub>Good for: CRT post-processing · Also in: Shaders & Psychedelic</sub> |
| [NTSCplayer](https://github.com/ferropop/NTSCplayer) | 142 | 🟢 Active | C++ | Media player that adds an NTSC / VHS look to video in real time during playback.<br><sub>Good for: Retro players</sub> |
| [VhsFx](https://github.com/NullTale/VhsFx) | 90 | 🟡 Slowing | Unity | VHS post-processing effect for Unity URP.<br><sub>Good for: VHS post-processing · Also in: Glitch & Post FX</sub> |
| [VHSEffect](https://github.com/zulubo/VHSEffect) | 33 | 🟡 Slowing | Unity | Realistic VHS post-processing effect for Unity.<br><sub>Good for: VHS post-processing</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="origami"></a>

### Origami & Papercraft

<img src="assets/styles/origami.png" alt="Origami & Papercraft sample" width="240" align="right">

> A sheet of paper folding along its creases, plus paper models and papercraft-style 3D

**Picks:** [Origami Simulator](https://github.com/amandaghassaei/OrigamiSimulator) · [Rabbit Ear](https://github.com/rabbit-ear/rabbit-ear) · [ORIPA](https://github.com/oripa/oripa) · [Papercraft](https://github.com/rodrigorc/papercraft)

8 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Origami Simulator](https://github.com/amandaghassaei/OrigamiSimulator) | 1.4k | 🟢 Active | JavaScript / WebGL | Real-time WebGL origami simulator. Import a crease pattern and watch a sheet of paper fold itself into a crane.<br><sub>Good for: Origami animation · Also in: 3D</sub> |
| [Rabbit Ear](https://github.com/rabbit-ear/rabbit-ear) | 656 | 🟢 Active | JavaScript | Computational origami library: crease patterns, fold simulation, and origami SVG generation.<br><sub>Good for: Origami geometry</sub> |
| [ORIPA](https://github.com/oripa/oripa) | 336 | 🟢 Active | Java | Software for designing origami crease patterns, with a preview of the folded result.<br><sub>Good for: Origami design</sub><br><sub>⚠️ Mostly a graphical interface.</sub> |
| [OriSim3D](https://github.com/RemiKoutcherawy/OriSim3D-Android) | 304 | 🟢 Active | Kotlin (Android) | OpenGL origami folding simulation on Android that can demonstrate folds step by step.<br><sub>Good for: Mobile origami animation · Also in: 3D</sub> |
| [Papercraft](https://github.com/rodrigorc/papercraft) | 291 | 🟢 Active | Rust | Unfolds 3D models into paper models you can print, cut out, and glue together.<br><sub>Good for: Paper model unfolding · Also in: 3D</sub> |
| [Papercraft World](https://github.com/andrewwoan/aimee-xus-papercraft-world) | 201 | 🟢 Active | three.js | Papercraft-style seasonal 3D portfolio site. Useful as a three.js reference for the papercraft style.<br><sub>Good for: Papercraft 3D web · Also in: 3D</sub> |
| [Oriedita](https://github.com/oriedita/oriedita) | 137 | 🟢 Active | Java | Origami crease pattern editor and folding simulator (a fork of Orihime).<br><sub>Good for: Origami design</sub><br><sub>⚠️ Mostly GUI-based.</sub> |
| [kami](https://github.com/maxwase/kami) | 135 | 🟢 Active | Rust | Origami simulator driven by physical hinges.<br><sub>Good for: Origami simulation</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="geo"></a>

### Geometric & Low-poly

<img src="assets/styles/geo.png" alt="Geometric & Low-poly sample" width="240" align="right">

> A picture approximated step by step with triangles, circles and dots, low-poly and pointillist

**Picks:** [primitive](https://github.com/fogleman/primitive) · [Triangula](https://github.com/rh12503/triangula) · [Geometrize](https://github.com/Tw1ddle/geometrize) · [Polyvia](https://github.com/Ovilia/Polyvia)

7 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [primitive](https://github.com/fogleman/primitive) | 13.6k | ⚪ Dormant | Go | Approximates a photo step by step with triangles, ellipses, and other shapes. The process can be exported as an animation.<br><sub>Good for: Geometric reconstruction · Also in: Generative Art</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [Triangula](https://github.com/rh12503/triangula) | 3.9k | 🟡 Slowing | Go | Turns images into high-quality triangle or polygon abstract art.<br><sub>Good for: Low poly</sub> |
| [Geometrize](https://github.com/Tw1ddle/geometrize) | 2.2k | ⚪ Dormant | C++ | Desktop app that turns images into basic geometric shapes. Can export SVG and a step-by-step animation.<br><sub>Good for: Geometric reconstruction</sub><br><sub>⚠️ Not updated since 2022; mainly a graphical app.</sub> |
| [Polyvia](https://github.com/Ovilia/Polyvia) | 1.2k | ⚪ Dormant | JavaScript | Low-poly style image and video processing.<br><sub>Good for: Low poly</sub><br><sub>⚠️ Not updated since 2019.</sub> |
| [triangler](https://github.com/tdh8316/triangler) | 99 | 🟢 Active | Python | Converts images into low-poly art using Delaunay triangulation.<br><sub>Good for: Low poly</sub> |
| [lowpoly](https://github.com/tasercake/lowpoly) | 87 | 🟡 Slowing | Python | Reliable low-poly image generator.<br><sub>Good for: Low poly</sub> |
| [Delaunay Stippler](https://github.com/NHasan143/delaunay-stippler) | 68 | 🟢 Active | JavaScript | Web tool that turns images into stipple art, placing dots with a weighted Voronoi algorithm.<br><sub>Good for: Pointillism · Also in: Plotter & Line Art</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="raytrace"></a>

### Path Tracing

<img src="assets/styles/raytrace.png" alt="Path Tracing sample" width="240" align="right">

> Physically correct light bounces, with soft shadows, caustics and depth of field

**Picks:** [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) · [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) · [GLSL-PathTracer](https://github.com/knightcrawler25/GLSL-PathTracer) · [ToyPathTracer](https://github.com/aras-p/ToyPathTracer)

7 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) | 3k | 🟢 Active | C++ / Python | Research-grade physically based renderer. Build scenes and render frame-by-frame animation with Python scripts.<br><sub>Good for: Realistic rendering · Also in: 3D</sub> |
| [Yocto/GL](https://github.com/xelatihy/yocto-gl) | 2.9k | ⚪ Dormant | C++ | Small C++ libraries for data-driven physically based rendering, common in academia.<br><sub>Good for: Realistic rendering · Also in: 3D</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) | 2.1k | 🟢 Active | JavaScript | GPU path tracing renderer for three.js, giving web 3D scenes realistic lighting, reflections, and depth of field.<br><sub>Good for: Realistic rendering · Also in: 3D</sub> |
| [GLSL-PathTracer](https://github.com/knightcrawler25/GLSL-PathTracer) | 2.1k | ⚪ Dormant | C++ / GLSL | Small GPU physically based path tracer, good for learning and for rendering material showcases.<br><sub>Good for: Realistic rendering · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Not updated since 2024.</sub> |
| [ToyPathTracer](https://github.com/aras-p/ToyPathTracer) | 1.1k | 🟡 Slowing | C++ / C# | Toy path tracer by Aras, a well-known Unity graphics engineer, accompanied by a blog series on optimization.<br><sub>Good for: Tutorials</sub> |
| [mutracer](https://github.com/pissang/mutracer) | 198 | 🟢 Active | TypeScript / WebGPU | WebGPU physically based path tracer, written by one of the ECharts authors.<br><sub>Good for: Realistic rendering · Also in: 3D</sub> |
| [retrace.gl](https://github.com/stasilo/retrace.gl) | 196 | 🟢 Active | JavaScript | Define signed distance field CSG shapes in code, ray trace them, and export the result.<br><sub>Good for: Ray-traced 3D · Also in: Shaders & Psychedelic, 3D</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="space"></a>

### Space & Stars

<img src="assets/styles/space.png" alt="Space & Stars sample" width="240" align="right">

> The solar system, starfields, galaxy arms and black holes

**Picks:** [Stellarium Web](https://github.com/Stellarium/stellarium-web-engine) · [astroterm](https://github.com/da-luce/astroterm) · [Singularity](https://github.com/MisterPrada/singularity) · [Solar Wanderer](https://github.com/hyqzz/Solar-Wanderer)

9 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [astroterm](https://github.com/da-luce/astroterm) | 2.6k | 🟢 Active | C (CLI) | Planetarium in your terminal. Renders stars, planets, and constellations live as characters.<br><sub>Good for: Terminal starfields · Also in: ASCII & Terminal</sub> |
| [Solar Wanderer](https://github.com/hyqzz/Solar-Wanderer) | 777 | 🟢 Active | three.js | A 1:1 real-time solar system in the browser using NASA JPL ephemeris data. Fly to any planet.<br><sub>Good for: Solar system animation · Also in: 3D</sub> |
| [linecast](https://github.com/ashuttl/linecast) | 698 | 🟢 Active | CLI | Weather, tides, sun, moon, and stars in the terminal, in a retro almanac style.<br><sub>Good for: Terminal sky charts · Also in: ASCII & Terminal</sub> |
| [Stellarium Web](https://github.com/Stellarium/stellarium-web-engine) | 667 | 🟢 Active | JavaScript / C | Web engine of the well-known astronomy software Stellarium, rendering a realistic night sky in real time.<br><sub>Good for: Starfields</sub> |
| [Singularity](https://github.com/MisterPrada/singularity) | 319 | 🟡 Slowing | three.js / TSL | Black hole written in TSL, the three.js shading language. Runs on WebGPU and WebGL.<br><sub>Good for: Space effects · Also in: Shaders & Psychedelic</sub> |
| [I, Voyager Planetarium](https://github.com/ivoyager/planetarium) | 162 | 🟢 Active | Godot | Open-source solar system simulation built on Godot.<br><sub>Good for: Solar system · Also in: 3D</sub> |
| [Galaxy Simulation](https://github.com/N0rvel/galaxy_sim) | 162 | 🟢 Active | JavaScript (three.js) | Simulates gravity between thousands of particles with three.js and shaders: a single galaxy, two colliding galaxies or an expanding universe.<br><sub>Good for: Galaxies · Particles · Also in: Particles & Physics</sub> |
| [Black Hole](https://github.com/ibra-kdbra/black-hole) | 113 | 🟢 Active | three.js / GLSL | Black hole and accretion disk made with three.js and GLSL shaders.<br><sub>Good for: Space effects · Also in: Shaders & Psychedelic</sub> |
| [Galaxy Shader](https://github.com/AmitDigga/threejs-galaxy-shader) | 73 | 🟡 Slowing | three.js | High-performance three.js galaxy shader with adjustable colors, spiral arms, and black hole effects.<br><sub>Good for: Galaxy effects · Also in: Shaders & Psychedelic, Particles & Physics</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="liquid"></a>

### Liquid Glass

<img src="assets/styles/liquid.en.png" alt="Liquid Glass sample" width="240" align="right">

> Refracting, color-splitting glass interfaces and liquid metal, in the style of Apple's Liquid Glass

**Picks:** [shuding/liquid-glass](https://github.com/shuding/liquid-glass) · [liquidGL](https://github.com/naughtyduk/liquidGL) · [Liquid Logo](https://github.com/paper-design/liquid-logo) · [Liquid Glass Studio](https://github.com/iyinchao/liquid-glass-studio)

16 projects, sorted by stars.

<br clear="right">

| Project | Stars | Status | Language | Description |
| --- | ---: | :---: | --- | --- |
| [AndroidLiquidGlass](https://github.com/Kyant0/AndroidLiquidGlass) | 4.8k | 🟢 Active | Kotlin (Compose) | Liquid glass effect for Compose Multiplatform. Brings Apple-style glass interfaces to Android.<br><sub>Good for: Liquid glass</sub> |
| [liquid-dom](https://github.com/AndrewPrifer/liquid-dom) | 2.6k | 🟢 Active | TypeScript | Adds a liquid glass effect to web elements.<br><sub>Good for: Liquid glass</sub> |
| [Liquid Glass for RN](https://github.com/callstack/liquid-glass) | 1.7k | 🟢 Active | React Native | Liquid glass component for React Native.<br><sub>Good for: Liquid glass</sub> |
| [Liquid Logo](https://github.com/paper-design/liquid-logo) | 1.5k | 🟡 Slowing | TypeScript | Small tool from the Paper team: turns a logo into a flowing liquid-metal animation.<br><sub>Good for: Logo motion · Also in: Shaders & Psychedelic, Motion Graphics</sub> |
| [Cloudy](https://github.com/skydoves/Cloudy) | 1.3k | 🟢 Active | Kotlin (Compose) | GPU blur and liquid glass effect library for Compose Multiplatform.<br><sub>Good for: Blur · Glass</sub> |
| [shuding/liquid-glass](https://github.com/shuding/liquid-glass) | 1.2k | 🟡 Slowing | SVG / JS | Copy-and-paste liquid glass shader, built with SVG filters.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub> |
| [liquidGL](https://github.com/naughtyduk/liquidGL) | 1.1k | 🟢 Active | WebGL / WebGPU | Liquid glass effect for the web, implemented in WebGL and WebGPU.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub> |
| [Liquid Glass Widgets](https://github.com/sdegenaar/liquid_glass_widgets) | 873 | 🟢 Active | Flutter | Liquid glass UI component library for Flutter.<br><sub>Good for: Liquid glass</sub> |
| [Liquid Glass Studio](https://github.com/iyinchao/liquid-glass-studio) | 850 | 🟢 Active | WebGL2 / WebGPU | By a Chinese developer: recreates Apple's liquid glass interface on the web, with real-time control of refraction, dispersion, and highlights.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub> |
| [orb](https://github.com/LerSent001/orb) | 760 | 🟢 Active | WebGPU | From a Chinese developer: real-time WebGPU liquid glass orb editor, exportable to the web or SwiftUI / Metal.<br><sub>Good for: Liquid glass orbs · Also in: Shaders & Psychedelic</sub> |
| [LiquidGlass](https://github.com/ybouane/liquidglass) | 656 | 🟢 Active | TypeScript / WebGL | A liquid glass effect library for the web: WebGL shaders add refraction, blur, chromatic aberration and lighting to any HTML element.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub> |
| [Glass SDK Liquid Glass](https://github.com/Glass-HQ/liquid-glass) | 549 | 🟢 Active | TypeScript / WebGPU | Liquid glass materials and controls for React, the web and Electron that refract live content with WebGPU, in light and dark appearances.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Requires WebGPU; Safari has known rendering issues.</sub> |
| [ShaderKit](https://github.com/jamesrochabrun/ShaderKit) | 491 | 🟢 Active | Swift / Metal (iOS) | Composable Metal shaders and holographic UI effects for SwiftUI.<br><sub>Good for: App motion · Also in: Shaders & Psychedelic</sub> |
| [liquid_glass_renderer](https://github.com/whynotmake-it/flutter_liquid_glass) | 462 | 🟢 Active | Dart (Flutter) | A Flutter package that renders liquid glass with fragment shaders (refraction, blending and lighting); several Flutter glass widget kits build on it.<br><sub>Good for: Liquid glass · Also in: Shaders & Psychedelic</sub> |
| [Plasma UI](https://github.com/CruxGarden/plasma-ui) | 339 | 🟢 Active | TypeScript (React / WebGL) | Liquid React panels rendered in WebGL: they fuse like droplets when they touch and refract whatever is behind them.<br><sub>Good for: Liquid glass · Interfaces · Also in: Shaders & Psychedelic</sub><br><sub>⚠️ Pre-1.0 and GPU-heavy; does not run well on mobile.</sub> |
| [liquid-glass-android](https://github.com/Mortd3kay/liquid-glass-android) | 186 | 🟡 Slowing | Kotlin (Compose) | Glassmorphism library for Jetpack Compose that uses AGSL shaders for blur, dispersion, and refraction.<br><sub>Good for: Glassmorphism</sub> |

<sub>[↑ Back to the style index](#index)</sub>

<a name="relations"></a>

## Relationships

[![Relationship graph](assets/graph.en.png)](https://syydaniel.github.io/awesome-code-animation/?lang=en#graph-sec)

<sub>Click the image for the [interactive graph](https://syydaniel.github.io/awesome-code-animation/?lang=en#graph-sec). Arrows point from a source to what grew out of it, and dotted lines mean similar, often paired, or same author. You can drag, zoom, switch to the Family tree card view, and click a project to see its full lineage.</sub>

264 relationships. Looking to switch tools? See Alternative. Want more features? See Plugin / extension and Built on.

### Forked from

<sub>Split off from another project and developed separately</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [Manim Community](https://github.com/ManimCommunity/manim) | Forked from | [Manim (3b1b)](https://github.com/3b1b/manim) | Community fork of 3b1b's ManimGL, with fuller docs and a different API |
| [Revideo](https://github.com/midrender/revideo) | Forked from | [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | Drops the editor dependency; built for headless batch rendering |

### Built on

<sub>Built on another project and can't run without it</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | Built on | [three.js](https://github.com/mrdoob/three.js) | Write three.js scenes with React |
| [Vanta.js](https://github.com/tengbao/vanta) | Built on | [three.js](https://github.com/mrdoob/three.js) | Most of the animated backgrounds are drawn with three.js |
| [ShaderGradient](https://github.com/ruucm/shadergradient) | Built on | [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | Renders gradients with React Three Fiber |
| [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | Built on | [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | Used as a post-processing effect in R3F |
| [Generative Design Code Package](https://github.com/generative-design/Code-Package-p5.js) | Built on | [p5.js](https://github.com/processing/p5.js) | Examples from the book Generative Design, written in p5.js |
| [The Nature of Code](https://github.com/nature-of-code/noc-book-2) | Built on | [p5.js](https://github.com/processing/p5.js) | Examples from the new edition of The Nature of Code, written in p5.js |
| [git-sim](https://github.com/initialcommit-com/git-sim) | Built on | [Manim Community](https://github.com/ManimCommunity/manim) | Uses Manim to animate Git operations |
| [roughViz](https://github.com/jwilber/roughViz) | Built on | [Rough.js](https://github.com/rough-stuff/rough) | Hand-drawn lines come from Rough.js |
| [vsketch](https://github.com/abey79/vsketch) | Built on | [vpype](https://github.com/abey79/vpype) | Same author; vsketch output goes straight into vpype for processing |
| [WFC Infinite City](https://github.com/marian42/wavefunctioncollapse) | Built on | [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | Generates 3D cities with the WFC algorithm |
| [bar_chart_race](https://github.com/dexplo/bar_chart_race) | Built on | [Matplotlib](https://github.com/matplotlib/matplotlib) | Draws each frame with Matplotlib |
| [party-mode](https://github.com/preziotte/party-mode) | Built on | [D3](https://github.com/d3/d3) | Draws visualizations with D3 |
| [Mosaic](https://github.com/d3cod3/Mosaic) | Built on | [openFrameworks](https://github.com/openframeworks/openFrameworks) | Built on openFrameworks |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | Built on | [p5.js](https://github.com/processing/p5.js) |  |
| [Poseidon](https://github.com/owenyuwono/poseidon) | Built on | [three.js](https://github.com/mrdoob/three.js) |  |
| [Singularity](https://github.com/MisterPrada/singularity) | Built on | [three.js](https://github.com/mrdoob/three.js) |  |
| [HyperFrames Motion Reel](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | Built on | [HyperFrames](https://github.com/heygen-com/hyperframes) | Uses the official HyperFrames skills to write and render compositions |
| [Glass SDK Liquid Glass](https://github.com/Glass-HQ/liquid-glass) | Built on | [vgpu](https://github.com/vercel-labs/vgpu) | Built with vgpu for WebGPU rendering |
| [Liquid Glass Widgets](https://github.com/sdegenaar/liquid_glass_widgets) | Built on | [liquid_glass_renderer](https://github.com/whynotmake-it/flutter_liquid_glass) | Its shader pipeline is adapted from liquid_glass_renderer |
| [Stroke Order Animator](https://github.com/chill-chinese/stroke-order-animator) | Built on | [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) | Stroke data comes from Make Me a Hanzi |
| [Galaxy Simulation](https://github.com/N0rvel/galaxy_sim) | Built on | [three.js](https://github.com/mrdoob/three.js) | Renders particles with three.js and shaders |
| [Procedural Terrains](https://github.com/ZyFou/ProceduralTerrains) | Built on | [three.js](https://github.com/mrdoob/three.js) | Both the terrain library and studio are built on three.js |

### Plugin / extension

<sub>Adds features to another project</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [three-vrm](https://github.com/pixiv/three-vrm) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Lets three.js load VRM avatars |
| [postprocessing](https://github.com/pmndrs/postprocessing) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Post-processing effects for three.js |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Particle effects for three.js |
| [three-nebula](https://github.com/creativelifeform/three-nebula) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Particle system for three.js |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | Plugin / extension | [Babylon.js](https://github.com/BabylonJS/Babylon.js) | Plays MMD models and motions in Babylon.js |
| [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | Plugin / extension | [PixiJS](https://github.com/pixijs/pixijs) | Displays Live2D models in PixiJS |
| [PixiJS Filters](https://github.com/pixijs/filters) | Plugin / extension | [PixiJS](https://github.com/pixijs/pixijs) | Official community filters for PixiJS |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | Plugin / extension | [p5.js](https://github.com/processing/p5.js) | Adds natural brushes and watercolor to p5.js |
| [p5.riso](https://github.com/antiboredom/p5.riso) | Plugin / extension | [p5.js](https://github.com/processing/p5.js) | Adds Riso-style color-separated printing to p5.js |
| [p5.plotSvg](https://github.com/golanlevin/p5.plotSvg) | Plugin / extension | [p5.js](https://github.com/processing/p5.js) | Exports p5.js sketches as pen plotter SVG |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | Plugin / extension | [Manim Community](https://github.com/ManimCommunity/manim) | Turns Manim animations into slides you can step through |
| [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | Plugin / extension | [Manim Community](https://github.com/ManimCommunity/manim) | Official community voiceover plugin |
| [ManimML](https://github.com/helblazer811/ManimML) | Plugin / extension | [Manim Community](https://github.com/ManimCommunity/manim) | Components for animating machine learning concepts |
| [manim-physics](https://github.com/Matheart/manim-physics) | Plugin / extension | [Manim Community](https://github.com/ManimCommunity/manim) | Physics simulation extension |
| [remocn](https://github.com/Remocn/remocn) | Plugin / extension | [Remotion](https://github.com/remotion-dev/remotion) | Community library of animation and transition components |
| [THREE.Terrain](https://github.com/IceCreamYou/THREE.Terrain) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Procedural terrain for three.js |
| [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Path tracing renderer for three.js |
| [CustomShaderMaterial](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Layers custom shaders onto three.js materials |
| [three-good-godrays](https://github.com/Ameobea/three-good-godrays) | Plugin / extension | [postprocessing](https://github.com/pmndrs/postprocessing) | Used as an effect in postprocessing |
| [TSL Textures](https://github.com/boytchev/tsl-textures) | Plugin / extension | [three.js](https://github.com/mrdoob/three.js) | Textures for TSL, the three.js shading language |
| [glsl-blend](https://github.com/jamieowen/glsl-blend) | Plugin / extension | [glslify](https://github.com/glslify/glslify) | Published in the glslify module format |
| [snapcn](https://github.com/shadcn-labs/snapcn) | Plugin / extension | [Remotion](https://github.com/remotion-dev/remotion) | Remotion components installed with the shadcn CLI |
| [Remotion Bits](https://github.com/av/remotion-bits) | Plugin / extension | [Remotion](https://github.com/remotion-dev/remotion) | Third-party animation components for Remotion |

### Official template / skill

<sub>A template or AI skill from the same team</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [Remotion TikTok Template](https://github.com/remotion-dev/template-tiktok) | Official template / skill | [Remotion](https://github.com/remotion-dev/remotion) | Official template for captioned short videos |
| [Remotion Audiogram Template](https://github.com/remotion-dev/template-audiogram) | Official template / skill | [Remotion](https://github.com/remotion-dev/remotion) | Official podcast audiogram template |
| [Remotion Skills](https://github.com/remotion-dev/skills) | Official template / skill | [Remotion](https://github.com/remotion-dev/remotion) | Official AI coding agent skill |
| [GSAP Skills](https://github.com/greensock/gsap-skills) | Official template / skill | [GSAP](https://github.com/greensock/GSAP) | Official AI skills |

### Renders with

<sub>Uses another project for rendering or low-level work by default</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [Code2Video](https://github.com/showlab/Code2Video) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | An LLM writes Manim code to generate teaching videos |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | An LLM writes Manim code |
| [MathLens](https://github.com/shuyicc/MathLens) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | Math problem explainer videos rendered with Manim |
| [manim-skill](https://github.com/Yusuke710/manim-skill) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | Teaches an AI coding agent to write Manim |
| [Manim Agent Skills](https://github.com/adithya-s-k/manim_skill) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | Teaches an AI coding agent to write Manim |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [weilanx Claude Videos](https://github.com/Azure12355/weilanx-claude-videos) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [cinetic](https://github.com/Leonxlnx/cinetic) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) | Defaults to the Remotion engine; also supports HyperFrames |
| [FredTalk](https://github.com/njrhts2kvv-star/FredTalk) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [RuiC Motion Reel](https://github.com/HRuiCcc/RuiC-motion-reel) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) | Standard promo videos use Remotion templates |
| [Knowledge Explainer](https://github.com/znyupup/knowledge-explainer-skill) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [DeepSeek Opus Motion](https://github.com/8533502-dev/deepseek-opus-motion-skill) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [What If Animation](https://github.com/kelano86/what-if-animation) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) | Also supports Canvas and HTML |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Renders with | [GSAP](https://github.com/greensock/GSAP) | Uses GSAP for animation by default |
| [html-video](https://github.com/nexu-io/html-video) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Also supports Remotion |
| [brag](https://github.com/latent-spaces/brag) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) |  |
| [Creator Style Kit](https://github.com/threeaus/creator-style-kit) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) |  |
| [MotionClone](https://github.com/blixvip/MotionClone) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Rebuilds a reference video as a HyperFrames project |
| [html-anime](https://github.com/blixvip/html-anime) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) |  |
| [Claude Animation Skills](https://github.com/artemnovitckii/claude-animation-skills) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | 2D skills use HyperFrames, 3D uses three.js |
| [motion2code](https://github.com/lovisdotio/motion2code) | Renders with | [GSAP](https://github.com/greensock/GSAP) | The recreated output is SVG plus GSAP code |
| [editly](https://github.com/mifi/editly) | Renders with | [FFmpeg](https://github.com/FFmpeg/FFmpeg) |  |
| [editly](https://github.com/mifi/editly) | Renders with | [GL Transitions](https://github.com/gl-transitions/gl-transitions) | Transition effects come from GL Transitions |
| [MoviePy](https://github.com/Zulko/moviepy) | Renders with | [FFmpeg](https://github.com/FFmpeg/FFmpeg) |  |
| [FFCreator](https://github.com/tnfe/FFCreator) | Renders with | [FFmpeg](https://github.com/FFmpeg/FFmpeg) |  |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | Renders with | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Wraps FFmpeg as a tool AI coding agents can call |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | Renders with | [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | Bundles RetroArch's retro shaders |
| [ff-tracking](https://github.com/mrsarac/ff-tracking) | Renders with | [fframes](https://github.com/dmtrKovalenko/fframes) | Renders with fframes |
| [HyperFrames Motion Director](https://github.com/geekjourneyx/hyperframes-motion-director) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) |  |
| [video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Hands the storyboard script to HyperFrames to render |
| [ReelMimic](https://github.com/edenfunf/reelmimic) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) |  |
| [LiveCanvas](https://github.com/pengchujin/livecanvas) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [Agentic Product Demo](https://github.com/Alexwtlf/agentic-product-demo) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [NTSCRT](https://github.com/finnmckenty/NTSCRT) | Renders with | [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) | Uses ntsc-rs for signal simulation |
| [Chinese-Style Paper Animation](https://github.com/AllenAI2014/remotion-guofeng-starter) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) |  |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | Renders with | [p5.brush](https://github.com/acamposuribe/p5.brush) | Hand-drawn strokes use p5.brush |
| [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) | Renders with | [Remotion](https://github.com/remotion-dev/remotion) | Composes and exports with Remotion; the picture is rendered through @remotion/three |
| [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | The agents write Manim CE code |
| [Fabric](https://github.com/Fabric-Project/Fabric) | Renders with | [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | Includes a Metal port of the Lygia shader library |
| [Patchies](https://github.com/heypoom/patchies) | Renders with | [Hydra](https://github.com/hydra-synth/hydra) | Ships Hydra nodes for video synthesis |
| [Diorama](https://github.com/sloemo01/diorama) | Renders with | [three.js](https://github.com/mrdoob/three.js) | Scenes are built and rendered with three.js |
| [genart](https://github.com/camilleroux/genart-skill) | Renders with | [p5.js](https://github.com/processing/p5.js) | Teaches Claude generative art with p5.js, Canvas, three.js and more |
| [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Renders frame by frame with HyperFrames |
| [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | Renders with | [GSAP](https://github.com/greensock/GSAP) | Motion runs on GSAP timelines |
| [Content Studio (design-agent)](https://github.com/langchain-ai/design-agent) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Builds its video in HyperFrames |
| [code-brand-film](https://github.com/nutllwhy/code-brand-film) | Renders with | [HyperFrames](https://github.com/heygen-com/hyperframes) | Rendered frame by frame with HyperFrames |
| [code-brand-film](https://github.com/nutllwhy/code-brand-film) | Renders with | [GSAP](https://github.com/greensock/GSAP) | A paused GSAP timeline drives the picture |
| [Kalem](https://github.com/leodavincs/kalem) | Renders with | [Paper.js](https://github.com/paperjs/paper.js) | Paper.js draws the self-drawing line and sketch scenes |
| [Kalem](https://github.com/leodavincs/kalem) | Renders with | [Manim Community](https://github.com/ManimCommunity/manim) | One of the engines it can pick |
| [Kalem](https://github.com/leodavincs/kalem) | Renders with | [three.js](https://github.com/mrdoob/three.js) | One of the engines it can pick |

### Data source

<sub>Uses data from another project</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [Hanzi Writer](https://github.com/chanind/hanzi-writer) | Data source | [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) | Stroke data comes from Make Me a Hanzi |

### Alternative

<sub>Does similar work, so one can replace the other</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [tsParticles](https://github.com/tsparticles/tsparticles) | Alternative | [particles.js](https://github.com/VincentGarreau/particles.js) | tsParticles reads particles.js configs, so it works as a drop-in replacement |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | Alternative | [three.js](https://github.com/mrdoob/three.js) | Web 3D engine with more features and built-in editing tools |
| [PlayCanvas](https://github.com/playcanvas/engine) | Alternative | [three.js](https://github.com/mrdoob/three.js) | Web 3D engine, geared toward games and Gaussian splatting |
| [Konva](https://github.com/konvajs/konva) | Alternative | [PixiJS](https://github.com/pixijs/pixijs) | Both render 2D Canvas; Konva favors interactive editing, PixiJS favors performance |
| [Two.js](https://github.com/jonobr1/two.js) | Alternative | [Paper.js](https://github.com/paperjs/paper.js) | Both are 2D vector drawing APIs |
| [DOjS](https://github.com/SuperIlu/DOjS) | Alternative | [p5.js](https://github.com/processing/p5.js) | API modeled on p5.js, but runs on MS-DOS |
| [canvas-sketch](https://github.com/mattdesl/canvas-sketch) | Alternative | [Fragment](https://github.com/raphaelameaume/fragment) | Both are workflow tools for generative art |
| [nannou](https://github.com/nannou-org/nannou) | Alternative | [openFrameworks](https://github.com/openframeworks/openFrameworks) | Creative coding frameworks: the Rust one and the C++ one |
| [Cinder](https://github.com/cinder/Cinder) | Alternative | [openFrameworks](https://github.com/openframeworks/openFrameworks) | Both are C++ creative coding frameworks |
| [OPENRNDR](https://github.com/openrndr/openrndr) | Alternative | [openFrameworks](https://github.com/openframeworks/openFrameworks) | Creative coding framework in Kotlin |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | Alternative | [Manim Community](https://github.com/ManimCommunity/manim) | Both suit explainer animation; Motion Canvas uses TypeScript and has a timeline editor |
| [Mafs](https://github.com/stevenpetryk/mafs) | Alternative | [MathBox](https://github.com/unconed/mathbox) | Both do web math visualization; Mafs leans 2D interactive, MathBox leans 3D |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Alternative | [Remotion](https://github.com/remotion-dev/remotion) | Both render web pages to video; HyperFrames uses HTML/CSS, Remotion uses React |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | Alternative | [Remotion](https://github.com/remotion-dev/remotion) | Both write video in TypeScript |
| [fframes](https://github.com/dmtrKovalenko/fframes) | Alternative | [Remotion](https://github.com/remotion-dev/remotion) | Both write video in code; fframes uses Rust and SVG, built for speed |
| [anime.js](https://github.com/juliangarnier/anime) | Alternative | [GSAP](https://github.com/greensock/GSAP) | JS animation engine, lighter weight |
| [Motion](https://github.com/motiondivision/motion) | Alternative | [GSAP](https://github.com/greensock/GSAP) | JS and React animation library |
| [react-spring](https://github.com/pmndrs/react-spring) | Alternative | [Motion](https://github.com/motiondivision/motion) | Both are React animation libraries; react-spring centers on spring physics |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | Alternative | [Lottie](https://github.com/airbnb/lottie-web) | Official LottieFiles player with better performance |
| [PAG](https://github.com/Tencent/libpag) | Alternative | [Lottie](https://github.com/airbnb/lottie-web) | Tencent's After Effects animation solution, supporting more AE features |
| [Rive Runtime](https://github.com/rive-app/rive-wasm) | Alternative | [Lottie](https://github.com/airbnb/lottie-web) | Interactive animation format with state machines |
| [MoviePy](https://github.com/Zulko/moviepy) | Alternative | [editly](https://github.com/mifi/editly) | Both edit video in code; MoviePy uses Python, editly uses JSON |
| [Butterchurn](https://github.com/jberg/butterchurn) | Alternative | [projectM](https://github.com/projectM-visualizer/projectm) | Both read MilkDrop presets; Butterchurn runs in the browser |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | Alternative | [projectM](https://github.com/projectM-visualizer/projectm) | Continuation of the original MilkDrop |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | Alternative | [ShaderGlass](https://github.com/mausimus/ShaderGlass) | Both can produce a CRT monitor look |
| [Hydra](https://github.com/hydra-synth/hydra) | Alternative | [cables](https://github.com/cables-gl/cables) | Both do real-time visuals; Hydra is code, cables is node patching |
| [TiXL](https://github.com/tixl3d/tixl) | Alternative | [cables](https://github.com/cables-gl/cables) | Node-based real-time motion graphics; TiXL is desktop-oriented |
| [Dither3D](https://github.com/runevision/Dither3D) | Alternative | [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | Both do 3D dithering; Dither3D is for Unity, the other for R3F |
| [chart.xkcd](https://github.com/timqian/chart.xkcd) | Alternative | [roughViz](https://github.com/jwilber/roughViz) | Both are hand-drawn style chart libraries |
| [Tegaki](https://github.com/gkurt/tegaki) | Alternative | [Hanzi Writer](https://github.com/chanind/hanzi-writer) | Both are writing animation tools; Tegaki supports any font |
| [osci-render](https://github.com/jameshball/osci-render) | Alternative | [scope-tui](https://github.com/alemidev/scope-tui) | Both relate to oscilloscope visuals; osci-render draws them, scope-tui views them |
| [Particle Life App](https://github.com/tom-mohr/particle-life-app) | Alternative | [Particle Life](https://github.com/hunar4321/particle-life) | Both are particle life; particle-life-app has a graphical interface |
| [ALIEN](https://github.com/chrxh/alien) | Alternative | [Lenia](https://github.com/Chakazul/Lenia) | Both are artificial life simulations |
| [Mandelbulber](https://github.com/buddhi1980/mandelbulber2) | Alternative | [XaoS](https://github.com/xaos-project/XaoS) | Both do fractal animation; Mandelbulber does 3D, XaoS does 2D zoom |
| [Zdog](https://github.com/metafizzy/zdog) | Alternative | [Isomer](https://github.com/jdan/isomer) | Both are lightweight pseudo-3D graphics libraries |
| [obelisk.js](https://github.com/nosir/obelisk.js) | Alternative | [Isomer](https://github.com/jdan/isomer) | Both draw isometric graphics; obelisk.js leans pixel art |
| [Arwes](https://github.com/arwes/arwes) | Alternative | [Cosmic UI](https://github.com/rizznme/cosmic-ui) | Both are sci-fi style UI components |
| [augmented-ui](https://github.com/propjockey/augmented-ui) | Alternative | [Arwes](https://github.com/arwes/arwes) | Cyberpunk borders in pure CSS |
| [AntV L7](https://github.com/antvis/L7) | Alternative | [deck.gl](https://github.com/visgl/deck.gl) | Both do large-scale map visualization and trajectory animation |
| [AntV G2](https://github.com/antvis/G2) | Alternative | [Apache ECharts](https://github.com/apache/echarts) | Two chart libraries widely used in China |
| [Vizzu](https://github.com/vizzuhq/vizzu-lib) | Alternative | [bar_chart_race](https://github.com/dexplo/bar_chart_race) | Both do data animation; Vizzu excels at morphing transitions between charts |
| [Pyxel](https://github.com/kitao/pyxel) | Alternative | [TIC-80](https://github.com/nesbox/TIC-80) | Both are retro game engines or fantasy consoles |
| [WASM-4](https://github.com/aduros/wasm4) | Alternative | [TIC-80](https://github.com/nesbox/TIC-80) | Both are fantasy consoles |
| [LÖVE](https://github.com/love2d/love) | Alternative | [raylib](https://github.com/raysan5/raylib) | Both are lightweight 2D/3D programming libraries; LÖVE uses Lua, raylib uses C |
| [Proton](https://github.com/drawcall/Proton) | Alternative | [tsParticles](https://github.com/tsparticles/tsparticles) | Both are web particle libraries |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | Alternative | [three-nebula](https://github.com/creativelifeform/three-nebula) | Both are three.js particle systems |
| [VHS](https://github.com/charmbracelet/vhs) | Alternative | [asciinema](https://github.com/asciinema/asciinema) | Both make terminal demos; VHS records from a script, asciinema records real sessions |
| [Terminalizer](https://github.com/faressoft/terminalizer) | Alternative | [asciinema](https://github.com/asciinema/asciinema) | Records the terminal and renders it to GIF |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | Alternative | [asciimatics](https://github.com/peterbrittain/asciimatics) | Both are Python terminal animation libraries |
| [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | Alternative | [Chafa](https://github.com/hpjansson/chafa) | Both convert images to terminal text art |
| [Slidev](https://github.com/slidevjs/slidev) | Alternative | [reveal.js](https://github.com/hakimel/reveal.js) | Both write presentations in code; Slidev uses Markdown and Vue |
| [Animotion](https://github.com/animotionjs/animotion) | Alternative | [Slidev](https://github.com/slidevjs/slidev) | Animated presentations written in Svelte |
| [EffectCraft](https://github.com/storytold/effectcraft) | Alternative | [Natron](https://github.com/NatronGitHub/Natron) | Both are open-source compositing software |
| [Animate](https://github.com/cth9191/animate) | Alternative | [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | Both are toolkits that have Claude write code in a chosen style to make videos |
| [Claude Drawing Skill](https://github.com/cloveric/claude-drawing-skill) | Alternative | [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | Both are multi-style code drawing skills |
| [reanimate](https://github.com/NiazMorshed2007/reanimate) | Alternative | [motion2code](https://github.com/lovisdotio/motion2code) | Both recreate existing animations frame by frame in code |
| [MotionClone](https://github.com/blixvip/MotionClone) | Alternative | [reanimate](https://github.com/NiazMorshed2007/reanimate) | Both recreate reference videos |
| [ranim](https://github.com/AzurIce/ranim) | Alternative | [Manim Community](https://github.com/ManimCommunity/manim) | Rust animation engine inspired by Manim |
| [animCJK](https://github.com/parsimonhi/animCJK) | Alternative | [Hanzi Writer](https://github.com/chanind/hanzi-writer) | Both are Chinese character stroke order animation; animCJK provides SVG animation directly |
| [heerich](https://github.com/meodai/heerich) | Alternative | [Isomer](https://github.com/jdan/isomer) | Both draw isometric or voxel graphics; heerich outputs SVG |
| [mapgen4](https://github.com/redblobgames/mapgen4) | Alternative | [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) | Both are procedural map generators |
| [demoit](https://github.com/dgageot/demoit) | Alternative | [doitlive](https://github.com/sloria/doitlive) | Both are used for live code demos |
| [doitlive](https://github.com/sloria/doitlive) | Alternative | [VHS](https://github.com/charmbracelet/vhs) | Both record terminal demos; doitlive types live, VHS records from a script |
| [timg](https://github.com/hzeller/timg) | Alternative | [video-to-ascii](https://github.com/joelibaceta/video-to-ascii) | Both play video in the terminal |
| [Realtime PyAudio FFT](https://github.com/aiXander/Realtime_PyAudio_FFT) | Alternative | [Meyda](https://github.com/meyda/meyda) | Both extract audio features; one in Python, one in JavaScript |
| [ManimCat](https://github.com/Wing900/ManimCat) | Alternative | [Generative Manim](https://github.com/marcelo-earth/generative-manim) | Both have AI write Manim animations from a single sentence |
| [Shader Editor](https://github.com/markusfisch/ShaderEditor) | Alternative | [Shader Toy for VS Code](https://github.com/stevensona/shader-toy) | Both preview GLSL live; one on Android phones, one in VS Code |
| [Sandboxels](https://github.com/R74nCom/sandboxels) | Alternative | [Sandspiel](https://github.com/MaxBittker/sandspiel) | Both are web falling sand sandboxes |
| [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) | Alternative | [Sandspiel](https://github.com/MaxBittker/sandspiel) | Veteran falling sand game, with more complex elements and physics |
| [TermiSand](https://github.com/BobdaProgrammer/TermiSand) | Alternative | [termsand](https://github.com/cgsdev0/termsand) | Both are falling sand simulations in the terminal |
| [webgl-wind](https://github.com/mapbox/webgl-wind) | Alternative | [earth](https://github.com/cambecc/earth) | Both do wind field particle animation |
| [ntscqt](https://github.com/JargeZ/ntscqt) | Alternative | [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) | Both do VHS effects; ntsc-rs is updated more often |
| [Retro Crisis Shaders](https://github.com/RetroCrisis/Retro-Crisis-GDV-NTSC) | Alternative | [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | Both are retro shaders for RetroArch |
| [VhsFx](https://github.com/NullTale/VhsFx) | Alternative | [VHSEffect](https://github.com/zulubo/VHSEffect) | Both are VHS post-processing for Unity |
| [Oriedita](https://github.com/oriedita/oriedita) | Alternative | [ORIPA](https://github.com/oripa/oripa) | Both are crease pattern editors |
| [OriSim3D](https://github.com/RemiKoutcherawy/OriSim3D-Android) | Alternative | [Origami Simulator](https://github.com/amandaghassaei/OrigamiSimulator) | Both simulate origami folding; OriSim3D runs on Android |
| [Geometrize](https://github.com/Tw1ddle/geometrize) | Alternative | [primitive](https://github.com/fogleman/primitive) | Geometrize is a port of the primitive approach |
| [Triangula](https://github.com/rh12503/triangula) | Alternative | [primitive](https://github.com/fogleman/primitive) | Both rebuild images from geometric shapes |
| [triangler](https://github.com/tdh8316/triangler) | Alternative | [Triangula](https://github.com/rh12503/triangula) | Both convert images to low poly |
| [mutracer](https://github.com/pissang/mutracer) | Alternative | [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) | Both do path tracing in the browser |
| [GLSL-PathTracer](https://github.com/knightcrawler25/GLSL-PathTracer) | Alternative | [ToyPathTracer](https://github.com/aras-p/ToyPathTracer) | Both are path tracers for learning |
| [Strange Attractor Renderer](https://github.com/Icelk/strange-attractor-renderer) | Alternative | [attractors](https://github.com/vdesmond/attractors) | Both draw strange attractors |
| [P(doom) MV (mexicat version)](https://github.com/mexicat/pdoom-video) | Alternative | [P(doom) MV](https://github.com/JohnHeibel/PDoomVideo) | Same song, two authors each making an MV in code |
| [Stellarium Web](https://github.com/Stellarium/stellarium-web-engine) | Alternative | [Solar Wanderer](https://github.com/hyqzz/Solar-Wanderer) | Both render celestial bodies in the browser |
| [linecast](https://github.com/ashuttl/linecast) | Alternative | [astroterm](https://github.com/da-luce/astroterm) | Both draw starfields in the terminal |
| [AquaInkGL](https://github.com/WishMelz/AquaInkGL) | Alternative | [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) | Both are procedural ink wash in the browser |
| [NoiseShader](https://github.com/keijiro/NoiseShader) | Alternative | [webgl-noise](https://github.com/ashima/webgl-noise) | Both are noise shader functions; NoiseShader is for Unity |
| [webgl-noise](https://github.com/ashima/webgl-noise) | Alternative | [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | Both provide shader noise functions; LYGIA covers more |
| [Poiyomi Toon Shader](https://github.com/poiyomi/PoiyomiToonShader) | Alternative | [UnityChan Toon Shader](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) | Both are Unity toon shaders |
| [Unity Toon Shader](https://github.com/Unity-Technologies/com.unity.toonshader) | Alternative | [UnityChan Toon Shader](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) | Both are Japanese-style toon shaders for Unity |
| [URP_Toon](https://github.com/ChiliMilk/URP_Toon) | Alternative | [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample) | Both are Unity URP toon shaders |
| [LiliumToonGraph](https://github.com/you-ri/LiliumToonGraph) | Alternative | [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample) | Both are Unity URP toon shaders |
| [godot-vrm](https://github.com/V-Sekai/godot-vrm) | Alternative | [three-vrm](https://github.com/pixiv/three-vrm) | Same VRM format; one for Godot, one for three.js |
| [Inferno](https://github.com/twostraws/Inferno) | Alternative | [SwiftUI Shaders](https://github.com/krispuckett/SwiftUIShaders) | Both are Metal shader collections for SwiftUI |
| [ShaderKit](https://github.com/jamesrochabrun/ShaderKit) | Alternative | [Inferno](https://github.com/twostraws/Inferno) | Both add Metal shader effects to SwiftUI |
| [AGSL Shader Playground](https://github.com/mejdi14/Android-AGSL-Shader-Playground) | Alternative | [Shader Editor](https://github.com/markusfisch/ShaderEditor) | Both run shaders on Android |
| [Shader Lab](https://github.com/basementstudio/shader-lab) | Alternative | [Paper Shaders](https://github.com/paper-design/shaders) | Both are web shader effect toolkits |
| [Universal Transition Shader](https://github.com/cashew-olddew/Universal-Transition-Shader) | Alternative | [GL Transitions](https://github.com/gl-transitions/gl-transitions) | Both are shader transition collections; one is for Godot |
| [GodotRetro](https://github.com/ahopness/GodotRetro) | Alternative | [Ultimate Retro Shaders](https://github.com/Zorochase/ultimate-retro-shader-collection) | Both are retro shaders for Godot |
| [Godot Ocean FFT](https://github.com/tessarakkt/godot4-oceanfft) | Alternative | [Poseidon](https://github.com/owenyuwono/poseidon) | Both use FFT for real-time ocean |
| [ShaderMan](https://github.com/smkplus/ShaderMan) | Alternative | [Shader Toy for VS Code](https://github.com/stevensona/shader-toy) | Both revolve around Shadertoy-style shaders |
| [Liquid Glass for RN](https://github.com/callstack/liquid-glass) | Alternative | [liquid-dom](https://github.com/AndrewPrifer/liquid-dom) | Both are liquid glass effects; one for React Native, one for the web |
| [liquidGL](https://github.com/naughtyduk/liquidGL) | Alternative | [Liquid Glass Studio](https://github.com/iyinchao/liquid-glass-studio) | Both do liquid glass on the web |
| [shuding/liquid-glass](https://github.com/shuding/liquid-glass) | Alternative | [liquid-dom](https://github.com/AndrewPrifer/liquid-dom) | Both are web liquid glass |
| [AndroidLiquidGlass](https://github.com/Kyant0/AndroidLiquidGlass) | Alternative | [Cloudy](https://github.com/skydoves/Cloudy) | Both are glass effects for Compose |
| [liquid-glass-android](https://github.com/Mortd3kay/liquid-glass-android) | Alternative | [AndroidLiquidGlass](https://github.com/Kyant0/AndroidLiquidGlass) | Both are Android liquid glass |
| [WebGL CRT Shader](https://github.com/gingerbeardman/webgl-crt-shader) | Alternative | [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | Both produce a CRT monitor look |
| [Shader School](https://github.com/stackgl/shader-school) | Alternative | [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | Both are beginner shader tutorials |
| [Raymarching Workshop](https://github.com/electricsquare/raymarching-workshop) | Alternative | [Bauble](https://github.com/ianthehenry/bauble) | Both revolve around SDF ray marching |
| [ManimGX](https://github.com/academa-labs/manimgx) | Alternative | [Manim Community](https://github.com/ManimCommunity/manim) | Keeps the Manim CE API on a Rust and wgpu core |
| [manim-web](https://github.com/maloyan/manim-web) | Alternative | [Manim (3b1b)](https://github.com/3b1b/manim) | A TypeScript port of Manim that needs no Python |
| [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | Alternative | [Code Animation Style Prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | Also collects prompts for code-rendered videos |
| [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) | Alternative | [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | A smaller Chinese collection with writing tips |
| [Infinite](https://github.com/n1m21n/Infinite) | Alternative | [TiXL](https://github.com/tixl3d/tixl) | Another node-based real-time audiovisual tool |
| [Oscillody](https://github.com/Akosmo/Oscillody) | Alternative | [osci-render](https://github.com/jameshball/osci-render) | Also makes oscilloscope-style audio visuals |
| [Fractal Garden](https://github.com/trebeljahr/fractal-garden) | Alternative | [XaoS](https://github.com/xaos-project/XaoS) | Also zooms fractals in real time, in the browser |
| [react-native-effects](https://github.com/blazejkustra/react-native-effects) | Alternative | [React Native Skia](https://github.com/wcandillon/react-native-skia) | Also shader effects in React Native, here with WebGPU |

### Often paired

<sub>Often used together</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [Theatre.js](https://github.com/theatre-js/theatre) | Often paired | [three.js](https://github.com/mrdoob/three.js) | Visual timeline and camera animation for three.js scenes |
| [Code Hike](https://github.com/code-hike/codehike) | Often paired | [Remotion](https://github.com/remotion-dev/remotion) | Code explainer components that can render to video in Remotion |
| [Lottie Skill](https://github.com/diffusionstudio/lottie) | Often paired | [Lottie](https://github.com/airbnb/lottie-web) | Has AI write Lottie files, then plays them with Lottie |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | Often paired | [TIC-80](https://github.com/nesbox/TIC-80) | Two tools commonly used in Demoscene live coding competitions |
| [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) | Often paired | [Rough.js](https://github.com/rough-stuff/rough) | Excalidraw's hand-drawn lines are drawn by Rough.js |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | Often paired | [three-vrm](https://github.com/pixiv/three-vrm) | Drives VRM characters with camera motion tracking |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | Often paired | [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | Drives Live2D characters with camera motion tracking |
| [Code Animation Style Prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | Often paired | [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | Style prompt library, usable with the style toolkit |
| [Shader Minifier](https://github.com/laurentlb/shader-minifier) | Often paired | [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | Common tool for Demoscene shaders |
| [FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | Often paired | [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | Both are foundational tools for procedural generation |

### Same author

<sub>By the same person or team</sub>

| Project | Relation | Project | Note |
| --- | :---: | --- | --- |
| [frame.js](https://github.com/mrdoob/frame.js) | Same author | [three.js](https://github.com/mrdoob/three.js) | Timeline editor written by mrdoob, the three.js author |
| [p5.js](https://github.com/processing/p5.js) | Same author | [Processing](https://github.com/processing/processing4) | Both maintained by the Processing Foundation; p5.js is the web version |
| [VAP](https://github.com/Tencent/vap) | Same author | [PAG](https://github.com/Tencent/libpag) | Both are animation effect tools open-sourced by Tencent |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | Same author | [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | Made by the LottieFiles team |
| [Lottie Skill](https://github.com/diffusionstudio/lottie) | Same author | [Diffusion Studio Core](https://github.com/diffusionstudio/core) | Made by the Diffusion Studio team |
| [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | Same author | [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | Patricio Gonzalez Vivo's shader toolchain |
| [glslCanvas](https://github.com/patriciogonzalezvivo/glslCanvas) | Same author | [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | The web examples in The Book of Shaders run on glslCanvas |
| [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | Same author | [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | Same author |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | Same author | [Rough.js](https://github.com/rough-stuff/rough) | Hand-drawn annotation library by the Rough.js author |
| [fishdraw](https://github.com/LingDong-/fishdraw) | Same author | [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) | Procedural drawing work by LingDong |
| [MarkovJunior](https://github.com/mxgmn/MarkovJunior) | Same author | [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | Two procedural generation projects by the same author |
| [AntV L7](https://github.com/antvis/L7) | Same author | [AntV G2](https://github.com/antvis/G2) | Made by Ant Group's AntV team |
| [Logstalgia](https://github.com/acaudwell/Logstalgia) | Same author | [Gource](https://github.com/acaudwell/Gource) | Same author |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | Same author | [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | The shotcraft series: promo videos, talking-head, explainers, style sample clips |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | Same author | [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) |  |
| [MG Styles 15](https://github.com/Vincentwei1021/mg-styles-15) | Same author | [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) |  |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | Same author | [huashu-motion](https://github.com/alchaincyf/huashu-motion) | Huashu's animation skill series |
| [motion-web](https://github.com/feitangyuan/motion-web) | Same author | [onetake](https://github.com/feitangyuan/onetake) | Same author |
| [Athenaion](https://github.com/Leonxlnx/athenaion) | Same author | [cinetic](https://github.com/Leonxlnx/cinetic) | Same author |
| [MotionClone](https://github.com/blixvip/MotionClone) | Same author | [html-anime](https://github.com/blixvip/html-anime) | Same author |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | Same author | [React Bits](https://github.com/DavidHDev/react-bits) | WebGL effect components by the author of React Bits |
| [audioMotion Player](https://github.com/hvianna/audioMotion.js) | Same author | [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | Same author: a player and a spectrum analyzer library |
| [Kinetograph](https://github.com/0xS4N4TG/kinetograph) | Same author | [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) | Same author |
| [L-System Explorer](https://github.com/anvaka/lsystem) | Same author | [FieldPlay](https://github.com/anvaka/fieldplay) | Same author, anvaka |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | Same author | [P(doom) MV](https://github.com/JohnHeibel/PDoomVideo) | Same author |
| [glslEditor](https://github.com/patriciogonzalezvivo/glslEditor) | Same author | [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | Same author |
| [GLSL Sandbox](https://github.com/mrdoob/glsl-sandbox) | Same author | [three.js](https://github.com/mrdoob/three.js) | Shader gallery by mrdoob, the three.js author |
| [Liquid Logo](https://github.com/paper-design/liquid-logo) | Same author | [Paper Shaders](https://github.com/paper-design/shaders) | Made by the Paper team |
| [LUMEN](https://github.com/Leonxlnx/lumenshaders) | Same author | [cinetic](https://github.com/Leonxlnx/cinetic) | Same author |
| [lemo-wake](https://github.com/lemomo-ai/lemo-wake) | Same author | [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | Same author; both have Claude make films in code |

<a name="all"></a>

## All projects

<details>
<summary>Show all 485 projects, sorted by stars</summary>

| Project | Stars | Styles | Status |
| --- | ---: | --- | :---: |
| [three.js](https://github.com/mrdoob/three.js) | 119k | [3D](#3d), [Particles & Physics](#particle), [Shaders & Psychedelic](#shader) | 🟢 |
| [D3](https://github.com/d3/d3) | 114k | [Data Animation](#data) | 🟢 |
| [Manim (3b1b)](https://github.com/3b1b/manim) | 96.8k | [Math Explainer](#math), [Data Animation](#data) | 🟢 |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | 88.6k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type), [Shorts, Captions & Editing](#short) | 🟢 |
| [Remotion](https://github.com/remotion-dev/remotion) | 75.1k | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type), [3D](#3d) | 🟢 |
| [anime.js](https://github.com/juliangarnier/anime) | 75k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [reveal.js](https://github.com/hakimel/reveal.js) | 72.6k | [Code & Terminal Demo](#code), [Motion Graphics](#mg) | 🟢 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 68.1k | [Shorts, Captions & Editing](#short), [Glitch & Post FX](#glitch) | 🟢 |
| [Apache ECharts](https://github.com/apache/echarts) | 67.8k | [Data Animation](#data) | 🟢 |
| [React Bits](https://github.com/DavidHDev/react-bits) | 52.5k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type), [Shaders & Psychedelic](#shader) | 🟢 |
| [Slidev](https://github.com/slidevjs/slidev) | 49.6k | [Code & Terminal Demo](#code) | 🟢 |
| [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) | 49.6k | [Code & Terminal Demo](#code), [Data Animation](#data) | ⚪ |
| [PixiJS](https://github.com/pixijs/pixijs) | 48.9k | [Motion Graphics](#mg), [Particles & Physics](#particle), [Generative Art](#gen) | 🟢 |
| [Manim Community](https://github.com/ManimCommunity/manim) | 42.8k | [Math Explainer](#math), [Data Animation](#data), [Code & Terminal Demo](#code) | 🟢 |
| [raylib](https://github.com/raysan5/raylib) | 35.8k | [Pixel & Retro](#pixel), [3D](#3d), [Generative Art](#gen) | 🟢 |
| [Motion](https://github.com/motiondivision/motion) | 35.5k | [Motion Graphics](#mg) | 🟢 |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | 33.9k | [3D](#3d) | 🟢 |
| [Lottie](https://github.com/airbnb/lottie-web) | 32.6k | [Motion Graphics](#mg) | 🟡 |
| [GSAP](https://github.com/greensock/GSAP) | 31.1k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [particles.js](https://github.com/VincentGarreau/particles.js) | 30.2k | [Particles & Physics](#particle) | ⚪ |
| [react-spring](https://github.com/pmndrs/react-spring) | 29.3k | [Motion Graphics](#mg) | 🟢 |
| [Taichi](https://github.com/taichi-dev/taichi) | 28.5k | [Particles & Physics](#particle), [3D](#3d) | 🟢 |
| [Graphite](https://github.com/GraphiteEditor/Graphite) | 28k | [Generative Art](#gen), [Motion Graphics](#mg) | 🟢 |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term) | 26.6k | [ASCII & Terminal](#ascii), [Pixel & Retro](#pixel), [VHS & Analog](#vhs) | 🟢 |
| [Babylon.js](https://github.com/BabylonJS/Babylon.js) | 26.4k | [3D](#3d) | 🟢 |
| [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | 25.6k | [Procedural Generation](#procgen), [Pixel & Retro](#pixel) | 🟢 |
| [p5.js](https://github.com/processing/p5.js) | 24.4k | [Generative Art](#gen), [Particles & Physics](#particle), [Music Visualization](#audio) | 🟢 |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | 23.5k | [Data Animation](#data) | 🟢 |
| [Magic UI](https://github.com/magicuidesign/magicui) | 23.5k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [brag](https://github.com/latent-spaces/brag) | 22.3k | [Motion Graphics](#mg) | 🟢 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 22.2k | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short) | 🟢 |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 21.8k | [3D](#3d) | 🟢 |
| [Rough.js](https://github.com/rough-stuff/rough) | 21.4k | [Hand-drawn & Whiteboard](#hand) | ⚪ |
| [VHS](https://github.com/charmbracelet/vhs) | 21.4k | [Code & Terminal Demo](#code), [ASCII & Terminal](#ascii) | 🟢 |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 20.2k | [Motion Graphics](#mg), [Code & Terminal Demo](#code), [Math Explainer](#math) | 🟢 |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 20.1k | [Motion Graphics](#mg), [Hand-drawn & Whiteboard](#hand), [Pixel & Retro](#pixel) | 🟢 |
| [3D Game Shaders for Beginners](https://github.com/lettier/3d-game-shaders-for-beginners) | 20.1k | [Shaders & Psychedelic](#shader), [3D](#3d) | ⚪ |
| [GSAP Skills](https://github.com/greensock/gsap-skills) | 18.9k | [Motion Graphics](#mg) | 🟢 |
| [mo.js](https://github.com/mojs/mojs) | 18.9k | [Motion Graphics](#mg) | 🟢 |
| [Plotly](https://github.com/plotly/plotly.py) | 18.9k | [Data Animation](#data) | 🟢 |
| [Matter.js](https://github.com/liabru/matter-js) | 18.7k | [Particles & Physics](#particle) | 🟢 |
| [Pyxel](https://github.com/kitao/pyxel) | 18.7k | [Pixel & Retro](#pixel) | 🟢 |
| [asciinema](https://github.com/asciinema/asciinema) | 18k | [Code & Terminal Demo](#code), [ASCII & Terminal](#ascii) | 🟢 |
| [PlayCanvas](https://github.com/playcanvas/engine) | 17.4k | [3D](#3d) | 🟢 |
| [WebGL Fluid](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) | 16.9k | [Particles & Physics](#particle), [Shaders & Psychedelic](#shader) | ⚪ |
| [Typed.js](https://github.com/mattboldt/typed.js) | 16.3k | [Kinetic Type & Lyrics](#type) | 🟡 |
| [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 16.3k | [Motion Graphics](#mg), [3D](#3d), [Generative Art](#gen) | 🟢 |
| [Terminalizer](https://github.com/faressoft/terminalizer) | 16.2k | [Code & Terminal Demo](#code), [ASCII & Terminal](#ascii) | ⚪ |
| [Vivus](https://github.com/maxwellito/vivus) | 15.5k | [Hand-drawn & Whiteboard](#hand) | ⚪ |
| [Paper.js](https://github.com/paperjs/paper.js) | 15.2k | [Generative Art](#gen), [Motion Graphics](#mg) | 🟢 |
| [MoviePy](https://github.com/Zulko/moviepy) | 15.2k | [Shorts, Captions & Editing](#short) | 🟢 |
| [Konva](https://github.com/konvajs/konva) | 15k | [Motion Graphics](#mg) | 🟢 |
| [deck.gl](https://github.com/visgl/deck.gl) | 14.8k | [Data Animation](#data), [3D](#3d), [Map & Route](#map) | 🟢 |
| [primitive](https://github.com/fogleman/primitive) | 13.6k | [Geometric & Low-poly](#geo), [Generative Art](#gen) | ⚪ |
| [Gource](https://github.com/acaudwell/Gource) | 13.2k | [Data Animation](#data), [Code & Terminal Demo](#code) | 🟡 |
| [Theatre.js](https://github.com/theatre-js/theatre) | 13.1k | [Motion Graphics](#mg), [3D](#3d) | ⚪ |
| [canvas-confetti](https://github.com/catdad/canvas-confetti) | 12.9k | [Particles & Physics](#particle) | 🟡 |
| [AntV G2](https://github.com/antvis/G2) | 12.7k | [Data Animation](#data) | 🟢 |
| [SVG.js](https://github.com/svgdotjs/svg.js) | 12k | [Motion Graphics](#mg) | 🟢 |
| [Zdog](https://github.com/metafizzy/zdog) | 10.7k | [Motion Graphics](#mg), [3D](#3d), [Isometric & Voxel](#iso) | ⚪ |
| [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js) | 10.5k | [Music Visualization](#audio) | 🟢 |
| [openFrameworks](https://github.com/openframeworks/openFrameworks) | 10.5k | [Generative Art](#gen), [Music Visualization](#audio), [3D](#3d) | 🟢 |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 10k | [Shorts, Captions & Editing](#short) | 🟢 |
| [Rough Notation](https://github.com/rough-stuff/rough-notation) | 9.8k | [Hand-drawn & Whiteboard](#hand), [Kinetic Type & Lyrics](#type) | ⚪ |
| [MapSCII](https://github.com/rastapasta/mapscii) | 9.3k | [Map & Route](#map), [ASCII & Terminal](#ascii) | ⚪ |
| [EffectCraft](https://github.com/storytold/effectcraft) | 9.2k | [Motion Graphics](#mg), [Glitch & Post FX](#glitch) | 🟢 |
| [tsParticles](https://github.com/tsparticles/tsparticles) | 9.1k | [Particles & Physics](#particle) | 🟢 |
| [LÖVE](https://github.com/love2d/love) | 9k | [Pixel & Retro](#pixel) | 🟢 |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 8.8k | [Pixel & Retro](#pixel) | 🟢 |
| [React Native Skia](https://github.com/wcandillon/react-native-skia) | 8.8k | [Motion Graphics](#mg), [Shaders & Psychedelic](#shader) | 🟢 |
| [Two.js](https://github.com/jonobr1/two.js) | 8.8k | [Motion Graphics](#mg), [Generative Art](#gen) | 🟢 |
| [MarkovJunior](https://github.com/mxgmn/MarkovJunior) | 8.5k | [Procedural Generation](#procgen), [Pixel & Retro](#pixel), [Isometric & Voxel](#iso) | 🟡 |
| [chart.xkcd](https://github.com/timqian/chart.xkcd) | 7.9k | [Hand-drawn & Whiteboard](#hand), [Data Animation](#data) | 🟢 |
| [URP Toon Shader Example](https://github.com/ColinLeung-NiloCat/UnityURPToonLitShaderExample) | 7.9k | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | 🟢 |
| [Remotion Skills](https://github.com/remotion-dev/skills) | 7.8k | [Motion Graphics](#mg) | 🟢 |
| [Arwes](https://github.com/arwes/arwes) | 7.6k | [Sci-fi HUD](#scifi), [Motion Graphics](#mg) | 🟢 |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 7.5k | [Hand-drawn & Whiteboard](#hand), [Ink & Watercolor](#ink) | 🟢 |
| [ThreeUI](https://github.com/MengTo/threeui) | 7.4k | [3D](#3d) | 🟢 |
| [Vanta.js](https://github.com/tengbao/vanta) | 7.4k | [3D](#3d), [Generative Art](#gen) | ⚪ |
| [roughViz](https://github.com/jwilber/roughViz) | 7.2k | [Hand-drawn & Whiteboard](#hand), [Data Animation](#data) | ⚪ |
| [The Book of Shaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | 7.1k | [Shaders & Psychedelic](#shader) | 🟡 |
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | 6.8k | [Isometric & Voxel](#iso), [Pixel & Retro](#pixel), [3D](#3d) | ⚪ |
| [nannou](https://github.com/nannou-org/nannou) | 6.8k | [Generative Art](#gen), [Music Visualization](#audio) | 🟢 |
| [earth](https://github.com/cambecc/earth) | 6.6k | [Flow & Wind Fields](#flow), [Map & Route](#map), [Data Animation](#data) | ⚪ |
| [CAVA](https://github.com/karlstav/cava) | 6.5k | [Music Visualization](#audio), [ASCII & Terminal](#ascii) | 🟢 |
| [Shan-Shui-Inf](https://github.com/LingDong-/shan-shui-inf) | 6.5k | [Ink & Watercolor](#ink), [Generative Art](#gen) | ⚪ |
| [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) | 6.2k | [Procedural Generation](#procgen), [Map & Route](#map) | 🟢 |
| [TIC-80](https://github.com/nesbox/TIC-80) | 6.2k | [Pixel & Retro](#pixel), [Live Coding & VJ](#live), [Demoscene](#demoscene) | 🟢 |
| [Unity Shader Essentials (book source)](https://github.com/candycat1992/Unity_Shaders_Book) | 6.1k | [Shaders & Psychedelic](#shader), [3D](#3d) | ⚪ |
| [css-doodle](https://github.com/css-doodle/css-doodle) | 6.1k | [Generative Art](#gen) | 🟢 |
| [Shaders](https://github.com/shader-effects-inc/shaders) | 6k | [Shaders & Psychedelic](#shader) | 🟢 |
| [Galacean Engine](https://github.com/galacean/engine) | 5.9k | [3D](#3d), [Particles & Physics](#particle) | 🟢 |
| [PAG](https://github.com/Tencent/libpag) | 5.8k | [Motion Graphics](#mg) | 🟢 |
| [Lottie Skill](https://github.com/diffusionstudio/lottie) | 5.8k | [Motion Graphics](#mg) | 🟢 |
| [Natron](https://github.com/NatronGitHub/Natron) | 5.8k | [Glitch & Post FX](#glitch) | 🟢 |
| [Kalidokit](https://github.com/yeemachine/kalidokit) | 5.7k | [Anime, MMD & VRM](#anime) | 🟡 |
| [editly](https://github.com/mifi/editly) | 5.6k | [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type) | 🟡 |
| [ALIEN](https://github.com/chrxh/alien) | 5.6k | [Artificial Life & Growth](#alife), [Particles & Physics](#particle) | 🟢 |
| [Cinder](https://github.com/cinder/Cinder) | 5.5k | [Generative Art](#gen), [3D](#3d) | 🟡 |
| [Canvas UI](https://github.com/DavidHDev/canvas-ui) | 5.5k | [Shaders & Psychedelic](#shader), [Particles & Physics](#particle) | 🟢 |
| [Chafa](https://github.com/hpjansson/chafa) | 5.4k | [ASCII & Terminal](#ascii) | 🟢 |
| [The Powder Toy](https://github.com/The-Powder-Toy/The-Powder-Toy) | 5.4k | [Falling Sand](#sand), [Particles & Physics](#particle) | 🟢 |
| [Code Hike](https://github.com/code-hike/codehike) | 5.4k | [Code & Terminal Demo](#code) | 🟡 |
| [Pts](https://github.com/williamngan/pts) | 5.4k | [Generative Art](#gen), [Data Animation](#data) | 🟢 |
| [glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) | 5.4k | [Shaders & Psychedelic](#shader) | 🟢 |
| [canvas-sketch](https://github.com/mattdesl/canvas-sketch) | 5.3k | [Generative Art](#gen) | 🟢 |
| [CMatrix](https://github.com/abishekvashok/cmatrix) | 5.3k | [ASCII & Terminal](#ascii) | ⚪ |
| [Orillusion](https://github.com/Orillusion/orillusion) | 5.2k | [3D](#3d), [Shaders & Psychedelic](#shader) | 🟢 |
| [TiXL](https://github.com/tixl3d/tixl) | 5.2k | [Live Coding & VJ](#live), [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [Hanzi Writer](https://github.com/chanind/hanzi-writer) | 5.1k | [Handwriting & Strokes](#hanzi), [Kinetic Type & Lyrics](#type) | 🟡 |
| [html-video](https://github.com/nexu-io/html-video) | 4.9k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [WFC Infinite City](https://github.com/marian42/wavefunctioncollapse) | 4.9k | [Procedural Generation](#procgen), [3D](#3d) | ⚪ |
| [SHADERed](https://github.com/dfranx/SHADERed) | 4.8k | [Shaders & Psychedelic](#shader) | ⚪ |
| [AndroidLiquidGlass](https://github.com/Kyant0/AndroidLiquidGlass) | 4.8k | [Liquid Glass](#liquid) | 🟢 |
| [Tweakpane](https://github.com/cocopon/tweakpane) | 4.8k | [Generative Art](#gen) | 🟡 |
| [git-sim](https://github.com/initialcommit-com/git-sim) | 4.7k | [Code & Terminal Demo](#code), [Data Animation](#data) | 🟢 |
| [Claude Animated Shorts](https://github.com/mromidev/claude-animated-shorts) | 4.6k | [3D](#3d), [Shorts, Captions & Editing](#short) | 🟢 |
| [projectM](https://github.com/projectM-visualizer/projectm) | 4.6k | [Music Visualization](#audio), [Shaders & Psychedelic](#shader) | 🟢 |
| [Shader School](https://github.com/stackgl/shader-school) | 4.4k | [Shaders & Psychedelic](#shader) | ⚪ |
| [ShaderGlass](https://github.com/mausimus/ShaderGlass) | 4.4k | [Pixel & Retro](#pixel), [Glitch & Post FX](#glitch), [VHS & Analog](#vhs) | 🟢 |
| [onetake](https://github.com/feitangyuan/onetake) | 4.4k | [Motion Graphics](#mg) | 🟢 |
| [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) | 4.3k | [ASCII & Terminal](#ascii), [Kinetic Type & Lyrics](#type) | 🟢 |
| [asciimatics](https://github.com/peterbrittain/asciimatics) | 4.3k | [ASCII & Terminal](#ascii) | 🟢 |
| [Godot Shaders](https://github.com/gdquest-demos/godot-shaders) | 4.2k | [Shaders & Psychedelic](#shader), [3D](#3d), [Pixel & Retro](#pixel) | 🟢 |
| [pywonderland](https://github.com/neozhaoliang/pywonderland) | 4.2k | [Fractals & Chaos](#fractal), [Math Explainer](#math) | 🟡 |
| [Revideo](https://github.com/midrender/revideo) | 4.2k | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short) | 🟢 |
| [VAP](https://github.com/Tencent/vap) | 4.2k | [Motion Graphics](#mg) | 🟢 |
| [UnityChan Toon Shader](https://github.com/unity3d-jp/UnityChanToonShaderVer2_Project) | 4.1k | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | ⚪ |
| [AntV L7](https://github.com/antvis/L7) | 4.1k | [Map & Route](#map), [Data Animation](#data) | 🟢 |
| [hairline](https://github.com/lucasmarkes/hairline) | 4.1k | [Isometric & Voxel](#iso), [Motion Graphics](#mg) | 🟢 |
| [Paper Shaders](https://github.com/paper-design/shaders) | 4k | [Shaders & Psychedelic](#shader) | 🟢 |
| [P(doom) MV (mexicat version)](https://github.com/mexicat/pdoom-video) | 4k | [Kinetic Type & Lyrics](#type), [Motion Graphics](#mg) | 🟢 |
| [Lenia](https://github.com/Chakazul/Lenia) | 3.9k | [Artificial Life & Growth](#alife), [Math Explainer](#math) | ⚪ |
| [Triangula](https://github.com/rh12503/triangula) | 3.9k | [Geometric & Low-poly](#geo) | 🟡 |
| [MG Styles 15](https://github.com/Vincentwei1021/mg-styles-15) | 3.9k | [Motion Graphics](#mg), [3D](#3d), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [farbrausch Tools](https://github.com/farbrausch/fr_public) | 3.8k | [Demoscene](#demoscene), [3D](#3d) | ⚪ |
| [thi.ng/umbrella](https://github.com/thi-ng/umbrella) | 3.8k | [Generative Art](#gen), [Data Animation](#data) | 🟢 |
| [Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) | 3.6k | [Motion Graphics](#mg) | 🟢 |
| [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | 3.6k | [ASCII & Terminal](#ascii) | ⚪ |
| [doitlive](https://github.com/sloria/doitlive) | 3.6k | [Code & Terminal Demo](#code), [ASCII & Terminal](#ascii) | 🟢 |
| [FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | 3.6k | [Procedural Generation](#procgen), [Generative Art](#gen) | 🟢 |
| [anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 3.5k | [Data Animation](#data), [Motion Graphics](#mg) | 🟢 |
| [ManimML](https://github.com/helblazer811/ManimML) | 3.5k | [Math Explainer](#math), [Data Animation](#data) | ⚪ |
| [LYGIA](https://github.com/patriciogonzalezvivo/lygia) | 3.5k | [Shaders & Psychedelic](#shader) | 🟢 |
| [Mafs](https://github.com/stevenpetryk/mafs) | 3.5k | [Math Explainer](#math) | 🟢 |
| [Particle Life](https://github.com/hunar4321/particle-life) | 3.4k | [Artificial Life & Growth](#alife), [Particles & Physics](#particle) | ⚪ |
| [Tegaki](https://github.com/gkurt/tegaki) | 3.3k | [Handwriting & Strokes](#hanzi), [Kinetic Type & Lyrics](#type), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [TypeGPU](https://github.com/software-mansion/TypeGPU) | 3.3k | [Shaders & Psychedelic](#shader) | 🟢 |
| [ShaderGradient](https://github.com/ruucm/shadergradient) | 3.2k | [Shaders & Psychedelic](#shader) | 🟢 |
| [Sandspiel](https://github.com/MaxBittker/sandspiel) | 3.2k | [Falling Sand](#sand), [Pixel & Retro](#pixel) | 🟢 |
| [Claude Animation Base](https://github.com/JohnHeibel/ClaudeAnimationBase) | 3.2k | [Hand-drawn & Whiteboard](#hand), [Anime, MMD & VRM](#anime) | 🟢 |
| [FFCreator](https://github.com/tnfe/FFCreator) | 3.2k | [Shorts, Captions & Editing](#short) | 🟡 |
| [fframes](https://github.com/dmtrKovalenko/fframes) | 3.1k | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short) | 🟢 |
| [Herk Edit Kit](https://github.com/nateherkai/herk-edit-kit) | 3.1k | [Shorts, Captions & Editing](#short) | 🟢 |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 3.1k | [Motion Graphics](#mg), [3D](#3d) | 🟢 |
| [gl-react](https://github.com/gre/gl-react) | 3k | [Shaders & Psychedelic](#shader) | 🟢 |
| [webgl-noise](https://github.com/ashima/webgl-noise) | 3k | [Shaders & Psychedelic](#shader), [Procedural Generation](#procgen) | ⚪ |
| [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) | 3k | [Path Tracing](#raytrace), [3D](#3d) | 🟢 |
| [P(doom) MV](https://github.com/JohnHeibel/PDoomVideo) | 3k | [Kinetic Type & Lyrics](#type), [Motion Graphics](#mg) | 🟢 |
| [postprocessing](https://github.com/pmndrs/postprocessing) | 3k | [Glitch & Post FX](#glitch), [3D](#3d) | 🟢 |
| [Bang Motion](https://github.com/bangtutorial/bang-motion) | 2.9k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Inferno](https://github.com/twostraws/Inferno) | 2.9k | [Shaders & Psychedelic](#shader), [Glitch & Post FX](#glitch) | 🟡 |
| [Yocto/GL](https://github.com/xelatihy/yocto-gl) | 2.9k | [Path Tracing](#raytrace), [3D](#3d) | ⚪ |
| [Isomer](https://github.com/jdan/isomer) | 2.9k | [Isometric & Voxel](#iso) | ⚪ |
| [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) | 2.9k | [Math Explainer](#math), [3D](#3d) | 🟢 |
| [ManimGX](https://github.com/academa-labs/manimgx) | 2.9k | [Math Explainer](#math), [3D](#3d) | 🟢 |
| [timg](https://github.com/hzeller/timg) | 2.8k | [ASCII & Terminal](#ascii), [Pixel & Retro](#pixel) | 🟢 |
| [Hydra](https://github.com/hydra-synth/hydra) | 2.8k | [Live Coding & VJ](#live), [Glitch & Post FX](#glitch), [Shaders & Psychedelic](#shader) | 🟡 |
| [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) | 2.8k | [Handwriting & Strokes](#hanzi) | 🟡 |
| [ntsc-rs](https://github.com/ntsc-rs/ntsc-rs) | 2.7k | [VHS & Analog](#vhs), [Glitch & Post FX](#glitch) | 🟢 |
| [vgpu](https://github.com/vercel-labs/vgpu) | 2.7k | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [Pixel2Motion](https://github.com/nolangz/pixel2motion) | 2.7k | [Motion Graphics](#mg) | 🟢 |
| [glslEditor](https://github.com/patriciogonzalezvivo/glslEditor) | 2.6k | [Shaders & Psychedelic](#shader) | ⚪ |
| [liquid-dom](https://github.com/AndrewPrifer/liquid-dom) | 2.6k | [Liquid Glass](#liquid) | 🟢 |
| [astroterm](https://github.com/da-luce/astroterm) | 2.6k | [ASCII & Terminal](#ascii), [Space & Stars](#space) | 🟢 |
| [fishdraw](https://github.com/LingDong-/fishdraw) | 2.6k | [Plotter & Line Art](#plotter), [Generative Art](#gen) | ⚪ |
| [Proton](https://github.com/drawcall/Proton) | 2.5k | [Particles & Physics](#particle) | 🟡 |
| [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft) | 2.5k | [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type) | 🟢 |
| [zero](https://github.com/sinclairzx81/zero) | 2.5k | [ASCII & Terminal](#ascii), [3D](#3d) | 🟢 |
| [Code2Video](https://github.com/showlab/Code2Video) | 2.4k | [Math Explainer](#math) | 🟢 |
| [reanimate](https://github.com/NiazMorshed2007/reanimate) | 2.3k | [Motion Graphics](#mg) | 🟢 |
| [obelisk.js](https://github.com/nosir/obelisk.js) | 2.3k | [Isometric & Voxel](#iso), [Pixel & Retro](#pixel) | ⚪ |
| [Teach Yourself Demoscene in 14 Days](https://github.com/psenough/teach_yourself_demoscene_in_14_days) | 2.3k | [Demoscene](#demoscene) | ⚪ |
| [three-vrm](https://github.com/pixiv/three-vrm) | 2.3k | [Anime, MMD & VRM](#anime), [3D](#3d) | 🟢 |
| [glslify](https://github.com/glslify/glslify) | 2.3k | [Shaders & Psychedelic](#shader) | ⚪ |
| [glslCanvas](https://github.com/patriciogonzalezvivo/glslCanvas) | 2.3k | [Shaders & Psychedelic](#shader) | ⚪ |
| [GL Transitions](https://github.com/gl-transitions/gl-transitions) | 2.3k | [Shorts, Captions & Editing](#short), [Glitch & Post FX](#glitch) | 🟢 |
| [Animate](https://github.com/cth9191/animate) | 2.2k | [Hand-drawn & Whiteboard](#hand), [Pixel & Retro](#pixel), [Math Explainer](#math), [Riso & Paper Collage](#riso) | 🟢 |
| [AMLL](https://github.com/amll-dev/applemusic-like-lyrics) | 2.2k | [Kinetic Type & Lyrics](#type), [Music Visualization](#audio) | 🟢 |
| [Geometrize](https://github.com/Tw1ddle/geometrize) | 2.2k | [Geometric & Low-poly](#geo) | ⚪ |
| [Excalidraw Animate](https://github.com/dai-shi/excalidraw-animate) | 2.1k | [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [ReelMimic](https://github.com/edenfunf/reelmimic) | 2.1k | [Shorts, Captions & Editing](#short) | 🟢 |
| [ossia score](https://github.com/ossia/score) | 2.1k | [Live Coding & VJ](#live) | 🟢 |
| [motion-skills](https://github.com/iart-ai/motion-skills) | 2.1k | [Motion Graphics](#mg) | 🟢 |
| [three-gpu-pathtracer](https://github.com/gkjohnson/three-gpu-pathtracer) | 2.1k | [Path Tracing](#raytrace), [3D](#3d) | 🟢 |
| [GLSL-PathTracer](https://github.com/knightcrawler25/GLSL-PathTracer) | 2.1k | [Path Tracing](#raytrace), [Shaders & Psychedelic](#shader) | ⚪ |
| [Vizzu](https://github.com/vizzuhq/vizzu-lib) | 2k | [Data Animation](#data) | 🟡 |
| [Astrofox](https://github.com/astrofox-io/astrofox) | 2k | [Music Visualization](#audio), [Motion Graphics](#mg) | 🟢 |
| [Butterchurn](https://github.com/jberg/butterchurn) | 2k | [Music Visualization](#audio), [Shaders & Psychedelic](#shader) | 🟡 |
| [gganimate](https://github.com/thomasp85/gganimate) | 2k | [Data Animation](#data) | 🟡 |
| [The Nature of Code](https://github.com/nature-of-code/noc-book-2) | 2k | [Generative Art](#gen), [Particles & Physics](#particle), [Artificial Life & Growth](#alife) | 🟡 |
| [anidoodle](https://github.com/alexgreensh/anidoodle) | 2k | [Hand-drawn & Whiteboard](#hand), [Generative Art](#gen) | 🟢 |
| [video-to-ascii](https://github.com/joelibaceta/video-to-ascii) | 1.9k | [ASCII & Terminal](#ascii) | 🟡 |
| [Durdraw](https://github.com/durdraw/durdraw) | 1.9k | [ASCII & Terminal](#ascii) | 🟢 |
| [AI Animation Skills](https://github.com/Unclecheng-li/AI_Animation) | 1.8k | [Motion Graphics](#mg), [Data Animation](#data) | 🟢 |
| [remocn](https://github.com/Remocn/remocn) | 1.8k | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short) | 🟢 |
| [Logstalgia](https://github.com/acaudwell/Logstalgia) | 1.8k | [Data Animation](#data) | 🟡 |
| [glitch-this](https://github.com/TotallyNotChase/glitch-this) | 1.8k | [Glitch & Post FX](#glitch) | ⚪ |
| [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1.8k | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Animotion](https://github.com/animotionjs/animotion) | 1.8k | [Code & Terminal Demo](#code), [Motion Graphics](#mg) | 🟢 |
| [Splitting](https://github.com/shshaw/Splitting) | 1.8k | [Kinetic Type & Lyrics](#type) | ⚪ |
| [Liquid Glass for RN](https://github.com/callstack/liquid-glass) | 1.7k | [Liquid Glass](#liquid) | 🟢 |
| [GLSL Sandbox](https://github.com/mrdoob/glsl-sandbox) | 1.7k | [Shaders & Psychedelic](#shader), [Live Coding & VJ](#live) | 🟢 |
| [Poiyomi Toon Shader](https://github.com/poiyomi/PoiyomiToonShader) | 1.7k | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | 🟢 |
| [Meyda](https://github.com/meyda/meyda) | 1.7k | [Music Visualization](#audio) | ⚪ |
| [Dither3D](https://github.com/runevision/Dither3D) | 1.6k | [Dither & 1-bit](#dither), [Shaders & Psychedelic](#shader), [3D](#3d) | 🟡 |
| [Unity Toon Shader](https://github.com/Unity-Technologies/com.unity.toonshader) | 1.6k | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | 🟢 |
| [MilkDrop 3](https://github.com/milkdrop2077/MilkDrop3) | 1.6k | [Music Visualization](#audio), [Shaders & Psychedelic](#shader) | 🟢 |
| [WASM-4](https://github.com/aduros/wasm4) | 1.5k | [Pixel & Retro](#pixel) | 🟢 |
| [pixi-live2d-display](https://github.com/guansss/pixi-live2d-display) | 1.5k | [Anime, MMD & VRM](#anime) | ⚪ |
| [Musializer](https://github.com/tsoding/musializer) | 1.5k | [Music Visualization](#audio) | 🟢 |
| [MathBox](https://github.com/unconed/mathbox) | 1.5k | [Math Explainer](#math), [3D](#3d) | ⚪ |
| [Bonzomatic](https://github.com/Gargaj/Bonzomatic) | 1.5k | [Shaders & Psychedelic](#shader), [Live Coding & VJ](#live), [Demoscene](#demoscene) | 🟡 |
| [Bonsai](https://github.com/scallyw4g/bonsai) | 1.5k | [Procedural Generation](#procgen), [Isometric & Voxel](#iso), [3D](#3d) | 🟢 |
| [Liquid Logo](https://github.com/paper-design/liquid-logo) | 1.5k | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader), [Motion Graphics](#mg) | 🟡 |
| [ShaderMan](https://github.com/smkplus/ShaderMan) | 1.5k | [Shaders & Psychedelic](#shader) | ⚪ |
| [p5.brush](https://github.com/acamposuribe/p5.brush) | 1.5k | [Hand-drawn & Whiteboard](#hand), [Generative Art](#gen) | 🟢 |
| [Motion Graphics Skills](https://github.com/Barty-Bart/motion-graphics) | 1.5k | [Motion Graphics](#mg) | 🟢 |
| [GLSL Primer Cards](https://github.com/wshxbqq/GLSL-Card) | 1.5k | [Shaders & Psychedelic](#shader) | ⚪ |
| [bar_chart_race](https://github.com/dexplo/bar_chart_race) | 1.5k | [Data Animation](#data) | ⚪ |
| [Code Animation Style Prompts](https://github.com/XiaoyeCodes/code-animation-prompts) | 1.4k | [Motion Graphics](#mg) | 🟢 |
| [Reanimate](https://github.com/reanimate/reanimate) | 1.4k | [Math Explainer](#math), [Motion Graphics](#mg) | 🟡 |
| [Origami Simulator](https://github.com/amandaghassaei/OrigamiSimulator) | 1.4k | [Origami & Papercraft](#origami), [3D](#3d) | 🟢 |
| [augmented-ui](https://github.com/propjockey/augmented-ui) | 1.4k | [Sci-fi HUD](#scifi) | ⚪ |
| [NoiseShader](https://github.com/keijiro/NoiseShader) | 1.4k | [Shaders & Psychedelic](#shader), [Procedural Generation](#procgen) | 🟡 |
| [CustomShaderMaterial](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial) | 1.4k | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟡 |
| [cinetic](https://github.com/Leonxlnx/cinetic) | 1.4k | [Motion Graphics](#mg) | 🟢 |
| [Manim Agent Skills](https://github.com/adithya-s-k/manim_skill) | 1.4k | [Math Explainer](#math) | 🟡 |
| [URP_Toon](https://github.com/ChiliMilk/URP_Toon) | 1.4k | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | ⚪ |
| [FieldPlay](https://github.com/anvaka/fieldplay) | 1.3k | [Flow & Wind Fields](#flow), [Math Explainer](#math) | 🟢 |
| [spectral.js](https://github.com/rvanwijnen/spectral.js) | 1.3k | [Hand-drawn & Whiteboard](#hand) | 🟡 |
| [Cloudy](https://github.com/skydoves/Cloudy) | 1.3k | [Liquid Glass](#liquid) | 🟢 |
| [three.quarks](https://github.com/Alchemist0823/three.quarks) | 1.3k | [Particles & Physics](#particle), [3D](#3d) | 🟢 |
| [libretro GLSL Shaders](https://github.com/libretro/glsl-shaders) | 1.3k | [Pixel & Retro](#pixel), [Shaders & Psychedelic](#shader), [VHS & Analog](#vhs) | 🟢 |
| [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) | 1.3k | [Motion Graphics](#mg) | 🟢 |
| [TerraForge3D](https://github.com/Jaysmito101/TerraForge3D) | 1.3k | [Procedural Generation](#procgen), [3D](#3d) | 🟢 |
| [three-nebula](https://github.com/creativelifeform/three-nebula) | 1.3k | [Particles & Physics](#particle), [3D](#3d) | 🟢 |
| [Fractal Sound Explorer](https://github.com/HackerPoet/FractalSoundExplorer) | 1.3k | [Fractals & Chaos](#fractal), [Music Visualization](#audio) | ⚪ |
| [Diffusion Studio Core](https://github.com/diffusionstudio/core) | 1.2k | [Shorts, Captions & Editing](#short) | 🟡 |
| [shuding/liquid-glass](https://github.com/shuding/liquid-glass) | 1.2k | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟡 |
| [Opus 5.5 Video Prompts](https://github.com/joeseesun/opus-video-prompts) | 1.2k | [Motion Graphics](#mg), [Hand-drawn & Whiteboard](#hand), [Shorts, Captions & Editing](#short) | 🟢 |
| [VFX-JS](https://github.com/fand/vfx-js) | 1.2k | [Glitch & Post FX](#glitch), [Kinetic Type & Lyrics](#type) | 🟢 |
| [line-art-animation](https://github.com/JDhruv14/line-art-animation) | 1.2k | [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [frame.js](https://github.com/mrdoob/frame.js) | 1.2k | [Demoscene](#demoscene), [Motion Graphics](#mg) | 🟡 |
| [Kubai Icons](https://github.com/kubai087/kubai-icons) | 1.2k | [Motion Graphics](#mg) | 🟢 |
| [ntscqt](https://github.com/JargeZ/ntscqt) | 1.2k | [VHS & Analog](#vhs), [Glitch & Post FX](#glitch) | ⚪ |
| [Polyvia](https://github.com/Ovilia/Polyvia) | 1.2k | [Geometric & Low-poly](#geo) | ⚪ |
| [PixiJS Filters](https://github.com/pixijs/filters) | 1.2k | [Glitch & Post FX](#glitch), [Shaders & Psychedelic](#shader) | 🟡 |
| [Etro](https://github.com/etro-js/etro) | 1.2k | [Shorts, Captions & Editing](#short) | 🟢 |
| [motion-anything](https://github.com/nexu-io/motion-anything) | 1.1k | [Motion Graphics](#mg), [Shaders & Psychedelic](#shader) | 🟢 |
| [Claude Animation Skills](https://github.com/artemnovitckii/claude-animation-skills) | 1.1k | [3D](#3d), [Map & Route](#map) | 🟢 |
| [glsl-blend](https://github.com/jamieowen/glsl-blend) | 1.1k | [Shaders & Psychedelic](#shader) | ⚪ |
| [ToyPathTracer](https://github.com/aras-p/ToyPathTracer) | 1.1k | [Path Tracing](#raytrace) | 🟡 |
| [webgl-wind](https://github.com/mapbox/webgl-wind) | 1.1k | [Flow & Wind Fields](#flow), [Map & Route](#map) | 🟢 |
| [twigl](https://github.com/doxas/twigl) | 1.1k | [Shaders & Psychedelic](#shader), [Live Coding & VJ](#live) | 🟡 |
| [Shader Editor](https://github.com/markusfisch/ShaderEditor) | 1.1k | [Shaders & Psychedelic](#shader) | 🟢 |
| [liquidGL](https://github.com/naughtyduk/liquidGL) | 1.1k | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [Realtime PyAudio FFT](https://github.com/aiXander/Realtime_PyAudio_FFT) | 1.1k | [Music Visualization](#audio) | 🟢 |
| [Mandelbulber](https://github.com/buddhi1980/mandelbulber2) | 1.1k | [Fractals & Chaos](#fractal), [3D](#3d) | 🟢 |
| [video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | 1.1k | [Shorts, Captions & Editing](#short) | 🟡 |
| [Radiant](https://github.com/pbakaus/radiant) | 1.1k | [Shaders & Psychedelic](#shader), [Generative Art](#gen) | 🟢 |
| [Particle Life App](https://github.com/tom-mohr/particle-life-app) | 1k | [Artificial Life & Growth](#alife), [Particles & Physics](#particle) | 🟡 |
| [adu-motion-video](https://github.com/adunext/adu-motion-video) | 1k | [Shorts, Captions & Editing](#short) | 🟢 |
| [Rive Runtime](https://github.com/rive-app/rive-wasm) | 1k | [Motion Graphics](#mg) | 🟢 |
| [Generative Design Code Package](https://github.com/generative-design/Code-Package-p5.js) | 1k | [Generative Art](#gen) | 🟢 |
| [Raymarching Workshop](https://github.com/electricsquare/raymarching-workshop) | 1k | [Shaders & Psychedelic](#shader), [3D](#3d) | ⚪ |
| [SeeCode](https://github.com/Aryanutkarsh/SeeCode) | 1k | [Code & Terminal Demo](#code), [Isometric & Voxel](#iso) | 🟢 |
| [Manim Slides](https://github.com/jeertmans/manim-slides) | 1k | [Math Explainer](#math), [Code & Terminal Demo](#code) | 🟢 |
| [OPENRNDR](https://github.com/openrndr/openrndr) | 988 | [Generative Art](#gen) | 🟢 |
| [vpype](https://github.com/abey79/vpype) | 986 | [Plotter & Line Art](#plotter) | 🟢 |
| [Godot Realistic Water](https://github.com/godot-extended-libraries/godot-realistic-water) | 985 | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟡 |
| [audioMotion](https://github.com/hvianna/audioMotion-analyzer) | 983 | [Music Visualization](#audio), [Data Animation](#data) | 🟢 |
| [Guizang Product Video](https://github.com/op7418/guizang-product-video-skill) | 968 | [Motion Graphics](#mg) | 🟢 |
| [DOjS](https://github.com/SuperIlu/DOjS) | 965 | [Pixel & Retro](#pixel), [Generative Art](#gen) | 🟡 |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | 957 | [Motion Graphics](#mg) | 🟢 |
| [mapgen4](https://github.com/redblobgames/mapgen4) | 954 | [Procedural Generation](#procgen), [Map & Route](#map) | 🟡 |
| [Fragment](https://github.com/raphaelameaume/fragment) | 951 | [Generative Art](#gen), [Shaders & Psychedelic](#shader) | 🟢 |
| [Generative Manim](https://github.com/marcelo-earth/generative-manim) | 942 | [Math Explainer](#math) | 🟢 |
| [Cinematic Skill](https://github.com/Moh4696/cinematic-skill) | 932 | [Motion Graphics](#mg) | 🟢 |
| [THREE.Terrain](https://github.com/IceCreamYou/THREE.Terrain) | 926 | [Procedural Generation](#procgen), [3D](#3d) | 🟢 |
| [Rossark Motion](https://github.com/rossark0/rossark-motion-skill) | 921 | [Motion Graphics](#mg) | 🟢 |
| [Claude Motion Design](https://github.com/howseen-ai/claude-motion-design) | 887 | [Motion Graphics](#mg) | 🟢 |
| [pixelsort](https://github.com/satyarth/pixelsort) | 876 | [Glitch & Post FX](#glitch) | 🟢 |
| [motion-web](https://github.com/feitangyuan/motion-web) | 875 | [3D](#3d), [Motion Graphics](#mg) | 🟢 |
| [Liquid Glass Widgets](https://github.com/sdegenaar/liquid_glass_widgets) | 873 | [Liquid Glass](#liquid) | 🟢 |
| [Liquid Glass Studio](https://github.com/iyinchao/liquid-glass-studio) | 850 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [genjutsu](https://github.com/AThevon/genjutsu) | 849 | [Generative Art](#gen), [Motion Graphics](#mg) | 🟢 |
| [Pintr](https://github.com/javierbyte/pintr) | 843 | [Plotter & Line Art](#plotter), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [Shader Park](https://github.com/shader-park/shader-park-core) | 833 | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [HaloFlux](https://github.com/Ryder191/haloflux) | 830 | [Sci-fi HUD](#scifi), [Music Visualization](#audio) | 🟢 |
| [GodotRetro](https://github.com/ahopness/GodotRetro) | 824 | [Shaders & Psychedelic](#shader), [Pixel & Retro](#pixel), [VHS & Analog](#vhs) | 🟢 |
| [party-mode](https://github.com/preziotte/party-mode) | 807 | [Music Visualization](#audio), [Data Animation](#data) | 🟢 |
| [Launch Motion Skills](https://github.com/charlie947/motion-graphics-skills) | 786 | [Motion Graphics](#mg) | 🟢 |
| [demoit](https://github.com/dgageot/demoit) | 780 | [Code & Terminal Demo](#code) | 🟢 |
| [Solar Wanderer](https://github.com/hyqzz/Solar-Wanderer) | 777 | [Space & Stars](#space), [3D](#3d) | 🟢 |
| [Cosmic UI](https://github.com/rizznme/cosmic-ui) | 766 | [Sci-fi HUD](#scifi) | 🟢 |
| [scope-tui](https://github.com/alemidev/scope-tui) | 763 | [Oscilloscope & Vector](#scope), [ASCII & Terminal](#ascii), [Music Visualization](#audio) | 🟢 |
| [orb](https://github.com/LerSent001/orb) | 760 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [osci-render](https://github.com/jameshball/osci-render) | 744 | [Oscilloscope & Vector](#scope), [Music Visualization](#audio) | 🟢 |
| [Machine Skill](https://github.com/AirsupHQ/machine-skill) | 738 | [3D](#3d) | 🟢 |
| [Athenaion](https://github.com/Leonxlnx/athenaion) | 733 | [3D](#3d) | 🟢 |
| [Shader Lab](https://github.com/basementstudio/shader-lab) | 728 | [Shaders & Psychedelic](#shader), [Motion Graphics](#mg) | 🟢 |
| [shadplay](https://github.com/alphastrata/shadplay) | 727 | [Shaders & Psychedelic](#shader), [Live Coding & VJ](#live) | 🟢 |
| [Shader Toy for VS Code](https://github.com/stevensona/shader-toy) | 723 | [Shaders & Psychedelic](#shader) | 🟢 |
| [Waveform for OBS](https://github.com/phandasm/waveform) | 722 | [Music Visualization](#audio) | 🟢 |
| [Diorama](https://github.com/sloemo01/diorama) | 715 | [3D](#3d), [Pixel & Retro](#pixel), [Dither & 1-bit](#dither) | 🟢 |
| [NTSCRT](https://github.com/finnmckenty/NTSCRT) | 710 | [VHS & Analog](#vhs) | 🟢 |
| [Procedural Terrains](https://github.com/ZyFou/ProceduralTerrains) | 701 | [Procedural Generation](#procgen), [3D](#3d) | 🟢 |
| [drawsvg](https://github.com/cduck/drawsvg) | 698 | [Motion Graphics](#mg), [Data Animation](#data) | 🟢 |
| [linecast](https://github.com/ashuttl/linecast) | 698 | [Space & Stars](#space), [ASCII & Terminal](#ascii) | 🟢 |
| [MotionClone](https://github.com/blixvip/MotionClone) | 685 | [Motion Graphics](#mg) | 🟢 |
| [Aora Bot](https://github.com/sam70361/aora-bot) | 681 | [Motion Graphics](#mg), [Anime, MMD & VRM](#anime) | 🟢 |
| [snapcn](https://github.com/shadcn-labs/snapcn) | 679 | [Shorts, Captions & Editing](#short), [Motion Graphics](#mg), [Code & Terminal Demo](#code) | 🟢 |
| [Content Studio (design-agent)](https://github.com/langchain-ai/design-agent) | 674 | [Motion Graphics](#mg), [Data Animation](#data) | 🟢 |
| [Stellarium Web](https://github.com/Stellarium/stellarium-web-engine) | 667 | [Space & Stars](#space) | 🟢 |
| [ranim](https://github.com/AzurIce/ranim) | 662 | [Math Explainer](#math) | 🟢 |
| [Rabbit Ear](https://github.com/rabbit-ear/rabbit-ear) | 656 | [Origami & Papercraft](#origami) | 🟢 |
| [LiquidGlass](https://github.com/ybouane/liquidglass) | 656 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [ff-tracking](https://github.com/mrsarac/ff-tracking) | 653 | [Motion Graphics](#mg), [Glitch & Post FX](#glitch) | 🟢 |
| [audioMotion Player](https://github.com/hvianna/audioMotion.js) | 646 | [Music Visualization](#audio) | 🟢 |
| [heerich](https://github.com/meodai/heerich) | 637 | [Isometric & Voxel](#iso), [3D](#3d) | 🟢 |
| [XaoS](https://github.com/xaos-project/XaoS) | 628 | [Fractals & Chaos](#fractal) | 🟢 |
| [vsketch](https://github.com/abey79/vsketch) | 615 | [Plotter & Line Art](#plotter), [Generative Art](#gen) | 🟢 |
| [Godot Ocean FFT](https://github.com/tessarakkt/godot4-oceanfft) | 614 | [Shaders & Psychedelic](#shader), [3D](#3d), [Particles & Physics](#particle) | 🟡 |
| [Fabric](https://github.com/Fabric-Project/Fabric) | 613 | [Live Coding & VJ](#live), [3D](#3d), [Shaders & Psychedelic](#shader) | 🟢 |
| [LiliumToonGraph](https://github.com/you-ri/LiliumToonGraph) | 609 | [Shaders & Psychedelic](#shader), [Anime, MMD & VRM](#anime) | 🟢 |
| [Bauble](https://github.com/ianthehenry/bauble) | 598 | [Shaders & Psychedelic](#shader), [3D](#3d), [Generative Art](#gen) | 🟢 |
| [shader-doodle](https://github.com/mmmerl/shader-doodle) | 590 | [Shaders & Psychedelic](#shader) | 🟢 |
| [Shader Minifier](https://github.com/laurentlb/shader-minifier) | 587 | [Demoscene](#demoscene), [Shaders & Psychedelic](#shader) | 🟢 |
| [world.execute(me) Lyric MV](https://github.com/Nyankomintsu/world-execute-me-lyric-mv) | 586 | [Kinetic Type & Lyrics](#type), [Anime, MMD & VRM](#anime) | 🟢 |
| [Whiteboard Teacher Video](https://github.com/liangdabiao/whiteboard-teacher-video) | 580 | [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [NTSC-CRT](https://github.com/LMP88959/NTSC-CRT) | 578 | [VHS & Analog](#vhs), [Pixel & Retro](#pixel) | 🟢 |
| [cables](https://github.com/cables-gl/cables) | 576 | [Live Coding & VJ](#live), [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [LiveCanvas](https://github.com/pengchujin/livecanvas) | 563 | [Shorts, Captions & Editing](#short) | 🟢 |
| [Opus Video Skills](https://github.com/tuzhechen2005/opus-video-skills) | 559 | [Motion Graphics](#mg), [Music Visualization](#audio) | 🟢 |
| [Processing](https://github.com/processing/processing4) | 550 | [Generative Art](#gen) | 🟢 |
| [Glass SDK Liquid Glass](https://github.com/Glass-HQ/liquid-glass) | 549 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [Shader Skills](https://github.com/gokayfem/shader-skills) | 548 | [Shaders & Psychedelic](#shader) | 🟢 |
| [play.core](https://github.com/ertdfgcvb/play.core) | 546 | [ASCII & Terminal](#ascii), [Generative Art](#gen) | 🟢 |
| [Code Video Showcase](https://github.com/Moessif/code-video-showcase) | 546 | [Motion Graphics](#mg), [3D](#3d) | 🟢 |
| [Kinetograph](https://github.com/0xS4N4TG/kinetograph) | 543 | [Shorts, Captions & Editing](#short), [Motion Graphics](#mg) | 🟢 |
| [Universal Transition Shader](https://github.com/cashew-olddew/Universal-Transition-Shader) | 529 | [Shaders & Psychedelic](#shader), [Shorts, Captions & Editing](#short) | 🟡 |
| [Beam](https://github.com/doodlewind/beam) | 527 | [Shaders & Psychedelic](#shader) | 🟢 |
| [Product Launch Motion](https://github.com/AbubakrChan/product-launch-motion) | 527 | [Motion Graphics](#mg) | 🟢 |
| [Remotion Bits](https://github.com/av/remotion-bits) | 523 | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type), [Particles & Physics](#particle) | 🟢 |
| [video-director](https://github.com/win4r/video-director) | 521 | [Motion Graphics](#mg) | 🟢 |
| [manim-web](https://github.com/maloyan/manim-web) | 520 | [Math Explainer](#math), [Data Animation](#data) | 🟢 |
| [Mosaic](https://github.com/d3cod3/Mosaic) | 519 | [Live Coding & VJ](#live), [Generative Art](#gen) | 🟢 |
| [Trail](https://github.com/amalChandran/trail-android) | 517 | [Map & Route](#map) | 🟢 |
| [ManimCat](https://github.com/Wing900/ManimCat) | 513 | [Math Explainer](#math) | 🟢 |
| [Learn wgpu (Chinese edition)](https://github.com/jinleili/learn-wgpu-zh) | 510 | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [modV](https://github.com/vcync/modV) | 498 | [Music Visualization](#audio), [Live Coding & VJ](#live) | 🟡 |
| [ShaderKit](https://github.com/jamesrochabrun/ShaderKit) | 491 | [Shaders & Psychedelic](#shader), [Liquid Glass](#liquid) | 🟢 |
| [Sandboxels](https://github.com/R74nCom/sandboxels) | 487 | [Falling Sand](#sand), [Pixel & Retro](#pixel) | 🟢 |
| [HyperFrames Motion Director](https://github.com/geekjourneyx/hyperframes-motion-director) | 486 | [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type) | 🟢 |
| [godot-vrm](https://github.com/V-Sekai/godot-vrm) | 486 | [Anime, MMD & VRM](#anime), [3D](#3d) | 🟢 |
| [Retro Crisis Shaders](https://github.com/RetroCrisis/Retro-Crisis-GDV-NTSC) | 482 | [VHS & Analog](#vhs), [Pixel & Retro](#pixel), [Shaders & Psychedelic](#shader) | 🟢 |
| [animCJK](https://github.com/parsimonhi/animCJK) | 482 | [Handwriting & Strokes](#hanzi), [Kinetic Type & Lyrics](#type) | 🟢 |
| [ASCII Magic](https://github.com/kailashsr38/ascii-magic-art) | 480 | [ASCII & Terminal](#ascii) | 🟢 |
| [Svader](https://github.com/sockmaster27/svader) | 464 | [Shaders & Psychedelic](#shader) | 🟢 |
| [liquid_glass_renderer](https://github.com/whynotmake-it/flutter_liquid_glass) | 462 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [DrawBot](https://github.com/typemytype/drawbot) | 456 | [Kinetic Type & Lyrics](#type), [Generative Art](#gen) | 🟢 |
| [Open Cubic Player](https://github.com/mywave82/opencubicplayer) | 453 | [Music Visualization](#audio), [Demoscene](#demoscene), [ASCII & Terminal](#ascii) | 🟢 |
| [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | 430 | [Motion Graphics](#mg), [3D](#3d) | 🟢 |
| [fy-code-animation](https://github.com/Akillll-DuoHe/fy-code-animation) | 429 | [Motion Graphics](#mg) | 🟢 |
| [Agentic Product Demo](https://github.com/Alexwtlf/agentic-product-demo) | 418 | [Shorts, Captions & Editing](#short) | 🟢 |
| [manim-physics](https://github.com/Matheart/manim-physics) | 414 | [Math Explainer](#math), [Particles & Physics](#particle) | 🟢 |
| [FredTalk](https://github.com/njrhts2kvv-star/FredTalk) | 404 | [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Shuimo UI](https://github.com/shuimo-design/shuimo-ui) | 401 | [Ink & Watercolor](#ink) | 🟢 |
| [react-native-effects](https://github.com/blazejkustra/react-native-effects) | 394 | [Shaders & Psychedelic](#shader) | 🟢 |
| [algovivo](https://github.com/juniorrojas/algovivo) | 393 | [Artificial Life & Growth](#alife) | 🟢 |
| [AquaInkGL](https://github.com/WishMelz/AquaInkGL) | 387 | [Ink & Watercolor](#ink), [Shaders & Psychedelic](#shader) | 🟡 |
| [shipvideo](https://github.com/diggerhq/shipvideo) | 386 | [Motion Graphics](#mg) | 🟢 |
| [What If Animation](https://github.com/kelano86/what-if-animation) | 386 | [Motion Graphics](#mg) | 🟢 |
| [lemo-wake](https://github.com/lemomo-ai/lemo-wake) | 379 | [Motion Graphics](#mg), [Shorts, Captions & Editing](#short) | 🟢 |
| [p5.riso](https://github.com/antiboredom/p5.riso) | 376 | [Riso & Paper Collage](#riso), [Generative Art](#gen) | 🟢 |
| [iso-figure](https://github.com/MrBongoC/ai-iso-skill) | 373 | [Isometric & Voxel](#iso), [Motion Graphics](#mg) | 🟢 |
| [Claude Drawing Skill](https://github.com/cloveric/claude-drawing-skill) | 373 | [Ink & Watercolor](#ink), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [LUMEN](https://github.com/Leonxlnx/lumenshaders) | 369 | [Shaders & Psychedelic](#shader), [Generative Art](#gen) | 🟢 |
| [motion2code](https://github.com/lovisdotio/motion2code) | 361 | [Motion Graphics](#mg) | 🟢 |
| [RayTK](https://github.com/t3kt/raytk) | 359 | [Shaders & Psychedelic](#shader), [Live Coding & VJ](#live), [3D](#3d) | 🟡 |
| [Godot VFX Library](https://github.com/haowg/GODOT-VFX-LIBRARY) | 359 | [Particles & Physics](#particle), [Shaders & Psychedelic](#shader) | 🟡 |
| [MathLens](https://github.com/shuyicc/MathLens) | 354 | [Math Explainer](#math) | 🟡 |
| [SwiftUI Shaders](https://github.com/krispuckett/SwiftUIShaders) | 353 | [Shaders & Psychedelic](#shader), [Glitch & Post FX](#glitch) | 🟢 |
| [ShaderMania](https://github.com/markusmoenig/ShaderMania) | 349 | [Shaders & Psychedelic](#shader) | 🟡 |
| [Coldtype](https://github.com/coldtype/coldtype) | 345 | [Kinetic Type & Lyrics](#type), [Generative Art](#gen) | 🟢 |
| [Ultimate Retro Shaders](https://github.com/Zorochase/ultimate-retro-shader-collection) | 344 | [Pixel & Retro](#pixel), [3D](#3d), [Shaders & Psychedelic](#shader) | 🟢 |
| [Infinite](https://github.com/n1m21n/Infinite) | 341 | [Live Coding & VJ](#live), [Music Visualization](#audio), [3D](#3d) | 🟢 |
| [Plasma UI](https://github.com/CruxGarden/plasma-ui) | 339 | [Liquid Glass](#liquid), [Shaders & Psychedelic](#shader) | 🟢 |
| [ORIPA](https://github.com/oripa/oripa) | 336 | [Origami & Papercraft](#origami) | 🟢 |
| [Dashi Style Explainers](https://github.com/chuspeeism/dashi-animationstyle) | 331 | [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | 328 | [Math Explainer](#math) | 🟢 |
| [Poseidon](https://github.com/owenyuwono/poseidon) | 325 | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [Riso Window Seat](https://github.com/sevenevesai/riso-windowseat) | 324 | [Riso & Paper Collage](#riso) | 🟢 |
| [cbirds](https://github.com/clainstone/cbirds) | 320 | [ASCII & Terminal](#ascii), [Particles & Physics](#particle) | 🟢 |
| [Singularity](https://github.com/MisterPrada/singularity) | 319 | [Space & Stars](#space), [Shaders & Psychedelic](#shader) | 🟡 |
| [termsand](https://github.com/cgsdev0/termsand) | 318 | [Falling Sand](#sand), [ASCII & Terminal](#ascii) | 🟢 |
| [ShaderToy Browser Extension](https://github.com/patuwwy/ShaderToy-Chrome-Plugin) | 313 | [Shaders & Psychedelic](#shader) | 🟢 |
| [flow-fields](https://github.com/romellogoodman/flow-fields) | 311 | [Flow & Wind Fields](#flow), [Generative Art](#gen) | 🟢 |
| [AGSL Shader Playground](https://github.com/mejdi14/Android-AGSL-Shader-Playground) | 310 | [Shaders & Psychedelic](#shader) | 🟢 |
| [Remotion TikTok Template](https://github.com/remotion-dev/template-tiktok) | 308 | [Shorts, Captions & Editing](#short), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Natural Disasters](https://github.com/Token-Gremlin/natural-disasters) | 307 | [Shaders & Psychedelic](#shader), [Particles & Physics](#particle), [3D](#3d) | 🟢 |
| [OriSim3D](https://github.com/RemiKoutcherawy/OriSim3D-Android) | 304 | [Origami & Papercraft](#origami), [3D](#3d) | 🟢 |
| [Dithering Shader](https://github.com/niccolofanton/dithering-shader) | 298 | [Dither & 1-bit](#dither), [3D](#3d), [Shaders & Psychedelic](#shader) | 🟢 |
| [Papercraft](https://github.com/rodrigorc/papercraft) | 291 | [Origami & Papercraft](#origami), [3D](#3d) | 🟢 |
| [svg-text-animate](https://github.com/oubenruing/svg-text-animate) | 280 | [Kinetic Type & Lyrics](#type), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [Remotion Audiogram Template](https://github.com/remotion-dev/template-audiogram) | 279 | [Music Visualization](#audio), [Shorts, Captions & Editing](#short) | 🟢 |
| [weilanx Claude Videos](https://github.com/Azure12355/weilanx-claude-videos) | 277 | [Hand-drawn & Whiteboard](#hand), [Pixel & Retro](#pixel) | 🟢 |
| [TSL Textures](https://github.com/boytchev/tsl-textures) | 275 | [Shaders & Psychedelic](#shader), [Procedural Generation](#procgen) | 🟢 |
| [html-anime](https://github.com/blixvip/html-anime) | 273 | [Anime, MMD & VRM](#anime), [Motion Graphics](#mg) | 🟢 |
| [babylon-mmd](https://github.com/noname0310/babylon-mmd) | 267 | [Anime, MMD & VRM](#anime), [3D](#3d) | 🟢 |
| [hitherdither](https://github.com/hbldh/hitherdither) | 260 | [Dither & 1-bit](#dither), [Pixel & Retro](#pixel) | 🟢 |
| [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer) | 257 | [Riso & Paper Collage](#riso), [Shorts, Captions & Editing](#short) | 🟢 |
| [Dither Guy](https://github.com/manoelpiovesan/dither-guy) | 254 | [Dither & 1-bit](#dither), [Pixel & Retro](#pixel) | 🟢 |
| [Krbn](https://github.com/vpalos/Krbn) | 253 | [Plotter & Line Art](#plotter), [3D](#3d) | 🟢 |
| [Claude MV Skill](https://github.com/Joker-chichi/claude-mv-skill) | 253 | [Hand-drawn & Whiteboard](#hand), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Radiance](https://github.com/zbanks/radiance) | 250 | [Live Coding & VJ](#live), [Shaders & Psychedelic](#shader), [Music Visualization](#audio) | 🟡 |
| [YouTube Motion Graphics](https://github.com/sirioberati/YouTube-AI-Motion-Graphics) | 248 | [Data Animation](#data), [Motion Graphics](#mg) | 🟢 |
| [isometric](https://github.com/elchininet/isometric) | 247 | [Isometric & Voxel](#iso) | 🟢 |
| [Codixel](https://github.com/mankidev/codixel) | 244 | [Pixel & Retro](#pixel) | 🟢 |
| [three-good-godrays](https://github.com/Ameobea/three-good-godrays) | 238 | [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [Space Colonization Experiments](https://github.com/jasonwebb/2d-space-colonization-experiments) | 229 | [Artificial Life & Growth](#alife), [Generative Art](#gen) | 🟡 |
| [p5.plotSvg](https://github.com/golanlevin/p5.plotSvg) | 220 | [Plotter & Line Art](#plotter) | 🟢 |
| [Patchies](https://github.com/heypoom/patchies) | 216 | [Live Coding & VJ](#live), [Generative Art](#gen) | 🟢 |
| [manim-skill](https://github.com/Yusuke710/manim-skill) | 216 | [Math Explainer](#math) | 🟢 |
| [code-brand-film](https://github.com/nutllwhy/code-brand-film) | 212 | [Motion Graphics](#mg) | 🟢 |
| [Vibe Knowledge Shorts](https://github.com/xiazhuo123456789/vibe-knowledge-video) | 211 | [Kinetic Type & Lyrics](#type), [Motion Graphics](#mg) | 🟢 |
| [BB-Video](https://github.com/BubbleBrainBB/BB-Video) | 211 | [Motion Graphics](#mg), [3D](#3d) | 🟢 |
| [RuiC Motion Reel](https://github.com/HRuiCcc/RuiC-motion-reel) | 207 | [Motion Graphics](#mg) | 🟢 |
| [HyperFrames Motion Reel](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | 207 | [Motion Graphics](#mg), [Kinetic Type & Lyrics](#type) | 🟢 |
| [Papercraft World](https://github.com/andrewwoan/aimee-xus-papercraft-world) | 201 | [Origami & Papercraft](#origami), [3D](#3d) | 🟢 |
| [mutracer](https://github.com/pissang/mutracer) | 198 | [Path Tracing](#raytrace), [3D](#3d) | 🟢 |
| [retrace.gl](https://github.com/stasilo/retrace.gl) | 196 | [Path Tracing](#raytrace), [Shaders & Psychedelic](#shader), [3D](#3d) | 🟢 |
| [WebGL CRT Shader](https://github.com/gingerbeardman/webgl-crt-shader) | 188 | [VHS & Analog](#vhs), [Shaders & Psychedelic](#shader) | 🟡 |
| [liquid-glass-android](https://github.com/Mortd3kay/liquid-glass-android) | 186 | [Liquid Glass](#liquid) | 🟡 |
| [genart](https://github.com/camilleroux/genart-skill) | 180 | [Generative Art](#gen), [Plotter & Line Art](#plotter) | 🟢 |
| [Fractal Garden](https://github.com/trebeljahr/fractal-garden) | 165 | [Fractals & Chaos](#fractal), [Math Explainer](#math) | 🟢 |
| [I, Voyager Planetarium](https://github.com/ivoyager/planetarium) | 162 | [Space & Stars](#space), [3D](#3d) | 🟢 |
| [Galaxy Simulation](https://github.com/N0rvel/galaxy_sim) | 162 | [Space & Stars](#space), [Particles & Physics](#particle) | 🟢 |
| [persian-motion-director](https://github.com/atmirrr/persian-motion-director) | 153 | [Kinetic Type & Lyrics](#type), [Motion Graphics](#mg) | 🟢 |
| [Sand Slide](https://github.com/kiwijuice56/sand-slide) | 143 | [Falling Sand](#sand), [Pixel & Retro](#pixel) | 🟢 |
| [NTSCplayer](https://github.com/ferropop/NTSCplayer) | 142 | [VHS & Analog](#vhs) | 🟢 |
| [Oriedita](https://github.com/oriedita/oriedita) | 137 | [Origami & Papercraft](#origami) | 🟢 |
| [kami](https://github.com/maxwase/kami) | 135 | [Origami & Papercraft](#origami) | 🟢 |
| [map-motion](https://github.com/SpaceZephyr/map-motion) | 126 | [Map & Route](#map) | 🟢 |
| [Kalem](https://github.com/leodavincs/kalem) | 119 | [Motion Graphics](#mg), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [Black Hole](https://github.com/ibra-kdbra/black-hole) | 113 | [Space & Stars](#space), [Shaders & Psychedelic](#shader) | 🟢 |
| [Stroke Order Animator](https://github.com/chill-chinese/stroke-order-animator) | 112 | [Handwriting & Strokes](#hanzi) | 🟡 |
| [Watercolor Playground](https://github.com/msurguy/watercolor-playground) | 107 | [Ink & Watercolor](#ink), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [L-System Explorer](https://github.com/anvaka/lsystem) | 101 | [Artificial Life & Growth](#alife), [Generative Art](#gen) | 🟢 |
| [sy-style-100](https://github.com/xiaoxiong20xx-code/sy-style-100) | 101 | [Motion Graphics](#mg) | 🟢 |
| [triangler](https://github.com/tdh8316/triangler) | 99 | [Geometric & Low-poly](#geo) | 🟢 |
| [DeepSeek Opus Motion](https://github.com/8533502-dev/deepseek-opus-motion-skill) | 97 | [Motion Graphics](#mg) | 🟢 |
| [VhsFx](https://github.com/NullTale/VhsFx) | 90 | [VHS & Analog](#vhs), [Glitch & Post FX](#glitch) | 🟡 |
| [ditherwave](https://github.com/sahilsaini5/ditherwave) | 90 | [Dither & 1-bit](#dither), [Shaders & Psychedelic](#shader) | 🟡 |
| [Strange Attractor Renderer](https://github.com/Icelk/strange-attractor-renderer) | 90 | [Fractals & Chaos](#fractal) | 🟡 |
| [lowpoly](https://github.com/tasercake/lowpoly) | 87 | [Geometric & Low-poly](#geo) | 🟡 |
| [Cyber Ocean](https://github.com/SahilK-027/Cyber-Ocean) | 82 | [Flow & Wind Fields](#flow), [3D](#3d), [Particles & Physics](#particle) | 🟢 |
| [FallingSandEngine](https://github.com/PieKing1215/FallingSandEngine) | 76 | [Falling Sand](#sand), [Pixel & Retro](#pixel) | 🟡 |
| [Knowledge Explainer](https://github.com/znyupup/knowledge-explainer-skill) | 74 | [Motion Graphics](#mg) | 🟡 |
| [Galaxy Shader](https://github.com/AmitDigga/threejs-galaxy-shader) | 73 | [Space & Stars](#space), [Shaders & Psychedelic](#shader), [Particles & Physics](#particle) | 🟡 |
| [Delaunay Stippler](https://github.com/NHasan143/delaunay-stippler) | 68 | [Geometric & Low-poly](#geo), [Plotter & Line Art](#plotter) | 🟢 |
| [wet-paint-flow](https://github.com/simonxxooxxoo/wet-paint-flow) | 68 | [Flow & Wind Fields](#flow), [Hand-drawn & Whiteboard](#hand) | 🟢 |
| [code-poem-film](https://github.com/bangbuilds/code-poem-film) | 66 | [Ink & Watercolor](#ink) | 🟢 |
| [Creator Style Kit](https://github.com/threeaus/creator-style-kit) | 60 | [Shorts, Captions & Editing](#short) | 🟢 |
| [gbro Collage Info Animation](https://github.com/pyang5166/gbro-collage-info) | 58 | [Riso & Paper Collage](#riso), [Dither & 1-bit](#dither) | 🟢 |
| [Oscillody](https://github.com/Akosmo/Oscillody) | 56 | [Oscilloscope & Vector](#scope), [Music Visualization](#audio) | 🟢 |
| [neon](https://github.com/Stanko/neon) | 44 | [Flow & Wind Fields](#flow), [Generative Art](#gen) | 🟡 |
| [Hopalong Attractor](https://github.com/ratwolfzero/hopalong_python) | 42 | [Fractals & Chaos](#fractal) | 🟢 |
| [Chinese-Style Paper Animation](https://github.com/AllenAI2014/remotion-guofeng-starter) | 37 | [Ink & Watercolor](#ink), [Riso & Paper Collage](#riso) | 🟢 |
| [VHSEffect](https://github.com/zulubo/VHSEffect) | 33 | [VHS & Analog](#vhs) | 🟡 |
| [proof-engine](https://github.com/Mattbusel/proof-engine) | 32 | [Fractals & Chaos](#fractal), [ASCII & Terminal](#ascii) | 🟢 |
| [VSand](https://github.com/Ealrann/VSand) | 31 | [Falling Sand](#sand) | 🟢 |
| [attractors](https://github.com/vdesmond/attractors) | 23 | [Fractals & Chaos](#fractal) | 🟡 |
| [TermiSand](https://github.com/BobdaProgrammer/TermiSand) | 22 | [Falling Sand](#sand), [ASCII & Terminal](#ascii) | 🟡 |

</details>

## Related lists

**Creative coding**

- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding): tutorials, books and tools for creative coding.
- [awesome-plotters](https://github.com/beardicus/awesome-plotters): code and resources for pen plotters.
- [morphogenesis-resources](https://github.com/jasonwebb/morphogenesis-resources): growing forms with code, including reaction-diffusion, differential growth, slime molds and L-systems.
- [awesome-demoscene](https://github.com/psykon/awesome-demoscene): demoscene tools, code and reading.
- [awesome-glsl](https://github.com/vanrez-nez/awesome-glsl): resources for learning GLSL shaders.
- [Awesome-Unity-Shader](https://github.com/QianMo/Awesome-Unity-Shader): a collection of striking Unity shaders, written up in Chinese.

**Claude / Opus galleries**: videos and prompts people made with Claude, good for inspiration. A few works use Blender or video generation models, which these lists usually mark, so check before relying on them.

- [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos): videos made with Claude Opus 5.5 and the prompts behind them.
- [opus-video-prompts](https://github.com/joeseesun/opus-video-prompts): Opus 5.5 code-video examples and copyable prompts, in Chinese.
- [awesome-claude-5-5-videos](https://github.com/athemeroy/awesome-claude-5-5-videos): Claude 5.5 video workflows with source and model noted.
- [awesome-opus-5.5-video](https://github.com/zhuyansen/awesome-opus-5.5-video): videos, motion graphics, 3D scenes and games made with Opus 5.5.
- [awesome-claude-video](https://github.com/opusvideo/awesome-claude-video): Claude Opus 5.5 videos and animation.

**AI video skills**

- [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills): skills that let coding agents make videos. Some call generation models, so its rules differ from this list.
- [awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills): AI skills for motion design.

## Contributing

Found a good project? [Suggest it in an issue](https://github.com/syydaniel/awesome-code-animation/issues/new/choose), or edit [`data/projects.json`](data/projects.json) and open a pull request. See [CONTRIBUTING.en.md](CONTRIBUTING.en.md).
Every Monday a search collects new candidates into an issue, and help judging them is welcome.
The READMEs and the web page are generated by `python scripts/build.py`, so please don't edit them by hand.

If this list helped you, a ⭐ star helps other people find it.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=syydaniel/awesome-code-animation&type=Date)](https://star-history.com/#syydaniel/awesome-code-animation&Date)

## License

The curation is released under [CC0 1.0](LICENSE) and is free to use. Works in `docs/showcase/` (videos and posters) stay with their authors and are not covered by CC0. Each project keeps its own license, so check it before commercial use.
