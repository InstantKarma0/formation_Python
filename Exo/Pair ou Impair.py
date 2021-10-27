# Ce programme permet de savoir si un nombre est Pair ou Impair

#On demande a l'utilisateur d'entrer un nombre
x = int(input("Entrez un nombre: "));

print("le nombre est pair") if x % 2 == 0 else print("le nombre est impair");

#            Structure If Ternaire en Python
# (Action si True) if (Condition) else (Action si False)