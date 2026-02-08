```markdown
Getting started
===============

Ce guide décrit les étapes pour reprendre le projet sur une machine propre
et lancer le pipeline (prétraitement → entraînement → prédiction).

1) Cloner le dépôt

```bash
git clone https://github.com/Lalmytox/Titanic-4.git
cd Titanic-4
```

2) Créer et activer un environnement virtuel, installer les dépendances

```bash
python -m venv .venv
# PowerShell (Windows)
.\.venv\Scripts\Activate.ps1
# Ou cmd.exe
.\.venv\Scripts\activate
pip install -r requirements.txt
```

3) Placer les données brutes

Télécharger `train.csv` et `test.csv` (Kaggle Titanic) et les déposer dans `data/raw/`.
Le script `titanic/features.py` lit `data/raw/train.csv` et `data/raw/test.csv`.

4) Générer les features (données traitées)

```bash
python -m titanic.features
# Résultat : fichiers dans data/processed/ (X_train.csv, y_train.csv, X_test.csv)
```

5) Entraîner le modèle

```bash
python -m titanic.modeling.train
# Le modèle est sauvegardé dans models/model.pkl
```

6) Faire des prédictions et produire le fichier de soumission

```bash
python -m titanic.modeling.predict
# Produit submission.csv à la racine
```

Commandes Make utiles

- `make requirements` : installe les dépendances
- `make data` : exécute `titanic/dataset.py` (préparation générique)
- `make test` : lance les tests (pytest)
- `make lint` / `make format` : vérification / formatage du code

Dépannage rapide

- Si un script ne se lance pas, vérifiez que l'environnement virtuel est activé
  et que `requirements.txt` a bien été installé.
- Si les chemins posent problème, consultez `titanic/config.py` pour les
  chemins par défaut (`data/raw`, `data/processed`, `models/`).

Si vous voulez, je peux :
- ajouter ou adapter des commandes `make` pour exécuter `features` / `train` / `predict` ;
- commiter ces modifications et préparer un petit guide d'exécution en français.
```
