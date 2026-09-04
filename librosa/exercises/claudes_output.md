# 15 Librosa Exercises: From Zero to Fluency

Each exercise lists the key terms, functions, and patterns you should research and understand in order to complete it. No code is provided — the 
discovery process is part of the learning.

## Understand STFT and its output

---

### Exercise 1 — Load and Inspect Audio

**"Hello, World" of librosa.**

Load an audio file and print basic information about it: the sample rate, the total number of samples, and the duration in seconds. Calculate the 
duration yourself from the other two values rather than using a helper function.

*Key terms and functions to look up:* `librosa.load()`, sample rate, audio array, NumPy array shape, duration formula (samples ÷ sample rate).

---

### Exercise 2 — Visualize the Waveform

Plot the raw audio waveform so you can see amplitude over time.

*Key terms and functions:* `librosa.display.waveshow()`, `matplotlib.pyplot`, time axis, amplitude, what the y-axis and x-axis each represent in a waveform plot.

---

### Exercise 3 — Compute and Visualize the Spectrogram

Compute the STFT of your audio and plot the resulting magnitude spectrogram. Use a decibel scale on the color axis so the quieter details are 
visible. Compare what you see to the waveform from Exercise 2 — notice what new information appears.

*Key terms and functions:* `librosa.stft()`, `np.abs()`, `librosa.amplitude_to_db()`, `librosa.display.specshow()`, `x_axis='time'`, 
`y_axis='hz'`, `n_fft`, `hop_length`, magnitude spectrogram, decibel scale, why dB is used instead of raw magnitude.

---

### Exercise 4 — Explore the Time-Frequency Trade-off

Run the STFT three times on the same audio using three very different `n_fft` values (try something small, something medium, and something large).
Plot all three spectrograms side by side and observe how the visual resolution changes along each axis. Write a short note to yourself describing what you observe.

*Key terms and functions:* `n_fft`, time-frequency uncertainty principle, frequency resolution, time resolution, `plt.subplots()` for side-by-side
plots.

---

### Exercise 5 — Extract and Inspect Phase

From the complex STFT matrix, extract both the magnitude and the phase separately. Print their shapes and data types. Reassemble them back into a 
complex matrix and verify the result matches the original by checking if the difference between the reassembled matrix and the original is 
effectively zero.

*Key terms and functions:* `np.abs()`, `np.angle()`, `np.exp()`, `1j`, complex number, magnitude, phase, `np.allclose()` for verifying numerical 
equality, polar form of a complex number.

---

## Build Feature Extraction Vocabulary

### Exercise 6 — Reconstruct Audio with the ISTFT

Take the STFT matrix, pass it through `librosa.istft()` unmodified, and save the result to a new audio file. Listen to both the original and the 
reconstructed file. Then write your own crude low-pass filter by zeroing out the top half of frequency bins in the magnitude matrix, reassemble 
with the original phase, run the ISTFT, and listen to the result.

*Key terms and functions:* `librosa.istft()`, `soundfile.write()` (or `librosa.output`), low-pass filter concept, frequency bins as rows in the 
STFT matrix, reassembling a complex matrix from magnitude and phase, what "zeroing out" rows means geometrically.

---

### Exercise 7 — Extract and Visualize Chroma Features

Extract chroma features from an audio file using all three methods (`chroma_stft`, `chroma_cqt`, `chroma_cens`) and plot them side by side. Pick a section of audio you know has a clear chord or melody and see if you can identify the dominant pitch classes in the plot.

*Key terms and functions:* `librosa.feature.chroma_stft()`, `librosa.feature.chroma_cqt()`, `librosa.feature.chroma_cens()`, pitch class, the 12 
pitch classes and their order in the matrix rows, `y_axis='chroma'` in specshow, what a bright cell in a chroma plot means.

---

### Exercise 8 — Extract and Visualize MFCCs

Extract 13 MFCCs from an audio file and plot the raw MFCC heatmap. Then normalize the matrix (subtract the mean, divide by the standard deviation,
per coefficient) and plot it again alongside the raw version. Observe which coefficients become more readable after normalization and think about
why.

*Key terms and functions:* `librosa.feature.mfcc()`, `n_mfcc`, `axis=1` with `keepdims=True` for per-row statistics, normalization vs. 
standardization, why coefficient 0 dominates the raw plot, `librosa.display.specshow()`.

