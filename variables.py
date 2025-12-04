def test_locale():
    message = "Je suis locale"
    print(message)

test_locale()



compteur = 0  
def incrementer():
    global compteur
    compteur += 1

incrementer()
incrementer()
print(compteur) 



compteur = 0

def incrementer(valeur):
    return valeur + 1

compteur = incrementer(compteur)
compteur = incrementer(compteur)
print(compteur)  