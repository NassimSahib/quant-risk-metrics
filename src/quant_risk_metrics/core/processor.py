import pandas as pd

class Processor:
    """Basic processor example."""

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["sum"] = df.sum(axis=1)
        return df
