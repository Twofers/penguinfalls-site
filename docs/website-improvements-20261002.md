# Penguin Falls design refinement — October 2, 2026

The website presents Penguin Falls as the independent software company behind Twofer and Sightlines. Twofer has its own marketing website; the company homepage gives it a concise introduction and direct link. Sightlines keeps its dedicated product page and interactive walkthrough.

## Design decisions

- One warm neutral canvas with navy text, fine dividing rules, generous spacing, and a shared page grid.
- Instrument Serif headings paired with DM Sans body and navigation text. The existing logo is preserved; a versioned navy SVG matches the site palette without changing cached originals.
- Company identity leads the homepage. Matching product displays use authentic app screenshots with concise descriptions and clear onward links.
- A short company story and a single navy contact/footer region complete the page.
- All seven pages now use the same styles, navigation, footer, and typography. The separate refresh and Sightlines policy stylesheets have been retired.
- Support and policy article contents are preserved exactly. Reduced-motion preferences, visible keyboard focus, progressive enhancement, and narrow-screen layouts remain supported.

Visual references inspected on October 2: [Metalab](https://www.metalab.com/) for deliberate typographic hierarchy and [Instrument](https://www.instrument.com/) for consistent spacing and restrained portfolio presentation. No reference-site artwork, copy, or code is used.

## Verification

Existing site-reference, analytics-privacy, JavaScript syntax, and Git whitespace checks are run for the candidate. Browser review covers desktop and phone layouts, menu open/Escape/focus, product navigation, and keyboard walkthrough behavior. Exact widths, candidate revision, and hosted results are recorded in qa-20261002/release.json after deployment.

All five policy/support article bodies were compared with the previous revision and are unchanged. Screenshot image pixels remain unchanged; the desktop layout crops them through CSS, while narrow phone layouts show the full screens.

## Analytics and environments

The included Hobby page-view capability is enabled in Vercel. The candidate loads analytics only on canonical production hosts, excludes DNT/GPC, and strips query strings and fragments. Custom-event reporting is not enabled; click hooks only dispatch local events. No paid upgrade or new service is introduced.

The independent Penguin Falls website is the only runtime scope. Twofer production and Sandbox, database schema, backend functions, and native/OTA builds are unchanged; app synchronization is not applicable.

## Publication status

This refinement is authorized for implementation and preview. Production remains on source 74a71c589f4ec66b4f5ddc45f6882bbe828306e5 until explicitly approved. Automatic approval review rejected the earlier promotion because explicit production release authorization was missing. No production promotion or main-branch push is part of this design refinement.

Hosted preview and source details are recorded in qa-20261002/release.json.
