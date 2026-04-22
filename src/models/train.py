# src/models/train.py
from src.data.loader import DataLoader
from src.data.merger import DataMerger
from src.behavior.interaction import InteractionEngine
from src.features.builder import FeatureBuilder


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from src.utils.logger import get_logger

logger = get_logger("ModelTrain")

class ModelTrainer:

    def train(self, df):
        try:
            logger.info("Training model...")

            df["target"] = df["total_score"].apply(lambda x: 1 if x > 5 else 0)

            X = df[["total_score", "total_amount", "price"]]
            y = df["target"]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2
            )

            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            joblib.dump(model, "src/models/model.pkl")

            logger.info("Model trained and saved")

        except Exception as e:
            logger.error(f"Training error: {e}")
            raise

if __name__ == "__main__":


    loader = DataLoader()
    data = loader.load_all()

    merger = DataMerger()
    merged = merger.merge(data)

    interaction_engine = InteractionEngine()
    interaction = interaction_engine.compute_score(
        data["events"], data["reviews"]
    )

    feature_builder = FeatureBuilder()
    features = feature_builder.build(merged, interaction)

    trainer = ModelTrainer()
    trainer.train(features)