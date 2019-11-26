# Michael Householder
# Github @Mikeh627
# Naruto quiz

def welcome_message():
    print("Welcome to the Naruto Character Quiz! Here we will determine the "
          "character you resemble most!")


def do_quiz():
    good_answer = False

    kakashi = 0
    naruto = 0
    sasuke = 0
    sakura = 0
    shikamaru = 0

    while not good_answer:
        print()
        print("Question #1) Which of these is describes you?")
        answer = input("Edgy, Chill, Obnoxious, Smart, or Cool?")

        if answer.lower() == "edgy":
            sasuke += 1
            good_answer = True

        elif answer.lower() == "chill":
            kakashi += 1
            good_answer = True

        elif answer.lower() == "obnoxious":
            naruto += 1
            good_answer = True

        elif answer.lower() == "smart":
            shikamaru += 1
            good_answer = True

        elif answer.lower() == "cool":
            kakashi += 1
            shikamaru += 1
            good_answer = True

        else:
            print("Invalid input, please make sure spelling is correct and "
                  "that you choose a valid input :)")
            good_answer = False
    good_answer = False

    while not good_answer:
        print()
        print("Question #2) What energy would you choose?")
        answer = input("Lightning, Wind, Shadow, or Healing?")

        if answer.lower() == "lightning":
            sasuke += 1
            kakashi += 1
            good_answer = True

        elif answer.lower() == "wind":
            naruto += 1
            good_answer = True

        elif answer.lower() == "shadow":
            shikamaru += 1
            good_answer = True

        elif answer.lower() == "healing":
            sakura += 1
            good_answer =True

        else:
            print("Invalid input, please make sure spelling is correct and "
                  "that you choose a valid input :)")
            good_answer = False
    good_answer = False

    while not good_answer:
        print()
        print("Question #3) Which element do you favor?")
        answer = input("Air, Water, Fire, or Earth?")

        if answer.lower() == "air":
            naruto += 1
            good_answer = True

        elif answer.lower() == "water":
            sakura += 1
            good_answer = True

        elif answer.lower() == "fire":
            kakashi += 1
            sasuke += 1
            good_answer = True

        elif answer.lower() == "earth":
            shikamaru += 1
            good_answer = True

        else:
            print("Invalid input, please make sure spelling is correct and "
                  "that you choose a valid input :)")
            good_answer = False
    good_answer = False

    while not good_answer:
        print()
        print("Question #4) What is your fighting style?")
        answer = input("Bold, Calm, Powerful, Tactful or Runaway?")

        if answer.lower() == "bold":
            naruto += 1
            good_answer = True

        elif answer.lower() == "calm":
            shikamaru += 1
            good_answer = True

        elif answer.lower() == "powerful":
            sasuke += 1
            good_answer = True

        elif answer.lower() == "tactful":
            kakashi += 1
            good_answer = True

        elif answer.lower() == "runaway":
            sakura += 1
            good_answer = True

        else:
            print("Invalid input, please make sure spelling is correct and "
                  "that you choose a valid input :)")
            good_answer = False
    good_answer = False

    while not good_answer:
        print()
        print("Question #5) What is most important to you?")
        answer = input("Friends, Power, Intelligence, Strategy or "
                       "Uselessness?")

        if answer.lower() == "friends":
            naruto += 1
            good_answer = True

        elif answer.lower() == "power":
            sasuke += 1
            good_answer = True

        elif answer.lower() == "intelligence":
            kakashi += 1
            good_answer = True

        elif answer.lower() == "strategy":
            shikamaru += 1
            good_answer = True

        elif answer.lower() == "uselessness":
            sakura += 1
            good_answer = True

        else:
            print("Invalid input, please make sure spelling is correct and "
                  "that you choose a valid input :)")
            good_answer = False
    good_answer = False

    while not good_answer:
        print()
        print("Question #6) What pass-time do you enjoy the most?")
        answer = input("Exercising, Reading, Nothing, Training, Sleeping?")

        if answer.lower() ==  "exercising":
            naruto += 1
            good_answer = True

        elif answer.lower() == "reading":
            kakashi += 1
            good_answer = True

        elif answer.lower() == "nothing":
            sakura += 1
            good_answer = True

        elif answer.lower() == "training":
            sasuke += 1
            good_answer = True

        elif answer.lower() == "sleeping":
            shikamaru += 1
            good_answer = True

        else:
            print("Invalid input, please make sure spelling is correct and "
                      "that you choose a valid input :)")
            good_answer = False
    good_answer = False


welcome_message()

do_quiz()


