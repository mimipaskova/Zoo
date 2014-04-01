import random


class Animal(object):
    """docstring for Animal"""
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def eat(self, food_type, food_weight):
        return self.weight*food_weight

    def grow(self, average_weight, weight_age):
        if(self.weight < average_weight):
            self.weight += average_weight
        return self.weight

    def is_alive(self, life_expectancy):
        if(self.age > life_expectancy*0.9):
            numb = random.randint(0, 100)
            if numb > 10:
                return False
        if(self.age > life_expectancy*0.8):
            numb = random.randint(0, 100)
            if numb > 20:
                return False
        return True
