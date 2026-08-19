/*
 * Accessible tabs, following the WAI-ARIA Authoring Practices tab pattern.
 * Arrow keys move focus and selection; Home/End jump to first/last tab.
 * Selecting a tab updates the URL hash so a specific section can be linked
 * or bookmarked directly (e.g. syllabus.html#policies).
 */
(function () {
  "use strict";

  var tablist = document.querySelector('[role="tablist"]');
  if (!tablist) return;

  var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
  var panels = tabs.map(function (tab) {
    return document.getElementById(tab.getAttribute("aria-controls"));
  });

  function selectTab(newTab, moveFocus) {
    tabs.forEach(function (tab, i) {
      var selected = tab === newTab;
      tab.setAttribute("aria-selected", selected ? "true" : "false");
      tab.tabIndex = selected ? 0 : -1;
      panels[i].hidden = !selected;
    });

    if (moveFocus) {
      newTab.focus();
    }

    var targetId = newTab.getAttribute("data-hash");
    if (targetId && history.replaceState) {
      history.replaceState(null, "", "#" + targetId);
    }
  }

  tabs.forEach(function (tab, index) {
    tab.addEventListener("click", function () {
      selectTab(tab, false);
    });

    tab.addEventListener("keydown", function (event) {
      var newIndex = null;

      switch (event.key) {
        case "ArrowRight":
        case "ArrowDown":
          newIndex = (index + 1) % tabs.length;
          break;
        case "ArrowLeft":
        case "ArrowUp":
          newIndex = (index - 1 + tabs.length) % tabs.length;
          break;
        case "Home":
          newIndex = 0;
          break;
        case "End":
          newIndex = tabs.length - 1;
          break;
        default:
          return;
      }

      event.preventDefault();
      selectTab(tabs[newIndex], true);
    });
  });

  // Deep-link support: open the tab matching the URL hash, on load and
  // whenever the hash changes (e.g. a same-page link to #rubrics). A hash
  // can also target a specific heading *inside* a panel (e.g. #rrj-rubric)
  // — in that case the owning tab is selected and the heading itself is
  // scrolled to, rather than just the top of the panel.
  function selectTabFromHash() {
    var hash = window.location.hash.replace("#", "");
    if (!hash) return;

    var matchedTab = tabs.find(function (tab) {
      return tab.getAttribute("data-hash") === hash;
    });
    if (matchedTab) {
      selectTab(matchedTab, false);
      matchedTab.scrollIntoView({ block: "nearest", inline: "center" });
      return;
    }

    var target = document.getElementById(hash);
    if (!target) return;
    var panel = target.closest('[role="tabpanel"]');
    if (!panel) return;
    var panelIndex = panels.indexOf(panel);
    if (panelIndex === -1) return;

    selectTab(tabs[panelIndex], false);
    requestAnimationFrame(function () {
      target.scrollIntoView({ block: "start" });
    });
  }

  window.addEventListener("hashchange", selectTabFromHash);

  var initialHash = window.location.hash.replace("#", "");
  var initialTab = tabs.find(function (tab) {
    return tab.getAttribute("data-hash") === initialHash;
  });

  selectTab(initialTab || tabs[0], false);
})();
