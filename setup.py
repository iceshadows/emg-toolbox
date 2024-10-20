from setuptools import setup, find_packages
import os

# 读取 README.md 文件的内容
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='emg_toolbox',
    version='1.0.1',
    author='Linus Zhang',
    author_email='products@wearlab.tech',
    description='EMG Toolbox is a Python toolkit for processing and analysing surface electromyography (sEMG) data. It includes a variety of feature extraction methods, signal filtering, and plotting functions, helping users efficiently preprocess and analyse EMG signals.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_repository',
    packages=['emg_toolbox'],
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
)
