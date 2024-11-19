import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # X-axis values
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # Y-axis values
z = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])  # Values to control color (e.g., third variable)

# Create a scatter plot with gradient colors based on the z values
scatter = plt.scatter(x, y, c=z, cmap='viridis', s=100, marker='o', edgecolors='black')
plt.xticks(range(min(x), max(x) + 1))  # x ticks from min to max of x values (inclusive)
plt.yticks(range(int(min(y)), int(max(y)) + 2))

# Adding a color bar
plt.colorbar(scatter, label='Z value (Color intensity)')

# Adding title and labels
plt.title('Complex Scatter Plot with Gradient Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
