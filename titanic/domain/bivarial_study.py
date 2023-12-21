import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


# Calculer les tris croisés


# Calculer la matrice de corrélation
def cramers_v(confusion_matrix):
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))


# Fonction pour calculer la matrice de corrélation avec le V de Cramer
def correlation_matrix_cramer_v(dataframe: pd.DataFrame):
    columns = dataframe.columns
    matrix = np.zeros((len(columns), len(columns)))

    for i in range(len(columns)):
        for j in range(i, len(columns)):
            if i == j:
                matrix[i, j] = 1.0
            else:
                confusion_matrix = pd.crosstab(dataframe[columns[i]], dataframe[columns[j]])
                matrix[i, j] = cramers_v(confusion_matrix)
                matrix[j, i] = matrix[i, j]

    return matrix



# Afficher la matrice de corrélation avec le V de Cramer
def print_matrix_cramer(df: pd.DataFrame):

    correlation_matrix = correlation_matrix_cramer_v(df)

    # Afficher la matrice de corrélation sous forme de heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Matrice de corrélation')
    plt.xticks(range(len(df.columns)), df.columns, rotation=90)
    plt.yticks(range(len(df.columns)), df.columns, rotation=0)
    plt.show()


