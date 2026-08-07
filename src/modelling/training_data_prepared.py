import pandas as pd
from sklearn.model_selection import train_test_split


def load_training_data(cleaned_file):
    df = pd.read_csv(cleaned_file)
    return df

def create_target(df):
    df = df.copy()
    df["target"] = (df["quality"] >= 6).astype(int)
    return df

def split_features_target(df):
    X = df.drop(["quality","target"], axis = 1)
    y = df["target"]
    return X, y

def split_training_test_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y,
                                                        test_size= 0.2, 
                                                        random_state= 42,
                                                        stratify= y)
    return X_train, X_test, y_train, y_test
    