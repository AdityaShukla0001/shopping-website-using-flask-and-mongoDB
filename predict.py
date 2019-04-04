# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


dataset = pd.read_csv('tractors_pred.csv')

x= dataset.iloc[:, [0,1,2,3,4,5]].values
y= dataset.iloc[:, 6].values

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state = 30)

classifier = KNeighborsClassifier()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)
y_pred