---

### Exercise 9 — Compute and Visualize Delta MFCCs

Extend Exercise 8 by computing the first and second delta features from your MFCC matrix. Plot all three — base MFCCs, delta, and delta-delta — in 
a vertical stack. Find a moment in your audio where you know a significant timbral change happens (a new instrument enters, a section changes) and 
see if the delta plot lights up at that moment.

*Key terms and functions:* `librosa.feature.delta()`, `order` parameter, first derivative, second derivative, what a high delta value means 
musically, velocity vs. acceleration analogy.

---

## Understand the Geometry of Comparison

### Exercise 10 — Manually Compare Two Vectors

Without using `cross_similarity()` yet, take one MFCC vector from frame 100 of one track and one from frame 100 of another track. Manually compute 
the Euclidean distance and cosine similarity between them using NumPy math (`np.linalg.norm()`, `np.dot()`). Then do the same for two chroma 
vectors from the same frames. Print all four results and reason about what they tell you.

*Key terms and functions:* `np.linalg.norm()`, `np.dot()`, Euclidean distance formula, cosine similarity formula (`dot(a,b) / (norm(a) * norm(b))`), what a distance of zero means, what a cosine similarity of 1 means, slicing a specific column from a matrix with `[:, frame_index]`.

---

### Exercise 11 — Self-Similarity Matrix

Feed the same track's chroma features into `cross_similarity()` twice (as both arguments) to produce a self-similarity matrix. Visualize it. 
Identify the main diagonal and explain why it is always perfectly bright. Look for any off-diagonal bright stripes and reason about what repeated 
musical structure they might correspond to in the track.

*Key terms and functions:* `librosa.segment.cross_similarity()`, self-similarity matrix, `mode='affinity'`, `metric='cosine'`, the main diagonal 
and why it's always 1, off-diagonal patterns, musical repetition and structure.

---

## Cross-Similarity Becomes Genuinely Musical

### Exercise 12 — Cross-Similarity Between Two Tracks

Choose two recordings that you expect to be harmonically related (two versions of the same song, or two songs that share a chord progression). 
Compute their chroma-based cross-similarity matrix and visualize it. Then do the same with MFCCs. Write down what you observe in each matrix and 
what musical property each one is revealing.

*Key terms and functions:* `librosa.segment.cross_similarity()`, chroma vs. MFCC as input features, interpreting diagonal stripes vs. rectangular 
blocks vs. uniform dim matrices, harmonic similarity vs. timbral similarity, why the same two tracks produce different matrices depending on the 
feature used.

---

### Exercise 13 — The Effect of Metric Choice

Take the cross-similarity computation from Exercise 12 and run it four times on the same pair of MFCC matrices, varying only the `metric` 
parameter: try `'cosine'`, `'euclidean'`, and at least one other metric supported by scikit-learn's pairwise distances. Plot all results side by 
side. Observe how the choice of metric changes the structure of the matrix. Think about which metric produces the most musically interpretable 
result and why.

*Key terms and functions:* `metric` parameter in `cross_similarity()`, cosine similarity vs. Euclidean distance, `mode='affinity'` vs. 
`mode='distance'`, scikit-learn's valid metric strings, how metric choice interacts with feature scale (and why normalizing MFCCs matters more for 
some metrics than others).

---

## Integrate everything

### Exercise 14 — Audio Alignment with DTW

Take two recordings of the same piece (or two sections of the same recording that repeat) and use their chroma cross-similarity matrix as input to 
Dynamic Time Warping. Plot the accumulated cost matrix and the optimal warping path on top of the cross-similarity matrix. Interpret what the 
warping path is telling you about the temporal relationship between the two recordings.

*Key terms and functions:* `librosa.sequence.dtw()`, Dynamic Time Warping concept, warping path, accumulated cost matrix, `subseq` parameter, why 
DTW is more powerful than simple frame-by-frame comparison, plotting the warping path with `matplotlib`, the difference between a distance matrix 
and a similarity matrix as DTW input.

---

### Exercise 15 — Full Analysis Pipeline

Build a complete analysis pipeline for two audio files of your choice. The pipeline should: load both files, extract both chroma and MFCC features 
with appropriate normalization, compute both a harmonic and a timbral cross-similarity matrix, visualize the MFCC heatmaps (with deltas) and both 
similarity matrices in a single multi-panel figure, and finally run DTW on the chroma-based similarity to produce an alignment path. Write a short 
paragraph interpreting what the combined output tells you about the musical relationship between the two tracks.

