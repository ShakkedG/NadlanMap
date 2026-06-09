# GovMap Vue - גרסה סטטית מוכנה להעלאה

הקובץ `index.html` הוא קובץ HTML אמיתי ולא קובץ CSS.

כדי להעלות ל-GitHub Pages, העלה את שלושת הקבצים הבאים לאותה תיקייה:

- `index.html`
- `settlements_flat.json`
- `settlements_wkt_2039.json`

האתר טוען את Vue דרך CDN, טוען את GovMap, מדליק את שכבת `235146`, ומצייר מעליה פוליגונים צבעוניים לפי `sid`.

בדיקה מקומית:

```bash
python -m http.server 8000
```

ואז לפתוח:

```text
http://localhost:8000
```

פתיחה ישירה ב-double click על `index.html` לא מומלצת כי הדפדפן בדרך כלל חוסם טעינת JSON מקובץ מקומי.
