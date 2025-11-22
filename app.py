from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/predict"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = {k: v for k, v in request.form.items()}

    response = requests.post(FASTAPI_URL, json=data)

    result = response.json()

    prediction = "Customer WILL Churn 😟" if result["prediction"] == 1 else "Customer will NOT Churn 🙂"

    probability = None
    if result["probability"] is not None:
        probability = f"{result['probability']*100:.2f}%"

    return render_template("index.html", prediction=prediction, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
