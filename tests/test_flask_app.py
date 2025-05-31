import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_valid(client):
    input_data = {
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 79,
        "BMI": 25.6,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 33
    }
    response = client.post('/predict', json=input_data)
    assert response.status_code == 200
    assert 'prediction' in response.get_json()

def test_predict_missing_field(client):
    # Missing 'Age' field should cause 400 error
    input_data = {
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 79,
        "BMI": 25.6,
        "DiabetesPedigreeFunction": 0.5
    }
    response = client.post('/predict', json=input_data)
    assert response.status_code == 400
    assert 'error' in response.get_json()

