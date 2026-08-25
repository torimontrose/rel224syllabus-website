# Print PDF syllabus generator

Generates the magazine-style print PDF from the exact text on the live site
(re-transcribed by hand into `rel224_data.py` / `build_rel224.py` — if the
live site's `index.html` changes, these files need to be updated to match).

## Regenerate the PDF

```
python3 build_rel224.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-margins \
  --print-to-pdf="REL224-Syllabus.pdf" --print-to-pdf-no-header \
  "file://$(pwd)/rel224-syllabus.html"
```

Output: `REL224-Syllabus.pdf`, plus `rel224-syllabus.html` (intermediate,
safe to ignore/delete and regenerate).

## Files

- `print-system.css` — shared component library (also used by FYW 1323 and
  REL 320's generators; identical copy in each repo, not linked)
- `gen_schedule.py` — shared schedule-table HTML generator
- `build_rel224.py` — page layout/content for this course
- `rel224_data.py` — schedule row data (and Ashoka game session dates),
  transcribed verbatim from the site

There is no cover photo for this course (none exists in the repo), so the
cover uses a small line-art mandala reproduced from the site's own
decorative SVG motif instead of a photograph.

## Rules this must follow (see project memory for full detail)

- White page background (ink-saving for printing) — small dark accent
  blocks (cover hero, schedule title bar) are fine to keep.
- Every line of prose/schedule content must match the live site **exactly**
  — no paraphrasing, no cuts.
- After any rebuild, verify every page's rendered content against the site
  text programmatically (extract PDF text via PyMuPDF, check for expected
  phrases + check no page's content exceeds ~780pt of the 792pt page height)
  before treating it as done.
