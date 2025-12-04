def afficher_message(message, prefix="[INFO]"):
    print(f"{prefix} {message}")

# Tests
afficher_message("Tout fonctionne")                  
afficher_message("Une erreur est survenue", prefix="[ERREUR]")  
