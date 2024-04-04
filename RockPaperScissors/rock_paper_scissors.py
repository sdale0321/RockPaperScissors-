import random 

user_wins = 0 #rock, paper, scissors is a 2 player game
computer_wins= 0 #creating 2 variables to account for each score 

options = ["rock", "paper", "scissors"]#variable to account for all options in the game 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() #making things case insesitive 
    if user_input == "q":
        break #enables user to stop progam whenever they choose 

    if user_input not in ["rock", "paper", "scissors"]:
        continue #recursive, starts the loop over asking them to type again 

    random_number = random.randint(0,2) #generating random number b/w 0 and 2 
    #rock is 0, paper is 1, and scissors is 2 
    computer_pick = options[random_number] #
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors": #checking if user won based on computer pick 
        print("You won!")
        user_wins += 1 
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1 #the reason we use elif statements here is because using else statements would
                        #require that we include another "continue" statement with each.
                        #eliminating that reduces code volume 

    else: 
        print("You lost!")
        computer_wins += 1 #^since the above code accounts for all the cases our user can win
                            #there is no need to account for all the loss cases, instead you can just increment computer_wins 
                            #by one since these are the only parameters of the game 

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times") #this info is printed upon quitting the game 
print("goodbye")

