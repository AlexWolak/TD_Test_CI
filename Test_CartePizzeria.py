import unittest
from unittest.mock import Mock
from cartePizzeria import CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()
        self.mock_pizza = Mock()
        self.mock_pizza.name = 'Margherita'
      
    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())
        self.carte.add_pizza(self.mock_pizza)
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)
        self.carte.add_pizza(self.mock_pizza)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_add_pizza(self):
        self.carte.add_pizza(self.mock_pizza)
        self.assertEqual(self.carte.nb_pizzas(), 1)
      
    def test_remove_pizza(self):
        self.carte.add_pizza(self.mock_pizza)
        self.carte.remove_pizza('Margherita')
        self.assertEqual(self.carte.nb_pizzas(), 0)
    
if __name__ == '__main__':
    unittest.main()

