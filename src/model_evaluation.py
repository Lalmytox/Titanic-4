from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.base import ClassifierMixin


def predict(model: ClassifierMixin, x_test: pd.DataFrame) -> pd.Series:
    """Predict Survived for the test set."""
    return pd.Series(model.predict(x_test))


def save_submission(
    passenger_id: pd.Series,
    predictions: pd.Series,
    output_path: str = "submission.csv",
) -> None:
    """Save Kaggle submission file with PassengerId and Survived."""
    out = pd.DataFrame(
        {
            "PassengerId": passenger_id,
            "Survived": predictions.astype(int),
        }
    )

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(path, index=False)
