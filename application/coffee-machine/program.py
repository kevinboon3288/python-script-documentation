from models.menu import *

def ShowMenuOption(coffeeMenu):
    print("****************************")
    print("1. Menu ")
    print("2. Current Machine Resource ")
    print("3. Set Machine Resource ")
    print("****************************")
    userInput = int(input(f"Select an option : "))
    if(userInput == 1):
        coffeeMenu.GetMenu()
    elif(userInput == 2):
        coffeeMenu.GetCurrentResource()
    elif(userInput == 3):
        coffeeMenu.SetCurrentResource()

def main():
    isEnd = False
    coffeeMenu = Menu()
    coffeeMenu.Init()

    while(not isEnd):
        if input(f"Start Menu (Y/N):").lower() != "y":
            isEnd = True
        else:
            ShowMenuOption(coffeeMenu)

if __name__ == "__main__":
    main()
