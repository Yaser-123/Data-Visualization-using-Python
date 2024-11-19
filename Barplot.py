import matplotlib.pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20], label="BMW", width=0.5, color='b')
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60], label="Audi", width=0.5, color='r')

plt.legend(loc = 'upper right')
plt.xlabel('Car')
plt.ylabel('Price')
plt.show()