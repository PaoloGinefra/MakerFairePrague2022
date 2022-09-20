
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

figs = [plt.axes([0.25, 0.9 - 0.05 * i, 0.65, 0.03]) for i in range(9)]
sliders = [Slider(figs[i], str(i), 0.0, 1.0) for i in range(9)]


# Create axes for frequency and amplitude sliders
axfreq = plt.axes([0.25, 0.9, 0.65, 0.03])
axamplitude = plt.axes([0.25, 0.1, 0.65, 0.03])

# Create a slider from 0.0 to 20.0 in axes axfreq
# with 3 as initial value
freq = Slider(axfreq, 'Frequency', 0.0, 20.0, 3)

# Create a slider from 0.0 to 10.0 in axes axfreq
# with 5 as initial value and valsteps of 1.0
amplitude = Slider(axamplitude, 'Amplitude', 0.0,
                   10.0, 5, valstep=1.0)


def update(val):
    f = freq.val
    a = amplitude.val


# Call update function when slider value is changed
freq.on_changed(update)
amplitude.on_changed(update)

# display graph
plt.show()
