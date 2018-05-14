from random import randint
num = randint(1,10)
print num
def main():
    print "Welcome to the number guessing game!"
    while True:
        guess = raw_input("Please guess a number between 1 to 10: ")
        if int(guess) == num:
            print "This is right!"
            break
        else:
            print "I'm sorry,Guess again!"
if __name__ == "__main__":
    main()
