# GovNadlan + GovMap Market Layer

אתר סטטי מבוסס Vue שמציג את GovMap, מדליק שכבה 235146, וצובע יישובים לפי יחס:

`עסקאות 2025 / ממוצע עסקאות שנתי 1999-2024`

## קבצים להעלאה ל-GitHub Pages

- `index.html`
- `settlements_flat.json`
- `settlements_wkt_2039.json`

## הרצה מקומית

מומלץ להריץ דרך שרת סטטי ולא לפתוח את הקובץ ישירות:

```bash
python -m http.server 8000
```

ואז לפתוח:

`http://localhost:8000`

## אינטגרציה עתידית ל-GovNadlan

כרגע הנתונים נטענים מקובץ מקומי. בהמשך יש להחליף את `fetchJson('settlements_flat.json')`
בקריאה ל-Backend שמחזיר סיכום שנתי לפי יישוב.
