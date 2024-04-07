import unittest
import numpy as np
import pandas as pd
from preprocessing import *

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


class TestScaleData(unittest.TestCase):
    def test_list_input(self):
        data_list = [1, 2, 3, 4, 5]
        scaled_data_list = scale_min_max(data_list)
        self.assertEqual(scaled_data_list, [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_pandas_series_input(self):
        data_series = pd.Series([1, 2, 3, 4, 5])
        scaled_data_series = scale_min_max(data_series)
        self.assertTrue(scaled_data_series.equals(pd.Series([0.0, 0.25, 0.5, 0.75, 1.0])))

    def test_numpy_array_input(self):
        data_array = np.array([1, 2, 3, 4, 5])
        scaled_data_array = scale_min_max(data_array)
        self.assertTrue(np.allclose(scaled_data_array, [0.0, 0.25, 0.5, 0.75, 1.0]))

class TestInvertScaleData(unittest.TestCase):
    def test_list_input(self):
        data_list = [0.0, 0.25, 0.5, 0.75, 1.0]
        scaled_data_list = invert_scale_min_max(data_list, 1, 5)
        self.assertEqual(scaled_data_list, [1, 2, 3, 4, 5])

    def test_pandas_series_input(self):
        data_series = pd.Series([0.0, 0.25, 0.5, 0.75, 1.0])
        scaled_data_series = invert_scale_min_max(data_series, 1, 5)
        self.assertTrue(scaled_data_series.equals(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])))

    def test_numpy_array_input(self):
        data_array = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        scaled_data_array = invert_scale_min_max(data_array, 1, 5)
        self.assertTrue(np.allclose(scaled_data_array, [1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
