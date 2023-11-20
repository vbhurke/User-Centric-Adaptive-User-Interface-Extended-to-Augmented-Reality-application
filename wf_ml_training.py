import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import joblib


def linear_reg(X_train, y_train):
    # Create a linear regression model
    lr_model = LinearRegression()
    # Train the model on the training set
    lr_model.fit(X_train, y_train)
    # Save the trained model to the 'models' folder
    model_filename = 'models\lr_model.joblib'
    joblib.dump(lr_model, model_filename)
    print(f'Model saved to {model_filename}')


def k_means_clustering(df_1,n_clusters):
    # Selecting relevant features for clustering
    features_for_clustering = ['PAGE VIEWS', 'ENTRANCES']
    # Extract features for clustering and standardize the data
    X = df_1[features_for_clustering]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Create KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    # Fit the model to the scaled data
    kmeans.fit(X_scaled)
    # Save the trained model to the 'models' folder
    model_filename = 'models\kmeans_model.joblib'
    joblib.dump(kmeans, model_filename)
    print(f'Model saved to {model_filename}')
    return X_scaled


