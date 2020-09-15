from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import numpy as np
import joblib


merged_data = pd.read_csv('data/merged_data.txt')

X = merged_data[['X','Y','Z','alpha','gamma','beta']]
y = merged_data['activity']

rf = RandomForestClassifier()
rf.fit(X,y)

filename = 'model/test_model_new.sav'
joblib.dump(rf, open(filename, 'wb'))