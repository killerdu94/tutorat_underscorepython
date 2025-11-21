#"""
#EXERCICE 3 : Listes et Boucles For
#===================================

#Thématiques couvertes :
#- Création et manipulation de listes
#- Accès aux éléments d'une liste
#- Parcourir une liste avec for
#- Utilisation de range()
#- Modification de listes
#"""

# ==========================================
# EXERCICE 3.1 : Création et affichage de listes
# ==========================================

# Créez une liste "fruits" contenant au moins 5 fruits différents
# Affichez la liste complète
# Affichez le premier fruit (index 0)
# Affichez le dernier fruit (index -1)

# Votre code ici :
fruits = ( "pomme", "banane", "kaki", "fruit de la passion", "tomate"),
print(fruits)
print(fruits[0])
print(fruits[-1])



# ==========================================
# EXERCICE 3.2 : Parcourir une liste avec for
# ==========================================

# Créez une liste "notes" contenant [12, 15, 18, 10, 14, 16]
# Utilisez une boucle for pour afficher chaque note
# Format : "Note : X/20"

# Votre code ici :
note = ["12", "15", "18", "10", "14", "16"]
for n in note:
    print("Note : " + n + "/20")



# ==========================================
# EXERCICE 3.3 : Calcul de la somme d'une liste
# ==========================================

# Créez une liste "nombres" contenant [5, 10, 15, 20, 25]
# Calculez la somme de tous les nombres dans la liste
# Affichez le résultat

# Votre code ici :

liste = [5,10,15,20,25]
total = 0
for ele in range(0, len(liste)):
    total = total + liste[ele]
print("Somme de tous les éléments d'une liste: ", total)







# ==========================================
# EXERCICE 3.4 : Trouver le maximum et le minimum
# ==========================================

# Créez une liste "temperatures" contenant [22, 25, 19, 28, 21]
# Trouvez et affichez la température maximale
# Trouvez et affichez la température minimale
# (Sans utiliser les fonctions max() et min())

# Votre code ici :
temperature =  [22, 25, 19, 28, 21]

max_temp = temperature[0]
min_temp = temperature[0]

for t in temperature:
    if t > max_temp:
        max_temp = t
    if t < min_temp:
        min_temp = t

print("Température maximale:", max_temp)
print("Température minimale:", min_temp)


# ==========================================
# EXERCICE 3.5 : Comptage avec range()
# ==========================================

# Affichez tous les nombres pairs de 2 à 20 (inclus)
# Utilisez range() avec un pas approprié

# Votre code ici :
for i in range(2, 21, 2):  
    print(i)



# ==========================================
# EXERCICE 3.6 : Table de multiplication
# ==========================================

# Affichez la table de multiplication de 7 (de 1 à 10)
# Format : "7 × 1 = 7"
#          "7 × 2 = 14"
#          etc.
# Utilisez une boucle for avec range()

# Votre code ici :
for i in range(1, 11):  
    print(f"7 × {i} = {7 * i}")




# ==========================================
# EXERCICE 3.7 : Filtrer les notes supérieures à 10
# ==========================================

# Créez une liste "notes" contenant [8, 12, 15, 9, 18, 7, 14]
# Créez une nouvelle liste vide "notes_valides"
# Parcourez la liste et ajoutez seulement les notes >= 10 à "notes_valides"
# Affichez les deux listes

# Votre code ici :
notes = [8, 12, 15, 9, 18, 7, 14]
notes_valides = []

for n in notes:
    if n >= 10:
        notes_valides.append(n)

print("Toutes les notes :", notes)
print("Notes valides (>=10) :", notes_valides)




# ==========================================
# EXERCICE 3.8 : Compter les occurrences
# ==========================================

# Créez une liste "couleurs" contenant ["rouge", "bleu", "vert", "rouge", "jaune", "rouge", "bleu"]
# Comptez combien de fois "rouge" apparaît dans la liste
# Affichez le résultat

# Votre code ici :
couleurs = ["rouge", "bleu", "vert", "rouge", "jaune", "rouge", "bleu"]
compteur_rouge = 0

for c in couleurs:
    if c == "rouge":
        compteur_rouge += 1

print("Nombre de fois que 'rouge' apparaît :", compteur_rouge)




# ==========================================
# EXERCICE 3.9 : Calcul de la moyenne d'une liste
# ==========================================

# Créez une liste "notes" contenant plusieurs notes
# Calculez la moyenne de ces notes
# Affichez la moyenne avec 2 décimales

# Votre code ici :
notes = [12, 15, 9, 18, 14]  
somme = 0

for n in notes:
    somme += n

moyenne = somme / len(notes)
print("Moyenne des notes :", round(moyenne, 2))




# ==========================================
# EXERCICE 3.10 : Parcourir avec index (enumerate)
# ==========================================

# Créez une liste "etudiants" contenant ["Ali", "Fatima", "Ahmed", "Salma"]
# Utilisez enumerate() pour afficher chaque étudiant avec son numéro
# Format : "Étudiant 1 : Ali"
#          "Étudiant 2 : Fatima"
#          etc.

# Votre code ici :
etudiants = ["Ali", "Fatima", "Ahmed", "Salma"]

for index, nom in enumerate(etudiants, start=1):
    print(f"Étudiant {index} : {nom}")




# ==========================================
# EXERCICE 3.11 : Ajouter des éléments
# ==========================================

# Créez une liste vide "achats"
# Ajoutez-y les éléments suivants un par un : "pain", "lait", "œufs", "fromage"
# Affichez la liste après chaque ajout

# Votre code ici :
achats = []
achats.append("pain")
print("Après ajout :", achats)

achats.append("lait")
print("Après ajout :", achats)

achats.append("œufs")
print("Après ajout :", achats)

achats.append("fromage")
print("Après ajout :", )




# ==========================================
# EXERCICE 3.12 : Liste de nombres pairs
# ==========================================

# Créez une liste vide "nombres_pairs"
# Utilisez une boucle for avec range() pour ajouter tous les nombres pairs de 0 à 20
# Affichez la liste complète

# Votre code ici :

nombres_pairs = []

for i in range(0, 21, 2): 
    nombres_pairs.append(i)

print("Nombres pairs de 0 à 20 :", nombres_pairs)


# ==========================================
# BONUS : Liste inversée
# ==========================================

# Créez une liste "nombres" contenant [1, 2, 3, 4, 5]
# Créez une nouvelle liste "inverse" qui contient les éléments dans l'ordre inverse
# (Sans utiliser la méthode reverse() ou [::-1])
# Affichez les deux listes

# Votre code ici :
nombres = [1, 2, 3, 4, 5]
inverse = []
for i in range(len(nombres) - 1, -1, -1):
    inverse.append(nombres[i])

print("Liste originale :", nombres)
print("Liste inversée :", inverse)


