# Import Dependencies
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the Wine Dataset
wine=load_wine()
X=wine.data
y=wine.target

# Split the Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train the KNN Model
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Make Predictions & Check Accuracy
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))