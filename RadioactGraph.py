import numpy as np
import matplotlib.pyplot as plt

Data = np.genfromtxt('RadioactGraph.txt')

x = Data[:,0]
y = Data[:,1]

plt.plot(x, y, color = 'c')
plt.grid()
plt.savefig('Graph.png')




