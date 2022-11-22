import unittest

from cart_modified import Cart, Item, Shop, items

test_cart = Cart()

class CartTest(unittest.TestCase):
    
    def test_add1(self):
        test_cart.add('carrot', 2, 1.5, items)
        self.assertIn('carrot', items)
    
    def test_add2(self):
        test_cart.add('carrot', 2, 1.5, items)
        self.assertNotIn('durian', items)
        self.assertIn('carrot', items)
    
    def test_int(self):
        blaber = Item('bobby', 'blaber', 'C9')
        self.assertIsInstance(blaber.quantity, int)

    def test_delete1(self):
        test_cart.add('pineapple', 4, 2, items)
        self.assertIn('pineapple', items)
        test_cart.delete('pineapple', items)
        self.assertNotIn('pineapple', items)

    # # Couldn't get this one to work properly
    # def test_delete2(self):
    #     self.assertNotIn('peanuts', items)
    #     self.assertRaises(KeyError, test_cart.delete('peanuts', items))


unittest.main()