import random

def getChosenWord():
    word_list = ["consider", "minute", "accord", "evident", "practice", "vain", "circumstances",
                "constitute", "level", "dwell", "entertain", "earnest", "convention", "furnish",
                "venture", "territory", "temper", "chamber", "liberal", "merit", "manifest",
                "resource", "contempt", "plead", "pleague", "oppress", "disposition", "allege"]
    return random.choice(word_list)

def promptSetup(word):
    display = []
    for _ in range(len(word)):
        display += "_"
    return display

def main():

    chosenWord = getChosenWord()
    prompts = promptSetup(chosenWord)

    while('_' in prompts):
        guess = input(f"{prompts} \nGuess a letter:\t").lower()
        for position in range(len(chosenWord)):
            if chosenWord[position] == guess:
                prompts[position] = chosenWord[position]
        print("\n")

    print(f"\nCongratzzz!!! You guessed {chosenWord}")

if __name__ == "__main__":
    main()
