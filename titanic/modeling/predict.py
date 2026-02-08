"""
Module de prédiction pour le projet Titanic.

Ce module utilise un modèle entraîné pour générer des prédictions
sur le dataset de test et créer un fichier de soumission Kaggle.
"""

from pathlib import Path

import pandas as pd
import joblib
from loguru import logger
import typer

from titanic.config import MODELS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "X_test.csv",
    raw_test_path: Path = RAW_DATA_DIR / "test.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    output_path: Path = Path("submission.csv"),
):
    """
    Génération des prédictions et création du fichier de soumission.

    Ce script :
    - Charge le modèle entraîné depuis models/model.pkl
    - Charge les features de test depuis data/processed/X_test.csv
    - Charge les données brutes pour récupérer les PassengerId
    - Génère les prédictions sur le dataset de test
    - Crée un fichier submission.csv avec PassengerId et Survived
    - Sauvegarde le fichier de soumission à la racine du projet

    Args:
        features_path: Chemin vers le fichier des features de test
        raw_test_path: Chemin vers le fichier de test brut (pour PassengerId)
        model_path: Chemin vers le modèle entraîné
        output_path: Chemin de sauvegarde du fichier de soumission
    """

    logger.info("Chargement du modèle")
    model = joblib.load(model_path)

    logger.info("Chargement des features de test")
    X_test = pd.read_csv(features_path)

    logger.info("Chargement des données brutes de test")
    test_data = pd.read_csv(raw_test_path)

    logger.info("Prédiction")
    predictions = model.predict(X_test)

    output = pd.DataFrame(
        {
            "PassengerId": test_data["PassengerId"],
            "Survived": predictions,
        }
    )

    output.to_csv(output_path, index=False)
    logger.success(f"Fichier de soumission sauvegardé : {output_path}")


if __name__ == "__main__":
    app()