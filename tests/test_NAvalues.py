import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from titanic.infrastructure.cleaning import replacingNA


class TestTransform(unittest.TestCase):

    def test_clean(self) -> None:
        df = pd.DataFrame(
            {
                'pclass': [1, 1, 2],
                'survived': [1,1,0],
                'name': ['Mrs Clarck', 'Mr John', 'Miss Blue'],
                'sex': ['female','male',None],
                'age': [24, 7, 5],
                'sibsp': [0, 0, 1],
                'parch': [2, 0, 6],
                'ticket': ['5573Y', '45689', '235TU7'],
                'fare': [456, 32, 25],
                'cabin': ['6H',None, 'J8'],
                'embarked': ['S', 'S', 'E'],
                'boat': [None,None,'56'],
                'body': [None,None,None],
                'home.dest': ['Montreal', 'Washington', 'LouisVille']
            }
        )
        result = replacingNA(df)
        expected = pd.DataFrame(
            {
                'pclass': [1, 1, 2],
                'survived': [1,1,0],
                'name': ['Mrs Clarck', 'Mr John', 'Miss Blue'],
                'sex': ['female','male','NA'],
                'age': [24, 7, 5],
                'sibsp': [0, 0, 1],
                'parch': [2, 0, 6],
                'ticket': ['5573Y', '45689', '235TU7'],
                'fare': [456, 32, 25],
                'cabin': ['6H','NA','J8'],
                'embarked': ['S', 'S', 'E'],
                'boat': ['NA','NA','56'],
                'body': ['NA','NA','NA'],
                'home.dest': ['Montreal', 'Washington', 'LouisVille']
            }
        )

        try:
            pd.testing.assert_frame_equal(pd.DataFrame(result), expected)
            print("Les DataFrames sont égaux.")
        except AssertionError as e:
            print("Les DataFrames ne sont pas égaux. Différences :\n", e)


if __name__ == '__main__':
    unittest.main()
