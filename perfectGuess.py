from random import randint 
n=randint(1,100)
guesses=0
a=-1
while(a!=n):
    guesses+=1
    a=int(input("Enter Guess Number "))
    if(a<n):
        print("Greater Number Please \n")
    else:
        print("Lower NUmber PLease! \n")
    
print(f"You have successfully guess the number {n} in the {guesses} attempt")