from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import logging

logger = logging.getLogger(__name__)
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    logger.info("Classification report:%s", report)
    return {"accuracy" : accuracy,
            "precision" : precision,
            "recall" : recall,
            "f1" : f1}