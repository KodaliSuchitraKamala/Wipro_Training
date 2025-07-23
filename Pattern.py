for i in range(7):
    for j in range(7):
        if abs(i - j) == 3 or i + j == 3 or i + j == 9 or i == 6 or j == 6 or i == 0 or j == 0 or j == 5 and i != 3 and  j != 3 :
            print("*", end =' ')
        elif i == 1 and i != 3 and  j != 3:
            print("*", end =' ')
        elif  j == 1 and i != 3 and  j != 3 :
            print("*", end =' ')
        else:
            print(" ", end = ' ')
    print()