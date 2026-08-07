from src.config import RED_WINE_FILE,CLEANED_RED_WINE_FILE,WHITE_WINE_FILE,CLEANED_WHITE_WINE_FILE
from src.ingestion.downloader import download_dataset
from src.ingestion.cleaner import load_dataset, standerdise_columns_name
from src.ingestion.storage import save_dataset
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
def process_dataset(input_file, output_file):
        df = load_dataset(input_file)
        df.columns = standerdise_columns_name(df.columns)
        save_dataset(df, output_file)

def main():
    logger.info("Starting data ingest pipeline")
    logger.info("Downloading dataset")
    download_dataset()
    logger.info("Processing white wine")
    process_dataset(WHITE_WINE_FILE, CLEANED_WHITE_WINE_FILE)
    logger.info("Processing red wine")
    process_dataset(RED_WINE_FILE, CLEANED_RED_WINE_FILE)
    logger.info("Pipeline completed")

if __name__ == "__main__":
    main()