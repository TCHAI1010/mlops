#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pathlib
import pandas as pd


# In[5]:


def check_data(df: pd.DataFrame) -> pd.DataFrame:
    
    missing_data = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    if missing_data == 0 and duplicates == 0:
        print("Il n'y a pas de données manquantes ni de duplicatas.")
    else:
        if missing_data > 0:
            print(f"Il y a {missing_data} données manquantes.")
        if duplicates > 0:
            print(f"Il y a {duplicates} lignes en doublon.")



# In[ ]:





# In[ ]:




