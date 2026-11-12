# TimberTalk CAD – Modul B

Modul B (LLM-CAD) lässt eine KI die Fragen eines Entscheidungsbaums aus der Datenbank beantworten und baut daraus Modell, CAD-Datei und Stückliste.

## Regeln
- Die API ruft nur den Service auf. Logik steht in `service.py` als normale Funktionen.
- Geld und Mengen sind `Decimal`, nie `float`.
- Kein Feature ohne Test und Steckbrief (`docs/features/`).
- Die KI wählt, der Code baut: Die KI liefert nur Antworten auf Knoten aus der Datenbank. Geometrie und Stückliste entstehen nur im Generator.
- Was gefragt wird, steht in der Datenbank – nie fest im Code oder Prompt.
- Maße in Millimeter als ganze Zahl (`int`).
- Eigene Tabellen von Team B tragen die Vorsilbe `cad_`. Tabellen von Team A werden nur gelesen.
- Bezeichner auf Englisch, Kommentare und Doku auf Deutsch.
- Funktionen statt Klassen, wo es geht. Keine versteckte Magie (keine Events, keine eigenen Dekoratoren).

## Ziel-Ordnerstruktur (noch nicht anlegen)
```
backend/timbertalk_cad/
├── features/
│   ├── templates/   # je models.py, service.py, api.py, test_*.py
│   ├── designs/
│   ├── assistant/
│   └── bom/
├── generators/      # Parameter → Bauteilliste (ohne CAD)
├── cad/             # Adapter FreeCAD/CadQuery, Export
├── bridge.py        # einzige Stelle, die Team A kennt
├── seeds/           # Entscheidungsbäume als YAML
└── migrations/
```

## Befehle (im Ordner `backend/`)
```
uv venv -p 3.12 && uv pip install -e ".[dev]"   # installieren
uv run uvicorn timbertalk_cad.main:app --reload  # starten → http://127.0.0.1:8000
uv run pytest                                     # testen
```

Baue nur, was im Steckbrief steht. Keine Vorarbeit für spätere Features.
