from src.customer import Customer
from src.drinks import Drinks
from src.food import Food


class CoffeeShop:

    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ['Mocha', 'Latte', 'Cappuchino', 'Hot Chocolate', 'Tea']

    def increase_till(self, amount):
        self.till += amount

    def reduce_wallet(self, customer, drink_price):
        customer.wallet -= drink_price

    def is_old_enough(self, customer):
        return customer.age

    def increase_energy_level(self, customer, drink):
        

    
            

    
