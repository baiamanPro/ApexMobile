// ===== Scroll reveal animation =====
(() => {
  const items = document.querySelectorAll(".scroll-reveal");
  if (!items.length) return;

  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -100px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add("active");
    });
  }, observerOptions);

  items.forEach((el) => observer.observe(el));
})();

// ===== Smooth scroll for anchors (#) =====
(() => {
  document.addEventListener("click", (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;

    const id = a.getAttribute("href");
    if (!id || id === "#") return;

    const target = document.querySelector(id);
    if (!target) return;

    e.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
})();

// ===== Product card hover =====
(() => {
  const cards = document.querySelectorAll(".product-card");
  cards.forEach((card) => {
    card.addEventListener("mouseenter", () => (card.style.zIndex = "10"));
    card.addEventListener("mouseleave", () => (card.style.zIndex = "1"));
  });
})();

// ===== Smooth page transitions (FIXED) =====
(() => {
  const page = document.body;

  // гарантируем классы
  page.classList.add("page");

  // fade-in
  window.addEventListener("DOMContentLoaded", () => {
    page.classList.remove("is-entering");
  });

  // 🔥 ПЕРЕХВАТ ТОЛЬКО НУЖНЫХ ССЫЛОК
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[data-nav]");
    if (!a) return;

    // разрешаем спец-клики
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;

    e.preventDefault();

    const href = a.href;
    if (!href) return;

    page.classList.add("is-leaving");

    const duration = 280;
    setTimeout(() => {
      window.location.href = href;
    }, duration);
  });

  // back / forward
  window.addEventListener("pageshow", () => {
    page.classList.remove("is-leaving");
    page.classList.remove("is-entering");
  });
})();
