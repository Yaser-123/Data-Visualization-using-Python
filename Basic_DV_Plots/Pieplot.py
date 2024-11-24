import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# Calculate total time for each activity
total_sleeping = sum(sleeping)
total_eating = sum(eating)
total_working = sum(working)
total_playing = sum(playing)

# Pie chart data
slices = [total_sleeping, total_eating, total_working, total_playing]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']  # Colors for the slices

# Create Pie Chart
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True, 
        explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

# Title
plt.title('Pie Plot Based on Given Data')

# Show the plot
plt.show()
