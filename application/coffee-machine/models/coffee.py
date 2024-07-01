from models.resource import Resource

class Coffee(Resource):
    def __init__(self, name):
        self.Name = name
        self.Price = 0.0
        self.Water =  0
        self.Milk = 0
        self.Coffee = 0