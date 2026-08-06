import pandas as pd

def save_dataset(df, filepath):
    df.to_csv(filepath, index = False)