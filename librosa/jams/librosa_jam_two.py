import librosa as ls
import numpy as np
import matplotlib.pyplot as plt

filename = './example_one.mp3'

y, sr = ls.load(filename, sr=48000)

print(y)
print(sr)

tempo, beats_frames = ls.beat.beat_track(y=y, sr=sr)

print(tempo)
print(beats_frames)

beat_times = ls.frames_to_time(beats_frames, sr=sr)

print(beat_times)


# ------------------------------------------------------------------------------------------------------------------------------------------------

hop_length = 512

# separates harmonic and percussives into to waveforms
y_harmonic, y_percussive = ls.effects.hpss(y)

print(y_harmonic)
print(type(y_harmonic))

print(y_percussive)
print(type(y_percussive))

tempo, beats_frames = ls.beat.beat_track(y=y_percussive, sr=sr)

print(tempo)
print(beats_frames)

print(y_percussive.ndim)

# # gx as in "graph x"; yugioh because millenial yolk; "yolk" because dad joke
# yugioh_gx = np.arange(len(y_percussive))
# plt.plot(yugioh_gx, y)
# plt.show()

# mfcc is a matrix which is a numpy.ndarray of shape (n_mfcc, T)
mfcc = ls.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

mfcc_delta = ls.feature.delta(mfcc)

beat_mfcc_delta = ls.util.sync(np.vstack([mfcc, mfcc_delta]), beats_frames)
