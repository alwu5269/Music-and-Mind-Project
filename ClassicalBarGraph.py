import matplotlib.pyplot as plt
import numpy as np

N = 5
frequency = (3,8,2,1,1,)

ind = np.arange(N)  
width = 0.48

fig, ax = plt.subplots()
rects1 = ax.bar(ind, frequency, width, color='black', yerr=None)

ax.set_xlabel('Range of Heart Beat Measures')
ax.set_ylabel('Frequency of Participants')
ax.set_title('Bar Graph of Heart Beat Measures for Classical')
ax.set_xticks(ind + width)
ax.set_xticklabels(('60-69.5', '70-79.5', '80-89.5', '90- 99.5', '100-100.5'))


plt.show()
