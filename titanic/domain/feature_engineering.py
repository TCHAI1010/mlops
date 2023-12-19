import pandas as pd
import numpy as np
import re


def transfomm_homedest(data:pd.DataFrame)-> pd.DataFrame:
    """
    Tranform the variable 'home.dest'.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe. Should have 'home.dest'.

    Returns
    -------
    pd.DataFrame
        Input dataframe with separated colums home et dest.
    """
    data['home'] = 'NA'
    data['dest'] = 'NA'

    # Iterer à travers les éléments de la colonne 'home.dest'
    for i in range(len(data['home.dest'])):
        if pd.notna(data['home.dest'][i]):
            string = re.split(r'[,/]', data['home.dest'][i])
            if len(string) == 4:
                data.at[i, 'home'] = ','.join([string[0], string[1]])
                data.at[i, 'dest'] = ','.join([string[2], string[3]])
            else:
                data.at[i, 'dest'] = ','.join(string)







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