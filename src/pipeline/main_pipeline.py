
from src.data.loader import DataLoader
from src.data.merger import DataMerger
from src.behavior.interaction import InteractionEngine
from src.features.builder import FeatureBuilder
from src.models.predict import Predictor
from src.targeting.filter import TargetSelector
from src.utils.logger import get_logger
from src.behavior.similarity import ProductSimilarity

logger = get_logger("Main_Pipeline")

class Pipeline:

    def run(self, product_input=None):
        loader = DataLoader()
        data = loader.load_all()
        # new integrate code for filtering
        product_df = data["products"]

        # ================================
        # 🔥 NEW: SIMILARITY-BASED FILTER
        # ================================

        similarity_engine = ProductSimilarity()

        products = data["products"]

        # new integrate : Build similarity matrix (uses your existing function)
        sim_matrix = similarity_engine.build_similarity(products)

        query = ""

        if product_input:
            name = product_input.get("product_name", "")
            category = product_input.get("category", "")
            brand = product_input.get("brand", "")

            query = f"{name} {category} {brand}"


        ''' # old
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
           ''' 
        '''
            # new integrate for filter ->old
        if product_input:
            name = product_input.get("product_name", "")
            category = product_input.get("category", "")
            brand = product_input.get("brand", "")

            filtered = product_df.copy()

            if name:
                filtered = filtered[
                    filtered["product_name"].str.contains(name, case=False, na=False)
                ]

            if category:
                filtered = filtered[
                    filtered["category"] == category
                ]

            if brand:
                filtered = filtered[
                    filtered["brand"].str.contains(brand, case=False, na=False)
            ]

            #  FALLBACK (IMPORTANT)
            if filtered.empty:
                logger.warning("No product match found. Using full dataset.")
                product_df = data["products"]   # fallback
            else:
                product_df = filtered
        '''
        #  NEW SIMILARITY FLOW
        if query.strip():
            product_df = similarity_engine.get_similar_products(
                products, sim_matrix, query
            )

            if product_df.empty:
                logger.warning("No similar products found → fallback to full dataset")
                product_df = products
        else:
            logger.warning("Empty query → using full dataset")
            product_df = products



        merger = DataMerger()
        merged = merger.merge(data)

        interaction_engine = InteractionEngine()
        interaction = interaction_engine.compute_score(
           data["events"], data["reviews"] )

        # new integrade for product base filter
        product_ids = product_df["product_id"].unique()
        interaction = interaction[
            interaction["product_id"].isin(product_ids)
        ]

        # new : handle empty interaction
        if interaction.empty:
            logger.warning("No interaction found. Using full interaction data.")
            interaction = interaction_engine.compute_score(
                data["events"], data["reviews"]
            )
            

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
       

        