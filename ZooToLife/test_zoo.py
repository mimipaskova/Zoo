import unittest
from zoo import Zoo
from animal import Animal


class testZoo(unittest.TestCase):

    def setUp(self):
        self.testAnim = Animal("zvqr", 10, 'gosh', 'male', 100)
        self.testZoo = Zoo(15, 12000)

    def test_get_animal_no_animals(self):
        self.assertEqual(0, self.testZoo.get_animal_count())

    def test_add_animal_with_count(self):
        self.testZoo.add_animal(self.testAnim)
        self.assertEqual(1, self.testZoo.get_animal_count())

    def test_remove_animal(self):
        self.testZoo.add_animal(self.testAnim)
        self.testZoo.remove_animal(self.testAnim)
        self.assertEqual(0, self.testZoo.get_animal_count())

    def test_income(self):
        self.testZoo.add_animal(self.testAnim)
        # Add some animals
        self.testAnimTosh = Animal("zver", 10, 'tosh', 'female', 120)
        self.testAnimTesi = Animal("cver", 10, 'tesi', 'male', 20)

        self.testZoo.add_animal(self.testAnimTesi)
        self.testZoo.add_animal(self.testAnimTosh)

        self.assertEqual(180, self.testZoo.income())

    def test_check_month_passed_days_reset(self):
        self.testZoo.month = 30
        self.check_month_passed()
        self.assertEqual(0, self.testZoo.month)

    def test_check_month_passed_dead_animal(self):
        self.testZoo.add_animal(self.testAnim)
        self.testAnim.age = 10000 # some infinite age
        self.testZoo.check_month_passed()
        self.assertEqual({}, self.testZoo.animals)

    # def outcome


if __name__ == "__main__":
    unittest.main()
