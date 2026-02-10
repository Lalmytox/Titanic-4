import joblib

from titanic.modeling.train import main


def test_train_creates_model_file(tmp_path, sample_train_data, monkeypatch):
    X, y = sample_train_data

    features_path = tmp_path / "X_train.csv"
    labels_path = tmp_path / "y_train.csv"
    model_path = tmp_path / "model.pkl"

    X.to_csv(features_path, index=False)
    y.to_csv(labels_path, index=False)

    monkeypatch.setattr("titanic.modeling.train.PROCESSED_DATA_DIR", tmp_path)
    monkeypatch.setattr("titanic.modeling.train.MODELS_DIR", tmp_path)

    main(features_path=features_path, labels_path=labels_path, model_path=model_path)

    assert model_path.exists()

    model = joblib.load(model_path)
    preds = model.predict(X)
    assert len(preds) == len(y)
