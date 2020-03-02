import unittest
import task
import math
from datetime import date


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
    
    def testList(self):
        list = [1,2,3,4,5]
        expectedFirst,expectedLast = task.firstlast(list)
        self.assertEqual(1, expectedFirst)
        self.assertEqual(5, expectedLast)
    
    def testList(self):
        date1 = date(2000, 1, 1)
        date2 = date(2000, 2, 28)
        expected = (date1-date2).days
        self.assertEqual(expected, task.days(date1, date2))


if __name__ == '__main__':
    unittest.main()