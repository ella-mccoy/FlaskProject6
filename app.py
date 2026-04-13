import os
import requests
import psycopg
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, redirect

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


def save_recipe(name: str) -> None:
    with psycopg.connect(DATABASE_URL, sslmode="require") as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO recipes (name) VALUES (%s);",
                (name,)
            )


def get_saved_recipes() -> list[str]:
    with psycopg.connect(DATABASE_URL, sslmode="require") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM recipes ORDER BY id DESC;")
            rows = cur.fetchall()
    return [row[0] for row in rows]


@app.route("/", methods=["GET", "POST"])
def home():
    meals = None
    query = ""
    error = None

    try:
        saved_recipes = get_saved_recipes()
    except Exception:
        saved_recipes = []

    if request.method == "POST":
        query = request.form.get("meal", "").strip()

        if query:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"

            try:
                response = requests.get(url, timeout=5)
                data = response.json()
                meals = data.get("meals")
            except requests.RequestException:
                error = "Could not connect to the recipe service. Please try again."

    return render_template(
        "index.html",
        meals=meals,
        query=query,
        error=error,
        saved_recipes=saved_recipes
    )


@app.route("/save", methods=["POST"])
def save():
    name = request.form.get("name", "").strip()
    if name:
        try:
            save_recipe(name)
        except Exception:
            pass
    return redirect("/")


@app.route("/recipes")
def recipes_json():
    return jsonify({"message": "Recipe API running"})


@app.route("/health")
def health():
    db_ok = True

    try:
        get_saved_recipes()
    except Exception:
        db_ok = False

    if db_ok:
        return jsonify({"status": "ok", "database": "connected"})
    return jsonify({"status": "unhealthy", "database": "not connected"}), 500


@app.route("/status")
def status():
    try:
        saved_recipes = get_saved_recipes()
        return jsonify({
            "status": "running",
            "database": "connected",
            "saved_recipe_count": len(saved_recipes)
        })
    except Exception as e:
        return jsonify({
            "status": "running",
            "database": "error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)