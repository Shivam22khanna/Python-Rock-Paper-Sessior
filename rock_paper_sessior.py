loose = ("the computer wins")
win = ("you win")
lives = 5
score = 0
drew = 0
computer_lives = 10
while True:
    print("To begain fill in the below information.")
    username = input("Please enter your ussername  :")
    password = input("please enter your password  :")
    searchfile = open("./account.txt", "r")
    for line in searchfile:
        if username and password in line:
            print("Access Granted")    


            print("********************************************************************")
            print("Live Rules")
            print("you start with",lives,"lives")
            print("if you win you get extra live")
            print("if you loose you loose a live")
            print("if you draw the lives stay the same")
            print("........................................................................")
            print("MAKE SURE YOU DONT USE CAPITALS ...[X]")
            print(".........................................................................")
            print("to see a list of rules type rules")
            print("..........................................................................")
            print("At any point type exit to leave the game")
            print("...........................................................................")
            print("can you beat the computer ??")
            print("Good Luck!!")
            print("****************************************************************************")
            while True:
                rps = input("Rock , Paper , Sessiors???? ")
                import random
                computer = ("rock" , "paper" , "sessiors")
                computer = random.choice(computer)

                # Rock if statements:
                if rps == "rock" and computer == "paper":
                    print("the computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -=1
                if rps == "rock" and computer == "sessiors":
                    print("the compputer choose",computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score +=1

                # Paper if statements:
                if rps == "paper" and computer == "rock":
                    print("the compputer choose",computer)
                    print("")
                    print(win)
                    computer_lives -=1
                    print("")
                    print("")
                    score +=1
                if rps == "paper" and computer == "sessiors":
                    print("the compputer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -=1

                # Sessiors if statements:
                if rps == "sessiors" and computer == "paper":
                    print("the compputer choose",computer)
                    print("")
                    print(win)
                    computer_lives -=1
                    print("")
                    print("")
                    score +=1
                if rps == "sessiors" and computer == "rock":
                    print("the compputer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -=1
                # Duplicates if statements:

                # rock == rock:
                if rps == "rock" and computer == "rock":
                    print("the compputer choose",computer)
                    print("")
                    print("you draw")
                    print("")
                    print("")
                    drew +=1

                # paper == paper:  
                if rps == "paper" and computer == "paper":
                    print("the compputer choose",computer)
                    print("")
                    print("you draw")
                    print("")
                    print("")
                    drew +=1

                # sessiors == sessiors:
                if rps == "sessiors" and computer == "sessiors":
                    print("the compputer choose",computer)
                    print("")
                    print("you draw")
                    print("")
                    print("")
                    drew +=1 

                # System:
                if rps == "rules":
                    print("************************************************************************************")
                    print("Rules")
                    print("************************************************************************************")
                    print("Rocks loses against paper")
                    print("Rock beat sessiors")
                    print("Paper beat rock")
                    print("Paper loses against sessiors")
                    print("Sessiors beat paper")
                    print("Sessiors loses against rock")
                    print("**************************************************************************************")
                # display lives:
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)

                # Lives:
                if lives == 0 or lives == "test":
                    print("thanks for playing.")
                    print("you have run out of lives")
                    print("you got ",score," correct")
                    print("you drew",drew,"times")
                    stop = input("press enter the exit.")
            # use import time for sleep time.
                    import time
                    time.sleep(900)
                if computer_lives == 0:
                    print("thanks for playing.")
                    print("the computer lost it's lives . You Win.")
                    print("you got",score,"correct")
                    print("you drew ",drew,"times")
                    stop = input("Press enter to exit.")
                    import time
                    time.sleep(900)

            # Exit:
                if rps == "exit":
                    break
        else:
            print("your username or password is incorrect.")
            print(".....................................................................................................")




                  



                     
                    
                    



                 
