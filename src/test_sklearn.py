from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import scipy
import pickle
import joblib
# from sklearn.externals import joblib
# joblib.dump(clf, 'filename.pkl') 

#then your colleagues can load it



# file_name = 'model/spectral_trained_model.sav'
# infile = open(file_name, 'rb')
# model = pickle.load(infile)
filename = 'model/anothertest_ec2.pkl'
clf = joblib.load(filename)


df = pd.read_csv('data/testactivity_2_13_13_34.txt')
print(df.head())
# X = df[['X','Y','Z','alpha','gamma','beta']]
# model.predict(X)
