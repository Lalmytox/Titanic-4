import pandas as pd

from titanic.modeling import predict


def test_predict_creates_submission(tmp_path, sample_test_data, dummy_model, monkeypatch):
    X_test, raw_test = sample_test_data

    features_path = tmp_path / "X_test.csv"
    raw_test_path = tmp_path / "test.csv"
    output_path = tmp_path / "submission.csv"

    X_test.to_csv(features_path, index=False)
    raw_test.to_csv(raw_test_path, index=False)

    # 🔑 Monkeypatch pour éviter d'écrire dans les vrais dossiers
    monkeypatch.setattr("titanic.modeling.predict.PROCESSED_DATA_DIR", tmp_path)
    monkeypatch.setattr("titanic.modeling.predict.MODELS_DIR", tmp_path)
    monkeypatch.setattr("titanic.modeling.predict.RAW_DATA_DIR", tmp_path)

    predict.main(
        features_path=features_path,
        raw_test_path=raw_test_path,
        model_path=dummy_model,
        output_path=output_path,
    )

    # Vérifier que le fichier de soumission est créé
    assert output_path.exists()

    # Vérifier le contenu minimal
    df = pd.read_csv(output_path)
    assert set(df.columns) == {"PassengerId", "Survived"}
    assert len(df) == len(raw_test)
