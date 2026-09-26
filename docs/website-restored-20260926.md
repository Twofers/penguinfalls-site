# Previous Penguin Falls website restored — September 26, 2026

Dan requested returning to the website that was live before the portfolio refresh.
The exact saved source from `penguinfalls-sightlines-launch` was republished,
including the existing branding, Twofer screens, and Sightlines disclosure pages.
The previous headline, “Software for local commerce,” is restored.

- Original pre-refresh deployment: `dpl_5WwGAhyFcz3YyHoaJ4822teoXwHk`.
- Restoration deployment: `dpl_C2Q7TwKpY2RfvWnQvmCZC5dDbVkp` (Ready, production).
- Both `https://www.penguinfalls.com/` and `https://penguinfalls.com/` returned
  HTTP 200 with the saved pre-refresh homepage.
- All 12 checked HTML, CSS, JavaScript, sitemap, and robots routes returned HTTP
  200 and matched the saved source after normalizing line endings.
- All 33 restored source files matched the saved baseline byte for byte before
  Git line-ending normalization. JavaScript syntax and diff checks passed.
- The restored homepage was verified in the browser.
- The full newer portfolio design remains saved on the remote branch
  `codex/penguin-falls-portfolio` at `63c60a8` for possible future use.
- This commit aligns `main` with the restored website. Vercel may redeploy these
  same static files after the source push.

Only the independent Penguin Falls website changed. App binaries, databases,
and backend services were untouched; Twofer production/Sandbox synchronization
is not applicable.
