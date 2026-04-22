

import joblib
from src.utils.logger import get_logger

logger = get_logger("Predict")

class Predictor:

    def __init__(self):
        self.model = joblib.load("src/models/model.pkl")

    def predict(self, df):
        try:
            X = df[["total_score", "total_amount", "price"]]
            df["probability"] = self.model.predict_proba(X)[:, 1]
            return df

        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise