# B00 – Skelett

## Ziel
Das Repo hat ein lauffähiges Grundgerüst: Server, Startseite, Datenbankprüfung, Tests und CI.

## Was der Zimmerer danach kann
- Noch nichts Fachliches. Er sieht im Browser „TimberTalk CAD läuft“ und ob die Datenbank gefunden wurde.

## Abnahme
- [ ] `uvicorn timbertalk_cad.main:app --reload` startet ohne Fehler.
- [ ] `http://127.0.0.1:8000/` zeigt „TimberTalk CAD läuft“ und den Datenbank-Status.
- [ ] `GET /api/cad/health` liefert `{"status": "ok", "db": "verbunden"}` bzw. `"nicht gefunden"`.
- [ ] Fehlt die Datenbank-Datei, wird sie nicht angelegt.
- [ ] `pytest` ist lokal und in GitHub Actions grün.

## Nicht dabei
- Tabellen
- Entscheidungsbaum
- KI
- CAD
- Anbindung an Team A (`bridge.py`)

## Neues Konzept fürs Team
- **APIRouter mit Präfix `/api/cad`**: Alle Endpunkte von Modul B hängen an einem Router. Team A kann ihn später mit einer Zeile (`app.include_router(router)`) in seine App einbauen.
- **Einstellungen aus der Umgebung**: Der Pfad zur Datenbank kommt aus `TIMBERTALK_DB_PATH` (oder `.env`). So zeigen Tests auf eine Testdatei, ohne Code zu ändern.
