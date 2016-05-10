#Bar graph with 4 bars
import matplotlib.pyplot as plt
import numpy as np
N = 4
frequency = (2,8,4,1)

ind = np.arange(N)  
width = 0.5

fig, ax = plt.subplots()
rects1 = ax.bar(ind, frequency, width, color='cyan', yerr=None)

ax.set_xlabel('Range of Heart Beat Measures')
ax.set_ylabel('Frequency of Particpants')
ax.set_title('Bar Graph of Heart Beat Measures for Blues Rock')
ax.set_xticks(ind + width)
ax.set_xticklabels(('60-68', '69.5-77.5', '79-87', '98-106'))

plt.show()
