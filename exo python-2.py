
#EXERCICE 2 : Concaténation de Chaînes et Structures Conditionnelles
#====================================================================

#Thématiques couvertes :
#- Concaténation de chaînes de caractères
#- Formatage de chaînes avec f-strings
#- Structures conditionnelles (if, elif, else)
#- Opérateurs de comparaison


# ==========================================
# EXERCICE 2.1 : Concaténation simple
# ==========================================

# Créez deux variables "prenom" et "nom"
# Concaténez-les pour former le nom complet avec un espace entre les deux
# Affichez le résultat

# Votre code ici :
prénom = "sara"
nom = "kouton"
nom_complet = prénom + " " + nom
print(nom_complet)



# ==========================================
# EXERCICE 2.2 : Messages personnalisés avec f-strings
# ==========================================

# Créez des variables : prenom, age, ville
# Utilisez une f-string pour créer et afficher le message suivant :
# "Bonjour, je m'appelle [prenom], j'ai [age] ans et j'habite à [ville]"

# Votre code ici :
prenom = "Lina"
age = 22
ville = "Tunis"
message = f"Bonjour, je m'appelle {prenom}, j'ai {age} ans et j'habite à {ville}"
print(message) 




# ==========================================
# EXERCICE 2.3 : Vérification de majorité
# ==========================================

# Demandez (ou créez une variable) l'âge d'une personne
# Si l'âge est >= 18, affichez "Vous êtes majeur"
# Sinon, affichez "Vous êtes mineur"

# Votre code ici :
age = 17
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")




# ==========================================
# EXERCICE 2.4 : Mention selon la note
# ==========================================

# Créez une variable "note" (sur 20)
# Affichez la mention selon ces critères :
# - 16 à 20 : "Très bien"
# - 14 à 15.99 : "Bien"
# - 12 à 13.99 : "Assez bien"
# - 10 à 11.99 : "Passable"
# - Moins de 10 : "Échec"
# Utilisez if/elif/else

# Votre code ici :
note = 13
if note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Échec")




# ==========================================
# EXERCICE 2.5 : Catégorisation de température
# ==========================================

# Créez une variable "temperature" (en degrés Celsius)
# Affichez un message selon la température :
# - >= 35 : "Canicule !"
# - >= 25 : "Il fait chaud"
# - >= 15 : "Il fait bon"
# - >= 5 : "Il fait frais"
# - < 5 : "Il fait froid"

# Votre code ici :
temperature = 18
if temperature >= 35:
    print("Canicule !")
elif temperature >= 25:
    print("Il fait chaud")
elif temperature >= 15:
    print("Il fait bon")
elif temperature >= 5:
    print("Il fait frais")
else:
    print("Il fait froid")




# ==========================================
# EXERCICE 2.6 : Vérification de nombre pair/impair
# ==========================================

# Créez une variable "nombre"
# Vérifiez si le nombre est pair (reste de division par 2 = 0)
# Affichez "Le nombre X est pair" ou "Le nombre X est impair"

# Votre code ici : 
nombre = 10
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair")
else:
    print(f"Le nombre {nombre} est impair")





# ==========================================
# EXERCICE 2.7 : Calcul de remise
# ==========================================

# Un magasin propose des remises selon le montant d'achat :
# - >= 1000 dinars : remise de 20%
# - >= 500 dinars : remise de 10%
# - >= 100 dinars : remise de 5%
# - < 100 dinars : pas de remise
# Créez une variable "montant" et calculez le prix après remise
# Affichez le montant initial, le pourcentage de remise et le montant final

# Votre code ici :
montant = 3951
if montant >= 1000:
    remise = 0.20
elif montant >= 500:
    remise = 0.10
elif montant >= 100:
    remise = 0.05
else:
    remise = 0.0
montant_final = montant * (1 - remise)
print(f"Montant initial : {montant} dinars")
print(f"Pourcentage de remise : {remise * 100}%")
print(f"Montant final après remise : {montant_final} dinars")




# ==========================================
# EXERCICE 2.8 : Jour de la semaine
# ==========================================

# Créez une variable "jour" avec un nombre entre 1 et 7
# Affichez le jour de la semaine correspondant :
# 1 = Lundi, 2 = Mardi, 3 = Mercredi, 4 = Jeudi, 5 = Vendredi, 6 = Samedi, 7 = Dimanche
# Si le nombre n'est pas entre 1 et 7, affichez "Jour invalide"

# Votre code ici :
jour = 4
if jour == 1:
    print("Lundi")
elif jour == 2:
    print("Mardi")
elif jour == 3:
    print("Mercredi")
elif jour == 4:
    print("Jeudi")
elif jour == 5:
    print("Vendredi")
elif jour == 6:
    print("Samedi")
elif jour == 7:
    print("Dimanche")
else:
    print("Jour invalide")




# ==========================================
# EXERCICE 2.9 : Validation de mot de passe simple
# ==========================================

# Créez une variable "mot_de_passe" avec une valeur
# Vérifiez si le mot de passe a au moins 8 caractères
# Si oui, affichez "Mot de passe valide"
# Sinon, affichez "Le mot de passe doit contenir au moins 8 caractères"

# Votre code ici :
mot_de_passe = "mypassword"
if len(mot_de_passe) >= 8:
    print("Mot de passe valide")
else:
    print("Le mot de passe doit contenir au moins 8 caractères")



# ==========================================
# EXERCICE 2.10 : Calcul de prix selon catégorie
# ==========================================

# Un cinéma applique des tarifs selon l'âge :
# - Enfant (< 12 ans) : 5 dinars
# - Étudiant (12 à 25 ans) : 8 dinars
# - Adulte (26 à 59 ans) : 12 dinars
# - Senior (>= 60 ans) : 7 dinars
# Créez une variable "age" et affichez le prix du billet

# Votre code ici :
age = 45
if age < 12:
    prix_billet = 5
elif age <= 25:
    prix_billet = 8
elif age <= 59:
    prix_billet = 12
else:
    prix_billet = 7
print(f"Le prix du billet est de {prix_billet} dinars") 



# ==========================================
# BONUS : Message combiné avec conditions
# ==========================================

# Créez un programme qui :
# - Demande le nom et l'âge (ou utilisez des variables)
# - Affiche "Bonjour [nom]" suivi de :
#   - "Bienvenue dans notre programme !" si l'âge >= 18
#   - "Vous devez être accompagné d'un adulte" si l'âge < 18
# Utilisez des f-strings pour formater le message

# Votre code ici :
nom = "keyveen"
age = 16
message = f"Bonjour {nom}. "
if age >= 18:
    message += "Bienvenue dans notre programme !"
else:
    message += "Vous devez être accompagné d'un adulte."
print(message)


