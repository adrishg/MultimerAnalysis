# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform

# Load your RMSD data into a DataFrame
# Example:
tsv_file_path = "/Users/adrianahernandezgonzalez/Documents/YarovLab/repositories/repo-MultimerAnalysis/similarity_matrix_NMRvsNMR.tsv"
df = pd.read_csv(tsv_file_path, sep='\t', index_col=0)

# Calculate the pairwise distance matrix from the DataFrame
distance_matrix = squareform(df.values)

# Perform hierarchical clustering
linkage_matrix = hierarchy.linkage(distance_matrix, method='average')

# Create a dendrogram
dendrogram = hierarchy.dendrogram(linkage_matrix, labels=df.index, orientation='left')

# Optionally, you can adjust the figure size and labels for better readability
plt.figure(figsize=(10, 8))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("RMSD Distance")
plt.ylabel("Protein Labels")

# Show the dendrogram
plt.show()
