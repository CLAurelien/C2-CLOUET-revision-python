list = [4,56,34,5,7,21,16,12,11,8]

def moyenne (list):
        lenght = len(list)
        total = sum(list)
        result = total / lenght
        return result

moy = moyenne(list)

print("Le chiffre max est : ", max(list))
print("Le chiffre min est : ", min(list))
print("La moyenne est : ", moy)