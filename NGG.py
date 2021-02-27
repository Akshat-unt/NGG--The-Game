import random
initial_score = 0
while True:
    number = random.randint(0, 9)
    guess = int(input("Guess the number:\n"))
    if number == guess:
        print("You got it!\n")
        score = initial_score+1
        initial_score = score
        print(initial_score)
        if initial_score == 10:
            print("you're all set!")
            print("Your score is: ", initial_score)
        if initial_score == -3:
            print("You need more practice. Better luck next time!")
            print("Your score is: ", initial_score)
            break
    if number != guess:
        print("Incorrect guess")
        score = initial_score-1
        initial_score = score
        print(initial_score)
        if initial_score == -3:
            print("You need more practice. Better luck next time!")
            print("Your score is: ", initial_score)
            break
        if initial_score == 10:
            print("you're all set!")
            print("Your score is: ", initial_score)