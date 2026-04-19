import pandas as pd

def parse_date(df, column):
    df[column] = pd.to_datetime(df[column])
    return df

def fill_missing(df):
    return df.fillna(df.mean(numeric_only=True))

def sort_by_date(df, column):
    return df.sort_values(by=column)