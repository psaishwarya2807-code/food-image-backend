from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simple food database
food_data = {
    "pani_puri": {
        "name": "Pani Puri",
        "type": "Junk Food",
        "ingredients": "Semolina puri, potato, chickpeas, spices",
        "calories": "300 kcal (6 pieces)",
        "best_time": "Occasionally, avoid night"
    },
    "salad": {
        "name": "Vegetable Salad",
        "type": "Healthy Food",
        "ingredients": "Cucumber, carrot, tomato, lettuce",
        "calories": "120 kcal",
        "best_time": "Anytime"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    food = None

    if request.method == "POST":
        image = request.files["image"]

        # TEMP logic (replace later with ML)
        filename = image.filename.lower()

        if "pani" in filename:
            food = food_data["pani_puri"]
        else:
            food = food_data["salad"]

        result = food["type"]

    return render_template("index.html", result=result, food=food)

if __name__ == "__main__":
    app.run(debug=True)