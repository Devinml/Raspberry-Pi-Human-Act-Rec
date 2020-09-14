from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import scipy
import pickle
file_name = 'model/spectral_trained_model.sav'
infile = open(file_name, 'rb')
model = pickle.load(infile)



df = pd.read_csv('data/testactivity_2_13_13_34.txt')
print(df.columns)
# X = df[['X','Y','Z','alpha','gamma','beta']]
# model.predict(X)
