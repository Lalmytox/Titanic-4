# Titanic documentation!
IUT Paris Cité | BUT VCOD (Groupe 5) 2025-2026

## Description

Ce dépôt contient une refonte d'un notebook Kaggle (Titanic) en projet Python structuré,
organisé selon le modèle cookiecutter-data-science : code modulaire, tests, et documentation.

## Commandes principales

Le `Makefile` expose des commandes pratiques utilisées dans le projet :

| Commande               | Description |
|------------------------|-------------|
| `make help`            | Affiche les règles disponibles dans le Makefile |
| `make requirements`    | Installe/Met à jour les dépendances via `requirements.txt` |
| `make data`            | Exécute `titanic/dataset.py` (préparation générique des données) |
| `make test`            | Lance les tests (`pytest`) |
| `make lint`            | Vérifie le style (`flake8`, `isort`, `black --check`) |
| `make format`          | Formate le code (`isort`, `black`) |
| `make clean`           | Supprime fichiers compilés et `__pycache__` |

Commandes de pipeline (exécutables via Python) :

```bash
python -m titanic.features                # Nettoyage et génération des features (data/processed)
python -m titanic.modeling.train          # Entraîne le modèle et le sauvegarde dans models/
python -m titanic.modeling.predict        # Produit le fichier de soumission (submission.csv)
```

## Emplacements importants

- Données brutes : `data/raw/` (attendez `train.csv` et `test.csv`)
- Données traitées : `data/processed/` (`X_train.csv`, `y_train.csv`, `X_test.csv`)
- Modèles sauvegardés : `models/` (`model.pkl`)
- Fichier de soumission exemple : `submission.csv`

Pour des instructions pas-à-pas, voir la page "Getting Started".
```