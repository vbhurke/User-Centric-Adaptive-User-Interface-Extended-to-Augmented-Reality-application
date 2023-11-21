#### SER594: Machine Learning Evaluation
#### User-Centric Adaptive User Interface for Augmented Reality application 
#### Viresh Bhurke
#### 11-20-23


Explainable Records
Record 1
Raw Data:
WEBSITE	PAGE PATH	PAGE URL	PAGE VIEWS	UNIQUE VIEWS	AVERAGE TIME ON PAGE (SECONDS)	ENTRANCES	BOUNCE RATE (%)	EXIT RATE (%)	
www.brla.gov	['', '2191', 'pillar-3-culture-and-art-engagements']	http://www.brla.gov/2191/pillar-3-culture-and-art-engagements	18	17	22.56	50	0.75	3.12	


Prediction Explanation: K-Means Predictions = 4
The k-means prediction helps identify the cluster with the closest proximity. The cluster indicates that the web path selected belongs to cluster 4 and shows similar trends to paths of cluster 4. In this cluster the values for entrances and page views are close but low. Indicating the path has small activity and is required to be optimized. This cluster has low potential but should be further looked into for improvement.

Record 2
Raw Data: 
WEBSITE	PAGE PATH	PAGE URL	PAGE VIEWS	UNIQUE VIEWS	AVERAGE TIME ON PAGE (SECONDS)	ENTRANCES	BOUNCE RATE (%)	EXIT RATE (%)	

www.brla.gov	['', '2760', 'land-use']	http://www.brla.gov/2760/land-use	2	1	17.5	0	0	0	


Prediction Explanation: K-Means Predictions   = 8
The given section clusters towards the 8th cluster of the model. It indicates in the cluster 8, which is implies highly insignificant path. We notice it has very low page views and entrances indicating the low use and need of this web path.  


Interesting Features
Feature A
Feature: 'PAGE VIEWS' - The page views is the views a page gets from the users. 

Justification: This has a high impact on the need of the webpage as a higher page view would significantly increase the need of the website. Page views has important value for determining the use of the web page for the website. This plays a crucial role in determining the  

Feature B
Feature: 'ENTRANCES' - This is the 

Justification: TODO

Experiments 
Varying A
Prediction Trend Seen: The page views with low value clusters towards the higher number of cluster group. The cluster in this field shows smaller values for high page views.

Varying B
Prediction Trend Seen: The clustering shows tending towards the higher values or a significantly important cluster ie. 1 as the value increases. 

Varying A and B together
Prediction Trend Seen: The cluster closes in to lower value class as A and B both increase. This trend shows that the web path becomes more important as the A and B vary simultaneously. 


Varying A and B inversely
Prediction Trend Seen: The cluster is affected by the inverse proportion when A and B are significantly different. The trend leads them towards a low value cluster if the entrances are high but leads to higher value when page views are extremely low. The cluster balances to a central value when the values are significantly different and low. Different is the difference in the numerical value.