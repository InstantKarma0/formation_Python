# Ce programme permet d'échanger les valeurs de 2 variables sans en déclarer une 3ème.

x = None; #Deviendra Int
y = None; #Deviendra Int

while x is None: #Boucle Vérification du type de x
    input_x = input("Quel est la valeur de x ?");
    
    try:
        x = int(input_x); #On essaie de muter le type de x en INT
        
    except ValueError: #Remonte une erreur si le type n'est pas bon
        print("{input} n'est pas un nombre entier, veuillez entrer un nombre uniquement".format(input=input_x));
#EO While

while y is None: #Boucle Vérification du type de y
    input_y = input("Quel est la valeur de x ?");
    
    try:
        y = int(input_y); #On essaie de muter le type de y en INT
        
    except ValueError: #Remonte une erreur si le type n'est pas bon
        print("{input} n'est pas un nombre entier, veuillez entrer un nombre uniquement".format(input=input_y));
#EO While


print("x est égal à " + str(x) + " et y est égal à " + str(y)); #Affichage des valeurs avant l'algorithme
print("Lancement de l'algorithme");

x = x * y;
y = x / y;
x = x / y;

print("Fin de l'algorithme");
print("x est égal à " + str(x) + " et y est égal à " + str(y)); #Affichage des valeurs après l'algorithme