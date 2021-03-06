from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle


def read_data(spectrum):
    """
    This function returns a dataframe based off
    wich data set that I want to evaluate
    Parameters
    ----------
    method of data analysis that want to train a model on
    Boolean

    Returns
    -------
    Pandas DataFrame
    """
    if spectrum:
        fp = 'data/feat.txt'
        return pd.read_csv(fp)
    elif spectrum is None:
        fp = 'data/joined_calc_data.csv'
        return pd.read_csv(fp)
    else:
        fp = 'data/stats_method.csv'
        return pd.read_csv(fp)


def prep_data(random_forest, spectrum):
    """
    Specify the model you want and the what data set
    you want to use and this function returns a data set
    that is prepped for that function
    Parmeters
    ---------
    random_forest = Boolean
    spectrum = Booolean
    Returns
    -------
    split data in DataFrames
    X_train, X_test, y_train, y_test
    """
    df = read_data(spectrum)
    df_test = df[(df['Participant'] == 1) |
                 (df['Participant'] == 8) |
                 (df['Participant'] == 7) |
                 (df['Participant'] == 10) |
                 (df['Participant'] == 17) |
                 (df['Participant'] == 11)]
    df_train = df[(df['Participant'] != 1) &
                  (df['Participant'] != 8) &
                  (df['Participant'] != 7) &
                  (df['Participant'] != 10) &
                  (df['Participant'] != 17) &
                  (df['Participant'] != 11)]
    X_train = df_train.drop(columns=['activitiy', 'Participant'], axis=1)
    X_test = df_test.drop(columns=['activitiy', 'Participant'], axis=1)
    if random_forest:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
        y_train = pd.get_dummies(y_train)
        y_test = pd.get_dummies(y_test)
    else:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
    return X_train, X_test, y_train, y_test


def split_data_standard(random_forest, spectrum):
    """
    Splits the data and scales the data
    Parameters
    ---------
    random_forest = Boolean
    spectrum = Booolean
    Returns
    -------
    scaled data
    X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = prep_data(random_forest, spectrum)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test, scaler


def random_forest(random_forest, spectrum):
    """
    performs a random foresst classifier on the prpeed data
    Parameters
    ----------
    random_forest = Boolean
    spectrum = Boolean
    Returns
    -------
    predictions on test set, y_test, and model
    """
    clf = RandomForestClassifier(random_state=0)
    (X_train,
     X_test,
     y_train,
     y_test, scaler) = prep_data(random_forest, spectrum)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    return prediction, y_test, clf, scaler


def logclassifier(random_forest, spectrum):
    """
    performs a log classifier on the prpeed data
    Parameters
    ----------
    random_forest = Boolean
    spectrum = Boolean
    Returns
    -------
    predictions on test set, y_test, and model
    """
    clf = LogisticRegression(max_iter=1000)
    (X_train,
     X_test,
     y_train,
     y_test, scaler) = split_data_standard(random_forest, spectrum)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    return prediction, y_test, clf, scaler


def results():
    # print("Random Forest")
    # print(classification_report(y_test_rf, preds))
    print('Log Classification')
    print(classification_report(y_test_log, prediction))
    print('Log Coef')
    # results = pd.DataFrame(classification_report(y_test_rf,
                                                #  preds,
                                                #  output_dict=True))
    # print(results.T.to_markdown())


if __name__ == '__main__':
    (prediction,
     y_test_log,
     clf,
     scaler) = logclassifier(False, True)
    # Uncomment this line to see the model results
    results()
    filename = 'model/log_model.pkl'
    pickle.dump(clf, open(filename, 'wb'))
    filename = 'model/scalar.pkl'
    pickle.dump(scaler,open(filename, 'wb'))
