# Audio Signal Noise Generator

This project contains a simple Python script that uses `numpy` and `scipy` to synthesize a clean audio signal, intentionally corrupt it with high-frequency noise, and export the result as a standard audio file. 

This is typically used as the first step in Digital Signal Processing (DSP) exercises to test audio filtering and noise reduction algorithms.

## Features
* Generates a foundational 400 Hz sine wave (clean signal).
* Generates a 4000 Hz sine wave (noise) at half the amplitude.
* Combines the two signals into a single corrupted audio track.
* Normalizes and exports the audio as a 16-bit PCM WAV file.

## Prerequisites
You will need Python 3.x installed along with the following libraries:
* `numpy`
* `scipy`

You can install the required dependencies using pip:
`pip install numpy scipy`

## How it Works
1. **Signal Generation:** The script creates a 3-second time array sampled at 44.1 kHz (CD-quality standard).
2. **Synthesis:** It uses mathematical sine functions (`np.sin`) to generate both the base tone and the high-pitch noise.
3. **Normalization:** The `save_wav` helper function ensures the final floating-point data is safely scaled to fit within the 16-bit integer range (-32768 to 32767) to prevent audio clipping. 
4. **File I/O:** The `scipy.io.wavfile` module writes the normalized array to your hard drive.

## Usage
Save the script as `generate_noise.py` (or your preferred name) and run it from your terminal:

`python generate_noise.py`

## Output
Running the script will generate the following file in your current working directory:
* `1_noisy_input.wav` - A 3-second audio file containing the combined 400 Hz tone and 4000 Hz noise.
