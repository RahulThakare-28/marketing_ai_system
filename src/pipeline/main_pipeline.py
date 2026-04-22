
from src.data.loader import DataLoader
from src.data.merger import DataMerger
from src.behavior.interaction import InteractionEngine
from src.features.builder import FeatureBuilder
from src.models.predict import Predictor
from src.targeting.filter import TargetSelector

class Pipeline:

    def run(self):
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

        predictor = Predictor()
        predictions = predictor.predict(features)

        selector = TargetSelector()
        result = selector.select(predictions)

        return result