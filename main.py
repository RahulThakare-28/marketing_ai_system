

import sys
from src.data.loader import DataLoader
from src.data.merger import DataMerger
from src.behavior.interaction import InteractionEngine
from src.features.builder import FeatureBuilder
from src.models.train import ModelTrainer
from src.pipeline.main_pipeline import Pipeline
from src.utils.logger import get_logger

logger = get_logger("Main")


def train_model():
    try:
        logger.info("=== TRAINING PIPELINE STARTED ===")

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

        logger.info("=== TRAINING COMPLETED SUCCESSFULLY ===")

    except Exception as e:
        logger.error(f"Training failed: {e}")


def run_pipeline():
    try:
        logger.info("=== PREDICTION PIPELINE STARTED ===")

        pipeline = Pipeline()
        result = pipeline.run()

        logger.info(f"Total target users: {len(result)}")
        print(result.head(20))

        logger.info("=== PIPELINE COMPLETED ===")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("python main.py train   # Train model")
        print("python main.py run     # Run prediction pipeline")
        sys.exit(1)

    command = sys.argv[1]

    if command == "train":
        train_model()

    elif command == "run":
        run_pipeline()

    else:
        print("Invalid command. Use 'train' or 'run'")