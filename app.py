# This code is part of a Flask application that serves a machine learning model for classification.

import joblib
import os
from flask import Flask, render_template, request

# === Load your trained model and encoder ===
clf = joblib.load("iris_model.joblib")
target_encoder = joblib.load("iris_encoder.joblib")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            sl = float(request.form["sepal_length"])
            sw = float(request.form["sepal_width"])
            pl = float(request.form["petal_length"])
            pw = float(request.form["petal_width"])

            pred_value = clf.predict([[sl, sw, pl, pw]])
            prediction = target_encoder.classes_[pred_value[0]]
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

