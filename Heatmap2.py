import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

data = np.random.randint(low= 1, high= 100, size= (10,10))

sn.heatmap(data, annot= True)

plt.show()