import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'],  labels=['Sleeping', 'Eating', 'Working', 'Playing'])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Stack Plot")
plt.legend(loc='upper right')
plt.show()

