import random
randnumber = random.randint(1,100)
userGuess = None
guesses = 0
#print(randnumber)

while(userGuess != randnumber):
    userGuess = int(input("Enter any number: "))
    guesses+= 1
    if (userGuess==randnumber):
        print("You Guess it Right!")
    else:
        if (userGuess>randnumber):
            print("You guess it wrong! please enter smaller number.")
        else:
            print("You guess it Wrong! please enter larger number.")

print(f"You guessed the number {guesses} guesses.")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You Have Just Broken The High Score.")
    with open("hiscore.txt","w") as f:
         f.write(str(guesses))