/*
 * Replaces the Creative theme's creative.js, which required jQuery, Bootstrap's
 * JS bundle, jquery-easing (for "easeInOutExpo") and magnific-popup (for a
 * portfolio lightbox this site does not have). Dropping those four libraries
 * removes ~170KB and four third-party requests.
 *
 * Anchor scrolling is deliberately NOT handled here: `scroll-behavior` and
 * `scroll-margin-top` in main.scss do it natively, which also gets a cold load
 * on /#work right. That leaves only three things that genuinely need script.
 */
(function () {
  'use strict';

  var nav = document.getElementById('mainNav');
  var toggler = document.querySelector('.navbar-toggler');
  var collapse = document.getElementById('navbarResponsive');

  // 1. Mobile nav toggle. Bootstrap's CSS already styles .collapse / .show and
  //    forces the menu visible at >=lg, so only the class toggle is needed.
  if (toggler && collapse) {
    toggler.addEventListener('click', function () {
      var open = collapse.classList.toggle('show');
      toggler.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    // Close it again once a link inside has been followed.
    collapse.addEventListener('click', function (e) {
      if (!e.target.closest('a')) return;
      collapse.classList.remove('show');
      toggler.setAttribute('aria-expanded', 'false');
    });
  }

  // 2. Solidify the navbar once the page is scrolled.
  function onScroll() {
    if (nav) nav.classList.toggle('navbar-scrolled', window.pageYOffset > 100);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // 3. Sticky mobile CTA: reveal once the hero is behind us, and hide again
  //    while the contact section is on screen so it never doubles up.
  var sticky = document.getElementById('stickyCta');
  if (sticky) {
    var hero = document.querySelector('header.masthead');
    var contact = document.querySelector('.contact-section');

    // Driven off scroll position rather than IntersectionObserver so the bar
    // has a correct state on first paint instead of waiting for a callback.
    function syncSticky() {
      var y = window.pageYOffset;
      var pastHero = hero ? y > hero.offsetHeight - 80 : true;
      var atContact = false;
      if (contact) {
        var top = contact.getBoundingClientRect().top + y;
        atContact = y + window.innerHeight > top + 120;
      }
      sticky.classList.toggle('is-hidden', !pastHero || atContact);
    }

    syncSticky();
    window.addEventListener('scroll', syncSticky, { passive: true });
    window.addEventListener('resize', syncSticky, { passive: true });
  }

  // 4. Highlight the nav item for the section currently in view.
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('#mainNav .navbar-nav a[href^="#"]');
  if (sections.length && navLinks.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (link) {
          link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { threshold: 0.4 });
    sections.forEach(function (s) { observer.observe(s); });
  }
})();
