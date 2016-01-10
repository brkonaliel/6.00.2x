import random
import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

result = list()
# for i in range(100000):
#     result.append(random.gauss(70, 10)+random.gauss(50, 10))
# pylab.figure()
# pylab.hist(result, bins=50)
# pylab.show()

a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
print xVals
print yVals
# exit()
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'
y_projected = a*xVals**3+b*xVals**2+c*xVals+d
pylab.figure()
pylab.plot(xVals, yVals, "b-", label="original")
pylab.plot(xVals, y_projected, "ro", label="projected")
pylab.legend()
print float(0.000000001)
# pylab.show()
n=100
for i in range(n, n**2, n**2/10):
    print i