def affiche_menu():
    print("Menu: ")
    print("*Action 1")
    print("* Action 2")

affiche_menu() #Appel à la fontion affiche_menu

def dire(text):
    print(text)

dire('Bonjour')
dire('Au Revoir')
dire('A Demain')

def addition(a, b):
    return a + b

somme = addition(10, 5)
print(somme)

def saluer(nom = 'Visiteur'):
    print('Bonjour ' + nom)
def

saluer('Clem')
saluer()