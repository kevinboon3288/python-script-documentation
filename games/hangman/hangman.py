import random

def getChosenWord():
    word_list = ["consider", "minute", "accord", "evident", "practice", "vain", "circumstances",
                "constitute", "level", "dwell", "entertain", "earnest", "convention", "furnish",
                "venture", "territory", "temper", "chamber", "liberal", "merit", "manifest",
                "resource", "contempt", "plead", "oppress", "disposition", "allege"]
    
    return random.choice(word_list)

def promptSetup(word):
    words = []
    for _ in range(len(word)):
        words += "_"
    return words

def main():
    lifePoint = 5
    isEnd = False
    chosenWord = getChosenWord()
    prompts = promptSetup(chosenWord)

    while(not isEnd):
        print(f"{' '.join(prompts)}")
        guess = input(f"\nGuess a letter:\t").lower()

        if guess not in chosenWord:
            lifePoint -= 1
            if lifePoint == 0:
                isEnd = True
                print(f"\nYou Lose!!! \nCorrect Word: {chosenWord} \nCurrent Life Point : {lifePoint}")
            else:
                print(f"\nWrong letter guessed!!! \nCurrent Life Point : {lifePoint}")
            continue

        for position in range(len(chosenWord)):
            if chosenWord[position] == guess:
                prompts[position] = chosenWord[position]

        if not '_' in prompts:
            isEnd = True
            print(f"\nCongratzzz!!! You guessed {chosenWord}")


if __name__ == "__main__":
    main()
