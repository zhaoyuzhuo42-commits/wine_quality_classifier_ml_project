from pathlib import Path

#Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR =PROJECT_ROOT/"data"
RAW_DATA_DIR = PROJECT_ROOT/"data"/"raw"
PROCESSED_DATA_DIR = PROJECT_ROOT/"data"/"processed"

#Dataset files
RED_WINE_FILE = RAW_DATA_DIR/"winequality-red.csv"
WHITE_WINE_FILE = RAW_DATA_DIR/"winequality-white.csv"
INFO_FILE = RAW_DATA_DIR/"winequality.names"
ZIP_FILE = RAW_DATA_DIR/"wine_quality.zip"
CLEANED_RED_WINE_FILE = PROCESSED_DATA_DIR/"cleaned_winequality-red.csv"
CLEANED_WHITE_WINE_FILE = PROCESSED_DATA_DIR/"cleaned_winequality-white.csv"

#Dataset resource
ZIP_URL = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"