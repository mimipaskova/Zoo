import random


class Animal:
    """docstring for Animal"""
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age  # In months
        self.name = name
        self.gender = gender  # Male / Female
        self.weight = weight
        self.pregnant = -1  # if positive - the animal is pregnant
                            # if zero the animal must give birth
                            # if negative and more tham -6, it can get pregnant

    def eat(self, food_weight):
        '''
        The animal eats
        '''
        return self.weight*food_weight

    def grow(self, average_weight, weight_age):
        '''
        The animal grows every month
        '''
        if self.gender == "female":
            self.pregnant -= 1
        if(self.weight < average_weight):
            self.weight += weight_age/30
        return self.weight

    def is_alive(self, life_expectancy):
        '''
        This method check if the animal is alive or die
        '''
        chance_of_dying = self.age / life_expectancy

        numb = random.randint(0, 100)
        if numb <= (chance_of_dying*100):
            return False
        return True

    def must_give_birth(self):
        return self.pregnant == 0
