"# major-project-ca-1-drug-review-9-10-11-12"


Inthis project we will be using the drug review dataset from mci to predict the ratings from the reviews given by users 

About Dateset : -
The dataset consist of sentences gathered reviews from various medical websites and other health resources . Each row would ideally consist of a single sentence and have a corresponding sentiment attach to it about the medicinal drug, which would be either Negative, Positive or Neutral. There are more than 20,000 sentences and they have been manually tagged.

Step by Step approach :-

Step 1: Importing all necessary modules
Importing the libraries like tkinter,numpy,sklearn,nltk, matplotlib etc

Step 2: Import Dataset
Importing dataset taken from https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29

Step 3: Lets have a look at our data set
Looking at the data using functions like head,colunm,row,etc.

Step 4: We have y in form of categorical data we need to convert it into quantitative data

Step 5: Cleaning or data Preprocessing

Step 5.1: Tokenization
Step 5.2: Stemming
Step 5.3: Lemmatization
Step 5.4: Sentiment Analysis

Step 6: feature extraction(using TfidfVectorizer)

Step 7: Split data set into training and testing sets

Step 8: Creating classifier and fitting data in classifier

Step 9: Perform Prediction
Step 10: Evaluation
Checking the accuracy scorce of the classifiers.

step 11: GUI ,In gui we created five window like home_page, to calculate the accuracy of our training model, to calculate confusion matrix, to calculate bar plots ,box plots and word which we have used. 
