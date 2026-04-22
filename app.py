
'''
from flask import Flask, render_template, request
from src.pipeline.main_pipeline import Pipeline
from src.utils.logger import get_logger

app = Flask(
    __name__, 
    template_folder="ui/templates",
    static_folder="ui/static"
    )


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
            logger.info("Running pipeline from Flask...")

            # new integrade, 
            product_input = {
                "product_name": product_name,
                "category": category,
                "brand": brand
            }

            df = pipeline.run(product_input)
            #df = pipeline.run()

            # new integrate for ui filter
            sort_order = request.form.get("sort_order", "desc")
            limit = int(request.form.get("limit", 20))

            df = df.sort_values(
                by="probability",
                ascending=(sort_order == "asc")
            )

            result = df = df.head(limit)
            #result = df.head(20).to_dict(orient="records") # old

        except Exception as e:
            logger.error(f"UI Error: {e}")
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)

'''

from flask import Flask, render_template, request
from src.pipeline.main_pipeline import Pipeline
from src.utils.logger import get_logger

# ✅ NEW: Load product data for dropdowns
from src.data.loader import DataLoader

app = Flask(
    __name__, 
    template_folder="ui/templates",
    static_folder="ui/static"
)

logger = get_logger("FlaskApp")

# ✅ NEW: Load data once (startup optimization)
loader = DataLoader()
data = loader.load_all()

products_df = data["products"]

product_names = sorted(products_df["product_name"].unique())
categories = sorted(products_df["category"].unique())
brands = sorted(products_df["brand"].unique())


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    show_result = False   # NEW
    error = None
    message = None
    

    if request.method == "POST":
        try:
            # -----------------------------
            # 🔹 USER INPUT FROM UI
            # -----------------------------
            product_name = request.form.get("product_name")
            category = request.form.get("category")
            brand = request.form.get("brand")

            logger.info(f"Input received: {product_name}, {category}, {brand}")

            pipeline = Pipeline()

            # -----------------------------
            # 🔥 OLD (IGNORED INPUT)
            # -----------------------------
            # df = pipeline.run()

            # -----------------------------
            # ✅ NEW: SEND INPUT TO PIPELINE
            # -----------------------------
            product_input = {
                "product_name": product_name,
                "category": category,
                "brand": brand
            }
            logger.info(f"Validated Input → {product_name}, {category}, {brand}")

            logger.info("Running pipeline with user input...")

            # new integrate
            #df = pipeline.run(product_input)
            # STRICT INPUT CHECK (IMPORTANT)
            df = None
            #if product_name and category and brand:
            if product_name and category and brand and category != "Select":
                logger.info("Running pipeline with user input...")
                df = pipeline.run(product_input)

                show_result = True

                logger.info(f"Pipeline output rows: {0 if df is None else len(df)}")
            else:
                logger.warning("Incomplete input → pipeline not executed")

            if df is not None and not df.empty:

                sort_order = request.form.get("sort_order", "desc")

                try:
                    limit = int(request.form.get("limit", 20))
                except:
                    limit = 20

                df = df.sort_values(
                    by="probability",
                    ascending=(sort_order == "asc")
                 )

                df = df.head(limit)

                result = df.to_dict(orient="records")

            else:
                message = "No matching customers found or insufficient input."


            # -----------------------------
            # 🔥 OLD UI FILTER LOGIC
            # -----------------------------
            # sort_order = request.form.get("sort_order", "desc")
            # limit = int(request.form.get("limit", 20))
            # df = df.sort_values(
            #     by="probability",
            #     ascending=(sort_order == "asc")
            # )
            # result = df = df.head(limit)

            # -----------------------------
            # ✅ NEW FILTER + SORT LOGIC
            # -----------------------------
            '''
            sort_order = request.form.get("sort_order", "desc")
            limit = int(request.form.get("limit", 20))

            df = df.sort_values(
               by="probability",
               ascending=(sort_order == "asc")
            )

            df = df.head(limit)

            # ✅ Convert for UI rendering
            result = df.to_dict(orient="records")
            '''

        except Exception as e:
            logger.error(f"UI Error: {e}")
            error = str(e)

    # -----------------------------
    # 🔥 OLD RENDER
    # -----------------------------
    # return render_template("index.html", result=result, error=error)

    # -----------------------------
    # ✅ NEW RENDER WITH DROPDOWNS
    # -----------------------------
    return render_template(
        "index.html",
        result=result,
        error=error,
        products=product_names,
        categories=categories,
        brands=brands,
        message=message,
        show_result=show_result
    )


if __name__ == "__main__":
    app.run(debug=True)