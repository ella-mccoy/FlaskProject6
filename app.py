import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    meals = None
    query = ""
    error = None

    if request.method == "POST":
        query = request.form.get("meal", "").strip()

        if query:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"

            try:
                response = requests.get(url, timeout=5)
                data = response.json()
                meals = data.get("meals")
            except requests.RequestException:
                error = "Unable to fetch recipes right now. Please try again later."


    return render_template("index.html", meals=meals, query=query, error=error)


@app.route("/recipes")
def recipes_json():
    return jsonify({"message": "Recipe API running"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)