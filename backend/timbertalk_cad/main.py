"""Startet FastAPI und liefert API und Frontend aus.

Start (im Ordner backend/): uvicorn timbertalk_cad.main:app --reload
"""

from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from timbertalk_cad.db import check_connection

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"

# Alle Endpunkte von Modul B liegen in diesem Router,
# damit Team A ihn später in seine App einbinden kann.
router = APIRouter(prefix="/api/cad")


@router.get("/health")
def health() -> dict:
    db_status = "verbunden" if check_connection() else "nicht gefunden"
    return {"status": "ok", "db": db_status}


app = FastAPI(title="TimberTalk CAD")
app.include_router(router)
# Zuletzt einbinden: "/" fängt sonst alle Pfade ab.
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
