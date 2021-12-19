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


# driver code: driver code is commented not to affect others' execution time when this package is used
# start()
# rg.intGenerator(-100, 100, 20)
# executionTimeInMilliseconds = end()
# print("time execution: " + str(executionTimeInMilliseconds) + " MS")

# result:
# time execution: 0.99951171875 MS