import subprocess
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import wf_ml_training
import wf_ml_prediction
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

to_summary = []
files = os.listdir(os.getcwd()+"\data_processing")
directory=os.getcwd()+"\data_processing"
# Filter files that start with "Website_Analytics_"
matching_files = [file for file in files if file.startswith('df_1')]


df_1 = pd.read_csv(str(directory)+"\df_1.csv")
print(df_1.head())

df_1['YEAR'] = pd.to_numeric(df_1['YEAR'])

train_data = df_1[df_1['YEAR'] <= 2021]
test_data = df_1[df_1['YEAR'] > 2021]

train_data = train_data.drop('YEAR', axis=1)
test_data = test_data.drop('YEAR', axis=1)

to_summary.append("Linear Regression : ")

print("Training Data Shape:", train_data.shape)
print("Testing Data Shape:", test_data.shape)
Tr_DS = "Training Data Shape: " + str(train_data.shape)
Te_DS = "Testing Data Shape:"+ str(test_data.shape)
to_summary.append(Tr_DS)
to_summary.append(Te_DS)

X_train = train_data[['BOUNCE RATE (%)','ENTRANCES']]
X_test = test_data[['BOUNCE RATE (%)','ENTRANCES']]
y_train = train_data['EXIT RATE (%)']
y_test = test_data['EXIT RATE (%)']

wf_ml_training.linear_reg(X_train, y_train)

y_pred = wf_ml_prediction.lr_prediction(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')           
print(f'R^2 Score: {r2}')
to_summary.append("Mean Squared Error : "+str(mse))
to_summary.append("R^2 Score : "+str(r2))



X_scaled = wf_ml_training.k_means_clustering(df_1, n_clusters=10)
to_summary.append("K-Means Clusterring (clusters 10) : ")
kmeans_model = wf_ml_prediction.kmeans_prediction(df_1, test_data)

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_model.labels_, cmap='viridis')
plt.xlabel('PAGE VIEWS')
plt.ylabel('ENTRANCES')
plt.title('K-Means Clustering')
plt.tight_layout
name_path=os.getcwd()+"\\visuals\\Image_df_1.png"
plt.savefig(name_path, dpi=300)
plt.clf()

silhouette_avg = silhouette_score(X_scaled, kmeans_model.labels_)
print(f"Silhouette Score: {silhouette_avg}")
to_summary.append("Silhouette Score: "+str(silhouette_avg))
db_index = davies_bouldin_score(X_scaled, kmeans_model.labels_)
print(f"Davies-Bouldin Index: {db_index}")
to_summary.append("Davies-Bouldin Index: "+str(db_index))

to_summary.append("KNN Classifier (neighbours = 5): ")
knn_X_test, knn_y_test = wf_ml_training.knn(df_1,5)
knn_y_pred = wf_ml_prediction.knn_prediction(knn_X_test)


knn_accuracy = accuracy_score(knn_y_test, knn_y_pred)
print("KNN Accuracy:", knn_accuracy)
to_summary.append("KNN Accuracy : "+str(knn_accuracy))

to_summary.append("KNN Classifier (neighbours = 20): ")
knn_X_test, knn_y_test = wf_ml_training.knn(df_1,20)
knn_y_pred = wf_ml_prediction.knn_prediction(knn_X_test)

knn_accuracy = accuracy_score(knn_y_test, knn_y_pred)
print("KNN Accuracy:", knn_accuracy)
to_summary.append("KNN Accuracy (neighbours = 20): "+str(knn_accuracy))

summary_text=os.getcwd()+"\data_processing\summary_.txt"
with open(summary_text, 'w') as f:
    for x in to_summary:
        f.write(x)
        f.write("\n")





