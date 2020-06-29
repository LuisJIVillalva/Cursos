import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

CONS = 18

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("Pan",7.0)
        self.jugo = Item("Jugo",5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self):
        print("Método tearDown despés de la preba")

    def test_cinco_mas_cinco_igual_dies(self):
        assert 5+5 == 10

    def test_nombre_producto_igual_pan(self):

        self.assertEqual(self.pan.name,"Pan")

    def test_nombre_producto_diferente_manzana(self):
        item = Item("Pan blanco",12.0)
        self.assertNotEqual(self.jugo.name,"Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto_pan(self):
        item= self.shopping_cart.get_item(self.pan)
        self.assertIs(item,self.pan)
        self.assertIsNot(item,self.jugo)

    def test_exceptio_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto(self):
        total= self.shopping_cart.total()
        self.assertGreater(total,0)
        self.assertLess(total,self.pan.price + 1.0)
        self.assertEqual(total,self.pan.price)

    def test_codigo_pan(self):
        self.asserNotRegex(self.pan.code(), self.pan.name)

    def test_fail(self):
        if 2 > 3:
            self.fail('Dos no es mayor a 3')
    #@unittest.skip("Colocamos nuestros motivos")
    #@unittest.skipIf(CONS < 18,"La versión es obsoleta") comopara a verdadero
    @unittest.skipUnless(3>5,"Colocamos nuestros motivos") #compara por el falso
    def test_prueba_skip(self):
        pass

if __name__ == '__main__':
    unittest.main()
