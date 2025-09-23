# Here i will make the code part related to the category list in the dropdown items mainly

from flask import (
    Blueprint,
    render_template,
    # url_for,
)


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


# i think to assign this with  "/item_category/<item_name>"

category_bp = Blueprint(
    "category",
    __name__,
    static_folder="static",
    template_folder="templates",
)


@category_bp.get("/")
def category_home():
    """
    This function is for the / of the route is just a way to say user nothings
    """
    text = "Thanks For Visit The Category Products"
    return text


@category_bp.get("/<category_name>")
def dropdown_category_item(category_name: str):

    category_name_value = CATEGORY_MAP.get(category_name)

    if not category_name_value:
        # return "Page Not Found", 404
        return render_template(
                "wrong_category_name.html",
                wrong_name=category_name,
            ),404
        

    return render_template(
        "category_item.html",
        product_name=category_name_value.upper(),
    )
