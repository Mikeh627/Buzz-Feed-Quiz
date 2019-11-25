print("Welcome! To the Spongebob Squarepants quiz!"), '\n'
print("Here you will be asked a series of questions regarding food, activities"
      ", etc. to see who you resemble most from Spongebob!"), '\n'


def invalid_input():
    print("Invalid input, please make sure there are no grammatical errors or "
          "incorrect capitals. :)")         # this is a function to no accept an invalid input


quiz_end = False    # this sets the quiz up to run until the end where we will make this a true statement and print who you got

questions = 1       # creating this variable with a int() will allow us to make the questions continue once the user inputs a str()

patrick = 0
sandy = 0
mrkrabs = 0         # these variables allow the program to know throughout the quiz which person has the hightest number which you get +1 for answering specific way throughout the quiz
plankton = 0
spongebob = 0

while not quiz_end:
    if questions == 1:          #this is the start of our while loop, the questions will be in this until satisfactory amount of questions are prompted to the user
        print()
        print("Which of these foods would you choose?"),
        print(input("Money, Chum, Ice Cream, or Krabby Patties?")),

        if input == "Money" or "money":
            mrkrabs + int(1)

        elif input == "Chum" or "chum":
            plankton + int(1)                               #these input score the user into different variables as mentioned earlier

        elif input == "Ice Cream" or "ice cream" or "Ice Cream":
            patrick + int(1)

        elif input == "Krabby patties" or "Krabby Patties":
            spongebob + int(1)
            sandy + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 1

    questions += 1          # this little guy allows us to go up after every question is answered

    if questions == 2:
        print()
        print("Which of the following is your favorite pass time?"),
        print(input("Money, cooking, science, Jellyfishing, or sleeping?"))

        if input == "Money" or input == "money":
            mrkrabs + int(1)

        elif input == "science" or input == "Science":
            plankton + int(1)
            sandy + int(1)

        elif input == "Sleeping" or input == "sleeping":
            patrick + int(1)

        elif input == "Cooking" or input == "cooking":
            spongebob + int(1)

        elif input == "Jelly Fishing" or input == "jellyfishing":
            spongebob + int(1)
            patrick + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 2

    questions += 1

    if questions == 3:
        print()
        print("Which of the following is your favorite color?"),
        print(input("Green, yellow, pink or blue?"))

        if input == "Green " or input == "green":
            mrkrabs + int(1)

        elif input == "Yellow" or input == "yellow":
            spongebob + int(1)
            sandy + int(1)

        elif input == "pink" or input == "Pink":
            patrick + int(1)

        elif input == "blue" or input == "Blue":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 3

    questions += 1

    if questions == 4:
        print()
        print("How would your friends describe you?"),
        print(input("Stupid, Funny, Stingy, Smart, or Creative?"))

        if input == "Stingy" or input == "stingy":
            mrkrabs + int(1)
            plankton + int(1)

        elif input == "Smart" or input == "Smart":
            plankton + int(1)
            sandy + int(1)

        elif input == "Stupid" or input == "stupid":
            patrick + int(1)
            spongebob + int(1)

        elif input == "Funny" or input == "Funny":
            patrick + int(1)

        elif input == "creative" or input == "Creative":
            sandy + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 4

    questions += 1

    if questions == 5:
        print()
        print("What is your favorite holiday"),
        print(input(" Annoy Squidward Day, The purge, Christmas, or Money "
                    "Day"))

        if input == "Money Day" or input == "money day":
            mrkrabs + int(1)

        elif input == "Christmas" or input == "christmas":
            sandy + int(1)

        elif input == "Annoy Squidward Day" or input == "annoy squidward day":
            patrick + int(1)
            spongebob + int(1)
            squidward - int(1)

        elif input == "the purge" or input == "The Purge":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 5

    questions += 1

    if questions == 6:
        print()
        print("Pick a word."),
        print(input("Money, Cheerful, Imagination, Science, Music"))

        if input == "Money" or input == "money":
            mrkrabs + int(1)

        elif input == "Cheerful" or input == "cheerful":
            spongebob + int(1)

        elif input == "Imagination" or input == "imagination":
            patrick + int(1)
            spongebob + int(1)

        elif input == "Science" or input == "science":
            sandy + int(1)

        elif input == "Music" or input == "music":
            squidward + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 6

    if questions == 7:
        print()
        print("Pick an instrument."),
        print(input("Violin, Mayonnaise, Guitar, Clarinet, or Drums"))

        if input == "Violin" or input == "violin":
            mrkrabs + int(1)

        elif input == "Guitar" or input == "guitar":
            spongebob + int(1)

        elif input == "Mayonnaise" or input == "mayonnaise":
            patrick + int(1)

        elif input == "Drums" or input == "drums":
            sandy + int(1)

        elif input == "Clarinet" or input == "clarinet":
            squidward + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 7

    if questions == 8:
        print()
        print("Are you ready????"),
        print(input("I'm ready, ready?, oh no, Ready to count me money, "
                    "ready for the secret formula!"))

        if input == "Ready to count me money" or input == "ready to count me" \
                                                          " money":
            mrkrabs + int(1)

        elif input == "I'm ready" or input == "I'm Ready":
            spongebob + int(1)

        elif input == "ready?" or input == "Ready?":
            patrick + int(1)

        elif input == "ready for the secret formula!":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 8

    if spongebob > 4:
        print("You resemble Spongebob Squarepants! [' o '] ")

    elif patrick > 4:
        print("You resemble Patrick Star! :O ")

    elif sandy > 4:
        print("you resemble Sandy Cheeks! >.< ")

    elif mrkrabs > 4:
        print("You resemble Mr. Krabs! $$$$ ")

    elif plankton > 4:
        print("Yoy resemble Plankton! >:) ")

    quiz_end = True

print("Thank you for playing! I hope you enjoyed! :D")

