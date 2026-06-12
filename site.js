(() => {
  const header = document.querySelector(".site-header");
  const setHeaderState = () => header.classList.toggle("is-scrolled", window.scrollY > 24);
  setHeaderState();
  window.addEventListener("scroll", setHeaderState, { passive: true });

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
