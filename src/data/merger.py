
from src.utils.logger import get_logger

logger = get_logger("DataMerger")

class DataMerger:

    def merge(self, data):
        try:
            logger.info("Merging datasets...")

            merged = data["order_items"].merge(
                data["orders"], on="order_id", how="left"
            )

            merged = merged.merge(
                data["products"], on="product_id", how="left"
            )

            merged = merged.merge(
                data["users"], on="user_id", how="left"
            )

            logger.info("Merge completed")
            return merged

        except Exception as e:
            logger.error(f"Merge failed: {e}")
            raise