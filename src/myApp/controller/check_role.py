from flask import session

def checkRole(role = "guest") :
    statut = session["statut"]
    if not session["login"]:
        statut = 3
    if role == "guest" :
        return statut <= 3
    if role == "member" :
        return statut <= 2
    if role == "admin" :
        return statut <= 0
    return statut <= 3