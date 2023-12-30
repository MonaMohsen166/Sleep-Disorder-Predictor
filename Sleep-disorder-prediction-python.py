# -*- coding: utf-8 -*-
"""Dotpy Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wUL6W-tpQ2aKUVUSTd7iw8xVQ8CHUGiW
"""

import pandas as pd
import sklearn
data=pd.read_csv('/content/Sleep_health_and_lifestyle_dataset.csv')
data.head()

x=data.iloc[:,1:12]
y=data.iloc[:,12:13]
x.head()

x=x.replace(to_replace = ['Male','Female'], value=[1,0])
x.head()

from sklearn.preprocessing import MinMaxScaler
scale=MinMaxScaler()
scale2=MinMaxScaler(feature_range=(0, 2))
x['Age'] = scale.fit_transform(x[['Age']])
x['Quality of Sleep'] = scale.fit_transform(x[['Quality of Sleep']])
x['Physical Activity Level'] = scale.fit_transform(x[['Physical Activity Level']])
x['Stress Level'] = scale.fit_transform(x[['Stress Level']])
x['Heart Rate'] = scale.fit_transform(x[['Heart Rate']])
x['Daily Steps'] = scale2.fit_transform(x[['Daily Steps']])
x.head()
x['Sleep Duration'] = scale.fit_transform(x[['Sleep Duration']])
x.head()

x=pd.get_dummies(x)
x.head()

data.isnull().sum()

y.head()

y=y.replace(to_replace = ['None','Insomnia','Sleep Apnea'], value=[0,1,2])
y.head()

x_corr=x.iloc[:,0:8]
x_corr.head()

import pandas as pd

# Create a DataFrame with a column containing values
# data = {'ColumnA': ['A', 'B', 'C', 'B', 'D']}
df = pd.DataFrame(data)

# Get all entries
all_entries = df['Occupation'].tolist()

# Create a set to keep track of seen entries
seen_entries = set()

# Iterate through the entries and print only if not seen before
for entry in all_entries:
    if entry not in seen_entries:
        seen_entries.add(entry)
        print(entry)

concatenated_data = pd.concat([x_corr, y], axis=1)
concatenated_data.head()

import seaborn as sb
dataplot=sb.heatmap(concatenated_data.corr(),annot=True)

del x['Daily Steps']

x.head()

y.head()

"""#Training, Testing, and Splitting"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

"""#Modelling
#SVC
"""

from sklearn.svm import SVC

model=SVC()

from sklearn.model_selection import GridSearchCV
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': [0.001, 0.01, 0.1, 1, 'scale', 'auto'],
}

grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
grid_search.fit(x_train, y_train)
best_params = grid_search.best_params_

print ("best parameters are:",best_params)

optimized_model =  SVC(
    C=0.01,                # Regularization parameter
    gamma=1,           # Kernel coefficient
    kernel='poly',         # Kernel type
          # Tolerance for stopping criterion
)

optimized_model.fit(x_train,y_train)

optimized_model.score(x_train,y_train)

optimized_model.score(x_test,y_test)

from sklearn.metrics import f1_score
y_pred2 = optimized_model.predict(x_test)
f1 = f1_score(y_test, y_pred2, average='weighted')

f1

import pickle
# Save the model to a file
with open('weights.sav', 'wb') as file:
    pickle.dump(model, file)

model=pickle.load(open('weights.sav', 'rb'))