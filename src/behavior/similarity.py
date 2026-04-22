

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.logger import get_logger

logger = get_logger("Similarity")

class ProductSimilarity:

    def build_similarity(self, products):
        try:
            logger.info("Building product similarity model...")

            products["text"] = (
                products["product_name"] + " " +
                products["category"] + " " +
                products["brand"]
            )

            tfidf = TfidfVectorizer(stop_words="english")
            tfidf_matrix = tfidf.fit_transform(products["text"])

            sim_matrix = cosine_similarity(tfidf_matrix)

            logger.info("Similarity model built")
            return sim_matrix

        except Exception as e:
            logger.error(f"Similarity error: {e}")
            raise