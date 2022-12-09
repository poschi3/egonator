import unittest
import egon
import vgn


class TestEgon(unittest.TestCase):
    def test_basic_price(self):
        # Nürnberg Hbf ->  Nürnberg Schoppershof
        self.assertEqual(egon.basic_price(2.4), 0.58)

        # Nürnberg Hbf -> Fürth Hbf
        self.assertEqual(egon.basic_price(7.1), 1.70)

        # Nürnberg Hbf -> Erlangen Hbf
        self.assertEqual(egon.basic_price(17.6), 4.22)

        # Nürnberg Hbf -> Bayreuth Hbf
        # This is not what VGN webiste says because we calculate discount in secound step
        self.assertEqual(egon.basic_price(41.6 + 24.8), 15.94)

    def test_discount(self):
        # No discount
        self.assertEqual(egon.discount(4), 4.00)
        self.assertEqual(egon.discount(12), 12.00)

        # Discount 1
        self.assertEqual(egon.discount(15), 13.50)
        self.assertEqual(egon.discount(72), 42.00)
        self.assertEqual(egon.discount(132), 72.00)

        # Discount 2
        self.assertEqual(egon.discount(133), 72.25)
        self.assertEqual(egon.discount(200), 89.00)
        self.assertEqual(egon.discount(723), 219.75)
        self.assertEqual(egon.discount(724), 220.00)

        # Discount 3
        self.assertEqual(egon.discount(725), 220.00)
        self.assertEqual(egon.discount(1000), 220.00)

    def test_price_for_days(self):
        egon.price_for_days(1, 10, 2, True)
        self.assertEqual(egon.price_for_days(1, 10, 2, False), 5.80)
        self.assertEqual(egon.price_for_days(10, 10, 1, False), 23.00)
        self.assertEqual(egon.price_for_days(10, 10, 2, False), 35.00)
        self.assertEqual(egon.price_for_days(10, 10, 5, False), 71.00)


        self.assertEqual(egon.price_for_days(1, 10, 2, True), 6.80)
        self.assertEqual(egon.price_for_days(10, 10, 2, True), 40.00)

class TestVgn(unittest.TestCase):
    def test_single_online(self):
        self.assertEqual(vgn.single_online(1, "A", 2), 5.50)
        self.assertEqual(vgn.single_online(1, "A", 1), 2.75)
        self.assertEqual(vgn.single_online(10, "A", 2), 55.00)
        self.assertEqual(vgn.single_online(10, "A", 5), 137.50)


    def test_single_offline(self):
        self.assertEqual(vgn.single_offline(1, "A", 2), 6.40)
        self.assertEqual(vgn.single_offline(10, "A", 2), 64.00)

    def test_day(self):
        self.assertEqual(vgn.day(1, "A"), 8.30)
        self.assertEqual(vgn.day(10, "A"), 83.00)

if __name__ == '__main__':
    unittest.main()
