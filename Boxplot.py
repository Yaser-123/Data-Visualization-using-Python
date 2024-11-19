import matplotlib.pyplot as plt

# Sample data
data = [
    [7, 8, 6, 11, 7],  # Sleeping hours
    [2, 3, 4, 3, 2],   # Eating hours
    [7, 8, 7, 2, 2],   # Working hours
    [8, 5, 7, 8, 13]   # Playing hours
]

# Create box plot with simple colors
plt.boxplot(data, 
            labels=['Sleeping', 'Eating', 'Working', 'Playing'], 
            boxprops=dict(color='black'),    # Set the box edge color
            whiskerprops=dict(color='blue'), # Set whiskers color
            flierprops=dict(markerfacecolor='red', marker='o'),  # Outlier color
            medianprops=dict(color='green') # Set median line color
           )

plt.gca().set_facecolor('skyblue')

# Title and labels
plt.title('Colorful Box Plot of Activity Hours')
plt.xlabel('Activity')
plt.ylabel('Hours')

# Show the plot
plt.show()
