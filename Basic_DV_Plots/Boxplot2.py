import numpy as np
import matplotlib.pyplot as plt

# Generate data from normal distributions
data1 = np.random.normal(100, 20, 200)  # Mean=100, Std Dev=20
data2 = np.random.normal(90, 15, 200)   # Mean=90, Std Dev=15
data3 = np.random.normal(110, 25, 200)  # Mean=110, Std Dev=25

# Create a box plot for the datasets
data = [data1, data2, data3]  # Combine datasets into a list
plt.boxplot(data, labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Add title and labels
plt.title('Box Plot for Multiple Datasets')
plt.ylabel('Values')

# Show the plot
plt.show()
