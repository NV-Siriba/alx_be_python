import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3,5),8)
        self.assertEqual(self.calc.add(-1,-1),-2)
        self.assertEqual(self.calc.add(3,-5),-2)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,1),2)
        self.assertEqual(self.calc.subtract(-1,-1),0)
        self.assertEqual(self.calc.subtract(3,-5),8)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(-1,-1),1)
        self.assertEqual(self.calc.multiply(3,-5),-15)
    def test_division(self):
        self.assertEqual(self.calc.divide(2,1),2)
        self.assertEqual(self.calc.divide(-1,-1),1)
        self.assertEqual(self.calc.divide(-2,2),-1)
        self.assertIsNone(self.calc.divide(2,0),"can not divide by 0")

if __name__ == '__main__':
    unittest.main()
