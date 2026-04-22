
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger("DataLoader")

class DataLoader:

    def __init__(self, base_path="data/raw/"):
        self.base_path = base_path

    def load_all(self):
        try:
            logger.info("Loading datasets...")

            data = {
                "users": pd.read_csv(self.base_path + "users.csv"),
                "products": pd.read_csv(self.base_path + "products.csv"),
                "orders": pd.read_csv(self.base_path + "orders.csv"),
                "order_items": pd.read_csv(self.base_path + "order_items.csv"),
                "reviews": pd.read_csv(self.base_path + "reviews.csv"),
                "events": pd.read_csv(self.base_path + "events.csv"),
            }

            logger.info("All datasets loaded successfully")
            return data

        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise