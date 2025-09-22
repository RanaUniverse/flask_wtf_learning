from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dropdown/<item_category>")
def show_category_dropdown(item_category: str):
    return (
        f"<h3>You Have Selected The Category of:</h3> "
        f"<br> "
        f"<h1> {item_category} </h1>"
    )
