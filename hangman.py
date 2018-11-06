import random
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
        "head" : "  O",
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

playing = True


word = random.choice(words)
done = False
wrong_guesses = []
right_guesses = []
while (not done) :
    gameover = ((len(wrong_guesses)+2) > num_wrong_guesses_allowed)
    gamewin = (len(right_guesses) > (len(word)))
    guess = input("What is your letter? ").lower()
    if guess in word:
        right_guesses.append(guess)
        draw_hangman(len(wrong_guesses))
        print("yay")
        if(gamewin):
            print ("You won!")
            continue
        continue
    else:
            wrong_guesses.append(guess)
            draw_hangman(len(wrong_guesses))
            print (wrong_guesses)
            if(gameover):
                done = True
                print("Game over, sorry")
            continue
