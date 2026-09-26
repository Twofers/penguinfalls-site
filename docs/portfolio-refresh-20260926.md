# Penguin Falls portfolio refresh — September 26, 2026

## Scope

Refresh Penguin Falls as the parent studio for Twofer, Sightlines, Penguin Bounce,
Penguin Slide, Penguin Express, and Penguin Crash. Add a support directory and six
product landing pages, update the company story and navigation, and give each
product search metadata and a social image.

The exact site previously serving www.penguinfalls.com was recovered from the
existing `penguinfalls-sightlines-launch` source. Its home, CSS, script, policies,
Sightlines pages, and sitemap matched the live responses before edits. That live
baseline contained newer branding and Sightlines disclosures missing from the
repository's former default branch. This release includes those existing files.

## Content and assets

- Six public US App Store listings verified September 26, 2026. Store IDs and
  artwork provenance are recorded in `data/app-store-snapshot.json` and
  `data/asset-sources.json`.
- Twofer's Google Play listing is linked; other apps display only their verified
  Apple platforms. Penguin Crash identifies iPhone/iPad and its 13+ rating.
- Screenshots are actual store screenshots, resized and compressed without
  changing the depicted UI. All 24 app images and seven social images total
  approximately 1.15 MB. The homepage loads only the images it uses.
- Sightlines' outdated prelaunch landing page is replaced with its available app
  page. Its existing support, privacy, and terms HTML is preserved byte for byte.
- Game support and privacy remain at their established Twofer URLs. Where a game
  has no separate service terms, the directory labels Apple's Standard EULA as
  “iOS license.” Existing game URLs and store metadata were not changed.
- Website policies now direct visitors to all product policies. No analytics,
  account collection, payment flow, or mailing list was added.

## Verification before promotion

- Fourteen HTML pages checked for local assets, clean-URL destinations, anchors,
  unique IDs, one H1, canonical links, and image alternative text. All 399 local
  references resolved.
- All generated JSON-LD parsed successfully; JavaScript syntax check passed.
- Ten updated pages rendered at 320px and 1280px widths with no horizontal page
  overflow or broken loaded images. Homepage and featured/product layouts were
  visually reviewed at desktop and 390px phone size.
- Mobile menu expansion, Escape-to-close, focus restoration, and navigation to
  the support directory were exercised successfully.
- All 16 distinct support, privacy, and terms/license destinations opened in the
  browser with the expected page headings. Some remote endpoints reject generic
  automated HTTP requests, so their actual browser rendering was verified.
- Preview: https://penguinfalls-site-kyg3l27jm-dansanders-2432s-projects.vercel.app
- Preview deployment: `dpl_9tXSWqPqUGHaosK2w9RXbQ17t5L8`.
- Prior production deployment for rollback: `dpl_5WwGAhyFcz3YyHoaJ4822teoXwHk`.

## Environment scope

This release changes only the independent Penguin Falls company website. Twofer
and Sightlines binaries, OTA channels, databases, and backend functions are not
part of this release. App production/Sandbox synchronization is not applicable.
The website uses a Vercel preview gate before promotion of the same static files.

## Production

Published September 26, 2026 after preview verification.

- Reviewed website source: `4b2cc2dc70bd8e12d8f9cd69ab5c797936779abe`,
  pushed to `Twofers/penguinfalls-site` on `main`.
- Promotion created production deployment `dpl_Ctmuz4yfcTMjEmX1kCPwqsweMGqo`.
- GitHub synchronization then built the same reviewed website source as
  `dpl_BAoiQE97qPiZnqwQGxf1xeQH9LZt`; Vercel reported it Ready.
- Both https://www.penguinfalls.com and https://penguinfalls.com serve the refresh.
- All 17 checked production HTML/CSS/JS/sitemap/robots routes returned HTTP 200
  and matched the reviewed source after normalizing Windows/Linux line endings.
  Results are in `production-checks-20260926.json`.
- Public source-only and environment-file probes returned 404. The custom missing
  page returned 404, and social/product images returned 200.
- The live homepage rendered all six products without image failures or page
  overflow. Navigation to the live support page displayed all six app contacts.
- A final documentation-only commit records these results. Documentation is
  excluded from the hosted site and does not change the reviewed public files.
