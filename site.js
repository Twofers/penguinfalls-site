(() => {
  const header = document.querySelector(".site-header");
  let renderedHeaderState;
  let nextHeaderState = false;
  let headerFrame = 0;

  const renderHeaderState = () => {
    headerFrame = 0;
    if (nextHeaderState === renderedHeaderState) return;
    header.classList.toggle("is-scrolled", nextHeaderState);
    renderedHeaderState = nextHeaderState;
  };

  const queueHeaderState = () => {
    nextHeaderState = window.scrollY > 24;
    if (!headerFrame) headerFrame = window.requestAnimationFrame(renderHeaderState);
  };

  renderHeaderState();
  window.requestAnimationFrame(queueHeaderState);
  window.addEventListener("scroll", queueHeaderState, { passive: true });

  const button = document.querySelector(".menu-toggle");
  const menu = document.querySelector("#site-menu");
  if (!button || !menu) return;

  const isOpen = () => button.getAttribute("aria-expanded") === "true";
  const setOpen = (open) => {
    button.setAttribute("aria-expanded", String(open));
    menu.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
  };

  button.addEventListener("click", () => setOpen(!isOpen()));
  menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => setOpen(false)));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && isOpen()) {
      setOpen(false);
      button.focus();
    }
  });
})();
