import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specify the file path to the TSV file containing the RMSD matrix with row and column names
tsv_file_path = "/Users/adrianahernandezgonzalez/Documents/YarovLab/repositories/repo-MultimerAnalysis/similarity_matrix.tsv"

# Load the RMSD matrix with row and column names from the TSV file
df = pd.read_csv(tsv_file_path, sep='\t', index_col=0)

# Create a heatmap using Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the figure size as needed
cax = ax.matshow(df, cmap='YlGn', interpolation='nearest')

# Set labels for the rows and columns
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

# Rotate the column labels
ax.set_xticklabels(df.columns, rotation=90)#, ha="right", rotation_mode="anchor")

# Rotate and align the reference labels vertically
ref_labels = df.index
ax.set_yticks(np.arange(len(ref_labels)))
ax.set_yticklabels(ref_labels, va='center', fontsize=8)
ax.tick_params(axis='y', pad=20)  # Adjust the padding as needed for spacing

# Add a colorbar
plt.colorbar(cax, label='RMSD')

# Set the title
plt.title('RMSD Heatmap')

# Show the heatmap
plt.show()
