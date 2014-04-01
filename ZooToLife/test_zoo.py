import unittest
from zoo import Zoo
from animal import Animal


class testZoo(unittest.TestCase):

    def setUp(self):
        self.testAnim = Animal("zvqr", 10, 'gosh', 'male', 100)
        self.testZoo = Zoo(15, 12000)

    def test_get_animal_no_animals(self):
        self.assertEqual(0, self.testZoo.get_animal_count())

    def test_add_animal(self):
        self.testZoo.add_animal(self.testAnim)

if __name__ == "__main__":
    unittest.main()
