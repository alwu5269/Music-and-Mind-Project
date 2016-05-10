#Bar graph 
%matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 5
frequency = (2,8,4,0,1)

ind = np.arange(N)  
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind, frequency, width, color='blue', yerr=None)

ax.set_xlabel('Range of Heart Beat Measures')
ax.set_ylabel('Frequency of Particpants')
ax.set_title('Bar Graph of Heart Beat Measures for Blues Rock')
ax.set_xticks(ind + width)
