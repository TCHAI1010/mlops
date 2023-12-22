import unittest
import numpy as np
import pandas as pd
import sys
sys.path.append('/mlops/titanic')
from titanic.domain.feature_engineering import *


class TestFeatureEngineering(unittest.TestCase):

    def test_tranform_homedest(self) -> None:
        df = pd.DataFrame(
            {
                'homeDestination': ['Zurich, Switzerland',
                                    'Yoevil, England / Cottage Grove, OR']
            }
        )
        result=transfomm_homedest(df)
        expected= pd.DataFrame(
            {
                'homeDestination': ['Zurich, Switzerland',
                                    'Yoevil, England / Cottage Grove, OR'],
                'home':['NA','Yoevil, England '],
                'dest':['Zurich, Switzerland',' Cottage Grove, OR']
            }
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_feature_selection(self) -> None:
        df = pd.DataFrame(
            {
                'age': [17,18,70],
                'sex':['male','male','female'],
                'fare':[500,200,100]
            }
        )
        result=feature_selection(df,['age','fare'])
        expected=pd.DataFrame(
            {
                'age': [17,18,70],
                'fare':[500,200,100]
            }
        )
        pd.testing.assert_frame_equal(result, expected)

    
    def test_encode_features(self) -> None:
        df=pd.DataFrame(
            {
                'age': [12,20,70],
                'fare':[10,30,60]
            }
        )
        result=encode_features(df)
        expected=pd.DataFrame(
            {
                'age': ['0-17','18-25','55+'],
                'fare':['0-25','26-50','50+']
            }
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_getDummies(self) -> None:
        df=pd.DataFrame(
            {
                'age': ['0-17','18-25','55+'],
                'fare':['0-25','26-50','50+']
            }
        )
        result=pd.DataFrame(
            {
                'age_18-25':[0,1,0],
                'age_55+':[0,0,1],
                'fare_26-50':[0,1,0],
                'fare_50+':[0,0,1]
            }
        )
        pd.testing.assert_frame_equal(result, expected)