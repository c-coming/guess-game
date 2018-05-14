from random import randint
num = randint(1,10)
print num
ddef main():
    print "Welcome to the number guessing game!"
    i = 0
    while True:
        i += 1
        if i <= 5:
            print "Time:",i
            try:
                guess = raw_input("Please guess a number between 1 to 10: ")
                if int(guess) == num:
                    print "This is right!"
                    break
                else:
                    print "I'm sorry, you're wrong."
            except:
                print "I'm sorry,Guess again!"
        else:
            print "Game Over!"
            break
if __name__ == "__main__":
main()
