(() => {
  const header = document.querySelector('.site-header');
  const button = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#site-menu');
  if (!header || !button || !menu) return;
  document.documentElement.classList.add('js');
  button.hidden = false;
  const isMobile = window.matchMedia('(max-width: 680px)');
  const isOpen = () => button.getAttribute('aria-expanded') === 'true';
  const setOpen = (open, restoreFocus = false) => {
    button.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open && isMobile.matches);
    if (restoreFocus) button.focus();
  };
  button.addEventListener('click', () => setOpen(!isOpen()));
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setOpen(false)));
  isMobile.addEventListener('change', () => setOpen(false));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && isOpen()) setOpen(false, true);
  });
  document.addEventListener('click', event => {
    if (isOpen() && !header.contains(event.target)) setOpen(false);
  });
  header.addEventListener('focusout', () => {
    window.requestAnimationFrame(() => {
      if (isOpen() && !header.contains(document.activeElement)) setOpen(false);
    });
  });
  let scheduled = false;
  const updateHeader = () => {
    header.classList.toggle('is-scrolled', window.scrollY > 10);
    scheduled = false;
  };
  updateHeader();
  window.addEventListener('scroll', () => {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(updateHeader);
    }
  }, { passive: true });
  document.querySelector('.skip-link')?.addEventListener('click', () => {
    window.requestAnimationFrame(() => document.querySelector('#main-content')?.focus({ preventScroll: true }));
  });
})();
