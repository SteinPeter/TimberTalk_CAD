# TimberTalk CAD

Modul B von TimberTalk: Eine KI beantwortet einen Entscheidungsbaum, und daraus entstehen ein parametrisches Modell, eine CAD-Datei und die Stückliste.
Das Repo läuft später als Addon und liest die SQLite-Datenbank von Modul A (Team A).

## Starten und testen
Im Ordner `backend/`:
```
uv venv -p 3.12 && uv pip install -e ".[dev]"   # installieren
uv run uvicorn timbertalk_cad.main:app --reload  # starten → http://127.0.0.1:8000
uv run pytest                                     # testen
```
Der Datenbankpfad steht in `TIMBERTALK_DB_PATH` (siehe `.env.example`, Standard `data/timbertalk.db` relativ zu `backend/`).

## Glossar
- **Vorlage** – ein Bauteiltyp, den man entwerfen kann (z. B. Carport), mit seinem Entscheidungsbaum.
- **Entscheidungsbaum** – die Fragen zu einer Vorlage und wie sie aufeinander folgen; steht in der Datenbank.
- **Knoten** – eine einzelne Frage im Entscheidungsbaum mit ihren erlaubten Antworten.
- **Entwurf** – ein konkretes Projekt: die gegebenen Antworten und die daraus berechneten Parameter.
- **Bauteilliste** – alle Bauteile eines Entwurfs mit Maßen in mm, erzeugt vom Generator.
- **Stückliste** – die zusammengefasste Bestellliste aus der Bauteilliste (Material, Menge, Preis).
