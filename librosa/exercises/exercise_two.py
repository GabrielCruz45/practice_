# Exercise 2 — Visualize the Waveform
# Plot the raw audio waveform so you can see amplitude over time.
# *Key terms and functions:* `librosa.display.waveshow()`, `matplotlib.pyplot`, 
# time axis, amplitude, what the y-axis and x-axis each represent in a waveform plot.


import librosa as wingardium_librosa
import numpy as np
import matplotlib.pyplot as plt

filename = '../test_samples/tracks/pasiempre.wav' # path depends from where you are 'python3'-ing from -> '../' or './' or else
y, sr = wingardium_librosa.load(filename, mono=False, duration=10)


wingardium_librosa.display.waveshow(y, sr=sr)


plt.show()

# import librosa
# import librosa.display
# import matplotlib.pyplot as plt

# # mono=False preserves stereo channels → shape: (2, n_samples)
# y, sr = librosa.load(filename, mono=False)

# fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# librosa.display.waveshow(y[0], sr=sr, ax=axes[0], color="steelblue")
# axes[0].set_title("Left Channel")

# librosa.display.waveshow(y[1], sr=sr, ax=axes[1], color="tomato")
# axes[1].set_title("Right Channel")

# plt.tight_layout()
# plt.show()

