"""
Module de feature engineering pour le dataset Titanic.

Ce module effectue le nettoyage des données et la création de caractéristiques
à partir des fichiers bruts de train et de test Kaggle.
"""

from pathlib import Path

import pandas as pd
from loguru import logger
import typer

from titanic.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    train_path: Path = RAW_DATA_DIR / "train.csv",
    test_path: Path = RAW_DATA_DIR / "test.csv",
):
    """
    Nettoyage des données et ingénierie des caractéristiques.

    Ce script :
    - Charge les fichiers train.csv et test.csv depuis le dossier data/raw/
    - Effectue une analyse exploratoire simple (taux de survie par sexe)
    - Sélectionne les features pertinentes (Pclass, Sex, SibSp, Parch)
    - Applique l'encodage one-hot pour les variables catégorielles
    - Aligne les colonnes entre train et test
    - Sauvegarde les features traitées dans data/processed/

    Args:
        train_path: Chemin vers le fichier d'entraînement brut
        test_path: Chemin vers le fichier de test brut
    """

    logger.info("Chargement des données")
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    # -------------------------
    # Analyse exploratoire simple
    # -------------------------
    women = train_data.loc[train_data["Sex"] == "female", "Survived"]
    men = train_data.loc[train_data["Sex"] == "male", "Survived"]

    rate_women = women.mean()
    rate_men = men.mean()

    logger.info(f"% of women who survived: {rate_women:.2%}")
    logger.info(f"% of men who survived: {rate_men:.2%}")

    # -------------------------
    # Feature engineering
    # -------------------------
    features = ["Pclass", "Sex", "SibSp", "Parch"]

    y = train_data["Survived"]

    X = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])

    # Alignement train / test
    X, X_test = X.align(X_test, join="left", axis=1, fill_value=0)

    # -------------------------
    # Sauvegarde
    # -------------------------
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    y.to_csv(PROCESSED_DATA_DIR / "y_train.csv", index=False)
    X.to_csv(PROCESSED_DATA_DIR / "X_train.csv", index=False)
    X_test.to_csv(PROCESSED_DATA_DIR / "X_test.csv", index=False)

    logger.success("Features sauvegardées dans data/processed/")


if __name__ == "__main__":
    app()
