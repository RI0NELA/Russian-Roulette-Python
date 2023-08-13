import random

print("Welcome to the Russian Roulette!")

print("---------------------------------")

play_yes_or_no = input("Do you want to play? (Yes x No) : ")

if play_yes_or_no == "Yes":
    print("Lets Play!")
else:
    print("Bye!")
    quit()

answers = (1,2,3,4,5,6)

answers1 = random.choice(answers)

randomize = random.choice(answers)

print("Possible answers are " + str(answers))

answer_question = input("Type your answer here! : ")

if answer_question == randomize:
    print("You Survived!")
else:
    print("You Lost!")
    while answer_question < str(random):
        try_again = input("Try again? (Yes x No) : ")
        if try_again == "Yes":
            print("Welcome to the Russian Roulette!")

            print("---------------------------------")

            play_yes_or_no = input("Do you want to play? (Yes x No) : ")

            if play_yes_or_no == "Yes":
                print("Lets Play!")
            else:
                print("Bye!")
                quit()
            
            print("Possible answers are " + str(answers))

            answer_question = input("Type your answer here! : ")

            if answer_question == randomize:
                print("You Survived!")
            else:
                print("You Lost!")
                
        else:
            print("Bye!")
            quit()