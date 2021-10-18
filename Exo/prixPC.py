# On déclare la variable nbCopie (int)
nbCopie = 0;
# On déclare la variable nbCopie (float)
prixTotal = 0.0;

# On affiche le label
print("Inserez le nombre de photocopie");
# On affecte la valeur de nb Copie
nbCopie = int(input());

# Condition si nbcopie plus petit ou égal a 10
if nbCopie <= 10:
    # On affecte la valeur de prixTotal (arrondie au centime pres)
    prixTotal = round(nbCopie * 0.10,3);

# Condition si nbCopie plus petit ou égal a 20
elif nbCopie <= 20:
    # On affecte la valeur de prixTotal (arrondie au centime pres)
    prixTotal =  round(nbCopie * 0.09,3);
    
# Dans le cas ou nbCopie est plus grand que 20
else:
    # On affecte la valeur de prixTotal (arrondie au centime pres)
    prixTotal =  round(nbCopie * 0.08,3);

# On affiche le nombre de photocopies et le montant en euros
print("Le prix pour {} photocopies est de {} euros".format(nbCopie, prixTotal));
