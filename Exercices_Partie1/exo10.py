def creationListe():
    length = int(input("Longueur de votre liste : "))
    liste = []
    for i in range(length):
        nb = int(input("Votre nombre pour la place "+ str(i) + " : "))
        liste.append(nb)
    return liste

def triListe (liste):
    for i in range(1, len(liste)):
        k = liste[i]
        j = i - 1
        while j >= 0 and k < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = k
    return liste

liste = creationListe()
print("Votre liste de départ est donc : ", liste)
listeTriee = triListe(liste)
print("Votre liste triée est : ", listeTriee)