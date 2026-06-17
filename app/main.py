from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(
    title="D2C Churn Prediction API",
    version="0.1.0"
)

print("Current Directory:", os.getcwd())

model = joblib.load("model.pkl")

print("Loaded model features:")
print(model.feature_names_in_)


class Customer(BaseModel):
    total_spend: float
    order_count: int
    ticket_count: int
    sessions_30d: int
    product_views_30d: int
    cart_adds_30d: int


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([customer.dict()])

    # Ensure exact feature order
    data = data[
        [
            "total_spend",
            "order_count",
            "ticket_count",
            "sessions_30d",
            "product_views_30d",
            "cart_adds_30d"
        ]
    ]

    prob = float(model.predict_proba(data)[0][1])
    pred = int(prob >= 0.5)

    if prob >= 0.7:
        risk = "high"
    elif prob >= 0.4:
        risk = "medium"
    else:
        risk = "low"

    if risk == "high":
        explanation = (
            "Low engagement and customer activity indicate high churn risk."
        )
    elif risk == "medium":
        explanation = (
            "Customer shows moderate churn risk and may benefit from retention campaigns."
        )
    else:
        explanation = (
            "Customer engagement appears healthy with low churn risk."
        )

    return {
        "churn_probability": round(prob, 2),
        "predicted_class": pred,
        "risk_level": risk,
        "risk_explanation": explanation
    }


@app.post("/batch_predict")
def batch_predict(customers: list[Customer]):

    df = pd.DataFrame(
        [c.dict() for c in customers]
    )

    df = df[
        [
            "total_spend",
            "order_count",
            "ticket_count",
            "sessions_30d",
            "product_views_30d",
            "cart_adds_30d"
        ]
    ]

    probs = model.predict_proba(df)[:, 1]

    results = []

    for prob in probs:

        pred = int(prob >= 0.5)

        if prob >= 0.7:
            risk = "high"
        elif prob >= 0.4:
            risk = "medium"
        else:
            risk = "low"

        results.append(
            {
                "churn_probability": round(float(prob), 2),
                "predicted_class": pred,
                "risk_level": risk
            }
        )

    return {
        "predictions": results
    }