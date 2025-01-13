from fonctions import  *

case = ["r", "r", "r", "r", "r", "r", "r", "r", "r"]

current_player = "cross"

end = False


#code :

while end == False :
    while 1 == 1:
        num_test = int(input_test())
        if case[num_test-1] != "r":
            print("case déja occupé")
        else:
            num = num_test
            num_test = "r"
            break #vérifie que la case n'est pas déja ocupée


    case[num-1] = current_player
    affichage_tableau(case[0], case[1], case[2], case[3], case[4], case[5], case[6], case[7], case[8])
    if is_winning(case[0], case[1], case[2], case[3], case[4], case[5], case[6], case[7], case[8]):
        print(current_player, " is the winner")
        break
    current_player = player_change(current_player)

input("tapez entrée pour sortir")
