

# old similarity.py


from sklearn.metrics.pairwise import cosine_similarity
from src.utils.logger import get_logger
from sklearn.feature_extraction.text import TfidfVectorizer

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

    # new method integrate
    def get_similar_products(self, products, sim_matrix , query, top_n=20):
        try:
            logger.info(f"Finding similar products for query: {query}")

            # If text column not exists → build it
            if "text" not in products.columns:
                products["text"] = (
                    products["product_name"] + " " +
                    products["category"] + " " +
                    products["brand"]
                )

            

            vectorizer = TfidfVectorizer(stop_words="english")
            product_matrix = vectorizer.fit_transform(products["text"])

            query_vec = vectorizer.transform([query])

            scores = cosine_similarity(query_vec, product_matrix).flatten()

            products["similarity"] = scores

            result = products.sort_values(
                by="similarity", ascending=False
            ).head(top_n)

            logger.info(f"Top similar products found: {len(result)}")

            return result

        except Exception as e:
            logger.error(f"Similarity search error: {e}")
            raise           
