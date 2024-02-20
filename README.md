# PythonBasics-Stats
statistics for small datasets

There are four small datasets in this lab. You are to write a python package which contains a series of functions which can analyze these data sets. The package, statzcw, will have a series of python files, each of which implement a standard statistic.

- zcount(list: List[]) -> float
- zmean(list: List[]) -> float
- zmode(list: List[]) -> float
- zmedian(list: List[]) -> float
- zvariance(list: List[]) -> float
- zstddev(list: List[]) -> float
- zstderr(list: List[]) -> float
- zcorr(listx: List[], listy: List[]) -> float

You may only use the following functions to construct your code:

- python builtin `sum()`
- python builtin `max()`
- python builtin `min()`
- python Math function `Math.sqrt()`
- python normal operators on floats (*, /, +, -, etc)

The four data sets are each a list of two pairs of numbers (X and Y). Each of them are in a CSV file.

For each data set (0-3), print out the following statistical measures.

- Count of X
- Count of Y
- Mean of X
- Sample Variance of X
- Mean of Y
- SampleVariance of Y
- Correlation between X and Y (should be ~0.816)

Also produce the

- Median of X
- Median of Y
- Mode of X
- Mode of Y
- Sample Std deviation of X
- Sample Std Deviation of Y
- Standard Error of the Mean of X
- Standard Error of the Mean of Y

for all three datasets.

And then you are asked: "what do the statistics show you about these four data sets?"

Write a couple of unit tests to test your various functions within the package.

see Roughs.md for more info.
