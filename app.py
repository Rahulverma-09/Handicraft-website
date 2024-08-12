from flask import Flask, render_template
from Database import load_items_from_db

app = Flask(__name__)

@app.route("/")
def display_home():
    return render_template("home.html")
    
@app.route("/items")
def display_items():
    item_info = load_items_from_db()
    return render_template("items.html", info=item_info)

@app.route("/contact")
def display_contacts():
    return render_template("contact.html")

@app.route("/about")
def display_about():
    return render_template("about.html")
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)


