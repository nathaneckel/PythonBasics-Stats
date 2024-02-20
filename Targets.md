### What you're working towards...

and by the way, this is the output of my soln of the lab.

```
$ ./tt
Data sets:, dataOne.csv dataThree.csv dataTwo.csv dataZero.csv

Run IO test

{'dataOne.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0], [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]), 
'dataThree.csv': ([8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0], [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]), 
'dataTwo.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0], [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]), 
'dataZero.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0], [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])}

Run Tests

statzcw results
dataOne.csv
9.0 11.0 7.501 4.128 0.816
dataThree.csv
9.0 11.0 7.501 4.123 0.817
dataTwo.csv
9.0 11.0 7.5 4.123 0.816
dataZero.csv
9.0 11.0 7.501 4.127 0.816

system statistics package results
dataOne.csv
9.0 11.0 7.501 4.128 0.816
dataThree.csv
9.0 11.0 7.501 4.123 0.817
dataTwo.csv
9.0 11.0 7.5 4.123 0.816
dataZero.csv
9.0 11.0 7.501 4.127 0.816
```

Everything should be _pretty close_ to each other, number-wise.

the output of the numbers is

- mean of X (9)
- sample variance of X (11)
- mean of Y (7.5)
- sample variance of Y ( 4.12)
- correlation of X vs Y (0.816)

and the shell script I'm using (tt) looks like this:

```
#!/usr/bin/env bash
files=*.csv
echo "Data sets:", $files
echo
echo "Run IO test"
echo
python3 test_io.py $files 
echo
echo "Run Tests"
echo
python3 test_stats.py $files 
```


You might also have to have two I/O routines:
`def readDataFile(file):`
and
`def readDataSets(files):`

the second one gets kicked off by 
`z = readDataSets(argv[1:])`

(and you have to consume the first line in each CSV, so you don't try to float('x') etc...)
