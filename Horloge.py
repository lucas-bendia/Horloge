import time

# Variable globale pour stocker l'heure réglée
heure_reglee = None

def afficher_heure():
    # Si l'heure a été réglée, utilisez cette heure
    if heure_reglee is not None:
        h, m, s = heure_reglee
    else:
        # Sinon, obtenez l'heure actuelle
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec

    # Affichage de l'heure
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def regler_heure(hms):
    global heure_reglee
    heure_reglee = hms

while True:
    print(afficher_heure())
    time.sleep(1)  # Attendre une seconde
