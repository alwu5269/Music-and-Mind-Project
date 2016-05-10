import matplotlib.pyplot as plt
import numpy as np

N = 4
frequency = (3,7,4,1)

ind = np.arange(N)  
width = 0.5

fig, ax = plt.subplots()
rects1 = ax.bar(ind, frequency, width, color='purple', yerr=None)

ax.set_xlabel('Range of Heart Beat Measures')
ax.set_ylabel('Frequency of Participants')
ax.set_title('Bar Graph of Heart Beat Measures for Hard Rock')
ax.set_xticks(ind + width)
ax.set_xticklabels(('59-66', '69-77', '80-87', '90-97'))

plt.show()
