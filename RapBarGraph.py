# a bar plot
import numpy as np
import matplotlib.pyplot as plt

N = 5
frequency = (1, 4, 4, 1, 5)

ind = np.arange(N)  # the x locations for the groups
width = 0.35      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, frequency, width, color='maroon', yerr=None)

# makes text for labels, title and axes ticks
ax.set_xlabel('Average Measure of Heart Beat(bpm)')
ax.set_ylabel('Frequency of Participants')
ax.set_title('Average Measure of Heart Beat - Rap\nBar Graph')
ax.set_xticks(ind + width)
ax.set_xticklabels(('59-65.2', '65.3-71.4', '71.5-77.6', '77.7-83.8', '83.9-90'))


plt.show()
