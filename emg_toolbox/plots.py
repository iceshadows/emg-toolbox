# Function to plot time-domain signal, includes filtering step within the function
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from .filters import PlifEegSubtractFilter
from scipy.fft import fft, fftfreq
from scipy.signal import welch

def plot_time_domain_signal(raw, fs):
    # Apply Butterworth Filter (10-300 Hz)
    lowcut = 10
    highcut = 300
    order = 4
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    filtered_data = signal.lfilter(b, a, raw)

    # Apply PowerLine Inference (Example)
    b, a = signal.butter(3, 0.05)
    zi = signal.lfilter_zi(b, a)
    z, _ = signal.lfilter(b, a, filtered_data, zi=zi * filtered_data[0])
    y = signal.filtfilt(b, a, filtered_data)

    # Time domain plot
    t = np.linspace(-1, 1, len(raw))
    plt.figure()
    plt.plot(t, raw, 'g', alpha=0.45)
    plt.plot(t, filtered_data, 'b', alpha=0.75)
    plt.plot(t, y, 'r')
    plt.legend(('Noisy signal', 'After Butterworth (10 - 300 Hz)', 'After PowerLine Inference'), loc='best')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Time-Domain Signal')
    plt.show()

# Function to plot frequency spectrum, includes filtering step within the function
def plot_frequency_spectrum(raw, fs):
    n = len(raw)
    T = 1 / fs
    
    # Apply Butterworth Filter (10-300 Hz)
    lowcut = 10
    highcut = 300
    order = 4
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    filtered_data = signal.lfilter(b, a, raw)

    # Apply PowerLine Inference (Example)
    b, a = signal.butter(3, 0.05)
    y = signal.filtfilt(b, a, filtered_data)

    # Frequency domain
    xf = fft(raw)
    xf_freq = fftfreq(n, T)[:n // 2]
    xf_mag = np.abs(xf[:n // 2])
    
    xn_freq = fftfreq(n, T)[:n // 2]
    xn_mag = np.abs(fft(filtered_data))[:n // 2]
    
    y_freq = fftfreq(n, T)[:n // 2]
    y_mag = np.abs(fft(y))[:n // 2]
    
    plt.figure()
    plt.plot(xf_freq, xf_mag, 'g', alpha=0.45)
    plt.plot(xn_freq, xn_mag, 'b', alpha=0.75)
    plt.plot(y_freq, y_mag, 'r')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum')
    plt.grid(True)
    plt.legend(('Noisy signal', 'After Butterworth (10 - 300 Hz)', 'After PowerLine Inference'), loc='best')
    plt.show()

# Function to plot power spectral density, includes filtering step within the function
def plot_power_spectral_density(raw, fs):
    # Apply Butterworth Filter (10-300 Hz)
    lowcut = 10
    highcut = 300
    order = 4
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    filtered_data = signal.lfilter(b, a, raw)

    # Apply PowerLine Inference (Example)
    b, a = signal.butter(3, 0.05)
    y = signal.filtfilt(b, a, filtered_data)

    # Power spectral density
    xf_f, xf_Pxx = welch(raw, fs=fs, nperseg=1024)
    xn_f, xn_Pxx = welch(filtered_data, fs=fs, nperseg=1024)
    y_f, y_Pxx = welch(y, fs=fs, nperseg=1024)
    
    plt.figure()
    plt.plot(xf_f, xf_Pxx, 'g', alpha=0.45)
    plt.plot(xn_f, xn_Pxx, 'b', alpha=0.75)
    plt.plot(y_f, y_Pxx, 'r')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density')
    plt.title('Power Spectral Density')
    plt.grid(True)
    plt.legend(('Noisy signal', 'After Butterworth (10 - 300 Hz)', 'After PowerLine Inference'), loc='best')
    plt.show()