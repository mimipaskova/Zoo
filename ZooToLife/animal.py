import sqlite3


class Animal(object):
    """docstring for Animal"""
    def __init__(self, species, age, name, gender, weight):
        self.species=species
        self.age=age
        self.name=name
        self.gender=gender
        self.weight=weight



    def eat(self, food_type, food_weight ):
        return self.weight*food_weight


