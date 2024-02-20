## To remind you of the basics of statistics...

Each of these are _pseudo-code_, they'll give you an idea of where you're going without a whole bunch of confusing, specialized, technical math symbols.

If I have a list, like this:

```
data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
```

#### Count

the count of data0 is 5, because it has 5 numbers in the list.

#### Mean

the mean (or average) is 3.0 (notice the floating point number!) which is usually computed
by summing the numbers in the list and dividing by the list's count.

so.

mean = sum(data0) / count(data0)

#### Mode

the mode is the _most common_ value in list
so let's change the data to be this

```
data2 = [1.0, 2.0, 2.0, 4.0, 5.0]
```

We just changed the 3.0 to another 2.0

When we do that, we now have 

- 2.0 - 2
- 1.0 - 1
- 4.0 - 1
- 5.0 - 1

And the _mode_ is the entry which has the _most number of occurences_

So the mode of `data2` is `2.0`

#### Median

The _median_ is the _middle value_

so the median of `data0` is `3.0`
and the median of `data2` is `2.0`

#### Variance (_Sample_ Variance)

The _sample variance_ of a list is a little trickier, but not too much.

_Variance measures how far a data set is spread out. It is mathematically defined as the average of the squared differences from the mean._

Count of values in the sample

`n = count(data0) - 1`   # or 4

the minus one here means we are calculating the SAMPLE Variance, not the POPULATION Variance,
which would not minus 1 from the count.

Mean of the data

`mean = sum(data0) / n `

Square the deviations from the mean for each value in the list

```
deviations = []
    for xi in data0
        deviations.append( absolute_value(mean - xi) ** 2 )
```

This loop gives us a list of the squared differences of the mean from each value in the list.     
Then to get the Variance, we just get the mean/average of those differences.

`variance = sum(deviations) / n`

or in this case of `data0`, 2.5

#### Standard Deviation

The standard deviation is just the square root of the variance of a list, so...

`std_dev = square-root(variance(data0))`

or in this case, 1.58 (or there-abouts)

#### Standard Error

This is simply the standard deviation divided by the square root of the count...

`std_err = standard_deviation(data0) / square_root( count(data0) )`

#### Correlation

The correlation is a little trickier still, you need to figure out the _covariance_ between the two lists.

And then the correlation is the covariance divided by the stddev of each list multiplied together

`correlation(l1, l2) = covariance(l1, l2) / (stddev(l1) * stddev(l2))`

so make a cov() function, and that needs to do something like this:

```
sum = 0
make sure the count or a and b are equal!
then we can just use count(a)
for i in range(0, count(a))
    sum += ((a[i] - mean(a)) * (b[i] - mean(b)))
cov = sum/(count(a)-1)
```

And if you do it right, your `correlation(data0, data2)` should be about `0.962`

### Conclusion

Using these are ways of building your code, you should be able to put them into python (or any other language).

You can always write your own sum() function if you need to.
Also, in python at least, you can square a number by `(x ** 2.0)` and of course you can also square root a number by `(x ** 0.5)` (cool, huh?).
