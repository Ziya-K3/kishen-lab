(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const progress = document.querySelector("[data-progress]");
  const nav = document.querySelector("[data-nav]");
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? window.scrollY / max : 0;
    if (progress) progress.style.width = `${ratio * 100}%`;
    nav?.classList.toggle("is-stuck", window.scrollY > 8);
    const wash = document.querySelector("[data-logo-wash]");
    if (wash && !reduce) {
      const y = window.scrollY || document.documentElement.scrollTop || 0;
      wash.style.setProperty("--wash-y", `${-y * 0.035}px`);
    }
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const menuButton = document.querySelector("[data-menu]");
  const mobile = document.querySelector("[data-mobile]");
  const closeMenu = () => {
    document.body.classList.remove("menu-open");
    menuButton?.setAttribute("aria-expanded", "false");
    mobile?.setAttribute("hidden", "");
  };
  menuButton?.addEventListener("click", () => {
    const open = document.body.classList.toggle("menu-open");
    menuButton.setAttribute("aria-expanded", String(open));
    if (open) mobile?.removeAttribute("hidden");
    else mobile?.setAttribute("hidden", "");
  });
  mobile?.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));

  const search = document.querySelector("[data-search]");
  const searchInput = document.querySelector("[data-search-input]");
  const searchResults = document.querySelector("[data-search-results]");
  let searchTimer = 0;

  const openSearch = () => {
    search?.removeAttribute("hidden");
    searchInput?.focus();
  };
  const closeSearch = () => {
    search?.setAttribute("hidden", "");
    if (searchInput) searchInput.value = "";
    if (searchResults) searchResults.innerHTML = "";
  };
  document.querySelector("[data-search-open]")?.addEventListener("click", openSearch);
  search?.addEventListener("click", (event) => {
    if (event.target === search) closeSearch();
  });
  document.addEventListener("keydown", (event) => {
    const tag = document.activeElement?.tagName;
    const typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT";
    if (event.key === "/" && !typing) {
      event.preventDefault();
      openSearch();
    }
    if (event.key === "Escape") {
      closeSearch();
      closeMenu();
    }
  });

  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");

  const renderHits = (results) => {
    if (!searchResults) return;
    if (!results.length) {
      searchResults.innerHTML = '<p class="search-empty">Nothing matched. Try biofilm, organoid, or award.</p>';
      return;
    }
    searchResults.innerHTML = results
      .map(
        (hit) => `<a href="${escapeHtml(hit.href)}">
          <small>${escapeHtml(hit.kind)}</small>
          <span><strong>${escapeHtml(hit.title)}</strong><em>${escapeHtml(hit.meta)}</em></span>
        </a>`
      )
      .join("");
  };

  searchInput?.addEventListener("input", () => {
    window.clearTimeout(searchTimer);
    const q = searchInput.value.trim();
    if (q.length < 2) {
      if (searchResults) searchResults.innerHTML = "";
      return;
    }
    searchTimer = window.setTimeout(async () => {
      const response = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
      const data = await response.json();
      renderHits(data.results || []);
    }, 140);
  });

  const plate = document.querySelector("[data-plate]");
  if (plate) {
    const tubules = plate.querySelector("[data-tubules]");
    const motes = plate.querySelector("[data-motes]");
    const cx = 320;
    const cy = 310;
    const ns = "http://www.w3.org/2000/svg";
    for (let i = 0; i < 72; i += 1) {
      const angle = (Math.PI * 2 * i) / 72;
      const inner = 64 + (i % 5) * 3;
      const outer = 188 + (i % 3) * 6;
      const line = document.createElementNS(ns, "line");
      line.setAttribute("x1", String(cx + Math.cos(angle) * inner));
      line.setAttribute("y1", String(cy + Math.sin(angle) * inner));
      line.setAttribute("x2", String(cx + Math.cos(angle) * outer));
      line.setAttribute("y2", String(cy + Math.sin(angle) * outer));
      line.setAttribute("class", "tubule");
      line.style.animationDelay = `${(i % 12) * 30}ms`;
      tubules?.appendChild(line);
    }
    const particles = [];
    for (let i = 0; i < 10; i += 1) {
      const dot = document.createElementNS(ns, "circle");
      dot.setAttribute("r", i % 3 === 0 ? "3.2" : "2.1");
      dot.setAttribute("class", "mote");
      motes?.appendChild(dot);
      particles.push({
        el: dot,
        radius: 18 + (i % 5) * 8,
        speed: 0.004 + (i % 4) * 0.0015,
        phase: (Math.PI * 2 * i) / 10,
      });
    }
    if (!reduce) {
      const tick = (time) => {
        particles.forEach((particle) => {
          const t = time * particle.speed + particle.phase;
          particle.el.setAttribute("cx", String(cx + Math.cos(t) * particle.radius));
          particle.el.setAttribute("cy", String(cy + Math.sin(t) * particle.radius * 0.86));
        });
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    } else {
      particles.forEach((particle, i) => {
        const t = particle.phase;
        particle.el.setAttribute("cx", String(cx + Math.cos(t) * particle.radius));
        particle.el.setAttribute("cy", String(cy + Math.sin(t) * particle.radius));
      });
    }
  }

  const counters = document.querySelectorAll("[data-count]");
  const format = (value) => value.toLocaleString("en-US");
  if (reduce) {
    counters.forEach((node) => {
      node.textContent = `${format(Number(node.dataset.count))}${node.dataset.suffix || ""}`;
    });
  } else if (counters.length) {
    const seen = new WeakSet();
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting || seen.has(entry.target)) return;
        seen.add(entry.target);
        const node = entry.target;
        const target = Number(node.dataset.count);
        const suffix = node.dataset.suffix || "";
        const start = performance.now();
        const duration = 1100;
        const step = (now) => {
          const t = Math.min(1, (now - start) / duration);
          const eased = 1 - Math.pow(1 - t, 3);
          node.textContent = `${format(Math.round(target * eased))}${suffix}`;
          if (t < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    counters.forEach((node) => counterObserver.observe(node));
  }

  const voices = [...document.querySelectorAll("[data-voice]")];
  const dots = [...document.querySelectorAll(".voice-dots button")];
  if (voices.length > 1) {
    let index = 0;
    const show = (next) => {
      index = next;
      voices.forEach((voice, i) => voice.classList.toggle("is-active", i === index));
      dots.forEach((dot, i) => {
        if (i === index) dot.setAttribute("aria-current", "true");
        else dot.removeAttribute("aria-current");
      });
    };
    dots.forEach((dot, i) => dot.addEventListener("click", () => show(i)));
    if (!reduce) {
      window.setInterval(() => show((index + 1) % voices.length), 7000);
    }
  }

  const alumniRoot = document.querySelector("[data-alumni]");
  alumniRoot?.querySelectorAll("[data-alumni-tab]").forEach((tab) => {
    tab.addEventListener("click", () => {
      const id = tab.dataset.alumniTab;
      alumniRoot.querySelectorAll("[data-alumni-tab]").forEach((item) => {
        item.setAttribute("aria-selected", String(item === tab));
      });
      alumniRoot.querySelectorAll("[data-alumni-panel]").forEach((panel) => {
        if (panel.dataset.alumniPanel === id) panel.removeAttribute("hidden");
        else panel.setAttribute("hidden", "");
      });
    });
  });

  const finder = document.querySelector("#finder");
  const paperIndex = document.querySelector("[data-paper-index]");
  const countLabel = document.querySelector("[data-count-label]");
  if (finder && paperIndex) {
    const paint = (papers, totalLabel) => {
      if (!papers.length) {
        paperIndex.innerHTML = '<p class="empty">Nothing in the index matches that filter. Try a broader word, or clear the year.</p>';
      } else {
        paperIndex.innerHTML = papers
          .map((paper) => {
            const doi = paper.doi
              ? `<a class="text-link" href="https://doi.org/${escapeHtml(paper.doi)}">doi.org/${escapeHtml(paper.doi)} <span aria-hidden="true">↗</span></a>`
              : "";
            const figure = paper.figure
              ? `<img class="paper-fig wide" src="/static/${escapeHtml(paper.figure)}" alt="">`
              : "";
            return `<article class="paper-row">
              <div class="paper-year">${escapeHtml(paper.year)}</div>
              <div>
                <p class="paper-meta">${escapeHtml(paper.journal)}${paper.meta ? ` · ${escapeHtml(paper.meta)}` : ""}</p>
                <h2>${escapeHtml(paper.title)}</h2>
                <p class="paper-authors">${escapeHtml(paper.authors)}</p>
                ${figure}
                <p>${escapeHtml(paper.summary)}</p>
                ${doi}
              </div>
              <span class="tag">${escapeHtml(paper.theme)}</span>
            </article>`;
          })
          .join("");
      }
      if (countLabel) countLabel.textContent = totalLabel;
    };

    finder.addEventListener("submit", async (event) => {
      event.preventDefault();
      const data = new FormData(finder);
      const params = new URLSearchParams();
      ["q", "year", "theme"].forEach((key) => {
        const value = String(data.get(key) || "");
        if (value) params.set(key, value);
      });
      const query = params.toString();
      history.replaceState(null, "", query ? `${location.pathname}?${query}` : location.pathname);
      const response = await fetch(`/api/publications?${query}`);
      const payload = await response.json();
      const indexed = document.querySelector(".page-hero .kicker span:last-child")?.textContent || "";
      const total = indexed.match(/\d+/)?.[0] || "";
      paint(payload.papers, `${payload.count} showing${total ? ` · ${total} indexed` : ""}`);
    });
  }
})();
