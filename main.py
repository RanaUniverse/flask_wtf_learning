from flask import (
    Flask,
    render_template,
)

from webapp.product_category.routes import CATEGORIES
from webapp.footers_sections.routes import footers_bp
from webapp.product_category.routes import category_bp

app = Flask(__name__)

app.register_blueprint(category_bp, url_prefix="/item_category")
app.register_blueprint(footers_bp)


@app.route("/")
def home():
    return render_template(
        "index.html",
    )


@app.context_processor
def inject_categories():
    return dict(
        categories=CATEGORIES,
    )


if __name__ == "__main__":
    # This below is in a development way to start this app
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
