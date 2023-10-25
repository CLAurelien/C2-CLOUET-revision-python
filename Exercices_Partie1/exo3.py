def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

num1 = int(input("Choisir le premier chiffre : "))
num2 = int(input("Choisir le deuxième chiffre : "))

resultAdd = addition(num1, num2)
print("L'addition est :", resultAdd)

resultSous = soustraction(num1, num2)
print("La soustraction est :", resultSous)

resultMul = multiplication(num1, num2)
print("La multiplication est :", resultMul)

resultDiv = division(num1, num2)
print("La division est :", resultDiv)