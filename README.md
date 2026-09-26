# Penguin Falls — apps and games

Static HTML, CSS, and a small navigation script, hosted by the existing
`penguinfalls-site` Vercel project at https://www.penguinfalls.com.
No framework, server, package install, or build step is required for hosting.

## Edit and preview

App content, verified store destinations, and support resources live in
`data/apps.json`. Regenerate the committed pages after changing that catalog or
`scripts/build-site.py`:

```powershell
python scripts/build-site.py
python scripts/preview.py
```

Open http://127.0.0.1:8767. The local preview supports the same clean page URLs.
The design and menu code are in `portfolio.css` and `portfolio.js`. Retained
`styles.css` and `site.js` record the previous live site; new pages use the
portfolio files. Existing Sightlines policy/support pages have their own CSS.

The site includes six product pages, `/support`, `/privacy`, `/terms`, and the
existing `/sightlines/support`, `/sightlines/privacy`, `/sightlines/terms` URLs.
Legacy `/products`, `/contact`, `/#company`, `/#twofer`, and `/#top` links remain
usable. The website policies cover this informational website; each app's own
resources are linked from the support directory.

## Artwork

`data/asset-sources.json` records the current public App Store images. Imported
screens retain their actual UI and are compressed as WebP. To deliberately
refresh artwork, first update the store snapshot, then run the download and
preparation scripts. Image preparation needs Pillow and uses Windows Georgia
and Segoe UI fonts for the 1200 × 630 social previews. It is not a deployment step.

## Release

Run local checks and visually review desktop and phone layouts. Create a Vercel
preview and verify the product, store, and support routes before promoting the
same deployment. Exclude scripts, local caches, environment files, data sources,
and documentation from the deployment via `.vercelignore`.

Keep the reviewed source in GitHub as part of publishing. Do not deploy an older
repository snapshot over a more recent live release. See
`docs/portfolio-refresh-20260926.md` for this release's provenance and checks.
