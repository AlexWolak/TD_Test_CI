class CartePizzeria:

    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
         
         if len(self.pizzas) == 0 :
             return True
         else :
            return  False
         
    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException("La pizza n'existe pas dans la carte")
        
class CartePizzeriaException(Exception):
    pass