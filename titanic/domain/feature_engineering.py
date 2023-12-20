import pandas as pd
import numpy as np
import re


def transfomm_homedest(data:pd.DataFrame)-> pd.DataFrame:
    """
    Tranform the variable 'homeDestination'.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataframe. Should have 'homeDestination'.

    Returns
    -------
    pd.DataFrame
        Input dataframe with separated colums home et dest.
    """
    data['home'] = 'NA'
    data['dest'] = 'NA'

    for i in range(len(data['homeDestination'])):
        if pd.notna(data['homeDestination'][i]):
            string = re.split(r'[,/]', data['homeDestination'][i])
            if len(string) == 4:
                data.at[i, 'home'] = ','.join([string[0], string[1]])
                data.at[i, 'dest'] = ','.join([string[2], string[3]])
            else:
                data.at[i, 'dest'] = ','.join(string)
    
    return(data)
    







def feature_selection(data:pd.DataFrame, selected_columns:list)-> pd.DataFrame:
    """
    Get the right dataframe for prediction.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataframe.
    selected_colums : list
        Input list of selected columns.

    Returns
    -------
    pd.DataFrame
        Input dataframe with only selected features.
    """     

    df=data.loc[:, selected_columns]
    return(df)


def encode_features(data:pd.DataFrame)-> pd.DataFrame:
    """
    Create age and fare classes. Shoulde have 'age' and 'fare'

    Parameters
    ----------
    data : pd.DataFrame
        Input dataframe.

    Returns
    -------
    pd.DataFrame
        output dataframe age and fare class.
    """ 

    df=data.copy()

    age_class = [0, 18, 26, 41, 56, 100]
    label_age = ['0-17', '18-25', '26-40', '41-55', '55+']
    fare_class = [0, 26, 51, 600]
    label_fare = ['0-25', '26-50', '50+']

    df['age'].replace('NA', pd.NA, inplace=True)
    df['fare'].replace('NA', pd.NA, inplace=True)

    df.loc[df['age'].notna(), 'age'] = pd.cut(df['age'][df['age'].notna()], bins=age_class, labels=label_age, right=False)

    df.loc[df['fare'].notna(), 'fare'] = pd.cut(df['fare'][df['fare'].notna()], bins=fare_class, labels=label_fare, right=False)


    df['age'].replace(pd.NA,'NA',  inplace=True)
    df['fare'].replace( pd.NA,'NA', inplace=True)

    return(df)


def getDummies(data: pd.DataFrame, cols: list)-> pd.DataFrame:
    """
    Create dummy variables.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataframe.

    Returns
    -------
    pd.DataFrame
        output dataframe with dummy variables.
    """ 

    df=pd.get_dummies(data, columns=cols, drop_first=True,dtype=float)
    return(df)






