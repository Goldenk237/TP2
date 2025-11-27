// Minimal accessible JavaScript for header
(function(){
  'use strict';

  const toggleBtn = document.querySelector('.nav-toggle');
  const navList = document.querySelector('#main-navigation');
  const header = document.querySelector('.site-header');

  if (toggleBtn && navList) {
    toggleBtn.addEventListener('click', function () {
      const expanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', String(!expanded));
      const newState = !expanded;
      navList.dataset.visible = String(newState);
      toggleBtn.setAttribute('aria-label', newState ? 'Fermer le menu' : 'Ouvrir le menu');

      if (newState) {
        // Move focus to first link in menu
        const first = navList.querySelector('a');
        if (first) first.focus();
      } else {
        // Return focus to the button
        toggleBtn.focus();
      }
    });

    // Close menu when clicking outside on small screens
    document.addEventListener('click', function (e) {
      const isClickInside = navList.contains(e.target) || toggleBtn.contains(e.target);
      if (!isClickInside && navList.dataset.visible === 'true') {
        toggleBtn.click();
      }
    });

    // Close menu with Escape key
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && navList.dataset.visible === 'true') {
        toggleBtn.click();
      }
    });
  }

  // Sticky header compacting on scroll
  if (header) {
    let lastScroll = 0;
    window.addEventListener('scroll', function () {
      const current = window.scrollY;
      if (current > 60) {
        header.classList.add('site-header--compact');
      } else {
        header.classList.remove('site-header--compact');
      }
      lastScroll = current;
    });
  }
})();
