import pandas as pd
import numpy as np
import re


def transfomm_homedest(data:pd.DataFrame)-> pd.DataFrame:
    """
    Tranform the variable 'homeDestination'.

    Parameters
    ----------
    df : pd.DataFrame
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
    







def feature_selection(data:pd.DataFrame, selected_colums:list)-> pd.DataFrame:
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


def name(data:pd.DataFrame)-> pd.DataFrame:
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
    

