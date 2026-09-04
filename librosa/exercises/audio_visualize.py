import librosa as wingardium_librosa
import matplotlib.pyplot as plt
import numpy as np

# load audio file; 
# sr=None -> keeps file's original sample rate; mono=False -> keeps file's original track
# librosa.load('./path/to/file.audio', sr=None, mono=False)
# wingardium_librosa.load('./test_samples/tracks/modus.aiff', sr=None, mono=False)
waveform, sample_rate = wingardium_librosa.load('./test_samples/tracks/modus.aiff')


# ------------------------------------------------------------create a waveform of the file---------------------------------------------------------

# create a window
# plt.figure(figsize=(10, 4))
# wingardium_librosa.display.waveshow(waveform, sr=sample_rate, color="blue")

# plt.title("Waveform")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")

# plt.tight_layout()

# plt.show()


# ------------------------------------------------------------create a spectogram of the file-------------------------------------------------------

stft = wingardium_librosa.stft(waveform)

# convert the amplitude values to decibels
# np.abs(stft) -> we're interested in the amplitude at each point in time, but not the phase
spectogram = wingardium_librosa.amplitude_to_db(np.abs(stft))

plt.figure(figsize=(10, 4))
wingardium_librosa.display.specshow(spectogram, sr=sample_rate, x_axis='time', y_axis='log')
plt.colorbar()
plt.title("Spectogram (db)")
plt.tight_layout()
plt.show()

