from flask import session


def checkRole(role="guest"):
    if not session or "login" not in session or "statut" not in session or type(session["statut"]) != int or session["statut"] > 3:
        statut = 3
    else:
        statut = session["statut"]
    if role == "guest":
        return statut <= 3
    if role == "member":
        return statut <= 2
    if role == "admin":
        return statut <= 0
    return statut <= 3
