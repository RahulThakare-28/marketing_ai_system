
'''
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
'''
from src.utils.logger import get_logger

logger = get_logger("DataMerger")

class DataMerger:

    def merge(self, data):
        try:
            logger.info("Merging datasets...")

            order_items = data["order_items"]
            orders = data["orders"]
            products = data["products"]
            users = data["users"]

            # 🔥 Step 1: Merge order_items + orders
            merged = order_items.merge(
                orders,
                on="order_id",
                how="left",
                suffixes=("", "_order")
            )

            # ✅ FIX: unify user_id
            if "user_id_order" in merged.columns:
                merged["user_id"] = merged["user_id"].fillna(merged["user_id_order"])
                merged.drop(columns=["user_id_order"], inplace=True)

            # 🔥 Step 2: Merge products
            merged = merged.merge(
                products,
                on="product_id",
                how="left"
            )

            # 🔥 Step 3: Merge users
            merged = merged.merge(
                users,
                on="user_id",
                how="left"
            )

            logger.info(f"Merged shape: {merged.shape}")
            logger.info("Merge completed successfully")

            return merged

        except Exception as e:
            logger.error(f"Merge failed: {e}")
            raise
