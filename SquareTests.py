import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_first_area(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_first_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, "Error: negative value")

    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, "Error: negative value")

    def test_float_perimeter(self):
        res = perimeter(3.42)
        self.assertEqual(res, 13.68)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_string_area(self):
        res = area("hi")
        self.assertEqual(res, "Error: wrong data type")

    def test_string_perimeter(self):
        res = perimeter("hi!!!")
        self.assertEqual(res, "Error: wrong data type")



if __name__ == '__main__':
    unittest.main()