from src.config import RED_WINE_FILE,WHITE_WINE_FILE,INFO_FILE, ZIP_FILE,ZIP_URL,RAW_DATA_DIR
from pathlib import Path
import requests
import zipfile

def dataset_exist():
    return (RED_WINE_FILE.exists() 
            and WHITE_WINE_FILE.exists() 
            and INFO_FILE.exists)

def download_file(url, destination):
    response = requests.get(url)
    response.raise_for_status()
    with open(destination, "wb") as file:
        file.write(response.content)

def extract_dataset(zip_file,destination):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)

def download_dataset():
    if dataset_exist() is True:
        return
    download_file(ZIP_URL, ZIP_FILE)
    extract_dataset(ZIP_FILE, RAW_DATA_DIR)


