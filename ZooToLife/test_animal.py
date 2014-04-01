import unittest
import animal


class testAnimal(unittest.TestCase):

    def setUp(self):
        self.new_animal = animal.Animal("tiger", 10, "Mimi", "female", 100)

    #def test_get_animal_no_animals(self):
        #self.assertEqual(0, self.testZoo.get_animal_count())

if __name__ == "__main__":
    unittest.main()
