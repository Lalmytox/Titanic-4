# Titanic

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Projet dvp web - groupe 5 | IUT Paris Cité | BUT VCOD 2025-2026

## Équipe et répartition des tâches
- **Tech Lead** : Clara – Validation des pull requests, coordination globale, gestion branche develop/main
- **Linting** : Terryl – Vérification du respect PEP8 (flake8), formatage code (black)
- **Documentation** : Matteo – Rédaction README.md, docstrings, rapport final
- **Tests unitaires** : William – Écriture tests pytest pour features/training/predict

## Stratégie de branches Git
| Branche   | Objectif                                          | Responsable principal |
|-----------|---------------------------------------------------|-----------------------|
| `main`    | Branche de production (code stable)               | Clara                 |
| `develop` | Branche commune pour le développement (intégration)| Tous (Clara valide)   |
| `persos`  | Branche que chacun utilise pour faire ses parties | Chaque membre         |

### Règles de collaboration
1. Chaque membre travaille sur sa branche `persos/[nom]` (ex: `persos/matteo-docs`)
2. Pull Request vers `develop` pour revue
3. Clara valide les PR avant merge dans `develop`
4. Merge de `develop` vers `main` uniquement pour versions finalisées

## Objectif du projet
Ce projet consiste à transformer un notebook Kaggle de prédiction de survie sur le Titanic en un projet Python structuré (via cookiecutter-data-science), respectant les bonnes pratiques d'ingénierie logicielle : modularité, tests, documentation, collaboration Git et pipeline CI/CD.

## Installation

### Cloner le dépôt
```bash
git clone https://github.com/Lalmytox/Titanic-4.git
cd Titanic-4
```

### Créer et activer un environnement virtuel
```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (cmd.exe)
.\.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### Installer les dépendances
```bash
pip install -r requirements.txt
# Si problème de dépendances :
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

### Préparer les données
Télécharger `train.csv` et `test.csv` depuis [Kaggle Titanic](https://www.kaggle.com/c/titanic/data) et les placer dans `data/raw/`.

## Utilisation

### Exécution du pipeline

```bash
# 1. Génération des features
python -m titanic.features
# Résultat : fichiers dans data/processed/ (X_train.csv, y_train.csv, X_test.csv)

# 2. Entraînement du modèle
python -m titanic.modeling.train
# Résultat : modèle sauvegardé dans models/model.pkl

# 3. Prédictions sur le test set
python -m titanic.modeling.predict
# Résultat : fichier submission.csv généré à la racine
```

### Lancement des tests

```bash
python -m pytest tests                  # lance tous les tests
python -m pytest tests/test_features.py # test des features uniquement
python -m pytest tests/test_train.py    # test de l'entraînement uniquement
python -m pytest tests/test_predict.py  # test des prédictions uniquement
```


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         titanic and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── titanic   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes titanic a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

