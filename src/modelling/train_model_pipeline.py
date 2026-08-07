import logging
from src.modelling.data_prepared import prepare_data
from src.modelling.train_model import train_classifier_model
from src.modelling.evaluate import evaluate_model
from src.modelling.save_model import save_model
from src.config import MODEL_DIR

logger = logging.getLogger(__name__)
def train_model(cleanfile):
    X_train, X_test, y_train, y_test = prepare_data(cleanflie)
    model = train_classifier_model(X_train, y_train)
    evaluate_model(X_test, y_test)
    save_model(MODEL_DIR, model)

