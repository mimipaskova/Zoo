import unittest
import animal


class testAnimal(unittest.TestCase):

    def setUp(self):
        self.new_animal = animal.Animal("tiger", 10, "Mimi", "female", 100)

    def test_eat_animal(self):
        self.assertEqual(6, self.new_animal.eat(0.06))

    def test_grow(self):
        self.assertEqual(100.4,self.new_animal.grow(250,12.0))

    def test_is_alive(self):
        self.new_animal.age=0
        self.assertEqual(True, self.new_animal.is_alive(20))
        self.new_animal.age=20
        self.assertEqual(False,self.new_animal.is_alive(20))

if __name__ == "__main__":
    unittest.main()
