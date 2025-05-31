import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def load_data():
    diabetes = pd.read_csv("model/diabetes.csv")
    X = diabetes[['Pregnancies','Glucose', 'BloodPressure', 'SkinThickness',
                  'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y = diabetes['Outcome']
    return X, y

def train_and_save_model():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=12, random_state=1)
    model.fit(X_train, y_train)

    with open('app/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Model training complete and saved to app/model.pkl")

if __name__ == "__main__":
    train_and_save_model()

