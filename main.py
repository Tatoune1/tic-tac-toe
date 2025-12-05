def affiche_grille(grid):
    """take as a parameter a 3X3 matrice and print it in console"""
    nb_to_symbole = [" ", "x", "o"]
    for i in range(3):
        line = " "
        for j in range(3):
            line = ligne + str(nb_to_symbole[grid[i][j]]) + " "
        print(line)

def grille_pleine(grid):
    """take as a parameter a 3X3 matrice and return True if full or False if not"""
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
    return True

def fin_de_jeu(grille):
    """prend en paramètre une matrice 3×3  grille et qui renvoie True si un joueur a gagné et False sinon"""
    #vérifie pour les 3 lignes si elles sont remplis par le même symbole
    for i in range(3):  
        gagne = False
        compare = []    #stocke 3 valeur dans une liste avant de les comparer
        for j in range(3):
            compare.append(grille[i][j])
        gagne =  compare[0] == compare[1] == compare[2] != 0
        if gagne:
            return True
            
    #vérifie pour les 3 colonnes si elles sont remplis par le même symbole
    for i in range(3):
        compare = []
        for j in range(3):
            compare.append(grille[j][i])
        gagne =  compare[0] == compare[1] == compare[2] != 0
        if gagne:
            return True
    
    #vérifie pour la première diagonale si elles est remplis par le même symbole
    compare = []
    for i in range (3):
        compare.append(grille[i][i])
    gagne =  compare[0] == compare[1] == compare[2] != 0
    if gagne:
        return True
    
    #vérifie pour la première diagonale si elles est remplis par le même symbole
    compare = []
    for i in range(3):
        compare.append(grille[i][2-i])
    gagne =  compare[0] == compare[1] == compare[2] != 0
    if gagne:
        return True
    
    #Si aucune condition n'est remplie, renvoie False
    return False

def coup_joueur(grille, num_joueur):
    """prend en paramètre une matrice 3×3  grille et un entier num_joueur qui fait joueur le joueur num_joueur"""
    assert type(num_joueur) == int, 'num_joueur doit être un entier'
    condition = True
    while condition:
        y = int(input("Donnez la ligne dans laquelle vous voulez jouer : \n"))
        assert (y==0) or (y==1) or (y==2)
        x = int(input("Donnez la colonne dans laquelle vous voulez jouer : \n"))
        assert (x==0) or (x==1) or (x==2), "Le chiffre doit être compris entre 1 et 3"
        if grille[y][x] == 0:
            grille[y][x]= num_joueur
            condition = False
    affiche_grille(grille)
    



grille_vide = [[0,0,0],
               [0,0,0],
               [0,0,0]]

#tutoriel pour utiliser la bonne notation
grille_remplie = [[0,1,2],
                 [1,0,0],
                 [2,0,0]]
for i in range(3):
        ligne = " "
        for j in range(3):
            ligne = ligne + str(grille_remplie[i][j]) + " "
        print(ligne)
print("Joueur 1 : x\nJoueur 2 : o")

condition = True
num_joueur = 1
while condition:
    coup_joueur(grille_vide, num_joueur)
    if grille_pleine(grille_vide):
        print("La grille est pleine")
        condition = False
    elif fin_de_jeu(grille_vide):
        print("joueur " + str(num_joueur) + " a gagné")
        condition = False
    if num_joueur == 1:
        num_joueur = 2
    else:
        num_joueur = 1
