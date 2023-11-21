import os
import csv
import joblib
import matplotlib.pyplot as plt

def lr_prediction(X_test):
    # Load the model
    lr_model = joblib.load('models\lr_model.joblib')
    # Make predictions
    y_pred = lr_model.predict(X_test)
    return y_pred

def kmeans_prediction(df_1, test_data):
    # Making a duplicate dataframe
    df1_copy = df_1
    features_for_clustering = ['PAGE VIEWS', 'ENTRANCES']
    # Load the model
    kmeans_model = joblib.load('models\kmeans_model.joblib')
    predictions = kmeans_model.predict(test_data[features_for_clustering])
    test_data['K-Means Predictions'] = predictions
    test_data.to_csv("data_processing\df1_test_data.csv", index=False)
    return kmeans_model

def knn_prediction(X_test):
    # Load the model
    knn_model = joblib.load('models\knn_model.joblib')
    # Make predictions on the test set
    y_pred = knn_model.predict(X_test)
    return y_pred
