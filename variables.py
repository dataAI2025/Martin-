########## Exercice: niveau 1

########## Jour 30 Days of Python Programming

##### Déclaration des variables 

First_name = "Martin"
Last_name = "BADJI"
Full_name = " BADJI", " Kpapou", " Martin"
pays =  " TOGO"
City = " Doumasséssé"
est_Married = "Single"
is_true = "No"
IS_light_on = "Yes"

################# Exercices : niveau 2

print(type( First_name), type(Last_name),type(pays), type (City), type ( est_Married),type(is_true),type (IS_light_on))

##### Longueur de mon prénom 
Len_First_name = First_name
print ("Len_First_name :", len (Len_First_name)) 
Len_Last_name = Last_name
print("len_last_name :", len ( Last_name))
########## Vérifions la comparaison des longueur
print ("Len_First_name > Len_Last_name")
num_one = 5 
num_two = 4
Add = num_one + num_two
print ( "L addition donne :", Add ) 
Soustract = num_two - num_one
print( "La soutraction donne :", Soustract)
division = num_one / num_two
print ( " la division donne :", division)
Modul_div = num_two % num_one
print ("La division du module est", Modul_div)
Floor_Division = num_one // num_two 
print ( "Floor_Division est ", Floor_Division)

################# Calculons la zone d'un cercle de rayon 30 mètres 

R = 30 
area_of_circle = 3.14*R** 2
print("La zone du cercle est",area_of_circle,"m^2")

################ Calculons la circonférence de ce cercle

circum_of_circle = 2*R*3.14
print ("La circonférence de cet cercle est ", circum_of_circle , "m")

# Demander à l'utilisateur de saisir le rayon
rayon = float(input("Entrez le rayon du cercle en mètres : "))
surface = 3.14*rayon**2
print (" La valeur du rayon que vous avez entré est", rayon)
print ( "La surface est:", surface, "m^2")

# Collecte des données utilisateur
first_name = input("Entrez votre prénom : ")
last_name = input("Entrez votre nom de famille : ")
country = input("Quel est votre pays ? ")
age = input("Quel âge avez-vous ? ")

# Affichage des données capturées
print("Prénom :", first_name)
print("Nom de famille :", last_name)
print("Pays :", country)
print("Âge :", age)
help ('keywords')