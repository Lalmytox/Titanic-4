from __future__ import annotations

from typing import List, Tuple

import pandas as pd

DEFAULT_FEATURES: List[str] = ["Pclass", "Sex", "SibSp", "Parch"]
TARGET_COL = "Survived"


def load_data(train_path: str, test_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Charge les fichiers CSV train/test (local)."""
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df


def make_features(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    features: List[str] = DEFAULT_FEATURES,
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """
    Construit X, y et X_test comme dans le tutoriel Titanic:
    - y = train['Survived']
    
    """
    y = train_df[TARGET_COL]

    x = pd.get_dummies(train_df[features])
    x_test = pd.get_dummies(test_df[features])

    x, x_test = x.align(x_test, join="left", axis=1, fill_value=0)

    passenger_id = test_df["PassengerId"]
    return x, y, x_test, passenger_id
