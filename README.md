# Introduction
This repository contains files for the individual course project in SER594: Data Science for Software Engineers (2023) created by VIRESH BHURKE for partial fulfillment of the course requirements.

At this time, this project has not been cleared by the course staff (R. Acuna) for public release, and must be kept within a private repository.
The program on running might give deprecated warnings. It will still run do not Kill it.

FOR MS5 check summary_ and visuals/Image_df_1
For windows it might give permission denied at 
wf_ml_prediction.py 
Then change : line 23
    test_data['K-Means Predictions'] = predictions
    test_data.to_csv("data_processing\df1_test_data.csv", index=False)
    return kmeans_model
to :
    test_data['K-Means Predictions'] = predictions
    test_data.to_csv("df1_test_data.csv", index=False)
    return kmeans_model

*** Note : This is windows error and can be resolved by changing some settings, the above solution is only for your assistance. 
