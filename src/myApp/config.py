ENV = "development"
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0 #vider le cache
SECRET_KEY="k3yop12"

#configuration du serveur web
WEB_SERVER = {
    "host":"localhost",
    "port":8080,
}

#configuration du serveur de BDD
DB_SERVER = {
    "user":"phpmyadmin",
    "password":"root",
    "host":"localhost",
    "port":3306,
    "database":"gsea21b_samuel_souchu", #nom de la base de donneés
    "raise_on_warnings": True
}

SEUIL = {
    'vert':5,
    'jaune':10,
    'orange':15,
    'rouge':20,
    'tdp':0.40
}