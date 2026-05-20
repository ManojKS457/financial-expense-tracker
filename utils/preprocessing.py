import pandas as pd

DATA_PATH = "data/sample_expense_data.csv"

def load_dataset():

    df = pd.read_csv(DATA_PATH)

    return df


def clean_dataset(df):

    df.dropna(inplace=True)

    df["amount"] = df["amount"].astype(float)

    return df