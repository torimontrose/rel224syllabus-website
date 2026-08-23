/*
 * "What's next?" button: jumps to the Weekly Schedule tab and highlights
 * the current week's row(s). Before the term starts it shows the first
 * week; after the term ends it shows the last week.
 */
(function () {
  "use strict";

  var btn = document.getElementById("whats-next-btn");
  if (!btn) return;

  function parseLocalDate(iso) {
    var parts = iso.split("-").map(Number);
    return new Date(parts[0], parts[1] - 1, parts[2]);
  }

  function startOfDay(d) {
    return new Date(d.getFullYear(), d.getMonth(), d.getDate());
  }

  function mondayOf(d) {
    var day = d.getDay(); // 0 = Sun ... 6 = Sat
    var diff = day === 0 ? -6 : 1 - day;
    var monday = new Date(d);
    monday.setDate(d.getDate() + diff);
    return monday;
  }

  btn.addEventListener("click", function () {
    var rows = Array.prototype.slice.call(
      document.querySelectorAll(".schedule-table tbody tr[data-date]")
    );
    if (!rows.length) return;

    var dated = rows.map(function (row) {
      return { row: row, date: parseLocalDate(row.getAttribute("data-date")) };
    });
    dated.sort(function (a, b) { return a.date - b.date; });

    var today = startOfDay(new Date());
    var first = dated[0].date;
    var last = dated[dated.length - 1].date;

    // Before the term, show its first week; after, show its last week.
    var anchor = today < first ? first : (today > last ? last : today);

    var monday = mondayOf(anchor);
    var sunday = new Date(monday);
    sunday.setDate(monday.getDate() + 6);

    var thisWeek = dated.filter(function (d) {
      return d.date >= monday && d.date <= sunday;
    });

    var target = thisWeek;
    if (!target.length) {
      var upcoming = dated.filter(function (d) { return d.date >= anchor; });
      target = upcoming.length ? [upcoming[0]] : [dated[dated.length - 1]];
    }

    var scheduleTab = document.getElementById("tab-schedule");
    if (scheduleTab && scheduleTab.getAttribute("aria-selected") !== "true") {
      scheduleTab.click();
    }

    window.requestAnimationFrame(function () {
      target[0].row.scrollIntoView({ behavior: "smooth", block: "center" });
      target.forEach(function (d) {
        d.row.classList.remove("schedule-row-highlight");
        // eslint-disable-next-line no-unused-expressions
        d.row.offsetWidth; // restart animation if clicked again quickly
        d.row.classList.add("schedule-row-highlight");
      });
    });
  });
})();
