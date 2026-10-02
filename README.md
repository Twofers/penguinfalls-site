# Penguin Falls LLC static website

A company website with a compact portfolio for Twofer and Sightlines, built with plain HTML, one shared stylesheet, and small scripts. There is no framework or build step.

## Preview and check

Run `python scripts/preview.py`, then open http://127.0.0.1:8768. The loopback server handles the same public clean URLs as Vercel.

Run `python scripts/check-site.py`, `node scripts/check-analytics.cjs`, and `node --check` for the three JavaScript files. Inspect desktop and phone layouts in a browser before deploying a preview.

## Design

All seven public pages use `styles.css`: shared type, colors, spacing, navigation, footer, links, and product presentation. Do not add page-specific override stylesheets. The homepage is the company overview; Twofer's detailed marketing stays on its own website. Sightlines retains its product walkthrough here.

App screenshots are authentic captures and must not be recolored or replaced with invented UI. Assets under `/assets` and `/brand` have immutable caching, so changed files need new versioned names.

## Behavior

`site.js` provides the accessible mobile menu and sticky-header state. `walkthrough.js` enhances the three Sightlines steps with keyboard-accessible tabs; all steps remain readable without JavaScript. `analytics.js` loads page views only on canonical production hosts, respects DNT/GPC, and redacts query strings and fragments. Local click hooks do not submit custom events or require a paid analytics plan.

## Release

Use the existing Vercel project and feature branch for preview deployments. Verify the hosted preview before requesting production promotion. Production publication requires Dan's explicit authorization. See `docs/website-improvements-20261002.md` and `docs/qa-20261002/release.json` for verification and release status.

This repository is independent of the Twofer app. Its production/Sandbox app synchronization, native/OTA releases, database migrations, and backend functions are not affected by these website changes.
