# Ce Programme permet de renvoyer les initiales à partir d'un nom et d'un prénom

# On demande le nom et on lui ajoute une majuscule au début
prenom = str(input('Entrez le prenom: ')).capitalize();
# On demande le prénom et on lui ajoute une majuscule au début
nom = str(input('Entrez le nom: ')).capitalize(); 

# On affiche le resultat
print("Les initiales de " + prenom + " " + nom + " sont: " + prenom[0] + nom[0])
