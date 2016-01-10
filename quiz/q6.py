import random
import pylab

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    # pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_seq = list()
    for num in range(numTrials):
        initial = die.roll()
        maxlongest = 1
        longest = maxlongest
        for roll in range(numRolls-1):
            current = die.roll()
            if initial == current:
                longest += 1
            else:
                if maxlongest < longest:
                    maxlongest = longest
                longest = 1
            initial = current
        longest_seq.append(maxlongest)
    makeHistogram(longest_seq, 10, "number of longest-runs", "frequency", "Longest run of a 9 Faced 3x6 Die")
    return getMeanAndStd(longest_seq)[0]
# One test case
# print getAverage(Die([1]), 10, 1000)






die = Die([1])
initial = die.roll()
results = list()
maxlongest = 1
longest = maxlongest
results.append(initial)
for roll in range(10):
    current = die.roll()
    results.append(current)
    if initial == current:
        longest += 1
    else:
        if maxlongest < longest:
            maxlongest = longest
        longest = 1
    initial = current
if maxlongest < longest:
    maxlongest = longest
print results, maxlongest