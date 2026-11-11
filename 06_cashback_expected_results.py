"""Expected cases from the FinPay Lab 4 edge-case table."""
import unittest
from cashback import calculate_cashback

class CashbackExpectedResults(unittest.TestCase):
    def test_basic_canteen(self):
        self.assertEqual(calculate_cashback(10000, "CANTEEN", "BASIC"), 200)
    def test_prime_canteen(self):
        self.assertEqual(calculate_cashback(10000, "CANTEEN", "PRIME"), 300)
    def test_premium_canteen(self):
        self.assertEqual(calculate_cashback(10000, "CANTEEN", "PREMIUM"), 400)
    def test_floor_not_round(self):
        self.assertEqual(calculate_cashback(333, "CANTEEN", "BASIC"), 6)
    def test_below_one_paise(self):
        self.assertEqual(calculate_cashback(49, "CANTEEN", "BASIC"), 0)
    def test_one_paise_boundary(self):
        self.assertEqual(calculate_cashback(50, "CANTEEN", "BASIC"), 1)
    def test_hostel_prime(self):
        self.assertEqual(calculate_cashback(10300, "HOSTEL", "PRIME"), 77)
    def test_topup(self):
        self.assertEqual(calculate_cashback(10000, "TOPUP", "BASIC"), 0)

if __name__ == "__main__":
    unittest.main()
