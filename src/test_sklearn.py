from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import scipy
rf = RandomForestClassifier()

df = pd.read_csv('data/testactivity_2_13_13_34.txt')
# X = df.drop('')
print(df.head())
