# Sans Docker

```bash
# Copie du projet
git clone https://github.com/user/testdocker
cd testdocker
# Mise en place de l'environnement
python3 -m venv venv
source venv/bin/activate
# Installation des dépendances
pip3 install -r requirements.txt
# Création des variables
echo "Django" > testdocker/.env
# Lancement de l'application
python3 manage.py runserver
```

# Avec Docker

```bash
# Créer l'image
docker build --tag testdocker .
# Lancement de l'application
docker run -dp 127.0.0.1:8000:8000 testdocker
docker run -dp 127.0.0.1:8000:8000 -e APP_DISPLAY_NAME=Python testdocker
# Arrêt de l'application
docker ps -a # pour récupérer le nom aléatoire
docker stop random_name # arrêt
# Suppression du container
docker rm random_name
```

```bash
# Envoyer l'image sur Docker Hub
# On crée d'abord le répertoire sur https://hub.docker.com/
# On se connecte avec l'utilisateur de Docker Hub
docker login
# Création du tag
docker tag testdocker user/testdocker
# Envoi de l'image sur le Hub
docker push user/testdocker
# Récupérer l'image depuis le Hub
docker pull user/testdocker
```