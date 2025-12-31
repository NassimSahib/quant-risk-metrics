import yaml
from pathlib import Path
from typing import Any, Dict

def load_settings(path: str | None = None) -> Dict[str, Any]:
    path = Path(path) if path else Path("config/settings.yaml")
    with path.open("r", encoding = "utf-8") as f:
        return yaml.safe_load(f)

