#Programme permettant de transformer une ficher de base 2 en base 10

i = int(0);
nbBinaire = str(0);
nbDecimal = int(0);
resultat = int(0);

print("Entrez le Nombre Binaire");
nbBinaire = input();
nbBinaire = nbBinaire[::-1];



for i in range(len(nbBinaire)):
    resultat = resultat + int(nbBinaire[i])*(2**(i));
    

print(resultat);
