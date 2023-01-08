from flask import Flask, render_template, session, request, redirect
from myApp.model import bdd
import secrets
import string
from random import randint 
import hashlib


app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars


#page accueil
@app.route("/")
@app.route("/accueil")
@app.route("/accueil/<infoMsg>")
def index(infoMsg=""):
    return render_template("index.html", maPage = "accueil.html", monTitre = "Accueil", info=infoMsg)

@app.route('/webmaster')
def webmaster():
    return render_template("index.html", maPage = "webmaster.html", monTitre = "Webmasters")

@app.route('/prevision')
def previsions():
    return render_template("index.html", maPage = "prevision.html", monTitre = "Prévisions")

@app.route('/compte')
@app.route('/compte/<infoMsg>')
def compte(infoMsg=""):
    return render_template("index.html", maPage = "compte.html", monTitre = "Création de compte", info=infoMsg)

@app.route('/login')
@app.route('/login/<infoMsg>')
def login(infoMsg=""):
    return render_template("index.html", maPage = "login.html", monTitre = "Se connecter", info=infoMsg)

#réception des données de connexion
@app.route("/connecter", methods=["POST"])
def connecter():
    login=request.form['login']
    mdp=request.form['mdp']
    #vérification de paramètres en BDD
    msg, user = bdd.verifAuthData(login,mdp)
    print([msg, user, session])

    try:
        #authentification réussie
        #initialisation des sessions
        session["idUser"]=user["idUser"]
        session["nom"]=user["nom"]
        session["prenom"]=user["prenom"]
        session["avatar"]=user["avatar"]
        session["login"]=user["login"]
        session["statut"]=user["statut"]
        session["mail"]=user["mail"]
        session["newMdp"]=user["newMdp"]
    
        if session["statut"]==1:
            return redirect("/accueil/authOK")
        else:
            return redirect("/compte/authOK")
    
    except TypeError as err:
        #echec d'authentification
        print("Failed verifAuth:{}".format(err))
        
        return redirect("/login/authEchec")
    
@app.route("/logout")
def deconnecter():
    #authentification réussie
    #initialisation des sessions
    session["idUser"]=""
    session["nom"]=""
    session["prenom"]=""
    session["avatar"]=""
    session["login"]=""
    session["statut"]=""
    session["mail"]=""
    session["newMdp"]=""

    return redirect("/accueil/logoutOK")
  
#réception des données du formulaire de création de compte
@app.route("/addUser", methods=['POST'])
def addUser():
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    mail = request.form["mail"]
    print(nom + " " + prenom + " " + mail)
    newMdp = 2
    motPasse = ''
    for i in range(10):
        motPasse += ''.join(secrets.choice(alphabet))
    login = request.form["login"]
    mdp = hashlib.sha256(motPasse.encode())
    mdpC = mdp.hexdigest() #mot de passe chiffré
    print(mdpC)
    print("user password, to be sent to the user '" + login + "': " + motPasse)
    statut = int(request.form["statut"])
    a = randint(1, 16)
    avatar = "" + str(a) + ".png"
    msg, lastId = bdd.add_userData(nom,prenom,mail,login,mdpC,statut, newMdp, avatar)
    print(msg)
    return redirect ("/compte/" +msg)
    