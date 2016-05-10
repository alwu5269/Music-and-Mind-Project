import matplotlib.pyplot as plt

bpm = (77, 74.33333, 75)
times = (.25, .5, .75)

line1 = plt.plot(times, bpm, marker='o', linestyle='-.', color='black', label = 'Jazz')

bpm = (77-9.77606, 77+9.77606)
times = (.25, .25)

line2 = plt.plot(times, bpm, marker='_', linestyle='-', color='blue', label = 'Standard Deviation')

bpm = (74.33333-8.61615, 74.33333+8.61615)
times = (.5, .5)

plt.plot(times, bpm, marker='_', linestyle='-', color='blue')

bpm = (75-8.98146, 75+8.981468)
times = (.75, .75)

plt.plot(times, bpm, marker='_', linestyle='-', color='blue')

plt.axis([0.2, 0.8, 60, 100])
plt.title('Average Measure of Heart Beat - Jazz\nLine Plot')
plt.ylabel('Average Measure of Heart Beat(bpm)')
plt.xlabel('Duration of song(proportion)')
plt.legend()

plt.show()
