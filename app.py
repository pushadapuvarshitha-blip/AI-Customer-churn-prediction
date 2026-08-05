from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load("churn_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "gender": [request.form["gender"]],
        "SeniorCitizen": [int(request.form["SeniorCitizen"])],
        "Partner": [request.form["Partner"]],
        "Dependents": [request.form["Dependents"]],
        "tenure": [int(request.form["tenure"])],
        "PhoneService": [request.form["PhoneService"]],
        "MultipleLines": [request.form["MultipleLines"]],
        "InternetService": [request.form["InternetService"]],
        "OnlineSecurity": [request.form["OnlineSecurity"]],
        "OnlineBackup": [request.form["OnlineBackup"]],
        "DeviceProtection": [request.form["DeviceProtection"]],
        "TechSupport": [request.form["TechSupport"]],
        "StreamingTV": [request.form["StreamingTV"]],
        "StreamingMovies": [request.form["StreamingMovies"]],
        "Contract": [request.form["Contract"]],
        "PaperlessBilling": [request.form["PaperlessBilling"]],
        "PaymentMethod": [request.form["PaymentMethod"]],
        "MonthlyCharges": [float(request.form["MonthlyCharges"])],
        "TotalCharges": [float(request.form["TotalCharges"])]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1] * 100

    if prediction == 1:
        result = "High Risk Customer"
    else:
        result = "Low Risk Customer"

    return render_template(
        "result.html",
        prediction=result,
        probability=round(probability, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)