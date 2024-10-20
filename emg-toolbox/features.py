import numpy as np
import scipy.signal as signal
import concurrent.futures
import pandas as pd
# 1. 均方根 (RMS)
def fRMS(data):
    """
    计算数据的均方根值 (RMS)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 均方根值
    """
    return np.sqrt(np.mean(np.square(data)))

# 2. 平均绝对值 (MAV)
def fMAV(data):
    """
    计算数据的平均绝对值 (MAV)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 平均绝对值
    """
    return np.mean(np.abs(data))

# 3. 过零点数 (ZC)
def fZC(data, dead_zone=1e-7):
    """
    计算数据的过零点数 (ZC)
    
    Parameters:
        data (np.ndarray): 输入数据
        dead_zone (float): 死区阈值，默认值为 1e-7
        
    Returns:
        float: 归一化过零点数
    """
    zc_count = 0
    for i in range(1, len(data)):
        if np.abs(data[i] - data[i-1]) > dead_zone and data[i] * data[i-1] < 0:
            zc_count += 1
    return zc_count / len(data)

# 4. 波形长度 (WL)
def fWL(data):
    """
    计算数据的波形长度 (WL)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 波形长度
    """
    return np.sum(np.abs(np.diff(data))) / len(data)

# 5. 斜率符号变化 (SSC)
def fSSC(data, dead_zone=1e-7):
    """
    计算数据的斜率符号变化数 (SSC)
    
    Parameters:
        data (np.ndarray): 输入数据
        dead_zone (float): 死区阈值，默认值为 1e-7
        
    Returns:
        float: 归一化的斜率符号变化数
    """
    ssc_count = 0
    for i in range(2, len(data)):
        diff1 = data[i-1] - data[i-2]
        diff2 = data[i-1] - data[i]
        if diff1 * diff2 > 0 and (np.abs(diff1) > dead_zone or np.abs(diff2) > dead_zone):
            ssc_count += 1
    return ssc_count / len(data)

# 6. 中值频率 (MF)
def fMF(data, fs):
    """
    计算中值频率 (MF)
    
    Parameters:
        data (np.ndarray): 输入数据
        fs (float): 采样频率
        
    Returns:
        float: 中值频率
    """
    f, Pxx = signal.welch(data, fs=fs)
    cumulative_power = np.cumsum(Pxx)
    half_total_power = cumulative_power[-1] / 2
    median_freq = f[np.where(cumulative_power >= half_total_power)[0][0]]
    return median_freq

# 7. 平均功率频率 (MPF)
def fMPF(data, fs):
    """
    计算平均功率频率 (MPF)
    
    Parameters:
        data (np.ndarray): 输入数据
        fs (float): 采样频率
        
    Returns:
        float: 平均功率频率
    """
    f, Pxx = signal.welch(data, fs=fs)
    return np.sum(f * Pxx) / np.sum(Pxx)

# 8. 功率谱密度 (PSD)
def fPSD(data, fs):
    """
    计算功率谱密度 (PSD)
    
    Parameters:
        data (np.ndarray): 输入数据
        fs (float): 采样频率
        
    Returns:
        tuple: 频率和功率谱密度
    """
    f, Pxx = signal.welch(data, fs=fs)
    return f, Pxx

# 9. 方差 (Variance VAR)
def fVAR(data):
    """
    计算数据的方差 (VAR)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 方差
    """
    return np.var(data)

# 10. 频谱熵 (Spectral Entropy)
def fSpectralEntropy(data, fs):
    """
    计算频谱熵 (Spectral Entropy)
    
    Parameters:
        data (np.ndarray): 输入数据
        fs (float): 采样频率
        
    Returns:
        float: 频谱熵
    """
    f, Pxx = signal.welch(data, fs=fs)
    Pxx_norm = Pxx / np.sum(Pxx)  # 归一化功率谱
    spectral_entropy = -np.sum(Pxx_norm * np.log(Pxx_norm + 1e-12))  # 防止 log(0)
    return spectral_entropy

# 11. 积分绝对值 (Integrated EMG, IEMG)
def fIEMG(data):
    """
    计算积分绝对值 (IEMG)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 积分绝对值
    """
    return np.sum(np.abs(data))

# 12. 自相关系数 (Autocorrelation Coefficient)
def fAutocorrelation(data, lag=1):
    """
    计算自相关系数
    
    Parameters:
        data (np.ndarray): 输入数据
        lag (int): 滞后阶数，默认值为 1
        
    Returns:
        float: 自相关系数
    """
    n = len(data)
    mean = np.mean(data)
    autocorr = np.sum((data[:n - lag] - mean) * (data[lag:] - mean)) / np.sum((data - mean) ** 2)
    return autocorr

# 13. 斜率变化率 (Slope Change Index, SCI)
def fSCI(data):
    """
    计算斜率变化率 (SCI)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 斜率变化率
    """
    return np.sum(np.abs(np.diff(np.diff(data)))) / len(data)

