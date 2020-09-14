from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import numpy as np



merged_data = pd.read_csv('data/merged_data.txt')

X = merged_data[['X','Y','Z','alpha','gamma','beta']]
y = merged_data['activity']

rf = RandomForestClassifier()
rf.fit(X,y)

filename = 'model/spectral_trained_model.pkl'
pickle.dump(rf, open(filename, 'wb'))