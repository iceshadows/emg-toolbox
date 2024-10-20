# EMG Toolbox

EMG Toolbox is a Python toolkit for processing and analysing surface electromyography (sEMG) data. It includes a variety of feature extraction methods, signal filtering, and plotting functions, helping users efficiently preprocess and analyse EMG signals.

## Features

- Various EMG feature extraction methods: Root Mean Square (RMS), Mean Absolute Value (MAV), Zero Crossing (ZC), Waveform Length (WL), Slope Sign Change (SSC), etc.
- Signal filtering: Supports Butterworth filter and powerline interference filter.
- Visualisation tools: Includes plotting functions for time-domain signals, frequency spectra, and power spectral density.
- Supports sliding window processing and multithreaded computation to improve feature extraction efficiency.

## Installation

Install EMG Toolbox using pip:

```bash
pip install emg-toolbox
```

## Quick Start

Below is an example of how to use EMG Toolbox for basic EMG signal processing and feature extraction:

### 1. Import Modules

```python
import numpy as np
from emg_toolbox.features import sliding_window, fRMS, fMAV, fZC
from emg_toolbox.plots import plot_time_domain_signal
```

### 2. Generate Example Data

```python
# Create random sEMG signal example
data = np.random.randn(1000)
fs = 1000  # Sampling frequency 1000 Hz
```

### 3. Sliding Window Feature Extraction

```python
# Calculate RMS feature using sliding window
window_size = 200
step_size = 100
rms_values = sliding_window(data, window_size, step_size, fRMS)
print(f"RMS (Sliding Window): {rms_values}")
```

### 4. Plot Time-Domain Signal

```python
# Plot time-domain signal
plot_time_domain_signal(data, fs)
```

## Module Overview

### 1. `features.py` - Feature Extraction

`features.py` provides a series of functions for extracting features from EMG signals, such as:

- `fRMS(data)`: Calculates the root mean square.
- `fMAV(data)`: Calculates the mean absolute value.
- `fZC(data, dead_zone)`: Calculates zero crossings.
- Other features include median frequency, mean power frequency, spectral entropy, etc.

The `sliding_window` function can be used to segment the signal and calculate features.

### 2. `plots.py` - Plotting Tools

`plots.py` offers several plotting tools for visualising EMG signals:

- `plot_time_domain_signal(raw, fs)`: Plots the time-domain signal.
- `plot_frequency_spectrum(raw, fs)`: Plots the frequency spectrum.
- `plot_power_spectral_density(raw, fs)`: Plots the power spectral density.

### 3. `filters.py` - Filters

`filters.py` includes a powerline interference filter (`PlifEegSubtractFilter`) to reduce powerline interference in EMG signals.

## Contribution

If you would like to contribute to EMG Toolbox, please fork this repository and submit a pull request. Bug reports and feature suggestions are welcome!

## License

GPL License

## Contact

If you have any questions or suggestions, please contact me:

- Email: products@wearlab.tech
