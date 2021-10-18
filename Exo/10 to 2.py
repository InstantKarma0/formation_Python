# Programme permettant de transformer un chiffre base 10 en base 2

reste = int(0);
resultat = int(0);
x = int(0);
nbBinaire = str("");
i = int(0);

while i == 0:

    print("Entrez le nombre Décimal");
    x = input();
    resultat = int(x);

    while resultat // 2 > 0:
        reste = resultat % 2;
        resultat = resultat // 2;
        nbBinaire = str(reste) + nbBinaire;
    
    nbBinaire = str(resultat) + nbBinaire;

    print (str(x) + " correspond à " + nbBinaire + " en binaire");
    print ("Voulez vous continuer? 0 = Oui, 1 = non.");
    i = int(input());
