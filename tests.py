import unittest
import egon


class TestEgon(unittest.TestCase):
    def test_calc_basic_price(self):
        # Nürnberg Hbf ->  Nürnberg Schoppershof
        self.assertEqual(egon.calc_basic_price(2.4), 0.58)

        # Nürnberg Hbf -> Fürth Hbf
        self.assertEqual(egon.calc_basic_price(7.1), 1.70)

        # Nürnberg Hbf -> Erlangen Hbf
        self.assertEqual(egon.calc_basic_price(17.6), 4.22)

        # Nürnberg Hbf -> Bayreuth Hbf
        # This is not what VGN webiste says because we calculate discount in secound step
        self.assertEqual(egon.calc_basic_price(41.6 + 24.8), 15.94)

    def test_calc_discount(self):
        # No discount
        self.assertEqual(egon.calc_discount(4), 4)
        self.assertEqual(egon.calc_discount(12), 12)

        # Discount 1
        self.assertEqual(egon.calc_discount(15), 13.5)
        self.assertEqual(egon.calc_discount(72), 42.0)
        self.assertEqual(egon.calc_discount(132), 72.0)

        # Discount 2
        self.assertEqual(egon.calc_discount(200), 95.0) #95 neu, # 89,5 alt


        # Discount 3
        self.assertEqual(egon.calc_discount(1000), 220.0) #95 neu, # 89,5 alt

if __name__ == '__main__':
    unittest.main()
