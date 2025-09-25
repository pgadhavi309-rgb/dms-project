from flask import Flask, render_template
import os

# Templates folder path
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, "Frontend", "templates")

app = Flask(__name__, template_folder=template_dir)

# Home Route
@app.route("/")
def home():
    items = ["Book", "Laptop", "Phone"]  # Example list for loop
    return render_template("home.html", name="Pragnesh", items=items)

# About Route
@app.route("/about")
def about():
    return render_template("about.html", page_title="About Page")

# Dynamic User Route (Optional)
@app.route("/user/<username>")
def user_page(username):
    return render_template("home.html", name=username, items=[])

if __name__ == "__main__":
    app.run(debug=True)
