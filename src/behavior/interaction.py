

from src.utils.logger import get_logger

logger = get_logger("Interaction")

class InteractionEngine:

    def compute_score(self, events, reviews):
        try:
            logger.info("Computing interaction scores...")

            event_weight = {
                "view": 1,
                "cart": 3,
                "purchase": 5
            }

            events["score"] = events["event_type"].map(event_weight)

            interaction = events.groupby(
                ["user_id", "product_id"]
            )["score"].sum().reset_index()

            rating_bonus = reviews.copy()
            rating_bonus["bonus"] = rating_bonus["rating"].apply(
                lambda x: 2 if x >= 4 else 0
            )

            rating_bonus = rating_bonus.groupby(
                ["user_id", "product_id"]
            )["bonus"].sum().reset_index()

            final = interaction.merge(
                rating_bonus, on=["user_id", "product_id"], how="left"
            ).fillna(0)

            final["total_score"] = final["score"] + final["bonus"]

            logger.info("Interaction scoring complete")
            return final

        except Exception as e:
            logger.error(f"Interaction error: {e}")
            raise