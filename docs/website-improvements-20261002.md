# Penguin Falls website improvements — October 2, 2026

This update implements Dan's approved website improvement plan while retaining
the navy visual identity and the Twofer/Sightlines-only scope.

## What changed

- The first screen introduces both apps, with direct product choices and icons.
- The company/founder story follows the product sections.
- Twofer clearly separates app downloads from offers coming soon in Irving and
  Coppell, matching its current website. The merchant link opens the existing
  Founding Partner page. Example offers are labeled as examples.
- App screenshots retain their original UI. Home-page dark-mode images are
  unchanged. The Sightlines walkthrough adds existing Nearby and World Line
  captures from the saved September 26 portfolio assets, without recoloring
  or fabricating UI.
- The walkthrough works by mouse, touch, arrow keys, Home, and End. Without
  JavaScript, all three steps remain readable.
- Company contact and both support paths are visible. Website policy links
  now cover both apps.
- Vercel's included Hobby page-view analytics is enabled; query strings and
  fragments are removed from page URLs. DNT/GPC and nonproduction hosts are
  excluded. Custom event reports are NOT enabled, and no plan upgrade was made.

## Measurement

Start with actual production visits and Sightlines page views. The page source
includes allowlisted data-track hooks for product choices, store links, business
links, contact, support, and demo steps. They dispatch only a local
penguinfalls:action CustomEvent; they do not submit custom analytics events.

Vercel's current Hobby plan does not include custom events. Store-click rates
and completed business inquiries therefore remain unmeasured on this site.
An approved compatible provider or paid plan is needed for that follow-up.
An outbound link click must not be counted as a completed download or inquiry.

After there is enough real traffic, compare visits to product views; once
custom tracking is authorized, compare clicks by action. Do not invent targets
or report a before/after improvement without a baseline. No scheduled automation
was requested or created.

## Local checks

- scripts/check-site.py validates public local references, fragments, one H1
  per page, unique IDs, image alt attributes, and ARIA labels.
- scripts/check-analytics.cjs checks production-only loading, DNT/GPC,
  path allowlisting, URL query/hash redaction, and no custom-event submission.
- node --check for site.js, walkthrough.js, analytics.js; git diff --check.
- Browser verification covers desktop and phone layouts, menu open/Escape,
  restored focus, tabs and arrow-key navigation, image loading, and overflow.

## Release

Preview must be verified before production promotion. Previous production:
dpl_BHJTjZWyJg4z7h9qjyTRjLsCLY69, source
74a71c589f4ec66b4f5ddc45f6882bbe828306e5.

This is the independent Penguin Falls static website. Twofer app production
and Sandbox, OTA/native builds, database schema, and backend functions are
unchanged; app environment synchronization is not applicable.

Hosted verification and final deployment IDs are recorded after release.
