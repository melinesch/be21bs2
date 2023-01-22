from flask import session

def checkRole(role = "guest") :
    if not session or not session["login"] or not session["statut"] :
        statut = 3
    else :
        statut = session["statut"]
    if role == "guest" :
        return statut <= 3
    if role == "member" :
        return statut <= 2
    if role == "admin" :
        return statut <= 0
    return statut <= 3