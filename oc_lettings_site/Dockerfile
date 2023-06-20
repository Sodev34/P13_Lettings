# image de base. 
FROM python:3.9

# variable d'environnement empêche Python de générer des fichiers bytecode inutiles.
ENV PYTHONDONTWRITEBYTECODE=1

# variable d'environnement désactive la mise en mémoire tampon pour que sortie 
# de l'application soit affichée dans les journaux du conteneur Docker.
ENV PYTHONUNBUFFERED=1

# Port nécessaire 
ENV PORT=8000

# répertoire de travail dans le conteneur.
WORKDIR /app

# Copie des fichiers nécessaires dans le conteneur.
COPY requirements.txt /app/

# Installe les dépendances.
RUN pip install -r requirements.txt

# Copie du projet. 
COPY . /app/

# Collecter les fichiers statiques.
RUN python3 manage.py collectstatic --noinput

# Expose le port par default pour l'application.
EXPOSE $PORT

# Configurer la commande exécutable dans le conteneur.
CMD python3 manage.py runserver 0.0.0.0:$PORT
