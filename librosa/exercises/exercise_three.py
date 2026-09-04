# Exercise 3 — Compute and Visualize the Spectrogram

# Compute the STFT of your audio and plot the resulting magnitude spectrogram. Use a decibel scale on the color axis so the quieter details are 
# visible. Compare what you see to the waveform from Exercise 2 — notice what new information appears.

# *Key terms and functions:* `librosa.stft()`, `np.abs()`, `librosa.amplitude_to_db()`, `librosa.display.specshow()`, `x_axis='time'`, 
# `y_axis='hz'`, `n_fft`, `hop_length`, magnitude spectrogram, decibel scale, why dB is used instead of raw magnitude.

import librosa as wingardium_librosa
import matplotlib.pyplot as plt
import numpy as np

filename = '../test_samples/tracks/pasiempre.wav'

y, sr = wingardium_librosa.load(filename)

D = wingardium_librosa.stft(y)
S = np.abs(wingardium_librosa.stft(y))

fig, ax = plt.subplots()

img = wingardium_librosa.display.specshow(wingardium_librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax)

ax.set_title('Power Spectrogram')
fig.colorbar(img, ax=ax, format="%+2.0f db")

plt.show()
