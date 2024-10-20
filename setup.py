from setuptools import setup

setup(
    name='emg_toolbox',
    version='0.1.0',
    author='Linus Zhang',
    author_email='products@wearlab.tech',
    description='A description of your library',
    long_description='A longer description of your library',
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
)
