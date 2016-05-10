import matplotlib.pyplot as plt

bpm = (79.06667, 75.53333, 86.25)
times = (.25, .5, .75)

plt.plot(times, bpm, marker='o', linestyle='--', color='black', label='Classical')

bpm = (77, 74.33333, 75)

plt.plot(times, bpm, marker='x', linestyle='-', color='m', label='Jazz')

bpm = (77.73333, 74.93333, 77.4)

plt.plot(times, bpm, linestyle='-', color='r', label='Rap')

bpm = (73.33333, 78, 71.6)

plt.plot(times, bpm, marker='*', linestyle='-.', color='green', label='Hard Rock')

bpm = (78.6, 74.93333, 75.1333)

plt.plot(times, bpm, marker='^', linestyle='--', color='blue', label='Blues Rock')

plt.axis([0.2, 0.8, 70, 105])
plt.title('Average Measure of Heart Beat - All Genres\nLine Plot')
plt.ylabel('Average Measure of Heart Beat(bpm)')
plt.xlabel('Duration of song(proportion)')
plt.legend()

plt.show()
