import json
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Load the data
with open('response.json') as f:
    data = json.load(f)

x_values = []
y_values = []

# Extract x and y coordinates
for annotation in data['responses'][0]['textAnnotations']:
    vertices = annotation['boundingPoly']['vertices']
    for vertex in vertices:
        x_values.append(vertex['x'])
        y_values.append((vertices[0]['y'] + vertices[2]['y']) / 2)  # Taking average of y-coordinates of first and third vertex

# Reshape data for scikit-learn
x_values = np.array(x_values).reshape(-1, 1)
y_values = np.array(y_values).reshape(-1, 1)

# Number of clusters
k = 5

# Create and fit a KMeans model for x coordinates
kmeans_x = KMeans(n_clusters=5, random_state=0).fit(x_values)
# Get the cluster centers for x coordinates
x_cluster_centers = kmeans_x.cluster_centers_
# Get the labels for each point for x coordinates
x_labels = kmeans_x.labels_

# Create and fit a KMeans model for y coordinates
kmeans_y = KMeans(n_clusters=10, random_state=0).fit(y_values)
# Get the cluster centers for y coordinates
y_cluster_centers = kmeans_y.cluster_centers_
# Get the labels for each point for y coordinates
y_labels = kmeans_y.labels_

print(f"X Cluster centers: \n {x_cluster_centers}")
print(f"X Labels: \n {x_labels}")

print(f"Y Cluster centers: \n {y_cluster_centers}")
print(f"Y Labels: \n {y_labels}")

# Plot the x coordinates
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(x_values, np.zeros_like(x_values), c=x_labels)
plt.scatter(x_cluster_centers, np.zeros_like(x_cluster_centers), c='red', marker='x')  # Plot the centers
plt.title('K-Means Clustering of x coordinates')

# Plot the y coordinates
plt.subplot(122)
plt.scatter(y_values, np.zeros_like(y_values), c=y_labels)
plt.scatter(y_cluster_centers, np.zeros_like(y_cluster_centers), c='red', marker='x')  # Plot the centers
plt.title('K-Means Clustering of y coordinates')

plt.show()