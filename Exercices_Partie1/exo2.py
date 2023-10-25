saisie = input("Saisissez une phrase : ")

print("Voici la phrase en majuscule : " + saisie.upper())
print("Voici la phrase en minuscule : " + saisie.lower())
length = len(saisie.split())
print("Cette phrase comporte ", length, " mots")