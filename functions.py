def input_test():
    while 0 == 0:
        try:
            num = input("numéro de la case ?\n")
            int(num)
            break
        except ValueError:
            print("il faut mettre un chiffre !")
    return num


def affichage_ligne(case1, case2, case3):
    if case1 == "cross" and case2 == "cross" and case3 == "cross":
        print("x    x|x    x|x    x\n"
              "  xx  |  xx  |  xx  \n"
              "x____x|x____x|x____x\n")

    elif case1 == "round" and case2 == "round" and case3 == "round":
        print("  00  |  00  |  00  \n"
              "00  00|00  00|00  00\n"
              "__00__|__00__|__00__\n")

    elif case1 == "r" and case2 == "r" and case3 == "r":
        print("      |      |      \n"
              "      |      |      \n"
              "______|______|______\n")

    elif case1 == "cross" and case2 == "cross" and case3 == "round":
        print("x    x|x    x|  00  \n"
              "  xx  |  xx  |00  00\n"
              "x____x|x____x|__00__\n")

    elif case1 == "cross" and case2 == "round" and case3 == "round":
        print("x    x|  00  |  00  \n"
              "  xx  |00  00|00  00\n"
              "x____x|__00__|__00__\n")

    elif case1 == "round" and case2 == "round" and case3 == "cross":
        print("  00  |  00  |x    x\n"
              "00  00|00  00|  xx  \n"
              "__00__|__00__|x____x\n")

    elif case1 == "round" and case2 == "cross" and case3 == "cross":
        print("  00  |x    x|x    x\n"
              "00  00|  xx  |  xx  \n"
              "__00__|x____x|x____x\n")

    elif case1 == "round" and case2 == "cross" and case3 == "round":
        print("  00  |x    x|  00  \n"
              "00  00|  xx  |00  00\n"
              "__00__|x____x|__00__\n")

    elif case1 == "cross" and case2 == "round" and case3 == "cross":
        "x    x|  00  |x    x\n"
        "  xx  |00  00|  xx  \n"
        "x____x|__00__|x____x\n"

    elif case1 == "cross" and case2 == "cross" and case3 == "r":
        print("x    x|x    x|      \n"
              "  xx  |  xx  |      \n"
              "x____x|x____x|______\n")

    elif case1 == "cross" and case2 == "r" and case3 == "r":
        print("x    x|      |      \n"
              "  xx  |      |      \n"
              "x____x|______|______\n")

    elif case1 == "r" and case2 == "r" and case3 == "cross":
        print("      |      |x    x\n"
              "      |      |  xx  \n"
              "______|______|x____x\n")

    elif case1 == "r" and case2 == "cross" and case3 == "cross":
        print("      |x    x|x    x\n"
              "      |  xx  |  xx  \n"
              "______|x____x|x____x\n")

    elif case1 == "r" and case2 == "cross" and case3 == "r":
        print("      |x    x|      \n"
              "      |  xx  |      \n"
              "______|x____x|______\n")

    elif case1 == "cross" and case2 == "r" and case3 == "cross":
        print("x    x|      |x    x\n"
              "  xx  |      |  xx  \n"
              "x____x|______|x____x\n")

    elif case1 == "round" and case2 == "round" and case3 == "r":
        print("  00  |  00  |      \n"
              "00  00|00  00|      \n"
              "__00__|__00__|______\n")

    elif case1 == "round" and case2 == "r" and case3 == "r":
        print("  00  |      |      \n"
              "00  00|      |      \n"
              "__00__|______|______\n")

    elif case1 == "r" and case2 == "r" and case3 == "round":
        print("      |      |  00  \n"
              "      |      |00  00\n"
              "______|______|__00__\n")

    elif case1 == "r" and case2 == "round" and case3 == "round":
        print("      |  00  |  00  \n"
              "      |00  00|00  00\n"
              "______|__00__|__00__\n")

    elif case1 == "r" and case2 == "round" and case3 == "r":
        print("      |  00  |      \n"
              "      |00  00|      \n"
              "______|__00__|______\n")

    elif case1 == "round" and case2 == "r" and case3 == "round":
        print("  00  |      |  00  \n"
              "00  00|      |00  00\n"
              "__00__|______|__00__\n")

    elif case1 == "cross" and case2 == "round" and case3 == "r":
        print("x    x|  00  |      \n"
              "  xx  |00  00|      \n"
              "x____x|__00__|______\n")

    elif case1 == "round" and case2 == "r" and case3 == "cross":
        print("  00  |      |x    x\n"
              "00  00|      |  xx  \n"
              "__00__|______|x____x\n")

    elif case1 == "r" and case2 == "cross" and case3 == "round":
        print("      |x    x|  00  \n"
              "      |  xx  |00  00\n"
              "______|x____x|__00__\n")

    elif case1 == "r" and case2 == "round" and case3 == "cross":
        print("      |  00  |x    x\n"
              "      |00  00|  xx  \n"
              "______|__00__|x____x\n")

    elif case1 == "cross" and case2 == "r" and case3 == "round":
        print("x    x|      |  00  \n"
              "  xx  |      |00  00\n"
              "x____x|______|__00__\n")

    elif case1 == "round" and case2 == "cross" and case3 == "r":
        print("  00  |x    x|      \n"
              "00  00|  xx  |      \n"
              "__00__|x____x|______\n")


def affichage_tableau(case1, case2, case3, case4, case5, case6, case7, case8, case9):
    affichage_ligne(case1, case2, case3) #affiche une première ligne
    affichage_ligne(case4, case5, case6)
    affichage_ligne(case7, case8, case9)

def player_change(current_player):
    if current_player == "cross":
        return "round"
    if current_player == "round":
        return "cross"
    else :
        return "r"

def is_winning(case1, case2, case3, case4, case5, case6, case7, case8, case9):
    if case1 == case2 == case3 != "r" or case4 ==case5 == case6 != "r" or case7 == case8 == case9 !="r" or case1 == case4 == case7 !="r" or case2 == case5 ==case8 !="r" or case3 == case6 == case9 !="r": #si une ligne droite est formé
        return True
    elif case1 == case5 == case9 !="r" or case7 == case5 == case3 !="r":
        return True
    else:
        return False
