
from src.data.loader import DataLoader
from src.data.merger import DataMerger
from src.behavior.interaction import InteractionEngine
from src.features.builder import FeatureBuilder
from src.models.predict import Predictor
from src.targeting.filter import TargetSelector

class Pipeline:

    def run(self, product_input=None):
        loader = DataLoader()
        data = loader.load_all()
        # new integrate code for filtering
        product_df = data["products"]

        if product_input:
            name = product_input.get("product_name", "")
            category = product_input.get("category", "")
            brand = product_input.get("brand", "")

            if name:
                product_df = product_df[
                product_df["product_name"].str.contains(name, case=False, na=False)
                ]

            if category:
                product_df = product_df[
                product_df["category"] == category
                ]

            if brand:
                product_df = product_df[
                product_df["brand"].str.contains(brand, case=False, na=False)
            ]

        merger = DataMerger()
        merged = merger.merge(data)

        interaction_engine = InteractionEngine()
        interaction = interaction_engine.compute_score(
            data["events"], data["reviews"]
        )
 
        # new integrade for product base filter
        product_ids = product_df["product_id"].unique()
        interaction = interaction[
            interaction["product_id"].isin(product_ids)
        ]

        feature_builder = FeatureBuilder()
        features = feature_builder.build(merged, interaction)

        predictor = Predictor()
        predictions = predictor.predict(features)

        selector = TargetSelector()
        result = selector.select(predictions)

        # new integrate 
        users = data["users"]
        result = result.merge(users, on="user_id", how="left")
        return result
       

        