

import numpy as np 
import pandas as pd 
import os
import seaborn as sns
import matplotlib.pyplot as plt

def afficher_distributions_categoriees_sns(test):
    pas_col = test.columns[[3, 5, 6, 7, 9, 13,10,12,8,14]]

    for colonne in test.columns:
        if colonne not in pas_col:
            plt.figure(figsize=(15, 5))
            sns.countplot(x=colonne, data=test, palette='viridis')
            
            plt.title(f'Distribution des modalités dans {colonne}')
            plt.xlabel('Modalité')
            plt.ylabel('Fréquence')
            plt.show()





