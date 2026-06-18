# D2C Churn Prediction API

## Project Overview

This project implements a FastAPI-based churn scoring service for a D2C personal-care brand. The API predicts customer churn risk and provides interpretable explanations to support retention strategies.

## Features

* Customer churn prediction
* Churn probability scoring
* Risk categorization (Low, Medium, High)
* Batch predictions
* API health monitoring
* Pydantic input validation
* Automated API testing

## Repository Structure

```text
d2c-churn-part4-fastapi/
│
├── app/
│   └── main.py
├── model.pkl
├── test_api.py
├── monitoring_plan.md
├── README.md
├── requirements.txt
├── Dockerfile
└── sample_request.json
```

## Setup Instructions

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /health

Checks whether the API is running.

Sample Response:

```json
{
  "status": "ok"
}
```

### POST /predict

Predict churn for a single customer.

Sample Request:

```json
{
  "total_spend": 5000,
  "order_count": 10,
  "ticket_count": 1,
  "sessions_30d": 15,
  "product_views_30d": 20,
  "cart_adds_30d": 5
}
```

Sample Response:

```json
{
  "churn_probability": 0.41,
  "predicted_class": 0,
  "risk_level": "medium",
  "risk_explanation": "Customer shows moderate churn risk and may benefit from retention campaigns."
}
```

### POST /batch_predict

Predict churn for multiple customers simultaneously.

## Running Tests

```bash
pytest test_api.py
```

Expected Output:

```text
3 passed
```

## Model Notes

The API uses a Random Forest model trained on customer engagement and transactional features:

* total_spend
* order_count
* ticket_count
* sessions_30d
* product_views_30d
* cart_adds_30d


