import numpy as np
import pandas as pd

def add_odd_ratio(df : pd.DataFrame) -> pd.DataFrame :
    """
    This function add the odd ratio transformation in a third column of a dataframe 

    Parameters :
    - df : a dataframe with the modalities used in the model and their different coefficients
  
    Return :
    - A dataframe, with the modalities, their coefficients and their odd ratios
    """
    df['Odds_Ratio'] = np.exp(df['Coeff'])
    
    return df

