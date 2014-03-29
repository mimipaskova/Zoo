#from animal import Animal


class Zoo():
    def __init__(self, capasity=10, budjet=10000):
        self.animals = {}
        self.capasity = capasity
        self.budjet = budjet

    def get_animal_count(self):
        result = 0
        for i in self.animals:
            result += len(i)
        return result
