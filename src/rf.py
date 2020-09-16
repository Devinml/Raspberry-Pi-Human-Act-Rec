from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import pandas as pd
import numpy as np
import joblib

merged_data = pd.read_csv('data/feat.txt')
X = merged_data.drop(columns=['activitiy', 'Participant'], axis=1)
y = merged_data['activitiy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

log = LogisticRegression(max_iter=1000)
log.fit(X_train,y_train)
preds = log.predict(X_test)
print(classification_report(y_test,preds))
print(log.coef_)

filename = 'model/log_classifier.pkl'
joblib.dump(log, filename) 

filename = 'model/scalar.pkl'
joblib.dump(scalar, filename) 

