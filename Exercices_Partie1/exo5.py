def fact():
    saisie = int(input("Quelle factorial voulez-vous avoir : "))
    result = 1
    for i in range(1,saisie+1):
        result *= i


    print("Le resultat est ", result)

fact()