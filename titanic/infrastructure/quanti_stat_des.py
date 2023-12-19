import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram (data: pd.DataFrame):
    """
    Plot histograms for quantitative variables in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Input data to generate plots.

    """
    for i in ['age', 'siblingsOrSpouses','parentsOrChildren', 'fare']:

        filtered_data=data[i][data[i] != 'NA']
        
        plt.hist(filtered_data, bins=30, color='skyblue', edgecolor='black')

        plt.title(f'Répartition de {i}')
        plt.xlabel('Valeurs')
        plt.ylabel('Fréquence')
        
        plt.show()