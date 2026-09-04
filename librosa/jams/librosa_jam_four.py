import librosa as ls
import librosa.display as lsd
import numpy as np
import matplotlib.pyplot as plt

filepath = './test_samples/tracks/modus.aiff'
y, sr = ls.load(filepath)

mfccs = ls.feature.mfcc(y=y, sr=sr, n_mfcc=13)

fig, ax = plt.subplots(figsize=(12, 4))
img = lsd.specshow(
    mfccs,
    x_axis='time',   # converts frame indices to seconds automatically
    sr=sr,
    ax=ax
)

fig.colorbar(img, ax=ax, label='MFCC Coefficient Value')
ax.set_ylabel('MFCC Coefficient Index')
ax.set_title('MFCC Feature Map')
plt.tight_layout()
plt.show()

stft_matrix = ls.stft(y, n_fft=2048, hop_length=512)

print(stft_matrix.shape)
print(stft_matrix.dtype)
