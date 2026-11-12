"""Tests für GET /api/cad/health."""

import sqlite3

from fastapi.testclient import TestClient

from timbertalk_cad.main import app

client = TestClient(app)


def test_health_with_existing_db(tmp_path, monkeypatch):
    db_file = tmp_path / "timbertalk.db"
    sqlite3.connect(db_file).close()  # leere SQLite-Datei anlegen
    monkeypatch.setenv("TIMBERTALK_DB_PATH", str(db_file))

    response = client.get("/api/cad/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "verbunden"}


def test_health_with_missing_db(tmp_path, monkeypatch):
    db_file = tmp_path / "fehlt.db"
    monkeypatch.setenv("TIMBERTALK_DB_PATH", str(db_file))

    response = client.get("/api/cad/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "nicht gefunden"}
    assert not db_file.exists()  # die Datei darf nicht angelegt werden
