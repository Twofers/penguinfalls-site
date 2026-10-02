# Penguin Falls LLC Static Site

Plain HTML, CSS, and a small shared `site.js` for Vercel hosting. There is no framework, build step, package manager, or server code.

## Preview Locally

The site uses clean URLs (`/privacy`, `/terms`), so preview with a server that resolves them:

```powershell
npx serve .
```

Then open the URL it prints (usually `http://localhost:3000`). Plain `python -m http.server` also works, but only with the `.html` extensions typed in the address bar.

## Deploy

Use the Vercel flow from Section 12 of `../penguinfalls-build-plan.md`: put this folder in a GitHub repo, import it into Vercel as "Other" or "No framework", leave the build command empty, keep the output directory as the root, deploy, then point `penguinfalls.com` and `www.penguinfalls.com` to the Vercel project.

## October 2026 product presentation

refresh.css extends the existing design. walkthrough.js progressively enhances
the Sightlines demo. analytics.js collects page views only on the canonical
production hosts and respects DNT/GPC; local click hooks do not send custom
events. No paid analytics plan has been enabled.

Preview: python scripts/preview.py at http://127.0.0.1:8768.
Checks: python scripts/check-site.py and node scripts/check-analytics.cjs.
See docs/website-improvements-20261002.md for candidate and release status.
Verify a hosted preview before promotion.
