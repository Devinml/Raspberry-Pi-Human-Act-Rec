from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import numpy as np
import joblib



merged_data = pd.read_csv('data/merged_data.txt')

X = merged_data[['X','Y','Z','alpha','gamma','beta']]
y = merged_data['activity']

rf = RandomForestClassifier()
rf.fit(X.astype(np.float),y.astype(np.int))

filename = 'model/anothertest.pkl'
# joblib.dump(rf, open(filename, 'wb'))
joblib.dump(rf, filename) 