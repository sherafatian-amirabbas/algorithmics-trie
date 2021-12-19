import time


global startingTime


# saves the current time in milliseconds to be used when monitor ends
def start():
    global startingTime
    startingTime = time.time() * 1000


# calculates execution time
# return value: floating point number as execution time in milliseconds
def end():
    global startingTime
    endtime = time.time() * 1000
    return endtime - startingTime


# driver code:
# start()
# YOUR CODE COMES HERE
# executionTimeInMilliseconds = end()
# print("time execution: " + str(executionTimeInMilliseconds) + " MS")