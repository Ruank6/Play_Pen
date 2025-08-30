import random

# Generate a random number between 1 and 100
randnum = random.randint(1, 101)

#Function to allow the computer to guess a number
def computer_guess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        #If the guess is in the middle, it is found
        if guess == randnum:
            count += 1
            return count
        #if guess is greater than the random number, search in the lower half
        elif guess > randnum:
            count += 1
            return computer_guess(lowval, guess - 1, randnum, count)
        #if guess is less than the random number, search in the upper half
        else:
            count += 1
            return computer_guess(guess + 1, highval, randnum, count)
    else:
        #number not found
        return -1
#End of computer_guess function    


#Loop for manually guessing a number
def manual_guess():



count = 0
guess = -99

while guess != randnum:
    count += 1
    print(f"Attempt #{count}")
    print("Guess the number between 1 and 100.")
    print("You have 10 attempts to guess the number.")
    
    if count >= 10:
        print("Sorry, you've used all your attempts. Better luck next time!")
        break
    else:   
    #Get the user's guess
        guess = int(input("Enter a number between 1 and 100: "))
        # Function to check the user's guess
        if guess < randnum:
            print("Your guess is too low.")
        elif guess > randnum:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the number correctly.")
# End of Loop for manuall guessiung

print("You took " + str(count) + " attempts to guess the random number " + str(randnum))
print("Computer took " + str(computer_guess(1, 100, randnum)) + " attempts to guess the number."    )
# End of GuessingGame.py