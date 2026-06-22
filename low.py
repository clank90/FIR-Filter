# First we implement the necessary libraries
#

import numpy as np
import scipy.signal as signal
from scipy.io import wavfile

# GENERATE THE AUDIO SIGNAL
#
#
sample_rate = 44100  # srandard audio sample rate
duration = 3.0
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# we generate a clean audio signal
clean_signal = np.sin(2 * np.pi * 400 * t)

# in order to hear the difference we create noise
noise = 0.5 * np.sin(2 * np.pi * 4000 * t)

# corrupted input (noisy signal)
noisy_signal = clean_signal + noise


# Helper function to save normalized 16-bit WAV files
def save_wav(filename, audio_data, rate):
    normalized = np.int16((audio_data / np.max(np.abs(audio_data))) * 32767)
    wavfile.write(filename, rate, normalized)
    print(f"Saved: {filename}")

    save_wav("1_noisy_input.wav", noisy_signal, sample_rate)
