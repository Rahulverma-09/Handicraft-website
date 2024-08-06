from flask import Flask, render_template
from Database import load_items_from_db

app = Flask(__name__)

@app.route("/")
def webservice():
    item_info = load_items_from_db()
    return render_template("home.html", info=item_info)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)


