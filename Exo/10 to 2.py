# Programme permettant de transformer un chiffre base 10 en base 2

#On initialise des variables
reste = int(0);
resultat = int(0);
x = int(0);
nbBinaire = str("");
i = int(0);

# Boucle Tant que i est égal a 0
while i == 0:

    # On demande a l'utilisateur d'entrer un nombre deciaml
    print("Entrez le nombre Décimal");
    x = input();
    # Cast the str to int
    resultat = int(x);

    # Tant que la division de resultat par 2 est possible
    while resultat // 2 > 0:
        #Le reste correspond au modulo de resultat par 2
        reste = resultat % 2;
        #Resultat correspon a la division de resultat par 2 sans reste
        resultat = resultat // 2;
        
        #On ajoute le cast de reste en str devant le string nbBinaire
        nbBinaire = str(reste) + nbBinaire;
    
    #A la fin on ajoute le 
    nbBinaire = str(resultat) + nbBinaire;

    #On affiche le resultat du programme
    print (str(x) + " correspond à " + nbBinaire + " en binaire");
    
    #On demande a l'utilisateur si il veut convertir un autre nombre decimal en nombre binaire
    print ("Voulez vous continuer? 0 = Oui, 1 = non.");
    i = int(input());