import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('datafile.csv')
X=dataset.iloc[:,-1].values
Y=dataset.iloc[:,0].values
Y1=Y
print(type(X))

Y=pd.get_dummies(Y)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
Y=np.array(ct.fit_transform(Y))
#print(Y1,Y)
import array
X=X.reshape(-1,1)
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)

classifier.fit(x_train,y_train)

print(classifier.predict([[9.83]]))