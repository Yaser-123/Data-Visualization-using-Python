import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
bins = [1, 2, 3, 4, 5, 6]

# Histogram with rwidth
plt.hist(data, bins=bins, rwidth=0.8, color='r', edgecolor='none')
plt.gca().set_facecolor('skyblue')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with rwidth')

plt.show()
