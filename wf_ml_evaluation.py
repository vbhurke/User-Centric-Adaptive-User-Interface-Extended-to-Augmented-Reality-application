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


files = os.listdir(os.getcwd()+"\data_processing")
directory=os.getcwd()+"\data_processing"
# Filter files that start with "Website_Analytics_"
matching_files = [file for file in files if file.startswith('df_1')]

# Printing initial values
df_1 = pd.read_csv(str(directory)+"\df_1.csv")
print(df_1.head())

# Splitting Training and Testing data according
df_1['YEAR'] = pd.to_numeric(df_1['YEAR'])

# Split the dataset based on the 'YEAR' column
train_data = df_1[df_1['YEAR'] <= 2021]
test_data = df_1[df_1['YEAR'] > 2021]

# Drop the 'YEAR' column from the training and testing sets
train_data = train_data.drop('YEAR', axis=1)
test_data = test_data.drop('YEAR', axis=1)

# Display the shape of the training and testing sets
print("Training Data Shape:", train_data.shape)
print("Testing Data Shape:", test_data.shape)

X_train = train_data[['BOUNCE RATE (%)','ENTRANCES']]
X_test = test_data[['BOUNCE RATE (%)','ENTRANCES']]
y_train = train_data['EXIT RATE (%)']
y_test = test_data['EXIT RATE (%)']

wf_ml_training.linear_reg(X_train, y_train)

y_pred = wf_ml_prediction.lr_prediction(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the performance metrics
print(f'Mean Squared Error: {mse}')           
print(f'R^2 Score: {r2}')


X_scaled = wf_ml_training.k_means_clustering(df_1, n_clusters=10)

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

db_index = davies_bouldin_score(X_scaled, kmeans_model.labels_)
print(f"Davies-Bouldin Index: {db_index}")





