import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    global CURRENTRABBITPOP
    if CURRENTRABBITPOP < 10:
        return
    else:
        addition = 0
        for i in range(CURRENTRABBITPOP):
            if random.random() < (1.0-float(CURRENTRABBITPOP)/MAXRABBITPOP):
                addition += 1
        CURRENTRABBITPOP = CURRENTRABBITPOP+addition
def foxGrowth():
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    if CURRENTRABBITPOP < 10 or CURRENTFOXPOP < 10:
        return
    else:
        eaters = 0
        addition = 0
        deaths = 0
        for i in range(CURRENTFOXPOP):
            if random.random() < float(CURRENTRABBITPOP)/MAXRABBITPOP and CURRENTRABBITPOP > 10:
                eaters += 1
                CURRENTRABBITPOP -= 1
        for i in range(eaters):
            if random.random() < 1.0/3:
                addition += 1
        for i in range(CURRENTFOXPOP-eaters):
            if random.random() < 9.0/10:
                deaths += 1
        CURRENTFOXPOP = CURRENTFOXPOP+addition-deaths
        if CURRENTFOXPOP < 10:
            CURRENTFOXPOP = 10


def runSimulation(numSteps):
    rabbit_populations = list()
    fox_populations = list()
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    result = (rabbit_populations, fox_populations)
    return result
result = runSimulation(200)
print result[0]
print result[1]
pylab.figure()
pylab.plot(result[0], "r-",label="Rabbit")
pylab.plot(result[1], "b-", label="Fox")
pylab.legend()

x_axis = range(200)
a, b, c = pylab.polyfit(x_axis, result[0], 2)
d, e, f = pylab.polyfit(x_axis, result[1], 2)
print a,b,c
print d,e,f
poly_rabbit = pylab.polyval([a,b,c], x_axis)
poly_fox = pylab.polyval([d,e,f], x_axis)
print poly_rabbit
print poly_fox
pylab.figure()
pylab.plot(poly_rabbit, "r-", label="Rabbit Poly")
pylab.plot(poly_fox, "b-", label="Fox Poly")
pylab.legend()
pylab.show()