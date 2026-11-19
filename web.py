"""Sirve el frontend y conecta /api con la aplicación FastAPI original."""

from pathlib import Path

from starlette.responses import FileResponse

from alquilometro_api.app import app as backend

FRONTEND = Path(__file__).resolve().parent / "frontend"
ASSETS = {
    "/": ("index.html", "text/html"),
    "/index.html": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
    "/app.js": ("app.js", "text/javascript"),
}


async def app(scope, receive, send):
    if scope["type"] == "http":
        path = scope["path"]
        if path.startswith("/api/"):
            scope = {**scope, "path": path[4:]}
            if "raw_path" in scope:
                scope["raw_path"] = scope["raw_path"][4:]
        elif scope["method"] in {"GET", "HEAD"} and path in ASSETS:
            name, media_type = ASSETS[path]
            response = FileResponse(FRONTEND / name, media_type=media_type)
            await response(scope, receive, send)
            return

    await backend(scope, receive, send)
