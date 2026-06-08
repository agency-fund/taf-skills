/* Entrance-animation driver. Pairs with anim.css.
   - Assigns staggered transition delays to [data-reveal] / [data-grow-w] / [data-grow-h]
     in DOM order (90ms steps, capped at 1.2s).
   - For grow elements, copies the inline width/height into --grow-w/--grow-h.
   - Starts after fonts are ready so nothing animates in a fallback font.
   - ?static=1 (or printing) renders the final state with no motion. */
(function () {
  var STEP = 0.09, CAP = 1.2;
  var els = document.querySelectorAll('[data-reveal], [data-grow-w], [data-grow-h]');
  var i, el, d;
  for (i = 0; i < els.length; i++) {
    el = els[i];
    d = Math.min(i * STEP, CAP);
    if (!el.style.getPropertyValue('--reveal-delay')) {
      el.style.setProperty('--reveal-delay', d.toFixed(2) + 's');
    }
    if (el.hasAttribute('data-grow-w') && el.style.width) {
      el.style.setProperty('--grow-w', el.style.width);
    }
    if (el.hasAttribute('data-grow-h') && el.style.height) {
      el.style.setProperty('--grow-h', el.style.height);
    }
  }
  var isStatic = /[?&]static=1/.test(location.search);
  function go() {
    if (isStatic) document.body.classList.add('anim-static');
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { document.body.classList.add('anim-go'); });
    });
  }
  if (isStatic) { document.body.classList.add('anim-static', 'anim-go'); return; }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(go);
    setTimeout(go, 700); // safety
  } else { go(); }
})();
