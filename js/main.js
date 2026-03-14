// js/main.js - Bevel & Gold Interactons

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');

  if (menuToggle && navLinks) {
    const closeMenu = () => {
      menuToggle.setAttribute('aria-expanded', 'false');
      menuToggle.setAttribute('aria-label', 'Open menu');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    };

    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeMenu();
      } else {
        menuToggle.setAttribute('aria-expanded', 'true');
        menuToggle.setAttribute('aria-label', 'Close menu');
        navLinks.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });

    // Close menu when a navigation link is clicked
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMenu);
    });
  }

  // Accordion Logic
  const accordions = document.querySelectorAll('.accordion');

  accordions.forEach(accordion => {
    const header = accordion.querySelector('.accordion-header');
    const content = accordion.querySelector('.accordion-content');

    if (header && content) {
      header.addEventListener('click', () => {
        const isExpanded = header.getAttribute('aria-expanded') === 'true';

        // Ensure only one accordion closes smoothly (optional, remove to allow multiple open)
        /*
        accordions.forEach(a => {
            const h = a.querySelector('.accordion-header');
            const c = a.querySelector('.accordion-content');
            h.setAttribute('aria-expanded', 'false');
            c.setAttribute('aria-hidden', 'true');
        });
        */

        // Toggle current accordion
        header.setAttribute('aria-expanded', !isExpanded);
        content.setAttribute('aria-hidden', isExpanded);
      });
    }
  });

  // Smooth Scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      // Only prevent default if it's a valid ID selector
      if (targetId !== '#' && targetId.startsWith('#')) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: 'smooth'
          });
          // Update focus for accessibility
          targetElement.setAttribute('tabindex', '-1');
          targetElement.focus();
        }
      }
    });
  });
});
