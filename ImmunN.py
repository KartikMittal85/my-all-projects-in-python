import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import matrics
from sklearn.matrics import accuracy_score
from sklearn.matrics import confusion_matrix,classification_report
from sklearn.matrics import precision_score,recall_score, f1_score
datasat= pd.read_csv("Immuno.csv") 
dataset.shape
dataset.isnull().any()
dataset=dataset.fillna(mathod='ffill')

x=dataset.iloc[:,0:7]
y=dataset.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_sate=0)

