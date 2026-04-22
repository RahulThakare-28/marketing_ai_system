
'''
import numpy as np
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
'''

import numpy as np
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

            # ===============================
            # 🔥 HANDLE MISSING VALUES (FIXED)
            # ===============================

            # Replace infinite values
            final = final.replace([np.inf, -np.inf], np.nan)

            # Fill missing values
            final["total_score"] = final["total_score"].fillna(0)

            if final["total_amount"].isnull().sum() > 0:
                median_amount = final["total_amount"].median()
                final["total_amount"] = final["total_amount"].fillna(median_amount)

            if final["price"].isnull().sum() > 0:
                median_price = final["price"].median()
                final["price"] = final["price"].fillna(median_price)

            logger.info("Missing values handled successfully")

            return final

        except Exception as e:
            logger.error(f"Feature error: {e}")
            raise