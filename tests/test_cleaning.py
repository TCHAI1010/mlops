import unittest
import numpy as np
import pandas as pd
from titanic.infrastructure.cleaning import*

class TestCleaning(unittest.TestCase):

    def test_renameColumns(self) -> None:
        df = pd.DataFrame(
            {
                'home.dest': [5,4,2,5],
                'pclass':[5,4,2,5],
                'sibsp':[5,4,2,5],
                'parch':[5,4,2,5]
            }
        )
        result=renameColumns(df)
        expected= pd.DataFrame(
            {
                'homeDestination': [5,4,2,5],
                'passengerClass':[5,4,2,5],
                'siblingsOrSpouses':[5,4,2,5],
                'parentsOrChildren':[5,4,2,5]
            }
        )
        pd.testing.assert_frame_equal(result, expected)


    def test_replacingNA(self) -> None:
        df = pd.DataFrame(
            {
                'home.dest': [np.nan,4,2,5],
                'pclass':[5,4,np.nan,5],
                'sibsp':[5,np.nan,2,5],
                'parch':[5,4,2,np.nan]
            }
        )
        result=replacingNA(df)
        expected= pd.DataFrame(
            {
                'home.dest': ['NA',4,2,5],
                'pclass':[5,4,'NA',5],
                'sibsp':[5,'NA',2,5],
                'parch':[5,4,2,'NA']
            }
        )
        pd.testing.assert_frame_equal(result, expected)

    def removeDuplicates(self) -> None:
        df = pd.DataFrame(
            {
                'home.dest': [5,4,2,5],
                'pclass':[5,4,2,5],
                'sibsp':[5,4,2,5],
                'parch':[5,4,2,5]
            }
        )
        result=drop_duplicates(df)
        expected= pd.DataFrame(
            {
                'home.dest': [5,4,2],
                'pclass':[5,4,2],
                'sibsp':[5,4,2],
                'parch':[5,4,2]
            }
        )
        pd.testing.assert_frame_equal(result, expected)
    