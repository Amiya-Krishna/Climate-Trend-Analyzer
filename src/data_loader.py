import pandas as pd
from .utils import parse_date, fill_missing, sort_by_date
from config import DATE_COLUMN

def load_data(path):
    df = pd.read_csv(path)

    df = parse_date(df, DATE_COLUMN)
    df = fill_missing(df)
    df = sort_by_date(df, DATE_COLUMN)

    print("\n📂 Dataset Loaded")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))

    return df