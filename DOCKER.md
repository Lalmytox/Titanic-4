# Guide d'utilisation Docker

## Construction locale

### Méthode 1 : Construction directe (recommandé pour le développement)
```bash
docker build -t titanic-prediction .
```

### Méthode 2 : Construction depuis GitHub
```bash
# Construire la dernière version
docker build -f Dockerfile.ghcr -t titanic-prediction .

# Construire une branche spécifique
docker build -f Dockerfile.ghcr --build-arg BRANCH=docs/matteo -t titanic-prediction .
```

## Utilisation des versions Release

Après avoir publié une Release sur GitHub, vous pouvez l'utiliser ainsi :

### Télécharger une Release spécifique
```bash
# Méthode 1 : Utiliser un git tag
docker build -f Dockerfile.ghcr --build-arg BRANCH=v1.0.0 -t titanic-prediction:v1.0.0 .

# Méthode 2 : Télécharger directement le code source de la Release
curl -L https://github.com/Lalmytox/Titanic-4/archive/refs/tags/v1.0.0.tar.gz | \
  tar xz && \
  cd Titanic-4-1.0.0 && \
  docker build -t titanic-prediction:v1.0.0 .
```

## Exécution du conteneur

```bash
# Entraîner le modèle
docker run -v ${PWD}/data:/app/data -v ${PWD}/models:/app/models titanic-prediction

# Prédiction
docker run -v ${PWD}/data:/app/data -v ${PWD}/models:/app/models titanic-prediction python -m titanic.modeling.predict

# Exécuter les tests
docker run -v ${PWD}/data:/app/data titanic-prediction python -m pytest tests
```

## Déploiement sur serveur cloud

```bash
# Construire sur le serveur cloud
git clone https://github.com/Lalmytox/Titanic-4.git
cd Titanic-4
docker build -t titanic-prediction .
docker run -v $(pwd)/data:/app/data -v $(pwd)/models:/app/models titanic-prediction
```
