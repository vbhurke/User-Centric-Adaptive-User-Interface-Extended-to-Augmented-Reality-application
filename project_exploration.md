#### SER594: Exploratory Data Munging and Visualization
#### User-Centric Adaptive User Interface for Augmented Reality application 
#### Viresh Bhurke
#### 10-18-2023

## Basic Questions
Dataset Author(s): 
Information Services (Government Baton Rogue) (You can check it under the section of 'Data Provided' on the webpage)
Contact : opendata@brgov.com.

Dataset Construction Date: 
The Dataset is updated daily (In this project I will be using data file of 15 October 2023)

Dataset Record Count: 
The dataset on this date has 52302 rows (might change excluding header). This may change assuming when you download the dataset. It has 10 columns which will be described in the next section. 

Dataset Field Meanings:
WEBSITE : This field contains the websites of open baton rougue. The Open Data BR provides names of main websites. (Qualitative)
YEAR : The year the data of the fields was  collected. (Quantitative)
PAGE PATH : The path and filename of the website.  (Qualitative)
PAGE URL : The complete url of the page the row contains data about.  (Qualitative)
PAGE VIEWS : The number of times the page was viewed. (Quantitative)
UNIQUE VIEWS : The unique views are the unique users viewing the url. (Quantitative)
AVERAGE TIME ON PAGE (SECONDS) : The average seconds spent on the webpage by viewers. (Quantitative)
ENTRANCES : This field shows number of viwers who entered the website from the pages. (Quantitative)
BOUNCE RATE (%) : This is the rate at which viewers entered but did not interact on it. (Quantitative)
EXIT RATE (%) : The rate of users that viwed the page and exited. (Quantitative)

Dataset File Hash(es): 
link : https://data.brla.gov/Government/Website-Analytics/n9u7-h9i7
(To download the dataset click on Export -> CSV. The name of the file will change based on what date you dowload the date will come on the last _2023...)
Website_Analytics_20231017 : a2c56997afafdc22596a113eab9523b9

Interpretable Records
Record 1
Raw Data: WEBSITE


Interpretation: The data contains the websites which are used by the public to view data. This can tell me how many distinct main websites are available in the data set. We can find out the most used website or the most recorded website on the basis. This data is highly meaningfull as it identifies the unique websites

Record 2
Raw Data: PAGE PATH
This is the filename or path of a specific page viewed on the website of the main page. 
Interpretation: This can help me understand the requirement of which page is most common and least common to decide which page should be given as a header or easily accesibleon the main page for viewers. This data is meaningfull to show information of the specific file of webpage which the data is about.

Record 3
Raw Data: PAGE VIEWS
This contains the number of times the specific file from the page url was viewed.
Interpretation: This can help me understand number of times the page was viewed and how often the page file is viewed. The importance and frquency of requirement of this data can be understood. It can also show the trend in the usage of the page. This is a meanigful data which indicates page views for wepage. 

Record 4
Raw Data: UNIQUE VIEWS
This contains the number of times a unique user viewed the website.
Interpretation: This can help me understand number of times the page was viewed by a unique user. This will help us understand the importance of the page for new users and its capability to attract new users. This data is meaningful for the uniqueness of the viewers.

Record 5
Raw Data: AVERAGE TIME ON PAGE (SECONDS)
This contains the amount of time a user spends on the page file.
Interpretation: This can help me understand if the website has high traffic and impact as user spend more or less time. This will also show if the description of the link clearly describes it contains and attracts appropriate users. Is the link description accurate?

Record 6
Raw Data: ENTRANCES
This contains the amount of time a user enters the page file from the page website.
Interpretation: This can help me understand where the entrances are occuring from and increase the priority of the link in the website. 

Record 7
Raw Data: BOUNCE RATE (%)
This contains the rate at which users leave without interacting with the website.
Interpretation: The bounce rate will help identify if the website is usefull or misleading the users. This will also help identify miss clicks and give more precise data of the views. 

Record 8
Raw Data: EXIT RATE (%)
This contains the rate at which users leave the website.
Interpretation: The exit rate will help identify if the webpage was left abruptly or traversed within the website to different webpage from the website.

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


Background Domain Knowledge
In an Adaptive User Interface, it is important to identify the user data and impact of features on users. In user interface the user should be easily be able to traverse through the webpages and links and come across the required or desired information. In order to make this easy it is important to take into consideration of relation of sites and how users tend to interact with them. You will notice the use of terms like 'button clicks' in the initial project document, the button clicks are linked to the links and similar to traversing to a webpage. In User Experience it is necessary to identify how the user is interacting with the product and build on the consensus of the data.
The study should be user centric and work to identify trends along with user behavior. It is thus natural to say that increasing the ease of use and content prioritization will develop and grow the software faster. The User Experience focuses on various factors of usability, interaction design, structure, findability and accessibility. The data for such users on a webpage can be mapped to an AR webpage which will have similar structure. Augmented application of such 2D webpages will have similar traversal and interactions, thus the data can be improvised to implement in an AR version of the application. 
Note :  The further scope will try to implement it in AR version. The user data for personal users such as time logs are private and not ethical for collecting. The data used does not contain such data but can be used to make the interface adaptive based on all users as general too. This technique can be used for AR applications as understood from [2] and [3].

"References : 

