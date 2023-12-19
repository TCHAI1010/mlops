import numpy as np
import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a raw extract of data.

    Parameters
    ----------
    df : pd.DataFrame
        Input data to clean.

    Returns
    -------
    pd.DataFrame
        Cleaned data.
    """
    df['age'] = pd.to_numeric(df['age'])
    df['fare'] = pd.to_numeric(df['fare'])


    df = df.drop_duplicates()
    df = df.dropna()
    return df