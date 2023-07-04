# -*- coding: utf-8 -*-
"""CUSTOMER SEGMENTATION ANALYSIS WITH PYTHON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nCTimPPotgtjUIhg-rhVEyiZxB9zEDqJ
"""

!pip install scikit-learn
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv('Mall_Customers.csv')

# Select the relevant features for segmentation
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Determine the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# Apply K-means clustering with the chosen number of clusters
k = 5  # chosen number of clusters
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
kmeans.fit(X)

# Assign cluster labels to the data points
labels = kmeans.labels_
data['Cluster'] = labels

# Visualize the clusters
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='viridis')
plt.title('Customer Segmentation')
plt.show()