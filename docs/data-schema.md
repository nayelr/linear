# Data contract (`data/chapter-N.json`)

Each file is one chapter’s **Supplementary Exercises**, problem **1** (True/False parts).

## Shape

```json
{
  "id": 1,
  "title": "Chapter 1 — Supplementary exercises",
  "meta": { "pdfPage": 105, "book": "Lay, Linear Algebra and Its Applications" },
  "items": [
    { "id": "a", "label": "1a", "text": "…", "answer": false }
  ]
}
```

- `id` — chapter number (1–4).
- `items[].id` — lowercase part letter (`a`–`z` or `a`–`t` depending on chapter).
- `items[].label` — display id (e.g. `1a`).
- `items[].text` — statement only (no “True or False” suffix).
- `items[].answer` — `true` if the statement is **mathematically true**, `false` otherwise (matches the answer key).

## Files

| File | Parts | PDF page (exercises) |
|------|-------|----------------------|
| `chapter-1.json` | a–z | 105 |
| `chapter-2.json` | a–p | 177 (all of problem 1 on this page) |
| `chapter-3.json` | a–p | 202–203 |
| `chapter-4.json` | a–t | 279–280 |
