import numpy as np
import pandas as pd


def get_intercept(modele):
    """
    This function takes a model in parameter and returns the intercept.


    Parameters:
    modele : regression model


    Returns:
    intercept : value of the intercept of the model.
    """
    intercept = modele.intercept_
    return intercept



def getCoefficients(df : pd.DataFrame, modele) -> pd.DataFrame:
    """
    This function returns the modalities used in the model and their coefficients


    Parameters :
    - modalities : liste of the modalities used.
    - modele :the model trained.


    Return :
    - An array with the modalities and the coefficients.
    """


    tab=pd.DataFrame(data={'Features':list(df.columns),
                       'Coeff':modele.coef_.flatten()})
    print(tab)
    return tab
