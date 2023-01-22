ENV = "development"
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0  # vider le cache
SECRET_KEY = "k3yop12"

# configuration du serveur web
WEB_SERVER = {
    "host": "localhost",
    "port": 8080,
}

# configuration du serveur de BDD
DB_SERVER = {
    "user": "phpmyadmin",
    "password": "root",
    "host": "localhost",
    "port": 3306,
    "database": "gsea21b_samuel_souchu",  # nom de la base de donneés
    "raise_on_warnings": True
}

SEUIL = {
    'vert': 20,
    'jaune': 40,
    'orange': 60,
    'rouge': 60,
    'tdp': 0.90
}

COULEUR = {
    'vert': '#62ad00',
    'jaune': '#ffc300',
    'orange': '#ff8c00',
    'rouge': '#d4022c',
    'zero': 'grey'
}


BUILD_ZERO = {
    'debut': [1, 1, 2022, 8],
    'fin': [31, 12, 2024, 19]
}

NB_MVT_TDP = 10               # Nombre de mouvement pour 1 tour de piste
# Active ou non la mise en cache du calcul des créneaux du calendrier
CACHE_BASE = True
