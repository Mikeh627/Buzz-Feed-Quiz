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

        if input == "Money" or "money":
            mrkrabs + int(1)

        elif input == "science" or "Science":
            plankton + int(1)
            sandy + int(1)

        elif input == "Sleeping" or "sleeping":
            patrick + int(1)

        elif input == "Cooking" or "cooking":
            spongebob + int(1)

        elif input == "Jelly Fishing" or "jellyfishing":
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

        if input == "Green " or "green":
            mrkrabs + int(1)

        elif input == "Yellow" or "yellow":
            spongebob + int(1)
            sandy + int(1)

        elif input == "pink" or "Pink":
            patrick + int(1)

        elif input == "blue" or "Blue":
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

        if input == "Stingy" or "stingy":
            mrkrabs + int(1)
            plankton + int(1)

        elif input == "Smart" or "Smart":
            plankton + int(1)
            sandy + int(1)

        elif input == "Stupid" or "stupid":
            patrick + int(1)
            spongebob + int(1)

        elif input == "Funny" or "Funny":
            patrick + int(1)

        elif input == "creative" or "Creative":
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

        if input == "Money Day" or "money day":
            mrkrabs + int(1)

        elif input == "Christmas" or "christmas":
            sandy + int(1)

        elif input == "Annoy Squidward Day" or "annoy squidward day":
            patrick + int(1)
            spongebob + int(1)

        elif input == "the purge" or "The Purge":
            plankton + int(1)

        else:
            print("this selection is invalid, please correct any spelling "
                  "errors, or choose a valid response :)")
            questions = 5

    questions += 1

    quiz_end = True

if spongebob > 3:
    print("You resemble Spongebob Squarepants! [' o '] ")
elif patrick > 3:
    print("You resemble Patrick Star! :O ")
elif sandy > 3:
    print("you resemble Sandy Cheeks! >.< ")
elif mrkrabs > 3:
    print("You resemble Mr. Krabs! $$$$ ")
elif plankton > 3:
    print("Yoy resemble Plankton! >:) ")
