import json
from ..model import bdd
from ..config import SEUIL, COULEUR, NB_MVT_TDP, BUILD_ZERO, CACHE_BASE
import os

# -----------------------------------------------------------------
# --------------------- FONCTIONS AUXILIAIRES ---------------------
# -----------------------------------------------------------------


def date_unitaire(date):
    an = date[0]+date[1]+date[2]+date[3]
    mois = date[5]+date[6]
    jour = date[8]+date[9]
    heure = date[11]+date[12]
    return [int(jour), int(mois), int(an), int(heure)]


def jour_fevrier(annee):
    if(annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
        return 29
    else:
        return 28


def heure_suivante(date_actu):
    nb_jour_mois = [31, jour_fevrier(
        date_actu[2]), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_actu[3] += 1
    if date_actu[3] == 24:
        date_actu[0] += 1
        date_actu[3] = 0
        if date_actu[0] > nb_jour_mois[date_actu[1]-1]:
            if date_actu[1] == 12:
                date_actu = [1, 1, date_actu[2]+1, 0]
            else:
                date_actu[1] += 1
                date_actu[0] = 1
    return date_actu


def construction_dico(vols):
    dico = {}
    for vol in vols:
        dep = vol[1]
        arr = vol[2]
        tdp = vol[3]
        ldep = date_unitaire(dep)
        larr = date_unitaire(arr)
        date_actu = [i for i in ldep]
        res = []
        if tdp:
            while date_actu != larr:
                h = str(date_actu[0])+'-'+str(date_actu[1]) + \
                    '-'+str(date_actu[2])+'-'+str(date_actu[3])
                # for _ in range(NB_MVT_TDP):
                res.append(h)
                date_actu = heure_suivante(date_actu)
        else:
            date_fin = [i for i in larr]
            hdep = str(date_actu[0])+'-'+str(date_actu[1]) + \
                '-'+str(date_actu[2])+'-'+str(date_actu[3])
            harr = str(date_fin[0])+'-'+str(date_fin[1]) + \
                '-'+str(date_fin[2])+'-'+str(date_fin[3])
            res.append(hdep)
            res.append(harr)
        for h in res:
            try:
                dico[h].append([vol[0], vol[3]])
            except:
                dico[h] = [[vol[0], vol[3]]]
        try:
            dico[str(larr[0])+'-'+str(larr[1])+'-'+str(larr[2]) +
                 '-'+str(larr[3])].append([vol[0], vol[3]])
        except:
            dico[str(larr[0])+'-'+str(larr[1])+'-'+str(larr[2]) +
                 '-'+str(larr[3])] = [[vol[0], vol[3]]]
    return dico


def nb_vols(l):
    nb_volsv = 0
    nb_tdp = 0
    for (immat, tdp) in l:
        if tdp == 1:
            nb_tdp += 1
            nb_volsv+=NB_MVT_TDP
        else:
            nb_volsv += 1
    return [nb_volsv, nb_tdp]


def heures_concerne(dico):
    res = {}
    for key in dico:
        res[key] = nb_vols(dico[key])
    return res


def convert_date_format(ligne):
    d, m, y, h = ligne.strip().split('-')
    if len(d) == 1:
        d = '0'+d
    if len(m) == 1:
        m = '0'+m
    if len(h) == 1:
        h = '0'+h
    date = y+'-'+m+'-'+d+' '+h+':00'
    return date


def convert_date_key(ligne):
    d, m, y, h = ligne.strip().split('-')
    return [int(d), int(m), int(y), int(h)]


def convert_key_date(date):
    return str(date[0])+'-'+str(date[1])+'-'+str(date[2])+'-'+str(date[3])


def couleur(mvt, tdp, solActive):
    color = COULEUR['vert']
    if not solActive:
        if mvt == 0:
            return COULEUR['zero']
        if mvt < SEUIL['vert']:
            color = COULEUR['vert']
        elif mvt < SEUIL['jaune']:
            color = COULEUR['jaune']
        elif mvt < SEUIL['orange']:
            if tdp/mvt < SEUIL['tdp']:
                color = COULEUR['orange']
            else:
                color = COULEUR['rouge']
        else:
            color = COULEUR['rouge']
    return color


def construit_tableau_event(dico):
    res = []
    for key in dico:
        if key[-2]+key[-1] != '13' and key[-2]+key[-1] != '-7' and key[-2]+key[-1] != '20':
            mvt, tdp = dico[key]
            event = {'text': 'MVT:'+str(mvt)+'   TDP:'+str(tdp), 'start_date': convert_date_format(key), 'end_date': convert_date_format(
                convert_key_date(heure_suivante(convert_date_key(key)))), 'color': couleur(mvt, tdp, False)}
            res.append(event)
    return res


def construit_tableau_event_sans_vol(dico):
    deb = [i for i in BUILD_ZERO['debut']]
    fin = [i for i in BUILD_ZERO['fin']]
    res = []
    while deb != fin:
        if convert_key_date(deb) not in dico:
            sdate = convert_date_format(convert_key_date(deb))
            deb = heure_suivante(deb)
            if deb[3] != 14 and deb[3] != 21 and deb[3] != 8:
                edate = convert_date_format(convert_key_date(deb))
                event = {'text': 'MVT:0 TDP:0', 'start_date': sdate,
                         'end_date': edate, 'color': couleur(0, 0, False)}
                res.append(event)
        else:
            deb = heure_suivante(deb)
    return res


def convert_json(t):
    res = '['
    for event in t:
        res += '{"text":"'+event["text"]+'",\n "start_date":"'+event["start_date"] + \
            '",\n "end_date":"'+event["end_date"] + \
            '",\n "color":"'+event["color"]+'"},\n'
    res = res[0:len(res)-2]
    res += '\n]'
    return res


def write_json(string, path):
    file = open(path, 'w')
    file.write(string)
    file.close()


def extract_bdd():
    _, base = bdd.get_volsData()
    vols = []
    for x in base:
        vols.append([x['immat'], str(x['depart'])[0:16],
                    str(x['arrivee'])[0:16], x['tourpiste']])
    return vols


# --------------------------------------------------------------
# --------------------- FONCTION FINALE ------------------------
# --------------------------------------------------------------


def final_cal():
    if not os.path.exists('cal.json') or not CACHE_BASE:
        # f = open('cal.json','w')
        vols = extract_bdd()
        dico = construction_dico(vols)
        dico = heures_concerne(dico)
        res = construit_tableau_event(
            dico) + construit_tableau_event_sans_vol(dico)
        write_json(convert_json(res), 'cal.json')
    else:
        f = open('cal.json')
        res = json.load(f)
    return res
