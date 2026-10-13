(function () {
  'use strict';
  var c = window.SHOP_CONFIG || {};

  // Textos preenchidos a partir de js/config.js
  document.querySelectorAll('[data-contact]').forEach(function (el) {
    var v = c[el.getAttribute('data-contact')];
    if (!v) return;
    el.textContent = el.getAttribute('data-contact') === 'instagram' ? '@' + v : v;
    el.classList.remove('contact-placeholder');
  });

  // Botões/links de WhatsApp: só aparecem quando o número está configurado
  var digits = String(c.whatsapp || '').replace(/\D/g, '');
  if (digits) {
    document.querySelectorAll('[data-link="whatsapp"]').forEach(function (el) {
      var msg = el.getAttribute('data-msg');
      el.href = 'https://wa.me/' + digits + (msg ? '?text=' + encodeURIComponent(msg) : '');
      el.target = '_blank';
      el.rel = 'noopener';
      el.hidden = false;
    });
  }

  // Ano do rodapé
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
