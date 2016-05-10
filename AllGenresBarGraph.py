# a bar plot
import numpy as np
import matplotlib.pyplot as plt

N = 5
bpm = (77.16, 75.27, 76.06, 74.57, 77.11)
StdDev = (22.3492, 15.8264, 17.9604, 22.4842, 17.122)

ind = np.arange(N)  # the x locations for the groups
width = 0.35      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, bpm, width, color='red', yerr=StdDev)

# makes text for labels, title and axes ticks
ax.set_xlabel('Genre of Music')
ax.set_ylabel('Average Measure of Heart Beat(bpm)')
ax.set_title('Average Measure of Heart Beat - All Genres\nBar Graph')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Classical', 'Jazz', 'Rap', 'Hard Rock', 'Blues Rock'))


plt.show()
