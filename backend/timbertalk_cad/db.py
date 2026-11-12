"""Verbindung zur SQLite-Datei. B0 legt keine Tabellen an."""

from collections.abc import Iterator

from sqlalchemy import Engine
from sqlmodel import Session, create_engine, text

from timbertalk_cad.settings import get_settings


def get_engine() -> Engine:
    return create_engine(f"sqlite:///{get_settings().db_path}")


def get_session() -> Iterator[Session]:
    with Session(get_engine()) as session:
        yield session


def check_connection() -> bool:
    # Fehlt die Datei, geben wir False zurück. Wichtig: vorher prüfen,
    # denn SQLite würde eine fehlende Datei beim Verbinden sonst anlegen.
    if not get_settings().db_path.is_file():
        return False
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
