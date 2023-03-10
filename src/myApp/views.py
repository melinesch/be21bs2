# --------------------------------------------------------------------------------
# --------------------------- Import des bibliothèques ---------------------------
# --------------------------------------------------------------------------------

from flask import Flask, render_template, session, request, redirect, jsonify
from myApp.model import bdd as bdd
import secrets
import string
from random import randint
import hashlib
import pandas
import os.path
from os import remove
import datetime
import locale
from .controller import auth, bib_vols


# --------------------------------------------------------------------------------
# -------------------------------- Configuration ---------------------------------
# --------------------------------------------------------------------------------


app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=5)


# --------------------------------------------------------------------------------
# ------------------------------ Routage des pages -------------------------------
# --------------------------------------------------------------------------------


@app.route("/")
@app.route("/accueil")
@app.route("/accueil/<infoMsg>")
def index(infoMsg=""):
    return render_template("index.html", maPage="accueil.html", monTitre="Accueil", info=infoMsg)


@app.route('/webmaster')
def webmaster():
    if auth.checkRole("guest"):
        return render_template("index.html", maPage="webmaster.html", monTitre="Webmasters")
    return redirect("/accueil/accessNotAllowed")


@app.route('/prevision')
@app.route('/prevision/<infoMsg>')
def previsions(infoMsg=""):
    if auth.checkRole("member"):
        return render_template("index.html", maPage="prevision.html", monTitre="Prévisions", info=infoMsg)
    return redirect("/accueil/accessNotAllowed")


@app.route('/compte')
@app.route('/compte/<infoMsg>')
@app.route('/compte/<infoMsg>/<pwd>')
def compte(infoMsg="", pwd=""):
    if auth.checkRole("admin"):
        return render_template("index.html", maPage="compte.html", monTitre="Création de compte", info=infoMsg, pwd=pwd)
    return redirect("/accueil/accessNotAllowed")


@app.route('/login')
@app.route('/login/<infoMsg>')
def login(infoMsg=""):
    return render_template("index.html", maPage="login.html", monTitre="Se connecter", info=infoMsg)


@app.route("/connecter", methods=["POST"])
def connecter():
    login = request.form['login']
    mdp = request.form['mdp']
    # vérification de paramètres en BDD
    msg, user = bdd.verifAuthData(login, mdp)

    try:
        # authentification réussie
        # initialisation des sessions
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["avatar"] = user["avatar"]
        session["login"] = user["login"]
        session["statut"] = user["statut"]
        session["mail"] = user["mail"]
        session["newMdp"] = user["newMdp"]

        if session["newMdp"] == 2:
            return redirect("/mdp/authOK")

        if session["statut"] == 0:
            return redirect("/compte/authOK")
        else:
            return redirect("/prevision/authOK")

    except TypeError as err:
        # echec d'authentification
        print("Failed verifAuth:{}".format(err))

        return redirect("/login/authEchec")


@app.route("/logout")
def deconnecter():
    # authentification réussie
    # initialisation des sessions
    session["idUser"] = ""
    session["nom"] = ""
    session["prenom"] = ""
    session["avatar"] = ""
    session["login"] = ""
    session["statut"] = ""
    session["mail"] = ""
    session["newMdp"] = ""

    return redirect("/accueil/logoutOK")


@app.route("/addUser", methods=['POST'])
def addUser():
    if auth.checkRole("admin"):
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        mail = request.form["mail"]
        login = request.form["login"]
        # verif si utilisateur existe déjà
        msg, count = bdd.verifDuplicateData(login, mail)
        if int(count) > 0:
            return redirect("/compte/duplicate")
        newMdp = 2
        motPasse = ''
        for i in range(10):
            motPasse += ''.join(secrets.choice(alphabet))
        mdp = hashlib.sha256(motPasse.encode())
        mdpC = mdp.hexdigest()  # mot de passe chiffré
        statut = int(request.form["statut"])
        a = randint(1, 16)
        avatar = "" + str(a) + ".png"
        msg, lastId = bdd.add_userData(
            nom, prenom, mail, login, mdpC, statut, newMdp, avatar)
        print(msg)
        return redirect("/compte/" + msg + "/" + motPasse)
    return redirect("/accueil/accessNotAllowed")


@app.route('/mdp')
@app.route('/mdp/<infoMsg>')
def mdp(infoMsg=""):
    if auth.checkRole("member"):
        return render_template("index.html", maPage="mdp.html", monTitre="Changer le mot de passe", info=infoMsg)
    return redirect("/accueil/accessNotAllowed")


