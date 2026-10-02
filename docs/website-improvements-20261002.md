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

Dan explicitly authorized publication with "ok publish". The verified preview was promoted to production on October 2, 2026. Live URL: https://www.penguinfalls.com/.

Production deployment: dpl_H6LmzMTSBpZcYTA5V3EAq8cb2FcH.
Verified runtime source: 7e6c69fa758f0f721519af4d8c267ef824dc5d68.
Preview deployment: dpl_5VF3eBMM3QUcH4tpZHcsnjhD4xf9.
Previous production deployment: dpl_BHJTjZWyJg4z7h9qjyTRjLsCLY69 (source 74a71c5).

All seven public pages and four shared CSS/JavaScript files returned HTTP 200 and matched the verified local source exactly. The apex domain redirects to the canonical www domain. Desktop appearance, the 390-pixel mobile menu and product navigation, and the Sightlines keyboard walkthrough were checked on production. The included analytics script is now published and loads on the canonical domain; no custom-event reporting or paid upgrade was enabled.

The publication authorization blocker is resolved. Automatic approval review separately rejected updating GitHub main because publication approval did not include a default-branch mutation. Main remains on 74a71c5; the released source and documentation remain on codex/product-first-homepage. Do not redeploy the old main revision over the published design. Explicit authorization is needed before aligning main.

Publication details and proof are recorded in qa-20261002/release.json. This release-record commit changes documentation only; production remains the verified candidate.

## Blue-theme preview requested after publication

Dan prefers the earlier blue theme. Candidate 8316681612a111e2d2f5e9a86109f688a9339ca1 restores the original navy (#14385f), deep navy (#0b2949), and sky blue (#9acbfc), with white text, blue product panels, and the existing reverse logo. The refined layout, typography, page copy, and actual app screenshot pixels are preserved.

Preview: https://penguinfalls-site-a5dk6cfza-dansanders-2432s-projects.vercel.app
Deployment: dpl_3nyJNkXVRuKAbFiJTcJo6Y1U4uCk.

All seven hosted pages use the blue theme. Desktop, phone, narrow-screen layouts, mobile menu focus, local references, and text contrast were checked. Tested normal-text color combinations range from 5.08:1 to 13.90:1. See qa-20261002/blue-theme-preview.json and the accompanying screenshots.

The blue theme is a review preview. Production remains the published 7e6c69f design, and main was not changed.
