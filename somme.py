def somme(*args):
    total = 0
    for valeur in args:
        total += valeur
    return total

# Tests
print(somme(1, 2))           
print(somme(1, 2, 3, 4))     

def produit(*args):
    total = 1
    for valeur in args:
        total *= valeur
    return total

# Tests
print(produit(2, 3, 4))      
print(produit())              

