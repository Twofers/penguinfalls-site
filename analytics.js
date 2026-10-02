(() => {
  // Only canonical production traffic belongs in the free page-view baseline.
  const productionHosts = new Set(['www.penguinfalls.com', 'penguinfalls.com']);
  const publicPaths = new Set(['/', '/sightlines', '/privacy', '/terms', '/sightlines/support', '/sightlines/privacy', '/sightlines/terms']);
  const path = window.location.pathname.replace(/\.html$/, '').replace(/\/$/, '') || '/';
  if (!publicPaths.has(path)) return;

  // Local hooks are ready for a future approved custom-event provider.
  // The current Hobby plan does not support custom-event reports.
  const actions = new Set(['explore_twofer', 'explore_sightlines', 'twofer_app_store', 'twofer_google_play', 'twofer_business', 'sightlines_app_store', 'sightlines_demo', 'demo_point', 'demo_review', 'demo_explore', 'company_contact', 'twofer_support', 'sightlines_support']);
  document.addEventListener('click', event => {
    const target = event.target instanceof Element ? event.target.closest('[data-track]') : null;
    const name = target?.getAttribute('data-track');
    if (actions.has(name)) {
      window.dispatchEvent(new CustomEvent('penguinfalls:action', { detail: { name, path } }));
    }
  });

  if (!productionHosts.has(window.location.hostname) || navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true) return;
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
  window.va('beforeSend', event => {
    const url = new URL(event.url);
    const eventPath = url.pathname.replace(/\.html$/, '').replace(/\/$/, '') || '/';
    if (!productionHosts.has(url.hostname) || !publicPaths.has(eventPath)) return null;
    url.search = '';
    url.hash = '';
    return { ...event, url: url.toString() };
  });
  const script = document.createElement('script');
  script.defer = true;
  script.src = '/_vercel/insights/script.js';
  document.head.appendChild(script);
})();
