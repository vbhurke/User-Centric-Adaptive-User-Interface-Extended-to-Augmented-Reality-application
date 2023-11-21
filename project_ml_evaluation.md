#### SER594: Machine Learning Evaluation
#### User-Centric Adaptive User Interface for Augmented Reality application 
#### Viresh Bhurke
#### 11-20-23

Evaluation Metrics
Metric 1
Name: Silhouette score

Choice Justification: The silhouette score is done for K-means clustering model. The clustering algorithm creates a cluster for the webpage in the specific cluster region. The features indicate the behaviour of the user and clusters them in a region. This clustering for 0 will give web-paths which show tendency for higher page views and entrances. The cluster indicates that this web path is more famous in terms of viewers and frequent use. The importance of the web path with user perspective will be understood and can be prioritized.   

Interpretation: The higher the silhouette score, ie closer to 1 it indicates the more defined clusterring of the data. The score should be higher in order to get an accurate decision of the classification.

Metric 2
Name: Davies-Bouldin

Choice Justification: This metric is used to evaluate the clustering algorithms. This metric takes into account both the compactness and separation of the cluster points. It is an efficient, robust and complementary to other metrics for evaluation. 

Interpretation: A lower Davies-Bouldin score indicates defined clustering classes. It is necessary to consider other metrics along with this. In this case we consider 

Metric 3
Name: Mean Squared Error

Choice Justification: This is used to evaluate the linear regression model for the predicted values. The MSE works efficiently in understanding the errors occured by the predictions. This will help me understand the errors it produces.

Interpretation: A high error would indicate that the model failed to perform well. The lower the value the better it is.

Metric 4
Name: R squared

Choice Justification : The R squared evaluates the variance of the target prediction in linear regression for the selected independent variances. 

Metric 5
Name: Accuracy

Choice Justification : The accuracy checks the prediction from knn classification. It checks the correct predictions vs the total predictions. This is an accurate way to understand the efficiency of the predicting 

Alternative Models
Alternative 1
Construction: Linear Regression Model 
The model uses simple linear regression to predict the exit rate i.e the rate of the users that leave the website after clicking or performing action on the website. The model is constructed by training data of Entrances and Bounce rate to get the Exit rate. The Exit rate helps us identify the rate of users which use the webpage rather than just visit or bounce off it. The bounce rate plays a crucial role in predicting the exit as it directly influencing the factor for the web page activity. The model performs this for all the paths of a webpage, as the fact of bounce rate for a path of website also influences the activity of webpage.    

Evaluation: The model is evaluated based on the MSE score of the predicted value of the exit rate. We calculate the R square value to check the variance in target.  

Alternative Models
Alternative 2
Construction: KNN model (5 clusters)
The model is constructed to classify the data for specific web paths. The model is trained for data such as 'PAGE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)', 'ENTRANCES'. This data is used to classify the web pages based on the page views which is the viewers for the page, the average time one spends on the page and the entrances or number of times the webpage was used. This is the most logical way to get a classification for the desired page views, average time and entrances. This classification groups the pages based on the path and should be able to predict the class which is the web path most suitable for the data values. This classification should be able to predict the web path most desired or the path with most potential with increase in the input type. I will be able to identify which web path has the highest probablity to reach an efficient state where 'PAGE VIEWS', 'AVERAGE TIME ON PAGE (SECONDS)', 'ENTRANCES', will be optimal. This was the most desired model to succeed as this would have given me the exact web path to target for future. Unfortunately the results were not good caused by uncertain behaviour in some subpaths or user behaviour having some more influence which was not collected.   

Evaluation : The model is evaluated from the predictions using the accuracy of correct predictions. This model predicts the class for the values. Unfortunately based on the values in summary_ it shows the model is not at all good for prediction.

Alternative Models
Alternative 3
Construction: KNN model (7 clusters)
The above model uses the same features to predict the class which is the path of web page. In this case I have increased the number of clustering which should be able to accomodate the classes more accurately. This will decrease the error if there is excess noise.  

Evaluation : Same as earlier the model evaluates based on predictions. The increase in clusters only caused more errors, thus indicating that the KNN model is not a suitable approach. The model is causing overfitting and giving false accuracy.

Best Model

Model: Kmeans Clustering 
The K-means clustering is valuable for web analysis, it provides an insight in the users behaviour and website optimization. The clustering can identify user patterns on the webpage such as frequency of visits and viewer for that. This is used to analyze the typical behaviour of user journey through the website. I have selected fields of 'PAGE VIEWS', 'ENTRANCES', to cluster the pages based on these features eventually leading to a prediction of which cluster a page will lie in. The clusters helps me identify which website should be given optimal 

Visualization
Visual 1
Analysis: The image is stored in \\visuals\\Image_df_1.png . This image shows the clustering of page stats. This gives me the clustering regions of web paths for the specific webpages of the websites.    