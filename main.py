# import the packages
# data manipulation package
import numpy as np
import pandas as pd 


# data visualization packages 
import matplotlib.pyplot as plt 
import  seaborn as sns 

# model related package 
# logistic regression model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# reading and exploring the dataset
# import dataset 
data=pd.read_csv("diabetes.csv")

# remove the outliers from the column
def remove_outliers(data , columns):
    for column in columns:
        if column in data.columns:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR 
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data 
data = remove_outliers(data, data.columns)

# take the input parameter and make the datafrom for predict 
def inputData():
    print("For correct prediction, please give the following health parameters:\n")

    num = {
        "Pregnancies": [float(input("Pregnancies value: "))],
        "Glucose": [float(input("Glucose level: "))],
        "BloodPressure": [float(input("BloodPressure value: "))],
        "SkinThickness": [float(input("SkinThickness: "))],
        "Insulin": [float(input("Insulin value: "))],
        "BMI": [float(input("BMI value: "))],
        "DiabetesPedigreeFunction": [float(input("DiabetesPedigreeFunction value: "))],
        "Age": [float(input("Patient age: "))]
    }

    ind = pd.DataFrame(num)

    print("\nInput data:")
    print(ind)

    return ind
#check is diabetic or not 
def isDiabtic(x, Score):
    if x==1: 
        print ("Diabetic patient ")
        print("With accuracy Score " ,Score)
    else:
        print ("Not diabetic patient ")
        print("With accuracy Score " ,Score)


# create the x and y variable 
X = data.drop(columns="Outcome")
y = data['Outcome']


# split the data into training and testing 
X_train, X_test, y_train, y_test =train_test_split(X , y ,test_size=0.2, random_state=100)


# standardization or scalling of the data 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# model creation and training 
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

# testing of the model
y_pred = log_reg.predict(X_test_scaled)
print(X_test.shape)
print(type(X_test))
# accuracy of the model
score = accuracy_score(y_test, y_pred)

# new production
new_predict =inputData()
print(new_predict.shape)
print(type(new_predict))
new_pred = log_reg.predict(new_predict.values())
isDiabtic(new_pred, score)

