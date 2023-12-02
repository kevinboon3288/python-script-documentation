class Resource():
    def __init__(self):
        self.Water = 0
        self.Milk = 0
        self.Coffee = 0

    def GetResource(self):
        print(f"Water\t:{self.Water}")
        print(f"Milk\t:{self.Milk}")
        print(f"Coffee\t:{self.Coffee}")

    def SetResource(self, water, milk, coffee):
        self.Water = water
        self.Milk = milk
        self.Coffee = coffee
        print("Set Machine Resource successfully")
