import pytest
import pandas as pd
from src.ingestion.cleaner import load_dataset, standerdise_columns_name
from src.config import WHITE_WINE_FILE,RED_WINE_FILE

def test_load_dataset(tmp_path):
    test_file = tmp_path /"test.csv"
    test_file.write_text(
        "fixed acidity;volatile acidity\n"
        "7.8;9\n"
    )
    result = load_dataset(test_file)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1, 2)

def test_standerdise_columns_name():
    data = ["fixed acidity",
    "volatile acidity",
    "citric acid"]
    result = standerdise_columns_name(data)
    assert result == ["fixed_acidity", "volatile_acidity", "citric_acid"]
