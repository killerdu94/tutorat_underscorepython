# ==========================================

# Créez trois variables :
# - Une variable "prenom" contenant votre prénom (type string)
# - Une variable "age" contenant votre âge (type integer)
# - Une variable "taille" contenant votre taille en mètres (type float)
# Affichez ces trois variables avec des messages appropriés

# Votre code ici :
prénom =  "keyveen"
âge = 18 
taille = 1.75
print( prénom, âge,"ans",  taille,"mètres")

# EXERCICE 1.2 : Calculs simples
# ==========================================

# Déclarez deux variables nombre1 = 25 et nombre2 = 7
# Calculez et affichez :
# - La somme
# - La différence
# - Le produit
# - Le quotient (division normale)
# - Le quotient entier (division entière)
# - Le reste de la division (modulo)

# Votre code ici :
a = 25
b = 7
somme = a + b
différence = a - b
produit = a * b
quotient = a / b
quotient_entier = a // b
reste = a % b
print("La somme :", somme)
print("La différence :", différence)
print("Le produit :", produit)
print("Le quotient :", quotient)
print("Le quotient entier :", quotient_entier)
print("Le reste de la division :", reste)

# EXERCICE 1.3 : Calcul de l'aire d'un rectangle
# ==========================================

# Créez deux variables "longueur" et "largeur" avec des valeurs de votre choix
# Calculez et affichez l'aire du rectangle (longueur × largeur)
# Le résultat doit être affiché avec un message : "L'aire du rectangle est : X"

# Votre code ici : 
longueur = 5
largeur = 3
aire = longueur * largeur
print("L'aire du rectangle est :", aire)

# EXERCICE 1.4 : Calcul de la vitesse moyenne
# ==========================================

# Un véhicule parcourt 150 km en 2 heures
# Créez deux variables "distance" (en km) et "temps" (en heures)
# Calculez et affichez la vitesse moyenne (distance / temps)
# Format d'affichage : "La vitesse moyenne est de X km/h"

# Votre code ici :
distance = 150
temps = 2  
vitesse_moyenne = distance / temps
print("La vitesse moyenne est de", vitesse_moyenne, "km/h")

# EXERCICE 1.5 : Conversions de température
# ==========================================

# Convertissez 25 degrés Celsius en Fahrenheit
# Formule : Fahrenheit = (Celsius × 9/5) + 32
# Créez une variable "celsius" = 25
# Calculez la température en Fahrenheit et affichez le résultat

# Votre code ici :
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrés Celsius est égal à {fahrenheit} degrés Fahrenheit")

# EXERCICE 1.6 : Calcul du pourcentage
# ==========================================

# Un étudiant a obtenu 18 points sur 20 à un examen
# Calculez le pourcentage obtenu
# Créez les variables nécessaires et affichez : "L'étudiant a obtenu X%"

# Votre code ici :

points_obtenus = 18
points_normal = 20
pourcentage = (points_obtenus/points_normal)*100



# EXERCICE 1.7 : Prix avec TVA
# ==========================================

# Un produit coûte 100 dinars (HT - Hors Taxes)
# La TVA est de 19%
# Calculez le prix TTC (Toutes Taxes Comprises)
# Affichez le prix HT, le montant de la TVA et le prix TTC

# Votre code ici :

prix_HT = 100
tva = 0.19
montant_TVA = prix_HT * tva
prix_TTC = prix_HT + montant_TVA
print("Prix HT :", prix_HT, "dinars")


# EXERCICE 1.8 : Opérations avec différents types
# ==========================================

# Observez le résultat des opérations suivantes :
# - Que se passe-t-il si vous multipliez une chaîne de caractères par un nombre ?
# Testez : "Bonjour " * 3

# - Que se passe-t-il si vous additionnez deux chaînes ?
# Testez : "Bonjour " + "Monde"

# Votre code ici :
resultat_multiplication = "Bonjour " * 3
resultat_addition = "Bonjour " + "Monde"    
print(resultat_multiplication)
print(resultat_addition)

# BONUS : Calcul du périmètre et de l'aire d'un cercle
# ==========================================

# Créez une variable "rayon" = 5 (en cm)
# Calculez :
# - Le périmètre (2 × π × rayon) où π ≈ 3.14159
# - L'aire (π × rayon²)
# Affichez les résultats avec des messages appropriés

# Votre code ici :
rayon = 5
pi = 3.14
perimetre = 2 * pi * rayon
aire_cercle = pi * rayon ** 2
print("Le périmètre du cercle est :", perimetre, "cm")
print("L'aire du cercle est :", aire_cercle, "cm²") 