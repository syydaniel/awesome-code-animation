# 参与贡献

谢谢你愿意推荐项目！这份合集的目标是帮人按**画风**找到合适的代码动画工具，所以收录时最看重两点：画面确实是代码画出来的，以及项目还值得用。

## 收录标准

1. **画面由代码绘制或渲染。** 用视频生成、图像生成模型出画面的项目不收。Claude / Opus 等 AI 编程助手写代码出片的项目可以收，归在 `agent`，但调用 Blender 出画面的不收。只有可选、默认关闭的生成功能时，可以收录，并在 `note` 里写清楚。
2. **主流画风：** GitHub 星数 1000 以上，或近一年内有更新且星数 200 以上。
3. **小众画风区和 Claude / Opus 区（`agent`）：** 近一年内有更新、星数 50 以上即可。
4. **仓库没有被归档。**

具体判断写在 [`scripts/rules.py`](scripts/rules.py) 里，每周刷新数据时会自动检查一遍。

## 最简单的方式：提 Issue

在 [Issues](../../issues/new/choose) 里选「推荐项目」，填上仓库地址和画风就行，维护者会补齐其余信息。

每周一还会自动生成一个「每周候选项目」Issue，列出搜到的、还没收录的项目，欢迎在里面帮忙判断。

## 直接提 Pull Request

1. 在 [`data/projects.json`](data/projects.json) 里加一条：

   ```json
   {
     "repo": "owner/name",
     "name": "显示名称",
     "tags": ["mg", "type"],
     "lang": "TypeScript",
     "use": "MV · 短视频",
     "desc": "一句话说明它能做出什么样的画面。",
     "note": "（可选）需要提醒的事，比如许可证限制、可选的生成功能。",
     "license": null,
     "stars": 0,
     "pushed_at": "2026-01-01",
     "archived": false
   }
   ```

   `tags` 用 [`data/styles.json`](data/styles.json) 里的 `key`，可以写多个，第一个放最主要的画风。带 `"zone": "niche"` 的是小众画风区。`stars`、`pushed_at`、`archived`、`license` 随便填，下一步会自动刷新。

2. 如果它和已收录的项目有关系（基于谁、是谁的插件、和谁同类），在 [`data/relations.json`](data/relations.json) 里加一条：

   ```json
   {"from": "owner/name", "type": "plugin", "to": "mrdoob/three.js", "note": "一句话说明"}
   ```

   `type` 可选：`fork` 分叉自、`built_on` 基于、`plugin` 插件 / 扩展、`official` 官方模板 / 技能、`uses` 用它渲染、`data` 数据来源、`alt` 同类可替换、`pair` 常搭配、`author` 同一作者。

3. 刷新数据并重新生成 README 和网页版：

   ```bash
   python scripts/update_stats.py   # 可选：需要联网，建议先 export GITHUB_TOKEN=...
   python scripts/build.py
   ```

4. 提交 `data/` 下改过的文件，以及 `README.md`、`README.en.md` 和 `docs/index.html`。

请不要直接修改 `README.md`、`README.en.md` 或 `docs/index.html`，它们是生成出来的，下次构建会被覆盖。

看过但决定不收的项目，写进 [`data/excluded.json`](data/excluded.json) 并注明原因，自动发现就不会再推荐它。

## 新增画风

在 `data/styles.json` 里加一条（小众画风加上 `"zone": "niche"`），并在 [`site/template.html`](site/template.html) 的 `SW` 对象里给它写一个小样图的绘制函数（240×96 的画布坐标）。之后运行：

```bash
pip install playwright && playwright install chromium
python scripts/build.py
python scripts/render_swatches.py   # 重新生成 assets/ 里的样图和横幅
python scripts/build.py
```

## 写说明的小建议

- 说清楚**能做出什么样的画面**，而不是只写技术名词。
- 一两句话就够，控制在 60 个字以内。
- 有许可证限制（比如商用要付费、AGPL、非商用）、只支持某个系统、或者带可选的生成功能的，写进 `note`。
