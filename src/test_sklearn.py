from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import scipy
import pickle
import joblib

file_name = 'model/spectral_trained_model.sav'
infile = open(file_name, 'rb')
# model = pickle.load(infile)
filename = 'model/test_model.sav'
loaded_model = joblib.load(filename)


df = pd.read_csv('data/testactivity_2_13_13_34.txt')
print(df.head())
# X = df[['X','Y','Z','alpha','gamma','beta']]
# model.predict(X)
