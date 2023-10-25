
def read(fichier):
    texte = open(fichier, "r")
    contenu = texte.read()
    texte.close()
    return contenu

fichier = input("Nom du fichier : ")
contenuTexte = read(fichier)
print(contenuTexte)
nbMots = len(contenuTexte.split())
print("Le fichier contient ", nbMots, "de mots.")

def write(fichierIni, fichierFin):
    contenuTexte = read(fichierIni)
    texte2 = open(fichierFin, "w")
    texte2.write(contenuTexte)

print("Pour copier un fichier")
fichierIni = input("Nom du fichier de départ : ")
fichierFin = input("Nom du fichier d'arrivée / ou création du fichier d'arrivée : ")
write(fichierIni, fichierFin)