@app.route("/changeMdp", methods=['POST'])
def changeMdp():
    if auth.checkRole("member"):
        # Récupération des données du formulaire
        oldMdp = request.form["oldMdp"]
        mdp = request.form["mdp"]
        confirmMdp = request.form["confirmMdp"]

        # Vérification de l'ancien mot de passe
        verif, user = bdd.verifAuthData(session["login"], oldMdp)
        if (verif != "authOK"):
            return redirect("/mdp/" + msg)

        # Vérification de la cohérence de confirmation
        if (mdp == "" or mdp != confirmMdp):
            return redirect("/mdp/passwordNotMatched")

        # Actions d'enregistrement
        newMdp = 0

        mdp = hashlib.sha256(mdp.encode())
        mdpC = mdp.hexdigest()  # mot de passe chiffré

        msg = bdd.update_userData("motPasse", mdpC, session["idUser"])
        msg2 = bdd.update_userData("newMdp", newMdp, session["idUser"])
        session["newMdp"] = 0
        return redirect("/prevision/" + msg)
    return redirect("/accueil/accessNotAllowed")


@app.route('/upload')
def upload():
    if auth.checkRole("admin"):
        return render_template("index.html", maPage="upload.html", monTitre="Page Import de données")
    return redirect("/accueil/accessNotAllowed")


@app.route("/fichiers/", methods=['GET', 'POST'])
@app.route("/fichiers/<infoMsg>", methods=['GET', 'POST'])
def fichiers(infoMsg=""):
    if os.path.exists('calboth.json'):
        remove('calboth.json')
    if os.path.exists('calmvt.json'):
        remove('calmvt.json')
    if os.path.exists('caltdp.json'):
        remove('caltdp.json')

    if auth.checkRole("admin"):
        if "testFile" in request.files:  # téléchargement du fichier excel
            file = request.files['testFile']
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            xls = pandas.read_excel(APP_ROOT + "/files/" + file.filename)
            data = xls.to_dict('records')
            # suppression des vols sur la même plage de dates
            listDate = [d.get('depart').timestamp() for d in data]
            mindate = datetime.datetime.fromtimestamp(min(listDate))
            maxdate = datetime.datetime.fromtimestamp(max(listDate))
            msg = bdd.reset_volData(file.filename.replace(
                ".xlsx", ""), mindate, maxdate)
            # ajout de tous les vols dans la table vols
            for vol in data:
                if (vol['tour de piste'] != 1):
                    vol['tour de piste'] = 0
                msg, lastId = bdd.add_volData(file.filename.replace(".xlsx", ""), vol['immat'], datetime.datetime.fromtimestamp(
                    vol['depart'].timestamp()), datetime.datetime.fromtimestamp(vol['arrivee'].timestamp()), vol['tour de piste'])
                #print (str(lastId) + " " + vol['immat'] + " -- " + msg)
            infoMsg = "uploadOK"
            return render_template("index.html", maPage="fichiers.html", vols=data, monTitre="Téléchargement terminé", fileName=file.filename, info=infoMsg)
        else:
            return render_template("index.html", maPage="fichiers.html", monTitre="Page téléchargement")
    return redirect("/accueil/accessNotAllowed")


@app.route('/visualisation')
@app.route('/visualisation/<infoMsg>')
def visualisation(infoMsg=""):
    if auth.checkRole("admin"):
        msg, listeVol = bdd.get_volsData()
        print(msg)
        return render_template("index.html", maPage="visualisation.html", liste=listeVol, monTitre="Page Visualisation", info=infoMsg)
    return redirect("/accueil/accessNotAllowed")


@app.route('/getCalendar', methods=["POST"])
def getCalendar():
    if auth.checkRole("member"):
        dict = bib_vols.final_cal('both')
        return jsonify(dict)
    return redirect("/accueil/accessNotAllowed")


@app.route('/getCalendar_tdp', methods=["POST"])
def getCalendar_tdp():
    if auth.checkRole("member"):
        dict = bib_vols.final_cal('tdp')
        return jsonify(dict)
    return redirect("/accueil/accessNotAllowed")


@app.route('/getCalendar_mvt', methods=["POST"])
def getCalendar_mvt():
    if auth.checkRole("member"):
        dict = bib_vols.final_cal('mvt')
        return jsonify(dict)
    return redirect("/accueil/accessNotAllowed")


@app.route("/suppVol/<idVol>")
def suppVol(idVol=""):
    if auth.checkRole("admin"):
        msg = bdd.del_volData(idVol)
        print(msg)
        return redirect("/visualisation/suppVolOK")
    return redirect("/accueil/accessNotAllowed")


@app.route("/addVol", methods=['POST'])
def addVol():
    if auth.checkRole("admin"):
        aeroclub = request.form['aeroclub']
        immat = request.form['immat']
        dateDepart = request.form['dateDepart']
        heureDepart = request.form['heureDepart']
        dateArrivee = request.form['dateArrivee']
        heureArrivee = request.form['heureArrivee']
        depart = dateDepart+" " + heureDepart
        arrivee = dateArrivee+" " + heureArrivee
        tourpiste = int(request.form['tourpiste'])
        msg, lastId = bdd.add_volData(
            aeroclub, immat, depart, arrivee, tourpiste)
        print(msg)
        return redirect("/visualisation/" + msg)
    return redirect("/accueil/accessNotAllowed")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html", maPage="404.html", monTitre="404")
