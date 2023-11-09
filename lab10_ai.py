#!/usr/bin/env python
# coding: utf-8

# # Using KNN Algorithm to predict if a person will have diabetes or not

# #### A supervised machine learning algorithm (as opposed to an unsupervised machine learning algorithm) is one that relies on labeled input data to learn a function that produces an appropriate output when given new unlabeled data.
# #### Supervised machine learning algorithms are used to solve classification or regression problems.
# #### classification - 0/1

# ### importing libraries

import numpy as np
import pandas as pd
import copy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### loading the dataset

data = pd.read_csv('diabetes.csv')


# #### Replace columns like [Gluscose,BloodPressure,SkinThickness,BMI,Insulin] with Zero as values with mean of respective column

zero_not_accepted = ['Glucose','BloodPressure','SkinThickness','BMI','Insulin']

for col in zero_not_accepted:
    data[col]= data[col].replace(0,np.NaN)
    mean = int(data[col].mean(skipna=True))
    data[col] = data[col].replace(np.NaN,mean)


# ### extracting independent variables

X = data.iloc[:,0:8]


# ### extracting dependent variable

y = data.iloc[:,8]


# ### Explorning data to know relation before processing

sns.heatmap(data.corr())


# ### splitting dataset into training and testing set

y = np.array(data['Outcome'])
Data=copy.deepcopy(data)
del Data['Outcome']
X = np.array(Data)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
print (" Training Data Set Dimensions=", X_train.shape, "Training True Class labels dimensions", y_train.shape) 
print (" Test Data Set Dimensions=", X_test.shape, "Test True Class labels dimensions", y_test.shape)  


# Implementing KNN

def Euclidian_Distance(pred,actual):
    #distance = √ a2 + b2 
    distance = np.sqrt(np.sum(np.square(pred - actual)))
    return distance


def getKNearest(distances,k):
    # Sort on the basis of distances and label
    # Get top k distances from the list of values
    return distances[np.argsort(distances[:,1])][:k]


def getClasses(k_nearest):
    # From the tuples list - k_nearest, fetch the classes only and return their list
    classes = [x[2] for x in k_nearest]
    return classes


def getMaxClass(classes):
    # Get the Max Class using np unique to get the count of each class
    unique, counts = np.unique(classes, return_counts=True)
    return unique[np.argmax(counts)]


def KNN(X_train, X_test, y_train, k):
    # make list pred
    pred = []
    # Iterate over the entire test set
    for i in range(len(X_test)):
        # make an info list 
        info = []
        # Iterate over the etire training set
        for j in range(len(X_train)):
            # Calculate the euclidean Distance of test and train
            euclidean_dist = Euclidian_Distance(X_test[i], X_train[j])
            # add eucl. dist and the label to the info list #(you will get the label from the y_train)
            info.append([euclidean_dist, j, y_train[j]])
        # thus