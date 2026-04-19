/**
 * Seekho — PostHog + CRO event instrumentation
 *
 * Single include for every HTML page. Handles:
 *   - PostHog init (one canonical project key)
 *   - Delegated clicks on any [data-ph-event] element
 *       (captures the event name + every data-ph-* as a property)
 *   - Automatic whatsapp_click on any link to wa.me / api.whatsapp.com
 *   - scroll_50 and scroll_75 milestones (fired once each per pageview)
 *   - form_start on first focus into any <form> field
 *   - faq_expand whenever a FAQ item opens (class="faq-item" toggling "open")
 *
 * Put this file at site root and include on every page:
 *   <script src="/analytics.js" defer></script>
 *
 * Swap PH_PROJECT_KEY for the real PostHog project key before launch.
 */

(function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // 1. PostHog init
  // ---------------------------------------------------------------------------
  var PH_PROJECT_KEY = 'phc_SEEKHO_PROJECT_KEY'; // TBD-replace-on-launch
  var PH_HOST = 'https://us.i.posthog.com';

  // PostHog snippet (inlined so we don't need a separate <script> tag per page)
  !function (t, e) {
    var o, n, p, r;
    e.__SV || (window.posthog = e, e._i = [], e.init = function (i, s, a) {
      function g(t, e) { var o = e.split('.'); 2 == o.length && (t = t[o[0]], e = o[1]); t[e] = function () { t.push([e].concat(Array.prototype.slice.call(arguments, 0))); }; }
      (p = t.createElement('script')).type = 'text/javascript';
      p.async = !0;
      p.src = s.api_host.replace('.i.posthog.com', '-assets.i.posthog.com') + '/static/array.js';
      (r = t.getElementsByTagName('script')[0]).parentNode.insertBefore(p, r);
      var u = e;
      for (void 0 !== a ? u = e[a] = [] : a = 'posthog', u.people = u.people || [], u.toString = function (t) { var e = 'posthog'; return 'posthog' !== a && (e += '.' + a), t || (e += ' (stub)'), e; }, u.people.toString = function () { return u.toString(1) + '.people (stub)'; }, o = 'init capture register register_once register_for_session unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group identify setPersonProperties setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags resetGroups onFeatureFlags addFeatureFlagsHandler onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep'.split(' '), n = 0; n < o.length; n++) g(u, o[n]);
      e._i.push([i, s, a]);
    }, e.__SV = 1);
  }(document, window.posthog || []);

  if (!window.__seekho_ph_initialized) {
    window.posthog.init(PH_PROJECT_KEY, {
      api_host: PH_HOST,
      defaults: '2026-01-30',
      capture_pageview: true
    });
    window.__seekho_ph_initialized = true;
  }

  // ---------------------------------------------------------------------------
  // 2. Helpers
  // ---------------------------------------------------------------------------
  function capture(event, props) {
    try {
      if (window.posthog && typeof window.posthog.capture === 'function') {
        window.posthog.capture(event, props || {});
      }
    } catch (e) { /* no-op */ }
  }

  function pageName() {
    var path = (window.location.pathname || '/').replace(/\/$/, '');
    if (!path || path === '') return 'home';
    return path.split('/').pop().replace(/\.html$/, '');
  }

  function dataProps(el) {
    var out = { page: pageName() };
    if (!el || !el.attributes) return out;
    for (var i = 0; i < el.attributes.length; i++) {
      var a = el.attributes[i];
      if (a.name.indexOf('data-ph-') === 0 && a.name !== 'data-ph-event') {
        out[a.name.slice('data-ph-'.length).replace(/-/g, '_')] = a.value;
      }
    }
    // Include element context for debugging
    if (el.tagName === 'A' && el.href) out.href = el.href;
    if (el.textContent) out.label = el.textContent.trim().slice(0, 80);
    return out;
  }

  // Find the nearest ancestor that carries data-ph-event
  function closestTracked(target) {
    var el = target;
    while (el && el !== document.body) {
      if (el.nodeType === 1 && el.hasAttribute && el.hasAttribute('data-ph-event')) return el;
      el = el.parentNode;
    }
    return null;
  }

  // ---------------------------------------------------------------------------
  // 3. Delegated click handler (all [data-ph-event] + WhatsApp auto-detect)
  // ---------------------------------------------------------------------------
  document.addEventListener('click', function (ev) {
    var tracked = closestTracked(ev.target);

    // Auto-detect WhatsApp links that don't have an explicit data-ph-event
    var anchor = ev.target && ev.target.closest ? ev.target.closest('a') : null;
    if (anchor && anchor.href && /wa\.me\/|api\.whatsapp\.com\//.test(anchor.href)) {
      var waProps = dataProps(anchor);
      waProps.source = (tracked && tracked.getAttribute('data-ph-event')) || waProps.source || 'auto';
      capture('whatsapp_click', waProps);
      // Fall through so an explicit data-ph-event on the same element still fires
    }

    if (tracked) {
      var eventName = tracked.getAttribute('data-ph-event');
      if (eventName) capture(eventName, dataProps(tracked));
    }
  }, { passive: true });

  // ---------------------------------------------------------------------------
  // 4. Scroll milestones
  // ---------------------------------------------------------------------------
  var scrollFired = { 50: false, 75: false };
  function onScroll() {
    var doc = document.documentElement;
    var scrollTop = window.scrollY || doc.scrollTop || 0;
    var viewport = window.innerHeight || doc.clientHeight || 0;
    var full = Math.max(doc.scrollHeight, document.body.scrollHeight) - viewport;
    if (full <= 0) return;
    var pct = (scrollTop / full) * 100;
    if (!scrollFired[50] && pct >= 50) {
      scrollFired[50] = true;
      capture('scroll_50', { page: pageName() });
    }
    if (!scrollFired[75] && pct >= 75) {
      scrollFired[75] = true;
      capture('scroll_75', { page: pageName() });
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  // ---------------------------------------------------------------------------
  // 5. form_start — first interaction with any <form> input
  // ---------------------------------------------------------------------------
  var formStarted = {};
  document.addEventListener('focusin', function (ev) {
    var field = ev.target;
    if (!field || !field.tagName) return;
    if (!/^(INPUT|SELECT|TEXTAREA)$/.test(field.tagName)) return;
    // Skip hidden / honeypot fields
    if (field.type === 'hidden' || field.closest('.honey')) return;
    var form = field.closest('form');
    var formId = form ? (form.id || form.name || 'form') : 'no-form';
    if (formStarted[formId]) return;
    formStarted[formId] = true;
    capture('form_start', { page: pageName(), form: formId });
  });

  // ---------------------------------------------------------------------------
  // 6. faq_expand — whenever a FAQ item opens (class="faq-item" gains "open")
  //    The pages toggle `.open` on `.faq-item` / `.faq-item-b`; we listen for
  //    the click on the question button and report.
  // ---------------------------------------------------------------------------
  document.addEventListener('click', function (ev) {
    var btn = ev.target && ev.target.closest ? ev.target.closest('.faq-q, .faq-q-b') : null;
    if (!btn) return;
    var item = btn.closest('.faq-item, .faq-item-b');
    if (!item) return;
    // Defer one tick so the page's own toggle handler sets `.open` first.
    setTimeout(function () {
      if (item.classList.contains('open')) {
        var label = (btn.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 120);
        capture('faq_expand', { page: pageName(), question: label });
      }
    }, 0);
  }, { passive: true });

  // ---------------------------------------------------------------------------
  // 7. Expose a tiny helper so page-level scripts can piggyback without
  //    re-implementing the PostHog guard.
  // ---------------------------------------------------------------------------
  window.seekhoTrack = capture;
})();
