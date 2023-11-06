#Arcade Games v2.0
# Version 1.0:
### Added RockPaperScissorsV2 and GuessNumberV1 to the Games list
# Version 2.0:
### Added the os.system('clear') to clear the screen after each game

import sys
import random
from enum import Enum
import os #To use the os.system('clear') command to clear the screen

title=" Arcade Games "
print(title.center(40,"-"))
player=input("\nWhat's you name? ")
welcome_back=False

def arcade():
    playerchoice=0
    global welcome_back
    
    def play():
        print(f"\n1 - Rock, Paper, Scissors\n2 - Guess the Number\n3 - Quit")
        playerchoice=input("")
        playerchoice=int(playerchoice)
        welcome_back=True                
                
        if playerchoice not in range(1,4):
            print(f"\n{player}, please choose of the options...")
            play()
        elif playerchoice==1:
            print("\nStarting Rock, Paper, Scissors...\n\n")
            rps()
        elif playerchoice==2:
            print("\nStarting Guess the Number...\n\n")
            guessnumber()
        elif playerchoice==3:
            print(f"\nThank you for trying Arcade Games, {player}!\nBye!")
            sys.exit()
    
    if welcome_back==True:
        print(f"\nWelcome back, {player}!")
        play()
    else:
        print(f"\nWelcome, {player}!\nPlease, choose one of options:")
        play()


### Rock Paper Scissors ###
def rps():
    global player
    global welcome_back
    
    os.system('clear')
    title=(" Rock, Paper, Scissors Game ")
    print(title.center(40,"-"))
    print(f"\nWelcome, {player}!")
    playerwins=0
    playerloss=0
    compwins=0
    comploss=0
    ties=0
    
    def play():
        # Class RPS = Rock,Paper,Scissors
        class RPS(Enum):
            Rock=1
            Paper=2
            Scissors=3
        
        print()
        playerchoice=input("1 - ROCK\n2 - PAPER\n3 - SCISSORS\nMake your choice: ")
                
        if playerchoice not in ["1","2","3"]:
            print(f"\n{player}, you must enter 1, 2 or 3...")
            play()
            
        compchoice=random.choice("123")
        comp=int(compchoice)
        player1c=int(playerchoice)

        print(f"\n{player} chose {str(RPS(player1c)).replace('RPS.','')}")
        print(f"The computer chose {str(RPS(comp)).replace('RPS.','')}")
        #Use the replace() to remove the class name of the output
        #It's necessary to use the str ocnstructor here, since we're applying it to the enum value
        #and then calling a string method. It's also not being converted before that happens.
        print()

        nonlocal playerwins
        nonlocal playerloss
        nonlocal compwins
        nonlocal comploss
        nonlocal ties

        if player1c==comp:
            print("It's a tie.")
            ties+=1
        elif player1c==1 and comp==2:
            print(f"{player} lost...")
            playerloss+=1
            compwins+=1
        elif player1c==2 and comp==1:
            print("You won!")
            playerwins+=1
            comploss+=1
        elif player1c==1 and comp==3:
            print("You won!")
            playerwins+=1
            comploss+=1
        elif player1c==3 and comp==1:
            print(f"{player} lost...")
            playerloss+=1
            compwins+=1
        elif player1c==2 and comp==3:
            print(f"{player} lost...")
            playerloss+=1
            compwins+=1
        elif player1c==3 and comp==2:
            print("You won!")
            playerwins+=1
            comploss+=1

        again=input("\nPress \"q\" to quit or press enter to try again... ").lower()
        if again in ["quit","q"]:
            print(f"\nFinal Score:\n{player} - Wins:{playerwins} Losses:{playerloss}") 
            print(f"COMPUTER - Wins:{compwins} Losses:{comploss}\nTIES:{ties}")
            #No need to use the str constructor here anymore, since the f-String don't need it
            if (playerwins > compwins):
                print(f"\n{player} wins!")
                print("Congratulations!!!")
            elif (playerwins < compwins):
                print("\nThe Computer won!")
                print(f"Better luck next time {player}...")
            elif (playerwins == compwins):
                print("\nIt's a Tie!")
                print(f"Try harder next time {player}...")
            print("\nGAME OVER")
            welcome_back=True
            cont=input("\n\nPress any key to continue...")
            os.system('clear')
            title=" Arcade Games "
            print(title.center(40,"-"))
            arcade()
        else:
            os.system('clear')
            print("Restarting...")
            play()
    play()

### Guess The Number ###
def guessnumber():
    global player
    global welcome_back
    
    os.system('clear')
    title=" Guess the Number "
    print(title.center(40,"-"))
    print(f"\nGreetings, {player}! Welcome to the Guess the Number challenge, here's how to play:")
    print("*Guess a number between 1 and 10\n*You have only 3 tries!")
        
    def play():
        playerwins=0
        gamecount=0
        tries=0
            
        compchoice=random.randrange(1,10)
        #print(f"COMPCHOICE:{compchoice}")   ###Use for debug only
        #randrange(), specify a range between 1 and 10
        
        gamecount+=1
        
        def playagain():
            nonlocal playerwins
            nonlocal gamecount
            nonlocal tries
            global player
            global welcome_back
            
            if tries<3:
                guess=input("\nGuess the number: ")
                playerguess=int(guess)
                       
                if playerguess not in range(1,10):
                    print(f"\nYou must choose a number between 1 and 10, {player}!")
                    playagain()
                    
                if playerguess==compchoice:
                    print(f"\nCongratulations {player}, you guessed it right!")
                    playerwins+=1
                    again=input(f"\nPlay again, {player}? (Press enter to continue or 'q' to quit) ").lower()
                    if again in ["quit","q"]:
                        winpercent=round(((playerwins/gamecount)*100),2)
                        print(f"Thank you for playing!\n\nFINAL SCORE:\n{player}'s wins: {playerwins}\nGame count: {gamecount}\nYour win percentage: {winpercent}%\n\nGAME OVER")
                        cont=input("\n\nPress any key to continue...")
                        os.system('clear')
                        title=" Arcade Games "
                        print(title.center(40,"-"))
                        welcome_back=True
                        arcade()
                    else:
                        tries=0
                        os.system('clear')
                        play()
                elif playerguess>compchoice:
                    print("Try a little lower...")
                    tries+=1
                    playagain()
                elif playerguess<compchoice:
                    print("Try a little higher...")
                    tries+=1
                    playagain()
            else:
                print(f"\nSorry, you only had 3 tries...\nThe answer was {compchoice}\nBetter luck next time!")
                again=input(f"\nPlay again, {player}? (Press enter to continue or 'q' to quit) ").lower()
                if again in ["quit","q"]:
                    winpercent=round(((playerwins/gamecount)*100),2)
                    print(f"\nThank you for playing!\n\n--- FINAL SCORE ---\n{player}'s wins: {playerwins}\nGame count: {gamecount}\nYour win percentage: {winpercent}%\n\nGAME OVER")
                    cont=input("\n\nPress any key to continue...")
                    os.system('clear')
                    title=" Arcade Games "
                    print(title.center(40,"-"))
                    welcome_back=True
                    arcade()
                else:
                    tries=0
                    play()
                    
        playagain()
    play()
        
arcade()
