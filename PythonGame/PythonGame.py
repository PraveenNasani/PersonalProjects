print("Hey!! Welocme to my game..\nHere are the steps to play the game\n-->Firstly we have to print the target score\n  .who ever scores target number is the winner.\n-->We have three constraints ROCK,PAPER,SCISSOR\n  .We have to select any one of the three constraints\n  .similarly system will select one constraint")
import random
playername=input("Enter Player Name: ")
targetscore=int(input("Enter Target Score : "))
print("%s Score: 0           Computer Score: 0"%playername)
s=['Rock','Scissor','Paper']
PlayerScore=0
ComputerScore=0
while True:
    x=input("select Rock, Paper or Scissor?: ")
    if x.lower() not in ['rock','paper','scissor']:
        print("You Entered wrongly,Please enter properly")
    else:
        y=random.choice(s)
        if y.lower()==x.lower():
            print("Rock!\nPaper!\nScissor!")
            print("You Selected: %s      ComputerSelected: %s"%(x.capitalize(),y))
            print("Oh!!You both selected %s"%y)
            print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
        else:
            if y.lower()=="rock":
                if x.lower()=="paper":
                    PlayerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Paper      ComputerSelected: %s"%(y))
                    print("You won-->Paper covers Rock")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
                else:
                    ComputerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Scissor      ComputerSelected: %s"%(y))
                    print("You lost-->Rock smashes scissor")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
            elif y.lower()=="paper":
                if x.lower()=="scissor":
                    PlayerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Scissor      ComputerSelected: %s"%(y))
                    print("You won-->Scissor cuts Paper")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
                else:
                    ComputerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Rock      ComputerSelected: %s"%(y))
                    print("You lost-->Paper covers Rock")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
            else:
                if x.lower()=="rock":
                    PlayerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Rock      ComputerSelected: %s"%(y))
                    print("You won-->Rock smashes scissor")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
                else:
                    ComputerScore+=1
                    print("Rock!\nPaper!\nScissor!")
                    print("YouSelected:Paper      ComputerSelected: %s"%(y))
                    print("You lost-->Scissor cuts Paper")
                    print("%s Score: %s    ComputerScore: %s"%(playername,PlayerScore,ComputerScore))
            z=max(PlayerScore,ComputerScore)
            if z==targetscore:
                if z==PlayerScore and z==ComputerScore:
                    print("Both are winners,because its a tie")
                elif z==PlayerScore:
                    print("Yayyy!!You won the game")
                else:
                    print("Oops!!You lost the game..Try Again")
                break
    
