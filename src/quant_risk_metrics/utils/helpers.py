
def normalize_colnames(df):
    df.columns = [c.lower().strip() for c in df.columns]
    return df
