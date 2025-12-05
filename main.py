def affiche_grille(grid):
    """take as a parameter a 3X3 matrice, print it in console"""
    nb_to_symbole = [" ", "x", "o"]
    for i in range(3):
        line = " "
        for j in range(3):
            line = line + str(nb_to_symbole[grid[i][j]]) + " "
        print(line)

def full_grid(grid):
    """take as a parameter a 3X3 matrice, return True if full or False if not"""
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
    return True

def end_of_game(grid):
    """take as a parameter a 3X3 matrice, return True if a player have won and False if not"""
    # check for all 3 lines, to see if they are fill with the same symbol
    for i in range(3):  
        won = False
        compare = []    # put 3 value in a list before comparing them
        for j in range(3):
            compare.append(grid[i][j])
        won =  compare[0] == compare[1] == compare[2] != 0
        if won:
            return True
            
    # check for all 3 columns, to see if they are fill with the same symbol
    for i in range(3):
        compare = []
        for j in range(3):
            compare.append(grid[j][i])
        won =  compare[0] == compare[1] == compare[2] != 0
        if won:
            return True
    
    # check the first diagonal, to see if it is are fill with the same symbol
    compare = []
    for i in range (3):
        compare.append(grid[i][i])
    won =  compare[0] == compare[1] == compare[2] != 0
    if won:
        return True
    
    # check the first diagonal, to see if it is are fill with the same symbol
    compare = []
    for i in range(3):
        compare.append(grid[i][2-i])
    won =  compare[0] == compare[1] == compare[2] != 0
    if won:
        return True
    
    # If none of the conditions are fullfill, return False
    return False

def play(grid, current_player):
    """take as a parameter a 3X3 matrice and an integer current_player, make the current player play"""
    assert type(current_player) == int, 'num_joueur doit être un entier'
    condition = True
    while condition:
        y = int(input("Give the index of the line wich you want to play : \n"))
        assert (y==0) or (y==1) or (y==2), "the index must be between 0 and 2"
        x = int(input("Give the index of the column wich you want to play : \n"))
        assert (x==0) or (x==1) or (x==2), "the index must be between 0 and 2"
        if grid[y][x] == 0:
            grid[y][x]= current_player
            condition = False
    affiche_grille(grid)
    


# give the index of the board lines and columns
example_grid = [[0,1,2],
                 [1,0,0],
                 [2,0,0]]
for i in range(3):
        line = " "
        for j in range(3):
            line = line + str(example_grid[i][j]) + " "
        print(line)
print("Player 1 : x\nPlayer 2 : o")


condition = True
current_player = 1
empty_grid = [[0,0,0],
               [0,0,0],
               [0,0,0]]

# main game loop
while condition:
    play(empty_grid, current_player)
    if full_grid(empty_grid):
        print("the grid is full")
        condition = False
    elif end_of_game(empty_grid):
        print("player " + str(current_player) + " won")
        condition = False
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
