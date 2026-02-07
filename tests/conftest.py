import pandas as pd
import pytest
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def sample_train():
    return pd.DataFrame({
        "Survived": [0, 1, 1],
        "Pclass": [3, 1, 2],
        "Sex": ["male", "female", "female"],
        "SibSp": [0, 1, 0],
        "Parch": [0, 0, 1],
    })

@pytest.fixture
def sample_train_data():
    """Crée un petit dataset factice X et y"""
    X = pd.DataFrame({
        "Pclass": [1, 2, 3],
        "SibSp": [0, 1, 0],
        "Parch": [0, 0, 1],
        "Sex_female": [0, 1, 0],
        "Sex_male": [1, 0, 1],
    })
    y = pd.Series([0, 1, 0])
    return X, y

@pytest.fixture
def sample_test():
    return pd.DataFrame({
        "Pclass": [3, 2],
        "Sex": ["male", "female"],
        "SibSp": [0, 1],
        "Parch": [0, 1],
    })

@pytest.fixture
def sample_test_data():
    """Crée un petit dataset de test factice"""
    X_test = pd.DataFrame({
        "Pclass": [1, 2],
        "SibSp": [0, 1],
        "Parch": [0, 1],
        "Sex_female": [1, 0],
        "Sex_male": [0, 1],
    })
    raw_test = pd.DataFrame({
        "PassengerId": [101, 102]
    })
    return X_test, raw_test


@pytest.fixture
def dummy_model(tmp_path):
    """Crée un petit modèle RandomForest factice et le sauvegarde"""
    X = pd.DataFrame({
        "Pclass": [1, 2, 3],
        "SibSp": [0, 1, 0],
        "Parch": [0, 0, 1],
        "Sex_female": [0, 1, 0],
        "Sex_male": [1, 0, 1],
    })
    y = pd.Series([0, 1, 0])

    model = RandomForestClassifier(n_estimators=5, max_depth=2, random_state=1)
    model.fit(X, y)

    model_path = tmp_path / "model.pkl"
    joblib.dump(model, model_path)
    return model_path
