import numpy as np
import matplotlib.pyplot as plt

bpm = (73.33333, 78,  71.6)
times = (.25, .5, .75)

line1 = plt.plot(times, bpm, marker='o', linestyle='-.', color='purple', label='Hard Rock')

bpm = (73.33333-9.16255, 73.33333+9.16255)
times = (.25, .25)

line2 = plt.plot(times, bpm, marker='_', linestyle='-', color='black', label='Standard Deviation')

bpm = (78-18.87553, 78+18.87553)
times = (.5, .5)

plt.plot(times, bpm, marker='_', linestyle='-', color='black')

bpm = (71.6-8.08084, 71.6+8.08084)
times = (.75, 0.75)

plt.plot(times, bpm, marker='_', linestyle='-', color='black')

plt.axis([0.2, 0.8, 55, 100])
plt.title('Average Heart Beat While Listening to Hard Rock\nLine Plot')
plt.ylabel('Average Measure of Heart Beat(bpm)')
plt.xlabel('Duration of song(proportion)')
plt.legend()

plt.show()
