liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste)
def carre(liste):
    for i in range(len(liste)):
        liste[i] = liste[i] * liste[i]
    print(liste)

carre(liste)