from __future__ import annotations

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(x: pd.DataFrame, y: pd.Series) -> RandomForestClassifier:
    """Train a RandomForestClassifier (tutorial hyperparameters)."""
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=1,
    )
    model.fit(x, y)
    return model
