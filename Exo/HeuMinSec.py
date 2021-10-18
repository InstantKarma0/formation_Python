# On déclare la Variable heure (int)
heures = 0;
# On déclare la Variable minutes (int)
minutes = 0;
# On déclare la Variable secondes (int)
secondes = 0;

# On affiche le label
print("Entrez les heures");
# On récupère la valeur de la variable heures
heures = int(input());

# On affiche le label
print("Entrez les minutes");
# On récupère la valeur de la variable minutes
minutes = int(input());

# On affiche le label
print("Entrez les secondes");
# On récupère la valeur de la variable secondes
secondes = int(input());

# On incremente les secondes
secondes = secondes + 1;

# Condition si secondes egal a 60
if secondes == 60:
    # On remet secondes a 0
    secondes = 0;
    # On incremente minutes
    minutes = minutes + 1;
    
    # Condition si minutes egal a 60
    if minutes == 60:
        # On remet minutes a 0
        minutes = 0;
        # On incremente heures
        heures = heures + 1;
        
        # Condition si heures egal a 24
        if heures == 24:
            # On remet Heure a 0
            heures = 0;


# On affiche l'heure qu'il sera dans une seconde
print("Dans une seconde il sera: {} heures, {} minutes et {} secondes".format(heures, minutes, secondes));
