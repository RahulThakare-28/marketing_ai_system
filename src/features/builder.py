

from src.utils.logger import get_logger

logger = get_logger("Features")

class FeatureBuilder:

    def build(self, merged, interaction):
        try:
            logger.info("Building features...")

            user_features = merged.groupby("user_id").agg({
                "total_amount": "mean",
                "price": "mean"
            }).reset_index()

            final = interaction.merge(user_features, on="user_id", how="left")

            logger.info("Feature building complete")
            return final

        except Exception as e:
            logger.error(f"Feature error: {e}")
            raise