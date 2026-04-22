
'''
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
'''
import os
import joblib
from src.utils.logger import get_logger

logger = get_logger("Predict")

class Predictor:

    def __init__(self):
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            model_path = os.path.join(base_path, "model.pkl")

            self.model = joblib.load(model_path)
            logger.info("Model loaded successfully")

        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise

    def predict(self, df):
        try:
            X = df[["total_score", "total_amount", "price"]]
            df["probability"] = self.model.predict_proba(X)[:, 1]

            # debug
            logger.info(f"Prediction sample:\n{df[['user_id','probability']].head()}")
            return df

        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise