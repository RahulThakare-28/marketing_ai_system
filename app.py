

from flask import Flask, render_template, request
from src.pipeline.main_pipeline import Pipeline
from src.utils.logger import get_logger

app = Flask(__name__)
logger = get_logger("FlaskApp")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            product_name = request.form.get("product_name")
            category = request.form.get("category")
            brand = request.form.get("brand")

            logger.info(f"Input received: {product_name}, {category}, {brand}")

            pipeline = Pipeline()

            # 🔥 For now pipeline ignores input (next upgrade we connect it)
            df = pipeline.run()

            result = df.head(20).to_dict(orient="records")

        except Exception as e:
            logger.error(f"UI Error: {e}")
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)