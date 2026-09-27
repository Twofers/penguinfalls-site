# Twofer and Sightlines website update — September 26, 2026

Dan requested advertising only Sightlines and Twofer and using dark-mode app
screenshots. This update extends the restored navy, blue, and white website.
It does not reinstate the broader app-and-games portfolio design.

## Published content

- Homepage navigation, company copy, and product sections feature Twofer and
  Sightlines. Game marketing and game pages remain absent.
- Twofer shows its dark-mode discovery and offer-detail screens, with links to
  its website, App Store listing, and Google Play listing.
- Sightlines shows its Night Mode screen, with its App Store and support links.
  Its old prelaunch landing page is replaced with current app information.
- Website policy navigation and footer ownership text include both apps.
  Existing Sightlines support, privacy, and terms documents are unchanged.

## Screenshots

These are existing app captures, copied without changing the interface or
inventing screen content. The web images total approximately 110 KB.

| Website asset | Source |
| --- | --- |
| `assets/apps/twofer-discovery-dark-20260926.webp` | Twofer public App Store screenshot `01-consumer-home.png` |
| `assets/apps/twofer-offer-dark-20260926.webp` | Twofer public App Store screenshot `02-deal-detail.png` |
| `assets/apps/sightlines-night-mode-20260926.webp` | Sightlines public App Store screenshot `04-night-mode.png`, actual version 1.0.1 (4) iPhone capture |

The existing web exports were copied from the saved portfolio source. Their
original URLs are recorded in `data/asset-sources.json` on the preserved branch
`codex/penguin-falls-portfolio`. Twofer's white offer cards are part of its actual
dark theme; the screenshots were not recolored. Sightlines uses its actual Night
Mode view. Current app availability was verified against the public listings:

- https://apps.apple.com/us/app/twofer-live-local-deals/id6765769303
- https://apps.apple.com/us/app/sightlines-direction-finder/id6808024469

## Verification

- Seven pages checked: 119 local references resolved; one H1 per page, unique
  IDs, image alternative text, and organization JSON-LD verified.
- JavaScript syntax and diff whitespace checks passed.
- Homepage and Sightlines page checked at 320px, 768px, and 1280px, with no
  persistent horizontal overflow or broken loaded images. A transient resize
  measurement on Sightlines was rechecked after layout settled at 320px.
- Original desktop visual style, both product sections, and phone layout
  reviewed in the browser. Phone menu opening, Escape closing, and returned
  focus verified.
- Hosted preview: `dpl_2iEjMT1DyUFvFvk8Rhj8FaDycHsK`.
- Preview URL: https://penguinfalls-site-mqoomcjok-dansanders-2432s-projects.vercel.app

This is a static Penguin Falls website update. It does not change app binaries,
OTA channels, databases, or backend functions. Twofer production/Sandbox
synchronization is not applicable; the website preview is checked before
production publication.
