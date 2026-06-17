from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict():

    payload = {
        "total_spend": 5000,
        "order_count": 10,
        "ticket_count": 1,
        "sessions_30d": 15,
        "product_views_30d": 20,
        "cart_adds_30d": 5
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200


def test_batch_predict():

    payload = [{
        "total_spend": 5000,
        "order_count": 10,
        "ticket_count": 1,
        "sessions_30d": 15,
        "product_views_30d": 20,
        "cart_adds_30d": 5
    }]

    response = client.post(
        "/batch_predict",
        json=payload
    )

    assert response.status_code == 200