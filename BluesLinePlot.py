#line graph with standard deviation
import matplotlib.pyplot as plt
import numpy as np

bpm= (78.6, 74.93333, 75.1333)
times = (.25, .5, .75)

line1 = plt.plot(times, bpm, marker='o', linestyle='-.', color='cyan', label='Blues Rock')

bpm= (78.6-14.68948, 78.6+14.68948)
times = (.25, .25)

line2 = plt.plot(times, bpm, marker='_', linestyle='-', color='black', label= 'Standard Deviation')

bpm= (74.9333-8.63106, 74.9333+8.63106)
times = (0.5, 0.5)

plt.plot(times, bpm, marker='_', linestyle='-', color='black')

bpm= (75.133-10.30164, 75.133+10.30164)
times = (0.75, 0.75)

plt.plot(times, bpm, marker='_', linestyle='-', color='black')

plt.axis([0.2, 0.8, 60, 100])
plt.title('Average Heart Beat While Listening to Blues Rock\nLine Plot')
plt.ylabel('Average Measure of Heart Beat(bpm)')
plt.xlabel('Duration of Song(proportion)')
plt.legend()

plt.show()
