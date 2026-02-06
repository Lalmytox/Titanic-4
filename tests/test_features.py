import pytest

from titanic.features import main 
from titanic.config import PROCESSED_DATA_DIR
import pandas as pd

def test_features_columns(sample_train):
    X = pd.get_dummies(sample_train[["Pclass", "Sex", "SibSp", "Parch"]])

    expected_cols = {
        "Pclass",
        "SibSp",
        "Parch",
        "Sex_female",
        "Sex_male",
    }

    assert expected_cols.issubset(set(X.columns))


def test_main_creates_files(tmp_path, sample_train, sample_test, monkeypatch):
    train_path = tmp_path / "train.csv"
    test_path = tmp_path / "test.csv"

    sample_train.to_csv(train_path, index=False)
    sample_test.to_csv(test_path, index=False)

    # 🔑 rediriger PROCESSED_DATA_DIR vers tmp_path
    monkeypatch.setattr(
        "titanic.features.PROCESSED_DATA_DIR",
        tmp_path
    )

    main(train_path=train_path, test_path=test_path)

    assert (tmp_path / "X_train.csv").exists()
    assert (tmp_path / "X_test.csv").exists()
    assert (tmp_path / "y_train.csv").exists()