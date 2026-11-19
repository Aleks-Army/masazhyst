# Масажист · Masazhyst — Combat Medic · TCCC Instructor

**Live:** https://aleks-army.github.io/masazhyst/ · **EN:** https://aleks-army.github.io/masazhyst/en/

> Чернетка / Draft: дати, події, назви сертифікатів і контакти позначені `[у дужках]` і будуть уточнені.

## UA
Сайт-візитка бойового медика та інструктора з тактичної медицини (TCCC). Статичний сайт без залежностей: `index.html` (українська), `en/index.html` (англійська), спільні `assets/`.

Текст лежить у `src/content_uk.py` та `src/content_en.py`; плейсхолдери записуються як `⟦текст⟧`. Перезбірка й перевірка посилань:

```bash
python3 src/build.py      # оновлює index.html та en/index.html
python3 src/linkcheck.py  # перевіряє внутрішні посилання
```

OPSEC: лише позивний — без імені, обличчя, підрозділів, дат ротацій і місць. Сайт не є офіційним ресурсом ЗСУ чи НАТО і не заявляє про сертифікацію НАТО.

## EN
Portfolio site of a Ukrainian combat medic and TCCC instructor. Dependency-free static site; copy lives in `src/content_*.py`, rebuild with `python3 src/build.py`.

OPSEC: call sign only — no name, face, units, rotation dates or locations. Not an official site of the Armed Forces of Ukraine or NATO; no NATO certification is claimed.

## License
Code and site content: MIT (see `LICENSE`). Fonts in `assets/fonts/` (Unbounded, Onest, JetBrains Mono) are under the SIL Open Font License 1.1.
