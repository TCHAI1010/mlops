import os
import pathlib
import pandas as pd


def load_data():
    """
    Load raw data.

    Returns
    -------
    tuple
        One dataframe.
    """
    df_titanic = pd.read_excel(
        os.path.join('data', 'titanic3.xls')
    )

    return df_titanic