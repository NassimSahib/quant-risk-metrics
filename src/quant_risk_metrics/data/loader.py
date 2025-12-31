from dataclasses import dataclass
from pathlib import Path
import pandas as pd

@dataclass(frozen=True)
class DataLoader:
    root: Path

    def load_csv(self, name : str) -> pd.DataFrame:
        """"Load a CSV file from data directory."""
        path = self.root / name
        return pd.read_csv(path)