# 14. 平均幅度变化 (Mean Amplitude Change, MAC)
def fMAC(data):
    """
    计算平均幅度变化 (MAC)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 平均幅度变化
    """
    return np.mean(np.abs(np.diff(data)))

# 15. 近似熵 (Approximate Entropy, ApEn)
def fApEn(data, m=2, r=0.2):
    """
    计算近似熵 (ApEn)
    
    Parameters:
        data (np.ndarray): 输入数据
        m (int): 嵌入维数，默认值为 2
        r (float): 相似度阈值，默认值为 0.2
        
    Returns:
        float: 近似熵
    """
    N = len(data)
    def _phi(m):
        x = np.array([data[i:i + m] for i in range(N - m + 1)])
        C = np.sum(np.abs(x[:, None] - x[None, :]).max(axis=2) <= r, axis=0) / (N - m + 1.0)
        return np.log(C).sum() / (N - m + 1.0)
    return np.abs(_phi(m) - _phi(m + 1))

# 16. 多尺度熵 (Multiscale Entropy, MSE)
def fMSE(data, scales=5, m=2, r=0.2):
    """
    计算多尺度熵 (MSE)
    
    Parameters:
        data (np.ndarray): 输入数据
        scales (int): 多尺度的数量，默认值为 5
        m (int): 嵌入维数，默认值为 2
        r (float): 相似度阈值，默认值为 0.2
        
    Returns:
        float: 多尺度熵
    """
    mse = []
    for tau in range(1, scales + 1):
        coarse_data = np.mean(data[:len(data) - len(data) % tau].reshape(-1, tau), axis=1)
        mse.append(fApEn(coarse_data, m, r))
    return np.mean(mse)

# 17. 分形维数 (Fractal Dimension, Katz Method)
def fFractalDimension(data):
    """
    计算分形维数 (Katz 方法)
    
    Parameters:
        data (np.ndarray): 输入数据
        
    Returns:
        float: 分形维数
    """
    L = np.sum(np.sqrt(1 + np.diff(data) ** 2))
    d = np.max(np.sqrt((np.arange(len(data)) - 0) ** 2 + (data - data[0]) ** 2))
    return np.log(L) / np.log(d + 1e-10)

# 滑动窗口计算特征函数
def sliding_window(data, window_size, step_size, feature_function, fs=None, overlap=False):
    """
    滑动窗口计算特征
    
    Parameters:
        data (np.ndarray): 输入数据
        window_size (int): 滑动窗口大小
        step_size (int): 滑动步长
        feature_function (callable): 特征函数
        fs (float, optional): 采样频率（用于特征函数需要频率信息时）
        overlap (bool, optional): 是否重叠窗口
        
    Returns:
        np.ndarray: 特征值数组
    """
    num_samples = len(data)
    if num_samples < window_size:
        return data  # 如果输入数据长度小于窗口大小，则直接返回原始数据
    features = []
    if overlap:
        for start in range(0, num_samples - window_size + 1, step_size):
            window_data = data[start:start + window_size]
            if fs is not None:
                feature_value = feature_function(window_data, fs)
            else:
                feature_value = feature_function(window_data)
            features.append(feature_value)
    else:
        for start in range(0, num_samples - window_size + 1, window_size):
            window_data = data[start:start + window_size]
            if fs is not None:
                feature_value = feature_function(window_data, fs)
            else:
                feature_value = feature_function(window_data)
            features.append(feature_value)
    return np.array(features)

# 定义特征提取函数
def extract_features(window_data, fs):
    # 在这里调用你需要的特征函数
    RMS = fRMS(window_data)
    MAV = fMAV(window_data)
    ZC = fZC(window_data)
    WL = fWL(window_data)
    SSC = fSSC(window_data)
    MF = fMF(window_data, fs)
    MPF = fMPF(window_data, fs)
    VAR = fVAR(window_data)
    spectral_entropy = fSpectralEntropy(window_data, fs)
    IEMG = fIEMG(window_data)
    autocorr = fAutocorrelation(window_data)
    SCI = fSCI(window_data)
    MAC = fMAC(window_data)
    # ApEn = fApEn(window_data)
    # MSE = fMSE(window_data)
    fractal_dimension = fFractalDimension(window_data)
    
    # 返回提取的特征值
    return RMS, MAV, ZC, WL, SSC, MF, MPF, VAR, spectral_entropy, IEMG, autocorr, SCI, MAC, fractal_dimension


