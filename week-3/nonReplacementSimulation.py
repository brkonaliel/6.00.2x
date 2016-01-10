import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    bucket = ["R", "R", "R", "G", "G", "G"]
    choices = []
    yes = 0.0
    for i in range(numTrials):
        while len(bucket):
            # print bucket.pop(random.choice(range(len(bucket))))
            choices.append(bucket.pop(random.choice(range(len(bucket)))))
            if len(choices) > 2:
                if choices[-1] == choices[-2] and choices[-2] == choices[-3]:
                    yes += 1
                    break
        bucket = ["R", "R", "R", "G", "G", "G"]
        choices = []
    return yes/numTrials

print noReplacementSimulation(100000)
def noReplacementSimulation2(numTrials):
    bucket = ["R", "R", "R", "G", "G", "G"]
    choices = []
    yes = 0.0
    for i in range(numTrials):
        for j in range(3):
            choices.append(bucket.pop(random.choice(range(len(bucket)))))
        if choices[-1] == choices[-2] and choices[-2] == choices[-3]:
            yes += 1
        bucket = ["R", "R", "R", "G", "G", "G"]
        choices = []
    return yes/numTrials

print noReplacementSimulation2(100000)