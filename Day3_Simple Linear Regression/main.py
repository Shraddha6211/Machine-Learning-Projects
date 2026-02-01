import kagglehub
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download latest version (or load cached)
path = kagglehub.dataset_download("parvmodi/cgpa-vs-package-in-lpa")

print("Path to dataset files:", path)

# List files in dataset directory
print(os.listdir(path))
# Load the CSV into df
df = pd.read_csv(os.path.join(path, "placement.csv"))

print(df.head())

plt.scatter(df['cgpa'],df['package'])
plt.xlabel('CGPA')
plt.ylabel('Package (in lpa)')
plt.show()

X = df.iloc[:,0:1]
y = df.iloc[:,-1]
print(y)

# Training and Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2, test_size=0.5)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train.values, y_train.values)
print(lr.predict(X_test.iloc[1].values.reshape(1,1)))
# print(y_test)

# Best Fit Regression line
plt.scatter(df['cgpa'],df['package'])
plt.plot(X_test, lr.predict(X_test), color ='red')
plt.xlabel('CGPA')
plt.ylabel('Package (in lpa)')
plt.show()

print(lr.coef_)
print(lr.intercept_)