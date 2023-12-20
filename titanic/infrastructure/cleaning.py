import numpy as np
import pandas as pd


def goodColumnsFormat(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function rename the columns of a DataFrame.

    Parameters :
    - dataframe : dataframe that need to be updated with the new names of columns.
    - nouveaux_noms : Une liste de nouveaux noms de colonnes.

    Return :
    - A new DataFrame with the renamed colums.
    """
    df['pclass'] = pd.to_numeric(df['pclass'])
    df['survived'] = pd.to_numeric(df['survived'])
    df['age'] = pd.to_numeric(df['age'])
    df['fare'] = pd.to_numeric(df['fare'])
    df['sibsp'] = pd.to_numeric(df['sibsp'])
    df['parch'] = pd.to_numeric(df['parch'])

    return df


def renameColumns(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function rename the columns of a DataFrame.

    Parameters :
    - dataframe : dataframe that need to be updated with the new names of columns.
    - nouveaux_noms : Une liste de nouveaux noms de colonnes.

    Return :
    - A new DataFrame with the renamed colums.
    """

    df = df.rename(columns={"pclass": "passengerClass",
                         "sibsp": "siblingsOrSpouses",
                         "parch": "parentsOrChildren",
                         "home.dest" : "homeDestination"
                         })
    return df   



def replacingNA(df: pd.DataFrame) -> pd.DataFrame:
    """  
    This function remove the missing values.

    Parameters :
    - dataframe : dataframe that need to be updated with the missings values. 
    Return :
    - A new DataFrame with the missings values replaced         .
    """
    df = df.fillna('NA')
    return df



def removeDuplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function remove the duplicates rows of the DataFrame.

    Parameters :
    - dataframe : dataframe that need to be updated with the new names of columns.

    Return :
    - A new DataFrame with no duplicated rows.
    """
    df = df.drop_duplicates()
    return df    














