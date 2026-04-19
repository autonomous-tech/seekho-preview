/**
 * Seekho Centralized Pricing — Single Source of Truth
 *
 * All prices marked TBD are Faryal's call. Best-faith placeholders pulled
 * from what's disclosed on her current site (extra-lesson and discount
 * amounts are verified from the existing FAQ; package totals are plausible
 * estimates and must be confirmed before launch).
 *
 * Usage in HTML:
 *   <span data-price="teach-me-everything-manual">Rs 35,000</span>
 *   <span data-price="extra-lesson-auto">Rs 2,000</span>
 *
 * Inner text is a fallback if JS doesn't load.
 */

var SEEKHO_PRICES = {
  // ---- Core packages (manual / automatic) — TBD-faryal ----
  // Teach Me Everything (full beginner programme)
  'teach-me-everything-manual': 35000,
  'teach-me-everything-auto':   40000,

  // Enhance My Skills (refresher / confidence build)
  'enhance-my-skills-manual':   22000,
  'enhance-my-skills-auto':     26000,

  // Student Bundle (discounted package for students)
  'student-bundle-manual':      15000,
  'student-bundle-auto':        18000,

  // ---- Add-ons (VERIFIED from seekhopakistan.com.pk FAQ) ----
  'extra-lesson-manual':         1800,
  'extra-lesson-auto':           2000,

  // ---- Discounts (VERIFIED from seekhopakistan.com.pk FAQ) ----
  'discount-own-auto-vehicle':   2000, // learn on your own auto vehicle
  'discount-no-pickup':          1800, // self pick-up/drop-off

  // ---- Booking ----
  'deposit':                      500
};

(function () {
  function formatPrice(amount) {
    return 'Rs ' + amount.toLocaleString('en-PK');
  }

  function populatePrices() {
    var els = document.querySelectorAll('[data-price]');
    for (var i = 0; i < els.length; i++) {
      var key = els[i].getAttribute('data-price');
      if (SEEKHO_PRICES[key] !== undefined) {
        els[i].textContent = formatPrice(SEEKHO_PRICES[key]);
      }
    }

    // Compute per-hour cost where requested
    var phEls = document.querySelectorAll('[data-per-hour]');
    for (var j = 0; j < phEls.length; j++) {
      var priceKey = phEls[j].getAttribute('data-per-hour');
      var hours = parseFloat(phEls[j].getAttribute('data-hours') || '0');
      if (SEEKHO_PRICES[priceKey] !== undefined && hours > 0) {
        var perHour = Math.round(SEEKHO_PRICES[priceKey] / hours);
        phEls[j].textContent = formatPrice(perHour) + '/hour';
      }
    }

    // Update JSON-LD Offer prices
    var schemas = document.querySelectorAll('script[type="application/ld+json"]');
    for (var k = 0; k < schemas.length; k++) {
      try {
        var data = JSON.parse(schemas[k].textContent);
        updateSchemaPrice(data);
        schemas[k].textContent = JSON.stringify(data, null, 2);
      } catch (e) { /* skip invalid JSON-LD */ }
    }
  }

  function updateSchemaPrice(obj) {
    if (!obj || typeof obj !== 'object') return;
    if (Array.isArray(obj)) {
      for (var i = 0; i < obj.length; i++) updateSchemaPrice(obj[i]);
      return;
    }
    if (obj['@type'] === 'Offer' && obj._priceKey && SEEKHO_PRICES[obj._priceKey] !== undefined) {
      obj.price = SEEKHO_PRICES[obj._priceKey];
      obj.priceCurrency = 'PKR';
    }
    for (var key in obj) if (obj.hasOwnProperty(key)) updateSchemaPrice(obj[key]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', populatePrices);
  } else {
    populatePrices();
  }
})();
