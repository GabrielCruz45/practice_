import librosa as wingardium_librosa
import numpy as np

y, sr = wingardium_librosa.load('./test_samples/tracks/gasolina.m4a')
print(f'Duration = {y.shape[0] / sr}')

print(y)
print(sr)
print(len(y))
print(type(y))
print(type(sr))

print(y.shape[0])

# count = 0
# for i in np.nditer(y):
#     print(i, end=' ')
#     print('\n')
#     count = count + 1
# 
# print(count)
