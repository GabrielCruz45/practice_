import librosa as ls
import numpy as np

filename_one = "./test_samples/kicks/kick_1.wav"
filename_two = "./test_samples/kicks/kick_2.wav"

y_sample_one, sr_sample_one = ls.load(filename_one)
y_sample_two, sr_sample_two = ls.load(filename_two)


print(type(y_sample_one))
print(y_sample_one)
print(np.ndim(y_sample_one))


print(ls.segment.cross_similarity(y_sample_one, y_sample_two, mode='affinity'))

