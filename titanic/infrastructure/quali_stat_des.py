#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np 
import pandas as pd 
import os


# In[18]:


titanic=pd.read_excel(r"C:\Users\159895\Downloads\M2_MLOPS\titanic3.xlsx")
titanic

#ne pas oublier le "pip install openpyxl" sur l'invite pour importer un xlsx


# In[19]:


def nettoyer_dataframe(titanic):
    # Supprimer les doublons
    titanic = titanic.drop_duplicates()
    return titanic 


# In[20]:


titanic.info() 


# In[21]:


#visualition de certaines infos macros sur la table
pd.set_option('display.float_format', '{:.2f}'.format)
titanic.describe() 


# In[22]:


mqt=titanic.isnull().sum()
print(mqt)


# In[50]:


# Remplacer les valeurs manquantes par "NA" dans tout le DataFrame
titanic = titanic.fillna("NA")
titanic 


# In[52]:


# Renommer les colonnes dans le DataFrame titanic
titanic = titanic.rename(columns={
    "pclass": "passengerClass",
    "sibsp": "siblingsOrSpouses",
    "home.dest": "homeDestination",
    "parch": "parentsOrChildren"
})
titanic


# In[81]:


import seaborn as sns
import matplotlib.pyplot as plt

def afficher_distributions_categoriees_sns(test):
    pas_col = test.columns[[3, 5, 6, 7, 9, 13]]

    for colonne in test.columns:
        if colonne not in pas_col:
            plt.figure(figsize=(15, 5))
            sns.countplot(x=colonne, data=test, palette='viridis')
            
            plt.title(f'Distribution des modalités dans {colonne}')
            plt.xlabel('Modalité')
            plt.ylabel('Fréquence')
            plt.show()

# Appeler la fonction pour afficher les graphiques de distribution avec Seaborn
afficher_distributions_categoriees_sns(test)


# In[82]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exemple de DataFrame test
# Assurez-vous de remplacer cela par votre propre façon de charger le DataFrame
test = ...

# Convertir la colonne "embarked" en type string
test['embarked'] = test['embarked'].astype(str)

# Créer une palette de couleurs pour chaque modalité
modalites = test['embarked'].unique()
couleurs_modalites = sns.color_palette("viridis", len(modalites))

# Créer l'histogramme avec des couleurs différentes pour chaque modalité
plt.figure(figsize=(8, 5))
sns.countplot(x='embarked', data=test, palette=couleurs_modalites, edgecolor='black')

plt.title('Distribution des modalités dans embarked')
plt.xlabel('Embarqué')
plt.ylabel('Fréquence')
plt.show()


# In[54]:


#HISTOGRAMMMES 
for colonne in titanic.columns:
    # Vérifier si la colonne est de type numérique
    if pd.api.types.is_numeric_dtype(titanic[colonne]):
        # Créer l'histogramme pour les variables quantitatives
        plt.figure(figsize=(10, 5))
        titanic[colonne].plot(kind='hist', edgecolor='black', bins=20)
        
        plt.title(f'Distribution de la variable {colonne}')
        plt.xlabel(colonne)
        plt.ylabel('Fréquence')
        plt.show()


# In[ ]:




