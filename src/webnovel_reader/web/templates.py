# Setup templates
from pathlib import Path

from fastapi.templating import Jinja2Templates

base_path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(base_path / "templates"))
