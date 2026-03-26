# Supplementary True/False quiz

Open the app with a local static server (required so `fetch` can load JSON):

```bash
cd /Users/nayelr/Desktop/MiscCS/linear
python3 -m http.server 8765
```

Then visit `http://localhost:8765`.

## Data

- Question text was aligned to the PDF (Chapter 1 exercises on **page 105**; other chapters: 177, 202–203, 279–280).
- Answers match the provided answer-key images.

To change answers or wording, edit `data/chapter-1.json` … `data/chapter-4.json` (see `docs/data-schema.md`).

## Optional: regenerate combined JSON

```bash
python3 scripts/merge_data.py
```

Writes `data/all.json` (not required for the default UI).
