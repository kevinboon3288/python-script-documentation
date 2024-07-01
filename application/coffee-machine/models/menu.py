from models.resource import Resource
from models.coffee import Coffee
import json
import os

class Menu():
    def __init__(self):
        self.CurrentResource = Resource()
        self.Coffees = []

    def GetCurrentResource(self):
        print("****************************")
        print("Machine Resource :")
        self.CurrentResource.GetResource()
        print("****************************")

    def SetCurrentResource(self):
        waterValue = input("Water\t: ")
        milkValue = input("Milk\t: ")
        coffeeValue = input("Coffee\t: ")
        self.CurrentResource.SetResource(waterValue, milkValue, coffeeValue)

    def GetMenu(self):
        print("\nCoffee Menu:")
        print("****************************")
        for counter in range(0, len(self.Coffees)):
            print(f"{counter+1}.{self.Coffees[counter].Name.upper()} ({self.Coffees[counter].Price})")
        print("****************************\n")

    def Init(self, json_path):
        if os.path.isdir(json_path):
            raise ValueError(f"Invalid repo directory path: {json_path}")

        with open(json_path) as file:
            data = json.load(file)
            for item in data:
                if item == "resource":
                    self.CurrentResource.Water = data[item].get("water")
                    self.CurrentResource.Milk = data[item].get("milk")
                    self.CurrentResource.Coffee = data[item].get("coffee")
                elif item == "menu":
                    for coffeeInfo in data[item]:
                        coffee = Coffee(coffeeInfo)                       
                        for info in data[item][coffeeInfo]:
                            if info == "cost":
                                coffee.Price = data[item][coffeeInfo].get(info)
                            elif info == "ingredient":
                                coffee.Water = data[item][coffeeInfo][info].get("water")
                                coffee.Milk = data[item][coffeeInfo][info].get("milk")
                                coffee.Coffee = data[item][coffeeInfo][info].get("coffee")                    
                        self.Coffees.append(coffee)
                else:
                    print("Not supported keys from data.json")