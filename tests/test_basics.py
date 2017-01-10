import unittest


import numpy as np
import pandas as pd


class TestSomething(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame.from_records(
            np.rec.array([(0, 1, 'a'), (1, 2, 'b'), (2, 3, 'c'), (3, 4, 'd')],
            dtype=[('index', '<i8'), ('one', '<i8'), ('two', 'O')])
        )

    def test_one(self):
        self.assertEqual(len(self.df), 4)
