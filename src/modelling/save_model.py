import pickle
import logging

logger = logging.getLogger(__name__)
def save_model(filepath, model):
    with open(filepath) as f:
        pickle.dump(model, f)
    logger.info("Model save to %s", filepath)