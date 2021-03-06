import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


#------------------------------Reading csv file into dataframe------------------------------
df=pd.read_csv(r"C:\Users\user\Desktop\CRIME\Dataset\data.csv")
print("Data loaded sucessfully................")
df['timestamp']=pd.to_datetime(df.timestamp,errors='coerce')

#-----------------------------encoding the categorical data---------------------------------
df['year'] = df['timestamp'].dt.year 
df['month'] = df['timestamp'].dt.month 
df['day'] = df['timestamp'].dt.day 
df['hour'] = df['timestamp'].dt.hour 
df['minute'] = df['timestamp'].dt.minute

df=df.dropna(axis=0)
print("Encoding of data is done.........")
df.dtypes

x=df.iloc[:,[7,8,9,10,11,12,13]].values
y=df.iloc[:,[1,2,3,4,5,6]].values

#------------------------------splitting data into testing and training data----------------
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=9)
print("20 percent of data has be splitted to test data....")

"""
#---------------------------------------KNN classifier -------------------------------------
model=KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(metrics.accuracy_score(y_test,y_pred)*100)
"""
#------------------------------------Desicion Tree classifier--------------------------------

modeldt=DecisionTreeClassifier(criterion='entropy')#ginni
modeldt.fit(x_train,y_train)
y_preddt=modeldt.predict(x_test)

print('Decisiontree',metrics.accuracy_score(y_test,y_preddt)*100)


#----------------------------Saving the model into sav file for reuse-------------------------

import pickle
filename = 'model.sav'
pickle.dump(modeldt, open(filename, 'wb'))
print("Model saved sucessfully........")
