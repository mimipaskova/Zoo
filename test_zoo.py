import unittest
from zoo import Zoo


class testZoo(unittest.TestCase):

    def setUp(self):
        self.testZoo = Zoo(15, 12000)

    def test_get_animal_no_animals(self):
        self.assertEqual(0, self.testZoo.get_animal_count())

if __name__ == "__main__":
    unittest.main()
