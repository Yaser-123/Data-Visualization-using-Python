import matplotlib.pyplot as plt

population_age=[22,55,62,45, 21, 22, 34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_age, bins=bins, histtype = 'bar', rwidth= 0.8)
plt.xlabel('Age group')
plt.ylabel('Number of People')
plt.title('Histogram')

plt.show()