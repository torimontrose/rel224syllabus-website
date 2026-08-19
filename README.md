# REL 224 Syllabus Website — Editing Guide

This is a plain HTML/CSS/JavaScript website. There's no build step, no
installs, and no command line needed to edit it — just open the file in a
text editor, change the text, save, and refresh your browser.

## Files

```
syllabus website/
├── index.html      ← all the syllabus content lives here
├── css/styles.css   ← colors, fonts, spacing (rarely needs editing)
├── js/tabs.js        ← makes the tabs work (you shouldn't need to touch this)
└── README.md         ← this file
```

**You will do almost all of your editing inside `index.html`.**

## How to edit the content

1. Open `index.html` in any text editor (TextEdit in plain-text mode,
   VS Code, Notepad, etc.).
2. Use Find (Cmd+F / Ctrl+F) to search for `EDIT:` — every spot that still
   needs your attention has an `<!-- EDIT: ... -->` comment above or next
   to it. There are only a few left, since this site was built from your
   real Fall 2025 syllabus content.
3. Save the file, then open `index.html` in your browser (double-click it,
   or drag it into a browser window) to see your changes.

All the placeholder items from initial setup (final exam date/time,
location, email address) have been confirmed and filled in. Search for
`EDIT:` in `index.html` if you want to check for anything new.

### Editing a table (grading breakdown, schedule, rubric)

Tables are built from repeating blocks that look like this:

```html
<tr><td>1</td><td>Tue. 8/25</td><td>Welcome!</td><td>...</td><td>RRJ 1*</td><td>Classes begin</td></tr>
```

Each `<tr>...</tr>` is one row. Each `<td>...</td>` inside it is one cell.
To edit a class session, find its row (search the date) and edit the text
inside the `<td>` tags.

### Editing a policy block

Policies live in blocks like this — just edit the text between the tags:

```html
<div class="policy-block">
  <h3>Course Activity Recordings</h3>
  <p>Your policy text goes here.</p>
</div>
```

### The Ashoka Game tab

Everything about the *Ashoka* role-playing game — the session schedule,
position paper prompt, citation checklist, and its dedicated grading
rubric — lives together on its own tab so it's self-contained. The
Graded Elements, Policies, and Rubrics tabs link over to it wherever the
old syllabus referenced Ashoka-specific content.

## Publishing the site

This site is static, so you can host it almost anywhere for free:

- **GitHub Pages** — push this folder to a GitHub repo and enable Pages in
  the repo settings (same process used for the FYW 1323 syllabus site).
- **Your university's web space** — many schools give faculty a personal
  web folder (ask your IT department).
- **Netlify / Vercel** — drag-and-drop the folder onto their dashboard.

You can also just email students the `index.html` file, or post it to your
LMS (Moodle) as a file — it will open correctly in any browser without
needing to be "hosted" anywhere.

## Accessibility notes (please keep these intact)

This site was built to meet WCAG accessibility guidelines for students
with disabilities:

- Tabs work with keyboard navigation (arrow keys, Home/End) and are
  announced correctly by screen readers.
- There's a "Skip to main content" link for keyboard users.
- Color contrast between text and backgrounds meets AA standards.
- Tables use proper header cells (`<th scope="col">`) so screen readers
  can announce column headers with each cell.
- The print stylesheet forces black-on-white text for anyone who prints
  the syllabus.
- The decorative mandala background (lotus-petal ring, gated square,
  concentric circles) is marked `aria-hidden="true"` so screen readers
  skip over it entirely — it's purely visual.

If you add new content, try to:
- Keep heading levels in order (don't skip from `<h2>` to `<h4>`).
- Use real table markup (`<table>`, `<tr>`, `<td>`) for tabular data
  rather than trying to fake it with spaces or line breaks.

## Changing colors or fonts

Open `css/styles.css` and look at the top of the file, inside the `:root {
... }` block. Every color used on the site is defined there once — change
a value there (e.g. `--saffron: #d9822b;`) and it updates everywhere that
color is used.
