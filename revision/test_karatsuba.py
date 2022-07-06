from karatsuba import karatsuba_multiplication
import unittest


class TestKaratsuba(unittest.TestCase):
    def test_karatsuba_multiplication(self):
        self.assertEqual(karatsuba_multiplication(56, 34), 1904)
    
    def test_karatsuba_multiplication2(self):
        self.assertEqual(karatsuba_multiplication(12, 34), 12*34)

    def test_karatsuba_multiplication3(self):
        self.assertEqual(karatsuba_multiplication(67, 89), 67*89)

    def test_karatsuba_multiplication4(self):
        self.assertEqual(karatsuba_multiplication(46, 134), 46*134)
    
    def test_karatsuba_multiplication5(self):
        self.assertEqual(karatsuba_multiplication(1234, 5678), 1234*5678)
    
    def test_karatsuba_multiplication6(self):
        self.assertEqual(
            karatsuba_multiplication(12344321, 56788765), 12344321*56788765)

    def test_karatsuba_multiplication_long(self):
        self.assertEqual(
            karatsuba_multiplication(
                3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627
            ),
            8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
        )