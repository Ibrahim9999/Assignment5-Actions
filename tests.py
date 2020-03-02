import unittest
import task
import math


class TestCase(unittest.TestCase):
    
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())
    
    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())
    
    def testArea(self):
        radius = 2
        expected = math.pi*radius*radius
        self.assertEqual(expected, task.area(radius))


if __name__ == '__main__':
    unittest.main()