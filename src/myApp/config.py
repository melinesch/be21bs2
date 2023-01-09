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
    "user":"root",
    "password":"root",
    "host":"localhost",
    "port":3306,
    "database":"gsea21b_samuel_souchu", #nom de la base de donneés
    "raise_on_warnings": True
}