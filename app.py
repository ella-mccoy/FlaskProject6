import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    meals = None
    query = ""

    if request.method == "POST":
        query = request.form.get("meal")

        if query:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
            response = requests.get(url)
            data = response.json()

            meals = data.get("meals")

    return render_template("index.html", meals=meals, query=query)


if __name__ == "__main__":
    app.run(debug=True)