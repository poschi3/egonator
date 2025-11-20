import unittest
import egon
import vgn


class TestEgon(unittest.TestCase):
    def test_basic_price(self):
        # Nürnberg Hbf ->  Nürnberg Schoppershof
        self.assertEqual(egon.basic_price(2.4), 0.72)

        # Nürnberg Hbf -> Fürth Hbf
        self.assertEqual(egon.basic_price(7.1), 2.13)

        # Nürnberg Hbf -> Erlangen Hbf
        self.assertEqual(egon.basic_price(17.6), 5.28)

        # Nürnberg Hbf -> Bayreuth Hbf
        # This is not what VGN webiste says because we calculate discount in secound step
        self.assertEqual(egon.basic_price(41.6 + 24.8), 19.92)

    def test_discount(self):
        # No discount
        self.assertEqual(egon.discount(4), 4.00)
        self.assertEqual(egon.discount(12), 12.00)

        # Discount 1
        self.assertEqual(egon.discount(15), 15.00)
        self.assertEqual(egon.discount(72), 45.00)
        self.assertEqual(egon.discount(88), 51.50)

        # Discount 2
        self.assertEqual(egon.discount(89), 51.75)
        self.assertEqual(egon.discount(133), 62.75)
        self.assertEqual(egon.discount(168), 70.00)

        # Discount 3
        self.assertEqual(egon.discount(169), 70.00)
        self.assertEqual(egon.discount(1000), 70.00)

    def test_price_for_days(self):
        egon.price_for_days(1, 10, 2, True)
        self.assertEqual(egon.price_for_days(1, 10, 2, False), 7.50)
        self.assertEqual(egon.price_for_days(10, 10, 1, False), 31.50)
        self.assertEqual(egon.price_for_days(10, 10, 2, False), 46.50)
        self.assertEqual(egon.price_for_days(10, 10, 5, False), 70.00)


        self.assertEqual(egon.price_for_days(1, 10, 2, True), 9.00)
        self.assertEqual(egon.price_for_days(10, 10, 2, True), 52.00)

class TestVgn(unittest.TestCase):
    def test_single_online(self):
        self.assertEqual(vgn.single_online(1, "A", 2), 7.30)
        self.assertEqual(vgn.single_online(1, "A", 1), 3.65)
        self.assertEqual(vgn.single_online(10, "A", 2), 73.00)
        self.assertEqual(vgn.single_online(10, "A", 5), 182.50)


    def test_single_offline(self):
        self.assertEqual(vgn.single_offline(1, "A", 2), 7.80)
        self.assertEqual(vgn.single_offline(10, "A", 2), 78.00)

    def test_day(self):
        self.assertEqual(vgn.day(1, "A"), 10.60)
        self.assertEqual(vgn.day(10, "A"), 106.00)

if __name__ == '__main__':
    unittest.main()
