n = int (input ("Entré un nombre pour obtenir sa racine carré: "))
i = 1

while n != n%0.001 :
    i = i + 1
    n = (n*n)/i
    print(n)
    break 
