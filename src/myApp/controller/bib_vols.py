# vols=[['immat','dep','arr','tdp']]
import json
from ..model import bdd


# --------------------------------------------------------------
# --------------------- VARIABLES GLOBALES ---------------------
# --------------------------------------------------------------


VERT='green'
JAUNE='#E9E100'
ORANGE='orange'
ROUGE='red'

COMPTE_MVT=False            # Indique si l'on compte les mouvvements sur la totalité des heures (True) ou seulement au départ et à l'arrivée
NB_MVT_TDP=7                # Nombre de tdp/h


# -----------------------------------------------------------------
# --------------------- FONCTIONS AUXILIAIRES ---------------------
# -----------------------------------------------------------------
    
       
def date_unitaire(date):
    an = date[0]+date[1]+date[2]+date[3]
    mois = date[5]+date[6]
    jour = date[8]+date[9]
    heure = date[11]+date[12]
    return [int(jour),int(mois),int(an),int(heure)]
    
    
def jour_fevrier(annee):
    if(annee%4==0 and annee%100!=0 or annee%400==0):
        return 29
    else:
        return 28
    
    
def heure_suivante(date_actu):
    nb_jour_mois=[31,jour_fevrier(date_actu[2]),31,30,31,30,31,31,30,31,30,31]
    date_actu[3]+=1
    if date_actu[3]==24:
        date_actu[0]+=1
        date_actu[3]=0
        if date_actu[0] > nb_jour_mois[date_actu[1]-1]:
            if date_actu[1]==12:
                date_actu=[1,1,date_actu[2]+1,0]
            else:
                date_actu[1]+=1
                date_actu[0]=1
    return date_actu
    
    
def construction_dico(vols):

    dico = {}
    for vol in vols:
        dep=vol[1]
        arr=vol[2]
        tdp=vol[3]
        ldep=date_unitaire(dep)
        larr=date_unitaire(arr)
        date_actu = [i for i in ldep]
        res=[]
        if tdp or COMPTE_MVT:
            while date_actu != larr:
                h = str(date_actu[0])+'-'+str(date_actu[1])+'-'+str(date_actu[2])+'-'+str(date_actu[3])
                for _ in range(NB_MVT_TDP):
                    res.append(h)
                date_actu=heure_suivante(date_actu)
        else:
            date_fin=[i for i in larr]
            hdep = str(date_actu[0])+'-'+str(date_actu[1])+'-'+str(date_actu[2])+'-'+str(date_actu[3])
            harr = str(date_fin[0])+'-'+str(date_fin[1])+'-'+str(date_fin[2])+'-'+str(date_fin[3])
            res.append(hdep)
            res.append(harr)
            
            
                
        for h in res:
            try:
                dico[h].append([vol[0],vol[3]])
            except:
                dico[h]=[[vol[0],vol[3]]]   
        try:
            dico[str(larr[0])+'-'+str(larr[1])+'-'+str(larr[2])+'-'+str(larr[3])].append([vol[0],vol[3]])
        except:
            dico[str(larr[0])+'-'+str(larr[1])+'-'+str(larr[2])+'-'+str(larr[3])] = [[vol[0],vol[3]]]
    return dico


def nb_vols(l):
    nb_vols=0
    nb_tdp=0
    for (immat,tdp) in l:
        nb_vols+=1
        if tdp==1:
            nb_tdp+=1
    return [nb_vols, nb_tdp]


def heures_concerne(dico):
    res={}
    for key in dico:
        res[key]=nb_vols(dico[key])
    return res


def convert_date_format(ligne):
    d,m,y,h=ligne.strip().split('-')
    if len(d)==1:
        d='0'+d
    if len(m)==1:
        m='0'+m
    if len(h)==1:
        h='0'+h 
    date=y+'-'+m+'-'+d+' '+h+':00'
    return date

    
def convert_date_key(ligne):
    d,m,y,h=ligne.strip().split('-')
    return [int(d),int(m),int(y),int(h)] 


def convert_key_date(date):
    return str(date[0])+'-'+str(date[1])+'-'+str(date[2])+'-'+str(date[3])


def couleur(mvt,tdp,solActive):
    color=VERT
    if not solActive:
        if mvt<20:
            color=VERT
        elif mvt<40:
            color=JAUNE
        elif mvt<60:
            if tdp/mvt<0.40:
                color=ORANGE
            else:
                color=ROUGE
        else:
            color=ROUGE
    return color
        
    
def construit_tableau_event(dico):
    res=[]
    # {text:"Meeting",    start_date:"2023-01-11 14:00", end_date:"2023-01-11 17:00", color:'green'}
    for key in dico:
        mvt,tdp = dico[key]
        event = {'text':'MVT:'+str(mvt)+'   TDP:'+str(tdp), 'start_date':convert_date_format(key), 'end_date': convert_date_format(convert_key_date(heure_suivante(convert_date_key(key)))),'color':couleur(mvt,tdp,False)}
        res.append(event)
    return res 
    
    
def convert_json(t):
    res='['
    for event in t:
        res+='{"text":"'+event["text"]+'",\n "start_date":"'+event["start_date"]+'",\n "end_date":"'+event["end_date"]+'",\n "color":"'+event["color"]+'"},\n'
    res=res[0:len(res)-2]
    res+='\n]'
    return  res


def write_json(string,path):
    file = open(path,'w')
    file.write(string)
    file.close() 
    
def extract_bdd():
    _,base=bdd.get_volsData()
    vols=[]
    for x in base:
        vols.append([x['immat'],str(x['depart'])[0:16],str(x['arrivee'])[0:16],x['tourpiste']])
    return vols
    

# --------------------------------------------------------------
# --------------------- FONCTION FINALE ------------------------
# --------------------------------------------------------------


def final_cal():
    vols=extract_bdd()
    dico = construction_dico(vols)
    dico = heures_concerne(dico)
    res = construit_tableau_event(dico)
    return res





