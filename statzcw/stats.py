import math
from typing import List

def zcount(data: List[float]) -> float :
    return len(data)    #    Count of elements in the data list.

def zmean(data: List[float]) -> float :
    return sum(data) / len(data)   #  Mean of the elements in the data list.

def zmode(data: List[float]) -> float :
    freq_map = {}
    for num in data:
        freq_map[num] = freq_map.get(num, 0) + 1
    max_freq = max(freq_map.values())
    modes = [num for num, freq in freq_map.items() if freq == max_freq]
    return modes[0]      # Mode of the elements in the data list.

def zmedian(data: List[float]) -> float :
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]   # Median of the elements in the data list.


def zvariance(data: List[float]) -> float :
    mean = zmean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)
            #  Sample variance of the elements in the data list.


def zstddev(data: List[float]) -> float :
    return math.sqrt(zvariance(data))
    # sqrt of variance # Sample standard deviation of the elements in the data list.

def zstderr(data: List[float]) -> float :
    return zstddev(data) / math.sqrt(len(data))     # Standard error of the mean of the elements in the data list.


def cov(a, b):
    mean_a, mean_b = zmean(a), zmean(b)
    return sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b)) / (len(a) - 1)
         # Covariance between two lists a and b.

def zcorr(datax: List[float], datay: List[float]) -> float :
    return cov(datax, datay) / (zstddev(datax) * zstddev(datay))  #  Correlation between two lists datax and datay.

def readDataFile(file):
    x, y = [], []
    with open(file) as f:
        next(f)  # Skip header
        for line in f:
            row = line.strip().split(',')
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y
        #    Read data from a CSV file and return as lists of X and Y values.


def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
            #       Read data sets from CSV files and return as a dictionary.
