a = 42
def affichage():
    print(a)

affichage()

def change(valeur):
    global a
    a = valeur

print(a)
change(10)
print(a)

nombre = 8
nombre = int(input("La table de multiplication que souhaitez voir :"))
print("Voici la table de multiplication de ", nombre)
for x in range(0, 11): #le 11 est exclu
    print(x, "x", nombre, " = ", x*nombre)
