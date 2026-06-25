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
clean_signal = np.sin(2 * np.pi * 200 * t) + np.sin(2 * np.pi * 300 * t)

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


def fir_signal(x, b_coeffs):

    N = len(b_coeffs)

    total_samples = len(x)

    y = np.zeros(total_samples)

    for n in range(total_samples):
        sample_sum = 0.0

        for k in range(N):
            if n - k >= 0:
                sample_sum += b_coeffs[k] * x[n - k]

        y[n] = sample_sum

    return y


num_taps = 200
b_moving_average = [1.0 / num_taps] * num_taps

print("Filtering noise (this may take a few seconds in pure Python)...")

y_fir = fir_signal(noisy_signal, b_moving_average)


save_wav("4_filtered_noise_FIR.wav", y_fir, sample_rate)
