import mysql.connector
from mysql.connector import errorcode
from ..config import DB_SERVER
import hashlib

#################################################################################################################
# connexion au serveur de la base de données

def connexion():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        error = None
    except mysql.connector.Error as err:
        error = err
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx, error


#################################################################################################################
# fermeture de la connexion au serveur de la base de données

def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()
    
    
def get_membresData():
    try:
        cnx, error = connexion()
        if error is not None:
           return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM membres"
        cursor.execute(sql)
        listeMembre = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKmembres"
    except mysql.connector.Error as err:
        listeMembre = None
        msg = "Failed get membres data : {}".format(err)
    return msg, listeMembre

def verifAuthData(login, mdp):
    try:
        cnx, error = connexion()
        if error is not None:
            return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification WHERE login=%s and motPasse=%s"
        mdp = hashlib.sha256(mdp.encode())
        mdpC = mdp.hexdigest() # mot de passe chiffré
        param=(login, mdpC)
        cursor.execute(sql, param)
        user = cursor.fetchone()
        close_bd(cursor, cnx)
        print(user)
        msg = "authOK"
    except mysql.connector.Error as err:
        user = None
        msg = "Failed get Auth data : {}".format(err)
    print(user)
    return msg, user

def del_membreData(idUser):
    try:
        cnx, error = connexion()
        cursor = cnx.cursor()
        sql = "DELETE FROM membres WHERE idUser=%s;"
        param = (idUser,)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "suppMembreOK"
    except mysql.connector.Error as err:
        msg = "Failed del membre data : {}".format(err)
    return msg

#ajout d'un utilisateur
def add_userData(nom, prenom, mail, login, pwd, statut, newMdp, avatar):
    try:
        cnx,error=connexion()
        cursor=cnx.cursor()
        sql="INSERT into identification (idUser,nom,prenom,mail,login,motPasse,statut,newMdp,avatar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        param=(0,nom,prenom,mail,login,pwd,statut, newMdp, avatar)
        print(sql)
        print(param)
        cursor.execute(sql,param)
        #récupère le dernier IdUser généré par le serveur sql
        lastId=cursor.lastrowid
        cnx.commit()
        close_bd(cursor,cnx)
        msg="addUserOK"
    except mysql.connector.Error as err:
        lastId=None
        msg="Failed add user data:{}".format(err)
    return msg, lastId

#modification d'un utilisateur
def update_userData(champ, newValue, idUser):
    try:
        cnx, error = connexion()
        cursor = cnx.cursor()
        sql = "UPDATE identification SET " + champ + "= %s WHERE idUser = %s;"
        param = (newValue, idUser)   
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "updateUserOK"
        if (champ == "motPasse"):
            msg = "updateUserMdpOK"
    except mysql.connector.Error as err:
        msg = "Failed update user data : {}".format(err)
    return msg

#ajout des vols 
def add_volData(aeroclub, immat, depart, arrivee, tourpiste):
    try:
        cnx, error = connexion()
        cursor = cnx.cursor()
        sql = "INSERT INTO vol (aeroclub, immat, depart, arrivee, tourpiste) VALUES (%s, %s, %s, %s, %s);"
        param = (aeroclub, immat, depart, arrivee, tourpiste)
        cursor.execute(sql, param)
    #recupere le dernier idVol généré par le serveur sql
        lastId = cursor.lastrowid
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "addVolOK"
    except mysql.connector.Error as err:
        lastId=None
        msg = "Failed add vol data: {}".format(err)
    return msg, lastId

# récupérer tous les vols à partir de la BdD
def get_volsData():
    try:
        cnx, error = connexion()
        if error is not None:
           return error, None
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM vol ORDER BY depart ASC, arrivee ASC"
        cursor.execute(sql)
        listeVol = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "OKvol"
    except mysql.connector.Error as err:
        listeVol = None
        msg = "Failed get vols data : {}".format(err)
    return msg, listeVol