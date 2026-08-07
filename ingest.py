from src.config import RED_WINE_FILE,CLEANED_RED_WINE_FILE,WHITE_WINE_FILE,CLEANED_WHITE_WINE_FILE
from src.downloader import download_dataset
from src.cleaner import load_dataset, standerdise_columns_name
from src.storage import save_dataset
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(levelname)s: %(message)s")
def process_dataset(input_file, output_file):
        df = load_dataset(input_file)
        df.columns = standerdise_columns_name(df.columns)
        save_dataset(df, output_file)

def main():
    logging.info("Starting data ingest pipeline")
    logging.info("Downloading dataset")
    download_dataset()
    logging.info("Processing white wine")
    process_dataset(WHITE_WINE_FILE, CLEANED_WHITE_WINE_FILE)
    logging.info("Processing red wine")
    process_dataset(RED_WINE_FILE, CLEANED_RED_WINE_FILE)
    logging.info("Pipeline completed")

if __name__ == "__main__":
    main()