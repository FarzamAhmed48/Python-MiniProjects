import random
'''
1 For Snake
-1 For Water
0 For Gun
'''
computer =random.choice([1,0,-1])
userInput= input("Enter 1 for Snake, 0 for Gun, -1 for Water: ")
dict={"s":1,"w":-1,"g":0}

comRes={1:"Snake",0:"Gun",-1:"Water"}
inpConv= dict[userInput]
comConv=comRes[computer]

print(f"You choose: {comRes[inpConv]}\nComputer Chose: {comConv}")
if(computer==inpConv):
    print("Match Draw")
else:
    if(computer==-1 and inpConv==1):
        print("You Win")
    elif(computer==-1 and inpConv==0):
        print("You Loose")

    elif(computer==1 and inpConv==-1):
        print("You Loose!")

    elif(computer==1 and inpConv==0):
        print("You Win!")


    elif(computer==0 and inpConv==1):
        print("You Loose!")

    elif(computer==0 and inpConv==-1):
        print("You Win!")

    else:
        print("Something went wrong")