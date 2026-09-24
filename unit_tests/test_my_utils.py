import os
import sys
import unittest
import random

import my_utils

# test cases for mean function
class TestMean(unittest.TestCase):
    
    # for list of all positive integers
    def test_mean_positive(self):
        self.assertAlmostEqual(my_utils.mean([1, 2, 3, 4, 5]), 3.0)

    # for list with positive and negative numbers
    def test_mean_negative(self):
        self.assertAlmostEqual(my_utils.mean([-10, -5, 0, 5, 10]), 0.0)

    # for list with one element
    def test_mean_one(self):
        self.assertAlmostEqual(my_utils.mean([20]), 20.0)

    # for empty list
    def test_mean_empty(self):
        self.assertRaises(ValueError, my_utils.mean, [])

    # for non numeric list elements
    def test_mean_non_numeric(self):
        self.assertRaises(TypeError, my_utils.mean, [1, 2, 'a'])

    # randomness test
    def test_mean_random(self):
        random.seed(42)
        data = [random.randint(-100, 100) for _ in range(20)]
        expected = sum(data) / len(data)
        self.assertAlmostEqual(my_utils.mean(data), expected)

# test cases for median function
class TestMedian(unittest.TestCase):

    # for an odd number of elements
    def test_median_odd(self):
        self.assertAlmostEqual(my_utils.median([3, 1, 2]), 2.0)

    # for an even number of elements
    def test_median_even(self):
        self.assertAlmostEqual(my_utils.median([4, 3, 2, 1]), 2.5)

    # for elements that are negative numbers
    def test_median_negative(self):
        self.assertAlmostEqual(my_utils.median([-5, -1, -10, 0]), -3.0)

    # for empty list
    def test_median_empty(self):
        self.assertRaises(ValueError, my_utils.median, [])

    # for non numeric list elements
    def test_median_non_numeric(self):
        self.assertRaises(TypeError, my_utils.median, [1, None, 3])

    # randomness test
    def test_median_random(self):
        random.seed(123)
        data = [random.randint(-50, 50) for _ in range(15)]
        sort = sorted(data)
        n = len(sort)
        expected = float(sort[n // 2])
        self.assertAlmostEqual(my_utils.median(data), expected)

# test case for standard deviation function
class TestStandardDeviation(unittest.TestCase):

    # for know elements
    def test_std_known(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertAlmostEqual(my_utils.standard_deviation(data), 2.0)

    # for list with one element
    def test_std_one(self):
        self.assertAlmostEqual(my_utils.standard_deviation([10]), 0.0)

    # for list where all elements are identical
    def test_std_identical(self):
        self.assertAlmostEqual(my_utils.standard_deviation([7, 7, 7, 7]), 0.0)

    # for empty list
    def test_std_empty(self):
        self.assertRaises(ValueError, my_utils.standard_deviation, [])

    # for non numeric list elements
    def test_std_non_numeric(self):
        self.assertRaises(TypeError, my_utils.standard_deviation, [1, 2, 'bad'])

    # randomness test
    def test_std_random(self):
        random.seed(7)
        data = [random.uniform(-10,10) for _ in range(10)]
        m = sum(data) / len(data)
        expected = (sum((x - m) ** 2 for x in data) / len(data)) ** 0.5
        self.assertAlmostEqual(my_utils.standard_deviation(data), expected)

if __name__ == '__main__':
    unittest.main()