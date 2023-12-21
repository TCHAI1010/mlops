from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
from sklearn.model_selection import cross_val_score, KFold, train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def apply_LogisticRegression(x,y):
    """
    Fit the logistic regression model

    Parameters
    ----------
    x
    y

    Returns
    ----------
    Training score
    Testing score
    Accuracy
    Classification Report
    Matrice de Confusion
    Cross validation Score
    Average Score
    """

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
    reg=LogisticRegression()
    reg.fit(x_train,y_train)

    y_pred = reg.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\nTraining Score:",reg.score(x_train,y_train))
    print("\nTesting Score:",reg.score(x_test,y_test))
    print("\nAccuracy:", accuracy)

    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=reg.classes_, yticklabels=reg.classes_)
    plt.title('Matrice de Confusion')
    plt.xlabel('Valeurs Prédites')
    plt.ylabel('Valeurs Réelles')
    plt.show()

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(reg,x,y,cv=kf)
    print("Scores de validation croisée:", scores)
    print("Score moyen:", np.mean(scores))

    return(reg)

