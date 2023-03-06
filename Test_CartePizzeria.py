import unittest
from unittest.mock import Mock
from cartePizzeria import CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        pizza = Mock()
        self.empty_pizza = CartePizzeria()
        self.not_empty_pizza = CartePizzeria()
        self.not_empty_pizza.pizzas = [pizza]


    def test_is_empty(self):
        self.assertTrue(self.empty_pizza.is_empty())

    def test_is_not_empty(self):
        self.assertFalse(self.not_empty_pizza.is_empty())
      

    def test_nb_pizzas_on_empty_cartePizzeria(self):
        self.assertEqual(self.empty_pizza.nb_pizzas(), 0)
    
    def test_nb_pizzas_on_not_empty_cartePizzeria(self):
        self.assertEqual(self.not_empty_pizza.nb_pizzas(), 1)
    

    def test_add_pizza(self):
        pizza = Mock()
        self.empty_pizza.add_pizza(pizza)
        self.assertEqual(self.empty_pizza.pizzas, [pizza])

    def test_add_pizza_with_not_empty(self):
        pizza = Mock()
        tmp = [pizza for pizza in self.not_empty_pizza.pizzas]
        self.not_empty_pizza.add_pizza(pizza)
        self.assertEqual(self.not_empty_pizza.pizzas, tmp + [pizza])
      
      
    #def test_remove_pizza(self):
    #    self.pizza.add_pizza(self.mock_pizza)
    #    self.pizza.remove_pizza('Margherita')
    #    self.assertEqual(self.pizza.nb_pizzas(), 0)
    #    self.assertRaises(CartePizzeriaException, self.pizza.remove_pizza, 'Pepperoni')

    
if __name__ == '__main__':
    unittest.main()


    #def test_is_empty(self):
    #    self.assertTrue(self.carte.is_empty())
    #    self.carte.add_pizza(self.mock_pizza)
    #    self.assertFalse(self.carte.is_empty())