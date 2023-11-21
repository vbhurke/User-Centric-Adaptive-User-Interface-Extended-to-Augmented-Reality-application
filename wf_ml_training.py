import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


def linear_reg(X_train, y_train):
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    model_filename = 'models\lr_model.joblib'
    joblib.dump(lr_model, model_filename)
    print(f'Model saved to {model_filename}')


def k_means_clustering(df_1,n_clusters):
    features_for_clustering = ['PAGE VIEWS', 'ENTRANCES']
    X = df_1[features_for_clustering]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    model_filename = 'models\kmeans_model.joblib'
    joblib.dump(kmeans, model_filename)
    print(f'Model saved to {model_filename}')
    return X_scaled


def knn(df_1,n_neighbors):
    list_1 = []
    count=0
    for x in df_1['PAGE PATH']:
        if len(x.split(','))>1:
            splitted_x = x.split(',')[1]
        else:
            splitted_x = 'null'
        df_1['PAGE PATH'][count] = splitted_x
        if not splitted_x in list_1:
            list_1.append(splitted_x)
        count += 1

    print(len(list_1))
    print(df_1.size)

    le = LabelEncoder()
    df_1['PAGE PATH LABEL'] = le.fit_transform(df_1['PAGE PATH'])
    train_data = df_1[df_1['YEAR'] <= 2021]
    test_data = df_1[df_1['YEAR'] > 2021]
    X_train = train_data[['PAGE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)', 'ENTRANCES']]
    X_test = test_data[['PAGE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)', 'ENTRANCES']]  # Adjust features as needed
    y_train = train_data['PAGE PATH LABEL']
    y_test = test_data['PAGE PATH LABEL']

    knn_classifier = KNeighborsClassifier(n_neighbors) 
    knn_classifier.fit(X_train, y_train)
    model_filename = 'models\knn_model_'+str(n_neighbors)+'.joblib'
    joblib.dump(knn_classifier, model_filename)
    print(f'Model saved to {model_filename}')
    return X_test, y_test

   


