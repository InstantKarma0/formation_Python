#Programme permettant de transformer une ficher de base 2 en base 10

#On initialise des variables
i = int(0);
nbBinaire = str(0);
nbDecimal = int(0);
resultat = int(0);

#On demande a l'utilisateur d'entrer un nombre binaire
print("Entrez le Nombre Binaire");
nbBinaire = input();
nbBinaire = nbBinaire[::-1];



for i in range(len(nbBinaire)):
    resultat = resultat + int(nbBinaire[i])*(2**(i));
    

print(resultat);
