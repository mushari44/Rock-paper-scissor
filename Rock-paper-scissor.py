import time

while True:
    import random
    print('\n1- Rock ')
    time.sleep(0.5)
    print('2- Paper')
    time.sleep(0.5)
    print('3- Scissors')
    time.sleep(0.5)
    random=random.randint(1,3)
    player=int(input('choose rock(1),paper(2),scissors(3) :'))
    Computer=(random)

    while player!=1and player!=2and player!=3 :
        player=int(input("chose between 1-3 : "))
    if player==1 and Computer==1:
        player='Rock'
        Computer='Rock'
        print("player choose",player,"\nComputer choose", Computer,"\nIt's tie")
    elif player==2 and Computer==2:
        player='Paper'
        Computer='paper'
        print("player choose", player, "\n Computer choose",     Computer, "\nIt's a tie")

    elif player==3 and Computer==3:
        player='scissors'
        Computer='scissors'
        print("player choose", player, "\nComputer choose",     Computer, "\nIt's a tie")

    elif player==1 and Computer==3:
        player='Rock'
        Computer='Scissors'
        print("player choose", player, "\nComputer choose",     Computer,"\n","player","wins")

    elif player==2 and Computer==1:
        player='Paper'
        Computer='Rock'
        print("player choose", player, "\nComputer choose",    Computer,"\n" ,"player wins")
    elif player==3 and Computer==2:
        player='Scissors'
        Computer='Paper'
        print("player choose", player, "\nComputer choose",     Computer, "\n","player wins")
    elif player==3 and Computer==1:
        player='Scissors'
        Computer='Rock'
        print("player choose", player, "\nComputer choose",     Computer, "\n", "Computer wins")
    elif player==1 and Computer==2:
        player='Rock'
        Computer='Paper'
        print("player choose", player, "\nComputer choose",     Computer, "\n","Computer  wins")
    elif player==2 and Computer==3:
        player='Paper'
        Computer='Scissors'
        print("player choose", player, "\n Computer choose",    Computer, "\n", "Computer wins")





    while True:
        Q=input("would you like to play again ? (y/n) ")
        if Q.lower()=="y":
            break
        elif Q.lower()=="n":
            exit()


