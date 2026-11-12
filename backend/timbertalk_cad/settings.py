"""Einstellungen aus Umgebungsvariablen bzw. .env."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Dieselbe SQLite-Datei, die Team A (Modul A) nutzt.
    # Umgebungsvariable: TIMBERTALK_DB_PATH
    db_path: Path = Path("data/timbertalk.db")

    model_config = SettingsConfigDict(env_prefix="TIMBERTALK_", env_file=".env")


def get_settings() -> Settings:
    # Bei jedem Aufruf neu lesen, damit Tests die Umgebungsvariable setzen können.
    return Settings()
