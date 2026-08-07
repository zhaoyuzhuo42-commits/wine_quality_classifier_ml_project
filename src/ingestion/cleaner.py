import pandas as pd

def load_dataset(file):
    df = pd.read_csv(file, sep=';')
    return df

def standerdise_columns_name(columns):
    new_name = []
    for col in columns:
        new_name.append(col.replace(" ", "_"))
    columns = new_name
    return columns
