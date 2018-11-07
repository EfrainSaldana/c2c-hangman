import random
import string

hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  ☺",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)
def duplicate (lst, value):
    return [i for i, v in enumerate(lst) if v == value]

complete = False
while (not complete):
    dashes = ""
    word = random.choice(words)
    for char in word:
        dashes = dashes + "_ "
    done = False
    wrong_guesses = []
    right_guesses = []
    character_list = []
    dashes = dashes.split()
    wordList = list(word)
    firstRun = 0
    for character in word:
        if character not in character_list:
            character_list.append(character)
    while (not done) :
        gameover = ((len(wrong_guesses)+1) > num_wrong_guesses_allowed)
        gamewin = len(character_list) == len(right_guesses)
        if(gamewin):
            print ("You won!")
            answer = input("Would you like to play again?").lower()
            if (answer == "no"):
                done = True
                complete = True
                break
            elif (answer == "yes"):
                done = True
                break
            else:
                print("Please reread the question (:")
        if(gameover):
            done = True
            print("Game over, sorry")
            print("Just for curisioty, the word was: " + word)
            answer = input("Would you like to play again? ").lower()
            if (answer == "no"):
                done = True
                complete = True
                break
            elif (answer == "yes"):
                done = True
                break
            else:
                print("Please reread the question (:")

        while (firstRun == 0):
            draw_hangman(len(wrong_guesses))
            print(dashes)
            print("")
            firstRun += 1
        guess = input("What is your letter? ").lower()
        if(guess.isalpha() and len(guess)<2):
            if guess in word:
                if guess in right_guesses:
                    print("You already tried this!")
                    print("Please choose another letter")
                    continue
                right_guesses.append(guess)
                counter = duplicate(wordList, guess)
                for x in counter:
                    dashes[x] = guess
                draw_hangman(len(wrong_guesses))
                print(dashes)
                print ("")
                print("This letter works!")
                print("Right guesses:" + str(right_guesses))
                print ("Wrong guesses: " + str(wrong_guesses))
                print("")
                continue
            else:
                    if guess in wrong_guesses:
                        print("You already tried this!")
                        print("Please choose another letter")
                        continue
                    wrong_guesses.append(guess)
                    draw_hangman(len(wrong_guesses))
                    print (dashes)
                    print("")
                    print("Right guesses:" + str(right_guesses))
                    print ("Wrong guesses: " + str(wrong_guesses))
                    print("")
                    continue
        else:
            print("Please type a single letter :)")
