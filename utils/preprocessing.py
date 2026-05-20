import pandas as pd

DATA_PATH = "data/expense_data.csv"

def load_dataset():

    df = pd.read_csv(
        DATA_PATH,
        nrows=10000
    )

    return df


def clean_dataset(df):

    df.dropna(inplace=True)

    df["amount"] = df["amount"].astype(float)

    return df