a = int (input("Entré votre un nombre entier A positif: "))
while a < 0 or a > 40000 :
    a = int (input("Votre chiffre A doit être compris entre 0 et 40000: "))
else:
    print("Votre chiffre A est valide")
    
    
b = int (input("Entré votre un nombre entier B positif: "))
while b < 0 or b > 40000 :
    b = int (input("Votre chiffre B doit être compris entre 0 et 40000: "))
else:
    print("Votre chiffre B est valide")


c = int (input("Entré votre un nombre entier C positif: "))
while c < 0 or c > 40000 :
    c = int (input("Votre chiffre C doit être compris entre 0 et 40000: "))
else:
    print("Votre chiffre C est valide")

moyenne = ((a + b + c) // 3)
print("La moyenne est de: " + str (moyenne))

    