import random 
num = random.randint(0,15)
chance = 0
while chance < 5:
    guess = int(input("Enter your guess: "))
    if(guess == num):
        print("Congratulations!")
        break
    elif(guess<num):
        print("Your guess is lower than the number.")
    else:
        print("Your guess is higher than the number.")
    chance = chance+1
if(chance >= 5):
    print("Game over.")