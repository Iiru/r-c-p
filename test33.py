import random

play = True
while play :

    #player_choice
    #scan player's choice

    player = input("Enter your choice (rock(r)/paper(p)/scissors(s)): ")
    player = player.lower()
    while (player != "r" and player != "p" and player != "s"):
        player = input("Enter your choice (rock(r)/paper(p)/scissors(s)): ")
        player = player.lower()





    #computer_random
    #decide computer's choice with random
    computer = random.randint(1,3)
    if (computer == 1):
        computer = "rock"
    elif (computer == 2):
        computer = "paper"
    elif (computer == 3):
        computer = "scissors"
    else:
        print ("Error. Enter your choice from rock, paper, scissors.")

    #result
    #show result
    if (player == computer):
        print ("\tDraw!")
    elif (player == "r"):
        if (computer == "paper"):
            print ("\tComputer choose paper. You won.");
        if (computer == "scissors"):
            print ("\tComputer choose scissors. You lost.");
    elif (player == "p"):
        if (computer == "rock"):
            print ("\tComputer choose rock. You won.");
        if (computer == "scissors"):
            print ("\tComputer choose scissors. You lost.");
    elif (player == "s"):
        if (computer == "rock"):
            print ("\tComputer choose rock. You lost.");
        if (computer == "paper"):
            print ("\tComputer choose paper. You won.");

    #restart
    #if want, can restart program
    userInput = input("Finish? Yes or No: ")
    userInput = userInput.lower()
    if (userInput == "yes"):
        play = False
        print ("See you again.")
    if (userInput == "no"):
        play = True



    #end
