from statzcw.stats import readDataSets
from sys import argv

if __name__ == "__main__":
    z = readDataSets(argv[1:])
    print(z)