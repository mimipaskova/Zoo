from animal import Animal
#from zoo_database import get_food_type, get_gestation, get_average_weight, get_weight_age
# make it *


def get_life_expectancy(amim):
    return 1

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
        self.days_of_month = 0

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
        if self.capasity > self.get_animal_count()+1:
            if self.animals.__contains__(animal.species):
                animals = self.animals[animal.get_species]
                self.animals[animal.get_species] = animals.append(animal)
                #  CHECK self.animalimals[animal.get_species] = dict.setdefault()
            else:
                self.animals[animal.species] = [animal]
            return "Animal added"
        else:
            return "Zoo is full"

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

    def __feed_animals(self):
        '''
        Returns the sum needed to
        feed all the animals
        '''
        result = 0
        for species in self.animals:
            all_eated = sum([anim.eat() for anim in self.animals[species]])
            if get_food_type(species) == "meat":
                result += self.meat_price * all_eated
            else:
                result += self.grass_price * len(self.animals[species])
        return result

    def outcome(self):
        '''
        Returns the dayly outcome for the Zoo
        '''
        return self.feed_animals()

    def __check_genders(self, animal):
        '''
        Returns the if the animal can have a baby
        '''
        if animal.gender == "female":
            if animal.must_give_birth():
                pass #  ADD NEW ANIMAL
                     #  ADD to day pass
        else:
            return False

    def __born_new_baby(self):
        pass

    def new_babies(self):
        '''
        Checks if new baby is to be added in the Zoo
        Uses __check_gender and __born_new_baby
        '''
        pass

    def check_month_passed(self):
        '''
        Adds a month has to animals if passed
        '''
        self.__add_month_to_age_if_not_dead()
        self.days_of_month += 1
        if self.days_of_month >= 30:
            self.days_of_month = 0

    def __add_month_to_age_if_not_dead(self):
        '''
        Adds a month to all animals if animal is alive
        else removes the animal from the zoo
        Prints a messege if an animal has died
        '''
        for species in self.animals:
            for anim in self.animals[species]:
                if anim.is_alive(get_life_expectancy(species)):
                    anim.age += 1
                    #anim.grow(get_average_weight(species), get_weight_age(species))
                else:
                    print("{} the {} has died\n".format(anim.name,
                                                        anim.species))
                    self.remove_animal(anim)

    def a_day_pass(self):
        '''
        Runs a day in the zoo
        '''
        self.check_month_passed()
        self.budjet = self.income() - self.outcome()
        self.new_babies()
