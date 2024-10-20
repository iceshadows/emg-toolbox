# EMG Toolbox

EMG Toolbox 是一个用于处理和分析表面肌电图 (sEMG) 数据的 Python 工具包。它包含了多种特征提取方法、信号过滤和绘图功能，帮助用户高效地对 EMG 信号进行预处理和特征分析。

## 功能

- 多种 EMG 特征提取方法：均方根 (RMS)、平均绝对值 (MAV)、过零点数 (ZC)、波形长度 (WL)、斜率符号变化 (SSC) 等。
- 信号过滤：支持 Butterworth 滤波器和电源线干扰滤波器。
- 可视化工具：包括时间域信号、频率谱和功率谱密度的绘图功能。
- 支持滑动窗口处理和多线程计算，提高特征提取效率。

## 安装

使用 pip 安装 EMG Toolbox:

```bash
pip install emg-toolbox
```

## 快速开始

以下是如何使用 EMG Toolbox 进行基本的 EMG 信号处理和特征提取的示例：

### 1. 导入模块

```python
import numpy as np
from emg_toolbox.features import sliding_window, fRMS, fMAV, fZC
from emg_toolbox.plots import plot_time_domain_signal
```

### 2. 生成示例数据

```python
# 创建随机 sEMG 信号示例
data = np.random.randn(1000)
fs = 1000  # 采样频率 1000 Hz
```

### 3. 滑动窗口特征提取

```python
# 使用滑动窗口计算均方根特征
window_size = 200
step_size = 100
rms_values = sliding_window(data, window_size, step_size, fRMS)
print(f"RMS (滑动窗口): {rms_values}")
```

### 4. 绘制时间域信号

```python
# 绘制时间域信号
plot_time_domain_signal(data, fs)
```

## 模块介绍

### 1. `features.py` - 特征提取

`features.py` 提供了一系列用于提取 EMG 信号特征的函数，例如：

- `fRMS(data)`: 计算均方根值。
- `fMAV(data)`: 计算平均绝对值。
- `fZC(data, dead_zone)`: 计算过零点数。
- 其他功能包括中值频率、平均功率频率、频谱熵等。

可以使用 `sliding_window` 函数对信号进行分段处理并计算特征。

### 2. `plots.py` - 绘图工具

`plots.py` 提供了多种绘图工具，方便对 EMG 信号进行可视化分析：

- `plot_time_domain_signal(raw, fs)`: 绘制时间域信号。
- `plot_frequency_spectrum(raw, fs)`: 绘制信号的频率谱。
- `plot_power_spectral_density(raw, fs)`: 绘制功率谱密度。

### 3. `filters.py` - 滤波器

`filters.py` 中包含了电源线干扰滤波器 (`PlifEegSubtractFilter`)，用于减少电源线干扰对 EMG 信号的影响。

## 贡献

如果您想为 EMG Toolbox 做出贡献，请 fork 本仓库并提交 pull request。欢迎提交 bug 报告和功能建议！

## 许可证

GPL License

## 联系方式

如果您有任何问题或建议，请联系我：

- Email: products@wearlab.tech
