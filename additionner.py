# Étape 3 – Fonction qui retourne un résultat
def additionner(a, b):
    total = a + b
    return total  # Renvoie la valeur au programme

# Utilisation avec return
resultat = additionner(3, 5)
print("Résultat avec return :", resultat)

# Exemple d'enchaînement
print("Enchaînement :", additionner(2, 4) * 10)

# Tester la différence avec print à l'intérieur
def additionner_sans_return(a, b):
    total = a + b
    print("Somme (print seulement) :", total)

res = additionner_sans_return(3, 5)
print("Résultat sans return :", res)  # Affiche None

# Vérifier le type
print("Type avec return :", type(additionner(3,5)))
print("Type sans return :", type(additionner_sans_return(3,5)))