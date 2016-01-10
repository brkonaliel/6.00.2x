import pylab
import random
import matplotlib.pyplot as plt

xVals = []
yVals = []
wVals = []
for i in range(10000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.hist(yVals, bins=10)
pylab.xlim(-1, 2)
pylab.title("Histogram of 1 random variable")


pylab.figure()
pylab.hist(xVals, bins=10)
pylab.xlim(-1, 3)
pylab.title("Histogram of 2 random variables")

pylab.figure()
pylab.hist(zVals, bins=10)
pylab.xlim(-1, 3)
pylab.title("Histogram of 2 random variables")

pylab.figure()
pylab.plot(sorted(xVals), yVals)


pylab.show()
# pylab.plot(xVals, zVals, tVals, label=["x + x", "x + y", "x + y + z"])
# pylab.plot(yVals, "o", label="y")
# pylab.plot(wVals, "o", label="w")
# pylab.plot(xVals, "ro", label="x+x")
# pylab.plot(zVals, "bo", label="x+y")
# pylab.plot(tVals, "yo", label="x+y+z")
# pylab.ylim(-1, 5)
# pylab.legend()
# pylab.figure()
# pylab.hist(xVals, bins=10)
# pylab.show()