*Key terms and functions:* Everything from exercises 1–14 combined. Additionally: `plt.figure()` and `gridspec` or `subplots()` for multi-panel 
layouts, designing a coherent analysis workflow, thinking about which feature and metric is appropriate for which question, interpreting results 
holistically rather than in isolation, `soundfile` for saving any processed audio you generate along the way.

---

### A Note on Progression

Exercises 1–5 are purely about understanding the STFT and its output — the foundation everything else rests on. Exercises 6–9 build the feature 
extraction vocabulary. Exercises 10–11 force you to understand the geometry of comparison *before* the library does it for you automatically. 
Exercises 12–13 are where cross-similarity becomes genuinely musical. Exercises 14–15 are where everything integrates into real analysis work.

If you find yourself stuck at any point, the most productive question to ask yourself is: *what is this function's input, what is its output, and 
what shape is each?* Keeping a running mental model of data shapes will prevent most confusion before it starts.

Good instinct to ask this — there's a meaningful amount of math running underneath everything we've covered, and being comfortable with it will take you from "I know how to call these functions" to "I understand why they work." Let me organize it by area.

------------------------------------------------------------------------------------------------------------------------------------------------

## Mathematics Worth Knowing

### Algebra and Arithmetic

The most foundational layer. You should be comfortable with **logarithms** — they appear constantly in audio (decibels, the Mel scale, the log step in MFCCs). Specifically, understanding that log compresses large values and expands small ones, and *why* that matches human perception, is worth internalizing deeply. **Exponents** go hand in hand with this since log and exponent are inverses of each other, which is exactly how you reassemble a complex number from its magnitude and phase (`magnitude * np.exp(1j * phase)`).

### Trigonometry

The Fourier Transform is built entirely on **sine and cosine waves**. You don't need to derive anything from scratch, but you should understand what a sine wave is, what frequency and amplitude mean geometrically, and critically — what the **cosine of an angle** represents. Cosine similarity is named after this directly. When two vectors have a cosine similarity of 1, the angle between them is 0° and cos(0°) = 1. When they're perpendicular, the angle is 90° and cos(90°) = 0. That's not a coincidence — it's the definition.

### Linear Algebra

This is probably the most important area and the one most worth investing time in seriously. The key concepts are:

**Vectors and vector operations** — you've been working with these throughout our conversation, but formalizing them helps. Dot products, vector norms, and the geometric interpretation of both.

**Matrices** — every feature matrix in librosa is a matrix. Understanding matrix shape, how to slice rows and columns, and what matrix operations mean geometrically will make working with librosa feel natural rather than mechanical.

**The dot product** specifically deserves attention because it's the engine behind cosine similarity. The formula `cos(θ) = dot(a,b) / (norm(a) * norm(b))` is something you should be able to derive and explain from scratch.

### Statistics

**Mean and standard deviation** appear constantly — you used them in Exercise 8 for normalization. Understanding what standardization is doing geometrically (shifting the center of your data to zero, scaling its spread to 1) matters for understanding *why* you normalize before comparing.

**Correlation** is conceptually close to cosine similarity and worth understanding as a parallel idea.

### Signal Processing Concepts (Not Strictly Math, But Mathematical in Nature)

**Convolution** underlies filtering — when you zeroed out frequency bins in Exercise 6, you were doing something equivalent to convolution in the frequency domain. Understanding the relationship between multiplication in the frequency domain and convolution in the time domain is a deep and rewarding insight.

**Sampling theory and the Nyquist theorem** — why does a 22,050 Hz sample rate let you represent frequencies up to 11,025 Hz? The answer is mathematical and explains why `n_fft=2048` produces `1025` frequency bins (exactly half plus one).

---

## Where Would You Start?

Here's a honest prioritization: **linear algebra first**, then **logarithms and trigonometry**, then **statistics**, then **signal processing theory**. Linear algebra gives you the most leverage across everything we've covered — vectors, matrices, dot products, and norms are the vocabulary of nearly every operation in librosa.

A useful question to reflect on: of the math areas listed above, which ones feel genuinely unfamiliar versus which ones feel like you've seen them but they're rusty? That distinction matters a lot for how you'd want to approach studying them.