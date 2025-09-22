from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)


CATEGORIES = [
    {"name": "Mobile Phones 📱", "slug": "phone"},
    {"name": "New Laptops 💻", "slug": "laptop"},
    {"name": "Books & Notes 📚", "slug": "book"},
    {"name": "Headphones 🎧", "slug": "headphones"},
    {"name": "Smartwatches ⌚", "slug": "smartwatch"},
    {"name": "Gaming Consoles 🎮", "slug": "gaming-console"},
    {"name": "Home Appliances 🏠", "slug": "appliances"},
    {"name": "Extra Items 🛒", "slug": "extra"},
]

CATEGORY_MAP: dict[str, str] = {cat["slug"]: cat["name"] for cat in CATEGORIES}


@app.route("/")
def home():
    return render_template(
        "index.html",
    )


@app.route("/items/<item_category>")
def show_category_dropdown(item_category: str):
    
    category_name_value = CATEGORY_MAP.get(item_category)

    return (
        f"<h3>You Have Selected The Category of:</h3> "
        f"<br> "
        f"<h1> {category_name_value} </h1>"
    )


@app.context_processor
def inject_categories():
    return dict(
        categories=CATEGORIES,
    )
