import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drinks import Drinks

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00) 
        self.customer = Customer("Guido van Rossum", 64.00, 24, 10.00)
        self.customer_2 = Customer("John Smith", 20.00, 15, 15.00)
        self.drinks = Drinks("Latte", 3.50, 5.00)


    

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50) 
        self.assertEqual(102.50, self.coffee_shop.till)

    def test_buy_drink(self):
        self.coffee_shop.increase_till(self.drinks.price)
        self.coffee_shop.reduce_wallet(self.customer, self.drinks.price)
        self.assertEqual(103.50, self.coffee_shop.till)
        self.assertEqual(60.50, self.customer.wallet)

    def test_is_old_enough(self):
        self.coffee_shop.is_old_enough(self.customer)
        self.assertGreaterEqual(self.customer.age, 16)

    def test_too_high_energy(self):
        self.