[1] Mahdi H. Miraz, Maaruf Ali, Peter S. Excell,
    "Adaptive user interfaces and universal usability through plasticity of user interface design,
    Computer Science Review, Volume 40, 2021, 100363", ISSN 1574-0137,
    https://doi.org/10.1016/j.cosrev.2021.100363.

[2] Julier, Simon & Livingston, Mark & Edward, Jessica & Ii, Swan & Baillot, Yohan & Brown, Dennis. (2004). "Adaptive User Interfaces in Augmented Reality".

[3] M. Nivethika, I. Vithiya, S. Anntharshika and S. Deegalla, "Personalized and adaptive user interface framework for mobile application," 2013 International          Conference on Advances in Computing, Communications and Informatics (ICACCI), Mysore, India, 2013, pp. 1913-1918, doi: 10.1109/ICACCI.2013.6637474.

[4]"Braham A, Buendía F, Khemaja M, Gargouri F. Generation of Adaptive Mobile Applications Based on Design Patterns for User Interfaces. Proceedings. 2019; 31(1):19." https://doi.org/10.3390/proceedings2019031019

[5] Link : 
What is User Experience : https://www.liferay.com/resources/l/user-experience#:~:text=User%20experience%20describes%20how%20people,interface%2C%20usability%20and%20user%20research.

[6] Book : "Adaptive User Interfaces edited by Dermot Browne" (describes what is required for adaptive user interface and the impact of it on the product)



Data Transformation
Transformation 1 
Description: WEBSITES : The data is checked to be string. In this section the website has been split with ('.'). Then the 'www' term is removed from list. This list is then combined. 

Soundness Justification: This is done as some similar websites data is stored with some websites missing 'www' term. This will generalize and make it easy to identify these sites. Note: The webpage is stored in same format as given in processed file. The value is then stored as string. 

Transformation 2
Description: YEAR : Store it as int value. Check if it can be converted to int. The data needs to be an integer year. 

Soundness Justification: The year is an integer value which needs to be checked and converted to int. The data is then stored as an integer value.  

Transformation 3
Description: PAGE PATH  : It stores paths separated by '\'. The path is split by '\' and saved in list.

Soundness Justification: The list contains path of the webpages, in order to identify the path of the webpage(category) it is necessary to get the name of the path.

Transformation 4
Description: PAGE VIEWS, UNIQUE VIEWS, ENTRANCES  :  This is checked to be an integer. If the value is a string (which can be null, na) it is given as 0

Soundness Justification: It stores number which is count. Thus the data is verified to be an integer. The garbage value is stored as 0, as it cannot be linked to previous entry and can also mean the webpage had no new entries.

Transformation 5
Description: AVERAGE TIME ON PAGE (SECONDS)  :  This is checked to be a float. If the value is a string (which can be null, na) it is given as 0

Soundness Justification: It is average of time and thus is a floating integer. If the value is not given it can be converted to 0 as the time is not specified in previous entries and is unique. If it is unable to convert to float it is stored as 0.

Transformation 6
Description: BOUNCE RATE (%), EXIT RATE (%) :  This is checked to be a float. The value is checked to be float between 0-100.

Soundness Justification: It is checked to be a valid percentage. It is related to path of the file and not just the website. The value can be generalized to 0 if it is invalid, this 
(duplicate above as many times as needed; remove this line when done)


Visualization
Visual 1
Analysis: Image_Websites
This histogram describes the histogram of frequency of data of websites. This visualization soundly showcases the frequency of the unique websites with their datasets. This will help identify which website has most entries and point to the direction of which website data should be explored. It can identify important websites or atleast point towards it.

Visual 2
Analysis: Image_Websites ('PAGE VIEWS' vs 'UNIQUE VIEWS')
This type of scatter plots for specific websites is unique for each website data. This will help me look at the pages with unique views and page views. The plot will tell if the webpage attracts new users or is required for daily viewing. This will help me identify if webpage focuses on attracting new users. The impact of the webpage for the general need to be advertised as main to attract users can be decided. The user interface will show this in the top suggestions for attracting new users.

Visual 3
Analysis: Image_Websites ('PATH' vs 'UNIQUE VIEWS')
This is the bar plot for all websites which shows the pages of the website with path and unique views. The webpages of specific websites which attract most unique viewers. This bar plot identifies the top paths of the webpage, this can be used to decide what links the website should contain to make it easier for navigation. This will also improve the structure and design. 

Visual 4
Analysis: Image_Websites ('PAGE VIEWS' vs 'ENTRANCES')
These scatter plots for each website show various page entries for the users to the page views. The scatter plot will identify from which set of pages the user entered the page compared to the views of the page. This will identify the navigation pattern. A low level indicates such link should be removed or is not required. The more the both values are the better the navigation is. This will also validate if existing linking(buttons on page) are valid. 

Visual 5
Analysis: Image_Websites ('PAGE VIEWS' vs 'AVERAGE TIME ON PAGE (SECONDS)')
These scatter plot will identify the relation of page views with time spent on them. This will tell which page has higher impact and should be prioritized. The time for each webpage is spent on it by users, both higher indicates making it easier to navigate will make the users easy to use the webpage. Many users who are unable to find this page may also find it easier after changing the interface. This will increase the interaction of users on the webpages. 