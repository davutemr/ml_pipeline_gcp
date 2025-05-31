import os
import pytest
from model.train import load_data, train_and_save_model

def test_load_data():
    X, y = load_data()
    assert X.shape[0] == y.shape[0]  # same number of rows
    assert 'Pregnancies' in X.columns  # example column check

def test_train_and_save_model():
    # Call training function - this will overwrite app/model.pkl
    train_and_save_model()

    # Check if model file created
    assert os.path.exists('app/model.pkl')
    
    #Check file is not empty
    assert os.path.getsize('app/model.pkl') > 0

