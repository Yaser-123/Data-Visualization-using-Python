import matplotlib.pyplot as plt
x=[1,1.5, 2, 2.5, 3,3.5,3.6]
y=[7.5,8,8.5,9,9.5,10,10.5]
x1=[8,8.5,9,9.5,10, 10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]

plt.scatter(x,y, label = "High income low saving", c = 'r')
plt.scatter(x1,y1, label = "low income High saving", c = 'b')

plt.xlabel('Saving *100')
plt.ylabel('Income *1000')
plt.title('Scatter Plot')

plt.show()
