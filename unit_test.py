import unittest
import math_parser

class GeneralTest(unittest.TestCase):
    variables = {"foo" : 4, "bar" : 5, "a" : 1, "b" : 2, "c" : 100}

    def testSingleVariable(self):
        self.assertEqual(math_parser.evaluate("foo", self.variables), 4)

    def test_1(self):
        self.assertEqual(math_parser.evaluate("foo+bar", self.variables), 9)

    def test_2(self):
        self.assertEqual(math_parser.evaluate("foo+(bar*c)", self.variables), 504)

    def test_3(self):
        self.assertEqual(math_parser.evaluate("foo+(bar*c)+b", self.variables), 506)

    def test_4(self):
        self.assertEqual(math_parser.evaluate("foo+(bar*c*a)+b", self.variables), 506)

    def test_5(self):
        self.assertEqual(math_parser.evaluate("foo+(bar*c*a)+(b*c)", self.variables), 704)

    def test_6(self):
        self.assertEqual(math_parser.evaluate("foo+(bar*c*a)+((b*c))", self.variables), 704)

class TestPrecedence(unittest.TestCase):
    variables = {"a" : 1, "b" : 2, "c" : 3}

    def test_1(self):
        self.assertEqual(math_parser.evaluate("a+b*c", self.variables), 7)

    def test_2(self):
        self.assertEqual(math_parser.evaluate("a*b+c", self.variables), 5)

if __name__ == '__main__':
    unittest.main()
