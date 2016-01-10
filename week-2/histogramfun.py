import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
def calcRatio(vowels, word):
    total = 0.0
    for char in word:
        if char in vowels:
            total += 1
    return total/len(word)
def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = ["a", "e", "i", "o", "u"]
    proportions = []
    for word in wordList:
        proportions.append(calcRatio(vowels, word))

    print proportions
    pylab.hist(proportions, bins=numBins)
    pylab.xlim(-0.5, 1.5)
    pylab.title("Histogram of Vowels in Words")
    pylab.xlabel("Ratios of # of vowels over length of keyword")
    pylab.ylabel("Frequency")
    pylab.show()
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
