(function () {
  document.documentElement.classList.add('js');

  var header = document.querySelector('.site-header');
  var body = document.body;

  // Solid header after scrolling
  function onScroll() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 40);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  function setMenu(open) {
    body.classList.toggle('menu-open', open);
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (toggle) {
    toggle.addEventListener('click', function () { setMenu(!body.classList.contains('menu-open')); });
    // close after choosing a link (also handles in-page anchors like #contact)
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.matchMedia('(min-width: 921px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  // "What we do" dropdown: click / keyboard, hover on desktop
  document.querySelectorAll('.drop').forEach(function (drop) {
    var btn = drop.querySelector('button');
    var close = function () { drop.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); };
    var open = function () { drop.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); };
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      drop.classList.contains('open') ? close() : open();
    });
    var fine = window.matchMedia('(hover: hover) and (min-width: 921px)');
    var t;
    drop.addEventListener('mouseenter', function () { if (fine.matches) { clearTimeout(t); open(); } });
    drop.addEventListener('mouseleave', function () { if (fine.matches) { t = setTimeout(close, 120); } });
    document.addEventListener('click', function (e) { if (!drop.contains(e.target) && fine.matches) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { close(); btn.focus(); } });
  });

  // Service rail arrows
  document.querySelectorAll('[data-rail]').forEach(function (ctrl) {
    var rail = document.getElementById(ctrl.getAttribute('data-rail'));
    if (!rail) return;
    ctrl.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        var tile = rail.querySelector('.tile');
        var step = tile ? tile.getBoundingClientRect().width + 16 : 320;
        rail.scrollBy({ left: b.dataset.dir === 'prev' ? -step : step, behavior: 'smooth' });
      });
    });
  });

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Contact form — front-end only for now
  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      var service = form.querySelector('input[name="service"]:checked');
      if (!service) {
        msg.textContent = 'Please choose the service you are interested in.';
        msg.classList.add('show');
        return;
      }
      msg.textContent = 'Thanks — your message is ready to send. (Form handling is not connected yet in this redesign preview.)';
      msg.classList.add('show');
    });
  });
})();
