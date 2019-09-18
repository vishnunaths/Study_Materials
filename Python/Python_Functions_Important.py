# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:19:04 2019

@author: kzt9qh
"""
# Pandas, DataFrame
X11_12 = [X11.iloc[i] + X12.iloc[i] for i in range(len(X11))]

# Counting every values
index = pd.Index(X11_12)
index.value_counts()
# Output
0    269268
1     66011
2     10267
dtype: int64

# Use  for checking columns for NaN in a columns
train_dataset.isna().any()

#All Regressors
#Regressor
# Fitting multiple linear regression to the training set
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.linear_model import LinearRegression
Linear_regressor = LinearRegression()
Linear_regressor.fit(X_train, y_train)

# Predicting the test results
y_pred = Linear_regressor.predict(X_test)

print('Linear Regression')
r2_score = r2_score(y_test, y_pred, sample_weight=None)
print(r2_score)

mean_absolute_error = mean_absolute_error(y_test, y_pred, sample_weight=None)
print(mean_absolute_error)

# Fitting polynomial regression on the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
poly_reg.fit(X_train,y_train)

# Predicting the test results
y_pred = poly_reg.predict(X_test)

print('Polynomial Regression')
r2_score = r2_score(y_test, y_pred, sample_weight=None)
print(r2_score)

mean_absolute_error = mean_absolute_error(y_test, y_pred, sample_weight=None)
print(mean_absolute_error)

# Fitting SVM on the dataset
from sklearn.svm import SVR
SVR_regressor = SVR(kernel = 'rbf') 
SVR_regressor.fit(X, y)

# Predicting the test results
y_pred = SVR_regressor.predict(X_test)

print('SVR Regressor')
r2_score = r2_score(y_test, y_pred, sample_weight=None)
print(r2_score)

mean_absolute_error = mean_absolute_error(y_test, y_pred, sample_weight=None)
print(mean_absolute_error)

# Fitting the Decision Tree Model to the dataset
from sklearn.tree import DecisionTreeRegressor
DT_regressor = DecisionTreeRegressor()
DT_regressor.fit(X,y)


# Predicting a new result
y_pred = DT_regressor.predict(X_test)

print('DT Regressor')
r2_score = r2_score(y_test, y_pred, sample_weight=None)
print(r2_score)

mean_absolute_error = mean_absolute_error(y_test, y_pred, sample_weight=None)
print(mean_absolute_error)

# Fitting the Random Forest Regression Model to the dataset
from sklearn.ensemble import RandomForestRegressor
RF_regressor = RandomForestRegressor(n_estimators=300, random_state=0)
RF_regressor.fit(X,y)

# Predicting a new result
y_pred = RF_regressor.predict(X_test)

print('RF Regressor')
r2_score = r2_score(y_test, y_pred, sample_weight=None)
print(r2_score)

mean_absolute_error = mean_absolute_error(y_test, y_pred, sample_weight=None)
print(mean_absolute_error)

# to check number of element in a list 
import collections
counter0=collections.Counter(trainList0)
print(counter0)

# Data preprocessing
# Function for Data preprocesing
def dataEncoding(datasetName,colDetail,isNumeric=0,LabelEnc_req=1,OneHot_req=1):
    """Function to convert column into machine learning format
    variable = isNumeric, LabelEnc_req,OneHot_req"""
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    if isNumeric == 0:
        X = datasetName.iloc[:,colDetail]
        X = X.values.reshape((len(X),1))
        if LabelEnc_req == 1 and OneHot_req == 1:
            LabEnc_X = LabelEncoder()
            LabEnc_X = LabEnc_X.fit(X)
            X = LabEnc_X.transform(X) 
            X = X.reshape((len(X),1))
            onehotEnc_X = OneHotEncoder(categorical_features = [0])
            onehotEnc_X = onehotEnc_X.fit(X)
            X = onehotEnc_X.transform(X).toarray()
            X = pd.DataFrame(X)
            X = X.values
        else:
            LabEnc_X = LabelEncoder()
            LabEnc_X = LabEnc_X.fit(X)
            X = LabEnc_X.transform(X) 
            X = X.reshape((len(X),1))
    else:
        X = datasetName.iloc[:,colDetail]
        X = X.values
        sc_X = StandardScaler()
        X = sc_X.fit_transform(X)
    return X
