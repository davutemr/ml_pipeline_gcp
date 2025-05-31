from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data received'}), 400

    try:
        Pregnancies = int(data['Pregnancies'])
        Glucose = int(data['Glucose'])
        BloodPressure = int(data['BloodPressure'])
        SkinThickness = int(data['SkinThickness'])
        Insulin = int(data['Insulin'])
        BMI = float(data['BMI'])
        DiabetesPedigreeFunction = float(data['DiabetesPedigreeFunction'])
        Age = int(data['Age'])
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid or missing input parameters'}), 400

    features = np.array([
        Pregnancies, Glucose, BloodPressure, SkinThickness,
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({'prediction': int(prediction)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

