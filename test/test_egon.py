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
        self.assertEqual(egon.discount(4), 4)
        self.assertEqual(egon.discount(12), 12)

        # Discount 1
        self.assertEqual(egon.discount(15), 13.5)
        self.assertEqual(egon.discount(72), 42.0)
        self.assertEqual(egon.discount(132), 72.0)

        # Discount 2
        self.assertEqual(egon.discount(133), 72.25)
        self.assertEqual(egon.discount(200), 89.0)
        self.assertEqual(egon.discount(723), 219.75)
        self.assertEqual(egon.discount(724), 220.0)

        # Discount 3
        self.assertEqual(egon.discount(725), 220.0)
        self.assertEqual(egon.discount(1000), 220.0)

    def test_price_for_days(self):
        egon.price_for_days(1, 10, True)
        self.assertEqual(egon.price_for_days(1, 10, False), 5.80)
        self.assertEqual(egon.price_for_days(10, 10, False), 35.0)

        self.assertEqual(egon.price_for_days(1, 10, True), 6.80)
        self.assertEqual(egon.price_for_days(10, 10, True), 40.0)

class TestVgn(unittest.TestCase):
    def test_single_online(self):
        self.assertEqual(vgn.single_online(1, "A"), 5.50)
        self.assertEqual(vgn.single_online(10, "A"), 55.0)

    def test_single_offline(self):
        self.assertEqual(vgn.single_offline(1, "A"), 6.40)
        self.assertEqual(vgn.single_offline(10, "A"), 64.0)

    def test_day(self):
        self.assertEqual(vgn.day(1, "A"), 8.30)
        self.assertEqual(vgn.day(10, "A"), 83.0)

if __name__ == '__main__':
    unittest.main()
