# Ce programme permet d'échanger les valeurs de 2 variables sans en déclarer une 3ème.

x = int(0);
y = int(0);

x = int(input("Quel est la valeur de x ?"));
y = int(input("Quel est la valeur de y ?"));
    
print("x est égal à " + str(x) + " et y est égal à " + str(y)); #Affichage des valeurs avant l'algorithme
print("Lancement de l'algorithme");

x = x * y;
y = x / y;
x = x / y;

print("Fin de l'algorithme");
print("x est égal à " + str(x) + " et y est égal à " + str(y)); #Affichage des valeurs après l'algorithme