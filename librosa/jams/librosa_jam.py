import librosa

# filename is a string containing the file path to the audio file
filename = librosa.example('nutcracker')


y, sr = librosa.load(filename)

print(f"y: {y}")
print(f"sr: {sr}")

tempo, beats_frames = librosa.beat.beat_track(y=y, sr=sr)

print(tempo, beats_frames)

beats_times = librosa.frames_to_time(beats_frames, sr=sr)
print(beats_times)