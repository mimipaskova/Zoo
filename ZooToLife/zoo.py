from animal import Animal
#from zoo_database import get_food_type


def get_food_type(anim):
    pass


class Zoo(Animal):
    def __init__(self, capasity=10, budjet=10000):
        self.animals = {}
        self.capasity = capasity
        self.budjet = budjet
        self.animal_income = 60
        self.meat_price = 4
        self.grass_price = 2

    def get_animal_count(self):
        result = 0
        for spec in self.animals:
            result += len(self.animals[spec])
        return result

    def add_animal(self, animal):
        '''
        Adds an animal to the zoo
        -If no such speacies in the zoo - adds it
        -Else add the animal to the list of animals of
          the species
        '''
        if self.animals.__contains__(animal.species):
            animals = self.animals[animal.get_species]
            self.animals[animal.get_species] = animals.append(animal)
            #  CHECK self.animalimals[animal.get_species] = dict.setdefault()
        else:
            self.animals[animal.species] = [animal]

    def remove_animal(self, animal):
        '''
        Removes an animal
        '''
        for anim in self.animals:
            if animal in self.animals[anim]:
                self.animals[anim].remove(animal)

    def income(self):
        '''
        Returns the dayly income for the Zoo
        '''
        return self.animal_income * self.get_animal_count()

    def feed_animals(self):
        '''
        Returns a the sum needed to
        feed all the animals
        '''
        result = 0
        # anim keeps the species of the animal
        for anim in self.animals:
            if get_food_type(anim) == "meat":
                result += self.meat_price * len( self.animals[anim] )
            else:
                result += self.grass_price * len( self.animals[anim] )
        return result

    def outcome(self):
        '''
        Returns the dayly outcome for the Zoo
        '''
        pass

    def __check_genders(self):
        pass

    def __born_new_baby(self):
        pass

    def new_babies(self):
        '''
        Checks if new baby is to be added in the Zoo
        Uses __check_gender and __born_new_baby
        '''
        pass
