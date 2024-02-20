from statistics import mean, variance, pvariance
import statistics 
from statzcw.stats import *
from sys import argv

data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
data2 = [1.0, 2.0, 2.0, 4.0, 5.0]

try:
    assert zcount(data0) == 5
    assert zmean(data0) == 3.0
    assert zmode(data2) == 2.0

    assert zmedian(data2) == 2.0
    assert zmedian(data0) == 3.0
except AssertionError as e:
    print(e)

# Creating a sample of data 
sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98] 

# tuple of a set of positive integers 
# numbers are spread apart but not very much 
sample1 = (1, 2, 5, 4, 8, 9, 12) 
  
# tuple of a set of negative integers 
sample2 = (-2, -4, -3, -1, -5, -6) 
  
# tuple of a set of positive and negative numbers 
# data-points are spread apart considerably  
sample3 = (-9, -1, -0, 2, 1, 3, 4, 19) 

sample10 = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,
          0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]

# # Prints variance of the sample sets
# print("Variance of sample set is % s" 
#       %(variance(sample))) 

# print("zvariance of sample set is ", zvariance(sample))

# # Variance of sample set is 0.40924
# print("\nVariance of Sample1 is % s " %(variance(sample1))) 
# print("sample1 zvar", zvariance(sample1))
# print("Variance of Sample2 is % s " %(variance(sample2))) 
# print("Sample2 zvar", zvariance(sample2))
# print("Variance of Sample3 is % s " %(variance(sample3))) 
# print("Sample3 zvar", zvariance(sample3))

# n = len(sample10) - 1
# m = sum(sample10) / n
# # calculate variance using a list comprehension
# deviations = [(m - xi) ** 2 for xi in sample10]
# var_res = sum(deviations) / n
# print("\nsample10 vari", variance(sample10))
# print("sample10 var ", var_res)
# print("sample10 zvar", zvariance(sample10))

# data1 = [3, 4, 4, 5, 7, 8, 12, 14, 14, 15, 17, 19, 22, 24, 24, 24, 25, 28, 28, 29]
# zerr = 2.001447

# test_list = [6, 7, 3, 9, 10, 15]
# test_var = zvariance(test_list)
# print(test_var, test_list)
# # assert test_var == 13.888888888888891
# # assert zerr == zstderr(data1)
# res = statistics.variance(test_list) 
# # printing result 
# print("The statistics.variance of list is : " + str(res)) 

if __name__ == "__main__":
    #print("var of data0", zvariance(data0))
    #print("corr of data0", zcorr(data0,data2))
    z = readDataSets(argv[1:])
    # print("z", z)
    print("statzcw")
    for k, v in z.items():
        print(k)
        x,y = v[0],v[1]
        xc = zcount(x)
        yc = zcount(y)
        xbar = zmean(x)
        ybar = zmean(y)
        xv = zvariance(x)
        yv = zvariance(y)
        xycorr = zcorr(x,y)
        print(round(xbar, 3), round(xv, 3), round(ybar, 3), round(yv, 3), round(xycorr, 3))
    print("system")
    for k, v in z.items():
        print(k)
        x,y = v[0],v[1]
        xc = len(x)
        yc = len(y)
        xbar = mean(x)
        ybar = mean(y)
        xv = variance(x)
        yv = variance(y)
        xycorr = zcorr(x,y)
        print(round(xbar, 3), round(xv, 3), round(ybar, 3), round(yv, 3), round(xycorr, 3))
    print("Everything should be _pretty close_ to each other, number-wise.")