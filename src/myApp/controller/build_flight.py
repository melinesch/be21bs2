# --------------------------------------------------------------------------------------
# ----------------- Programme pour créer un csv avec des vols aléatoires ---------------
# --------------------------------------------------------------------------------------

import random


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


file = 'vol.csv'


def build(deb, fin, nb):
    f = open(file, 'w')

    for i in range(365):
        for k in range(nb):
            hdep = 0
            while hdep == 13 or hdep == 0:
                hdep = random.randint(8, 20)
            if hdep < 10:
                hdeps = '0'+str(hdep)
            else:
                hdeps = str(hdep)
            strdep = str(deb[2])+'-'+str(deb[1])+'-' + \
                str(deb[0])+' '+hdeps+':00'

            d = random.randint(0, 3)
            cp = [i for i in deb]

            for _ in range(d):
                cp = heure_suivante(deb)

            if hdep+d < 10:
                hdep = '0'+str(hdep+d)
            else:
                hdep = str(hdep+d)
            strfin = str(cp[2])+'-'+str(cp[1])+'-'+str(cp[0])+' '+hdep+':00'

            tdp = random.randint(0, 1)
            if tdp == 1:
                ligne = "F-HEJB;"+strdep+';'+strfin+';1'
            else:
                ligne = "F-HEJB;"+strdep+';'+strfin+';'

            f.write(ligne+'\n')
            hdep = 0
        while deb[3] != 0:
            deb = heure_suivante(deb)
            print(deb)


build([1, 1, 2023, 8], [10, 1, 2023, 20], 140)
