"""
Vercel serverless entry point for the YT Music API.

Exposes a **handler** compatible with the AWS‑Lambda interface that
Vercel’s Python runtime expects, by wrapping the FastAPI **app**
defined in *src/main.py* with **Mangum**.
"""
from pathlib import Path
import sys

from mangum import Mangum  # type: ignore

# Ensure *src* is importable
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.main import app as fastapi_app  # noqa: E402

# Exported object Vercel looks for
handler = Mangum(fastapi_app)

# Local dev helper: `python api/index.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.index:fastapi_app", host="0.0.0.0", port=8000, reload=True)