def extract_all_features(data, fs, sliding=True, window_size=4000, step_size=100, overlap=False, return_dataframe=False):
    """
    从输入数据中提取特征，可选地使用滑动窗口方法。

    Parameters:
    data (np.ndarray): 输入的信号数据。
    fs (int): 信号的采样频率。
    sliding (bool): 如果为 True，则使用滑动窗口提取特征。默认值为 True。
    window_size (int): 每个窗口的大小（以采样点数为单位）。默认值为 4000。
    step_size (int): 滑动窗口的步长（以采样点数为单位，适用于 overlap 为 True 时）。默认值为 100。
    overlap (bool): 如果为 True，窗口将以 step_size 重叠；如果为 False，窗口将不重叠。默认值为 False。
    return_dataframe (bool): 如果为 True，返回包含特征的 pandas DataFrame。默认值为 False。

    Returns:
    Union[np.ndarray, pd.DataFrame]: 提取的特征，以 numpy 数组或 pandas DataFrame 格式返回。
    """
    features = []
    window_points = []
    if sliding:
        # 使用多线程处理滑动窗口
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # 提交滑动窗口任务给线程池
            futures = []
            if len(data) < window_size:
                features = extract_features(data, fs)
                window_points.append((0, len(data) - 1))
            if overlap:
                for start in range(0, len(data) - window_size + 1, step_size):
                    window_data = data[start:start + window_size]
                    futures.append(executor.submit(extract_features, window_data, fs))
                    window_points.append((np.int32(start), np.int32(start + window_size - 1)))
            else:
                for start in range(0, len(data) - window_size + 1, window_size):
                    window_data = data[start:start + window_size]
                    futures.append(executor.submit(extract_features, window_data, fs))
                    window_points.append((np.int32(start), np.int32(start + window_size - 1)))
            
            # 获取特征值
            for future in concurrent.futures.as_completed(futures):
                feature_values = future.result()
                features.append(feature_values)
    else:
        # 不使用滑动窗口，直接提取整个数据的特征
        features = extract_features(data, fs)
        window_points.append((0, len(data) - 1))
    
    # 添加滑窗起止数据点列
    window_points = np.array(window_points, dtype=np.int32)
    features = np.hstack((window_points, features))
    
    if return_dataframe:
        # 将特征数据转换为DataFrame
        columns = ['start', 'end'] + ['RootMeanSquare', 'MeanAbsoluteValue', 'ZeroCrossing', 'WaveformLength', 'SlopeSignChanges', 'MedianFrequency', 'MeanPowerFrequency', 'Variance', 'SpectralEntropy', 'IntegratedEMG', 'Autocorrelation', 'SpectralCentroid', 'MeanAbsoluteDeviation', 'FractalDimension']
        df = pd.DataFrame(features, columns=columns)
        return df
    else:
        return features

if __name__ == "__main__":
    # 示例数据和采样频率
    example_data = np.random.randn(1000)  # 随机生成的模拟 sEMG 信号
    sampling_frequency = 1000  # 采样频率 1000 Hz
    window_size = 200  # 滑动窗口大小
    step_size = 100  # 滑动步长

    # 使用滑动窗口计算各个特征
    rms_values = sliding_window(example_data, window_size, step_size, fRMS)
    mav_values = sliding_window(example_data, window_size, step_size, fMAV)
    zc_values = sliding_window(example_data, window_size, step_size, fZC)
    wl_values = sliding_window(example_data, window_size, step_size, fWL)
    ssc_values = sliding_window(example_data, window_size, step_size, fSSC)
    mf_values = sliding_window(example_data, window_size, step_size, fMF, sampling_frequency)
    mpf_values = sliding_window(example_data, window_size, step_size, fMPF, sampling_frequency)
    var_values = sliding_window(example_data, window_size, step_size, fVAR)
    spectral_entropy_values = sliding_window(example_data, window_size, step_size, fSpectralEntropy, sampling_frequency)
    iemg_values = sliding_window(example_data, window_size, step_size, fIEMG)
    autocorr_values = sliding_window(example_data, window_size, step_size, fAutocorrelation)
    sci_values = sliding_window(example_data, window_size, step_size, fSCI)
    mac_values = sliding_window(example_data, window_size, step_size, fMAC)
    apen_values = sliding_window(example_data, window_size, step_size, fApEn)
    mse_values = sliding_window(example_data, window_size, step_size, fMSE)
    fractal_dim_values = sliding_window(example_data, window_size, step_size, fFractalDimension)

    # 打印部分特征值
    print(f"RMS (滑动窗口): {rms_values}")
    print(f"MAV (滑动窗口): {mav_values}")
    print(f"ZC (滑动窗口): {zc_values}")
    print(f"WL (滑动窗口): {wl_values}")
    print(f"SSC (滑动窗口): {ssc_values}")
    print(f"MF (滑动窗口): {mf_values}")
    print(f"MPF (滑动窗口): {mpf_values}")
    print(f"VAR (滑动窗口): {var_values}")
    print(f"Spectral Entropy (滑动窗口): {spectral_entropy_values}")
    print(f"IEMG (滑动窗口): {iemg_values}")
    print(f"Autocorrelation (滑动窗口): {autocorr_values}")
    print(f"SCI (滑动窗口): {sci_values}")
    print(f"MAC (滑动窗口): {mac_values}")
    print(f"ApEn (滑动窗口): {apen_values}")
    print(f"MSE (滑动窗口): {mse_values}")
    print(f"Fractal Dimension (滑动窗口): {fractal_dim_values}")