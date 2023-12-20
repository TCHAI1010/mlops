#!/usr/bin/env python
# coding: utf-8



import os
import pathlib
import pandas as pd



def check_data():
    df_titanic = load_data()
    
    missing_data = df_titanic.isnull().sum().sum()

    duplicates = df_titanic.duplicated().sum()

    if missing_data == 0 and duplicates == 0:
        print("Il n'y a pas de données manquantes ni de duplicatas.")
    else:
        if missing_data > 0:
            print(f"Il y a {missing_data} données manquantes.")
        if duplicates > 0:
            print(f"Il y a {duplicates} lignes en doublon.")




