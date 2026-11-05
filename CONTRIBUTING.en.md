# Contributing

[Chinese version](CONTRIBUTING.md)

Thanks for suggesting a project! This list exists to help people find the right code animation tool by **visual style**, so two things matter most: the picture is really drawn by code, and the project is still worth using.

## What gets listed

1. **Frames are drawn or rendered by code.** Projects that make their pictures with video or image generation models aren't listed, and neither are ones that render through Blender or other 3D apps. Skills and films where AI coding agents like Claude or Opus write the code are welcome. They're filed by style as usual, with an extra `"agent": true`.
2. **Main styles:** 1,000+ GitHub stars, or 200+ stars with a push in the last year.
3. **Niche styles:** 20+ stars with a push in the last year. Small and interesting projects are welcome.
4. **Projects marked `"agent": true`:** 50+ stars with a push in the last year.
5. **The repository isn't archived.**

The exact checks are in [`scripts/rules.py`](scripts/rules.py) and run every week when the data refreshes.

## The easy way: open an issue

Under [Issues](../../issues/new/choose), pick "Suggest a project" and give the repository URL and style. The maintainer fills in the rest.

Every Monday an automatic "weekly candidates" issue lists projects that were found but aren't listed yet. Help judging them is welcome.

## Open a pull request

1. Add an entry to [`data/projects.json`](data/projects.json):

   ```json
   {
     "repo": "owner/name",
     "name": "Display name",
     "tags": ["mg", "type"],
     "lang": "TypeScript",
     "use": "Music videos · Short videos",
     "use_en": "MV · Shorts",
     "desc": "(optional Chinese description)",
     "desc_en": "One sentence on what kind of picture it makes.",
     "note_en": "(Optional) Anything to warn about, like license limits or an optional generation feature.",
     "license": null,
     "stars": 0,
     "pushed_at": "2026-01-01",
     "archived": false
   }
   ```

   `tags` are the `key` values in [`data/styles.json`](data/styles.json). You can list several, with the main style first. Styles with `"zone": "niche"` are niche styles. `stars`, `pushed_at`, `archived` and `license` can be anything, because the next step refreshes them.

   The site and README exist in Chinese and English. `name`, `desc`, `use`, `note` and `lang` each have an optional `*_en` field. `desc` and `use` are required by the build, so if you don't write Chinese, put the English text in both and the maintainer will translate it.

2. If it relates to a listed project (built on it, a plugin for it, similar to it), add an entry to [`data/relations.json`](data/relations.json):

   ```json
   {"from": "owner/name", "type": "plugin", "to": "mrdoob/three.js", "note": "(Chinese note)", "note_en": "One short clause."}
   ```

   `type` is one of: `fork`, `built_on`, `plugin`, `official`, `uses`, `data`, `alt`, `pair`, `author`.

3. Refresh the data and rebuild the READMEs and web page:

   ```bash
   python scripts/update_stats.py   # optional: needs network, export GITHUB_TOKEN=... first
   python scripts/build.py
   ```

4. Commit your changes under `data/`, plus `README.md`, `README.en.md` and `docs/index.html`.

Please don't edit `README.md`, `README.en.md` or `docs/index.html` by hand. They're generated, and the next build overwrites them.

Projects we looked at and decided against go in [`data/excluded.json`](data/excluded.json) with a reason, so automatic discovery stops suggesting them.

## Adding a style

Add an entry to `data/styles.json` (with `"zone": "niche"` for a niche style), and write a thumbnail function for it in the `SW` object in [`site/template.html`](site/template.html), using a 240×96 canvas. Then run:

```bash
pip install playwright && playwright install chromium
python scripts/build.py
python scripts/render_swatches.py   # regenerates the thumbnails, banners and graph images in assets/
python scripts/build.py
```

## Tips for descriptions

- Say **what kind of picture it makes**, not just the technology.
- One or two sentences is enough.
- If it has license limits (paid commercial use, AGPL, non-commercial), only works on one system, or has an optional generation feature, put that in `note_en`.
