import random

def brute_force(times):
    #choose(6/2)*choose(2/1)*choose(5/2)*choose(3/1)*choose(4/2)*choose(4/1)*choose(3/2)*choose(5/1)*choose(2/2) 
    #choose()
    #count = 0
    rightSide = []
    choose6(times, rightSide)

def choose6(times, rightSide):
    time = 0
    person1 = "person1"
    person2 = "person2"
    person3 = "person3"
    person4 = "person4"
    x = random.randrange(1, 3)
    y = random.randrange(1, 4)
    if x == 1 and y == 1:
        #print(person1, "and", person2, "go across")
        time = times[1]
        coming_back_choose2(times[0], times[1], time, times, rightSide)
    elif x == 1 and y == 2:
        #print(person1, "and", person3, "go across")
        time = times[2]
        coming_back_choose2(times[0], times[2], time, times, rightSide)
    elif x == 1 and y == 3:
        #print(person1, "and", person4, "go across")
        time = times[3]
        coming_back_choose2(times[0], times[3], time, times, rightSide)
    elif x == 2 and y == 1:
        #print(person2, "and", person3, "go across")
        time = times[2]
        coming_back_choose2(times[1], times[2], time, times, rightSide)
    elif x == 2 and y == 2:
        #print(person2, "and", person4, "go across")
        time = times[3]
        coming_back_choose2(times[2], times[3], time, times, rightSide)
    elif x == 2 and y == 3:
        #print(person3, "and", person4, "go across")
        time = times[3]
        coming_back_choose2(times[2], times[3], time, times, rightSide)
    #print("Time =", time)

def coming_back_choose2(p1, p2, totaltime, peopleTimes, rightSide):
    #print("In coming back")
    #print(totaltime)
    x = random.randrange(1, 3)
    if x == 1:
        #print("A person is coming back")
        totaltime = totaltime + p1
        rightSide.append(p2)
        #print(rightSide)
        choose5(peopleTimes, totaltime, rightSide)
    else:
        #print("A person is coming back")
        totaltime = totaltime + p2
        rightSide.append(p1)
        #print(rightSide)
        choose5(peopleTimes, totaltime, rightSide)

def choose5(peopleTimes, totaltime, rightSide):
    x = random.randrange(1, 4)
    #print(totaltime)
    if rightSide[0] == 1:
        if x == 1:
            #print(peopleTimes[1], "and", peopleTimes[2], "go across")
            totaltime = totaltime + peopleTimes[2]
            coming_back_choose3(peopleTimes[1], peopleTimes[2], totaltime, peopleTimes, rightSide)
        elif x == 2:
            #print(peopleTimes[1], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[1], peopleTimes[3], totaltime, peopleTimes, rightSide)
        else:
            #print(peopleTimes[2], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[2], peopleTimes[3], totaltime, peopleTimes, rightSide)
    elif rightSide[0] == 2:
        if x == 1:
            #print(peopleTimes[0], "and", peopleTimes[2], "go across")
            totaltime = totaltime + peopleTimes[2]
            coming_back_choose3(peopleTimes[0], peopleTimes[2], totaltime, peopleTimes, rightSide)
        elif x == 2:
            #print(peopleTimes[0], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[0], peopleTimes[3], totaltime, peopleTimes, rightSide)
        else:
            #print(peopleTimes[2], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[2], peopleTimes[3], totaltime, peopleTimes, rightSide)
    elif rightSide[0] == 5:
        if x == 1:
            #print(peopleTimes[0], "and", peopleTimes[1], "go across")
            totaltime = totaltime + peopleTimes[1]
            coming_back_choose3(peopleTimes[0], peopleTimes[1], totaltime, peopleTimes, rightSide)
        elif x == 2:
            #print(peopleTimes[1], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[1], peopleTimes[3], totaltime, peopleTimes, rightSide)
        else:
            #print(peopleTimes[1], "and", peopleTimes[3], "go across")
            totaltime = totaltime + peopleTimes[3]
            coming_back_choose3(peopleTimes[1], peopleTimes[3], totaltime, peopleTimes, rightSide)
    else:
        if x == 1:
            #print(peopleTimes[0], "and", peopleTimes[1], "go across")
            totaltime = totaltime + peopleTimes[1]
            coming_back_choose3(peopleTimes[0], peopleTimes[1], totaltime, peopleTimes, rightSide)
        elif x == 2:
            #print(peopleTimes[0], "and", peopleTimes[2], "go across")
            totaltime = totaltime + peopleTimes[2]
            coming_back_choose3(peopleTimes[0], peopleTimes[2], totaltime, peopleTimes, rightSide)
        else:
            #print(peopleTimes[1], "and", peopleTimes[2], "go across")
            totaltime = totaltime + peopleTimes[2]
            coming_back_choose3(peopleTimes[1], peopleTimes[2], totaltime, peopleTimes, rightSide)

def coming_back_choose3(p1, p2, totaltime, peopleTimes, rightSide):
    x = random.randrange(1, 4)
    #print(totaltime)
    if x == 1:
        #print("A person is coming back")
        totaltime = totaltime + p1
        rightSide.append(p2)
        choose4(peopleTimes, totaltime, rightSide)
    elif x == 2:
        #print("A person is coming back")
        totaltime = totaltime + p2
        rightSide.append(p1)
        choose4(peopleTimes, totaltime, rightSide)
    else:
        #print("A person is coming back")
        totaltime = totaltime + rightSide[0]
        rightSide.remove(rightSide[0])
        rightSide.append(p1)
        rightSide.append(p2)
        choose4(peopleTimes, totaltime, rightSide)

def choose4(peopleTimes, totaltime, rightSide):
    x = random.randrange(1, 4)
    #print(totaltime)
    if (rightSide[0] == 1 and rightSide[1] == 2) or (rightSide[0] == 2 and rightSide[1] == 1):
        #print(peopleTimes[2], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[2], peopleTimes[3], totaltime, peopleTimes, rightSide)
    elif (rightSide[0] == 1 and rightSide[1] == 5) or (rightSide[0] == 5 and rightSide[1] == 1):
        #print(peopleTimes[1], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[1], peopleTimes[3], totaltime, peopleTimes, rightSide)
    elif (rightSide[0] == 1 and rightSide[1] == 10) or (rightSide[0] == 10 and rightSide[1] == 1):
        #print(peopleTimes[1], "and", peopleTimes[2], "go across")
        totaltime = totaltime + peopleTimes[2]
        coming_back_choose4(peopleTimes[1], peopleTimes[2], totaltime, peopleTimes, rightSide)
    elif (rightSide[0] == 2 and rightSide[1] == 5) or (rightSide[0] == 5 and rightSide[1] == 2):
        #print(peopleTimes[0], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[0], peopleTimes[3], totaltime, peopleTimes, rightSide)
    elif (rightSide[0] == 2 and rightSide[1] == 10) or rightSide[0] == 10 and rightSide[1] == 2:
        #print(peopleTimes[0], "and", peopleTimes[2], "go across")
        totaltime = totaltime + peopleTimes[2]
        coming_back_choose4(peopleTimes[0], peopleTimes[2], totaltime, peopleTimes, rightSide)
    elif (rightSide[0] == 5 and rightSide[1] == 10) or (rightSide[0] == 10 and rightSide[1] == 5):
        #print(peopleTimes[0], "and", peopleTimes[1], "go across")
        totaltime = totaltime + peopleTimes[1]
        coming_back_choose4(peopleTimes[0], peopleTimes[1], totaltime, peopleTimes, rightSide)

def coming_back_choose4(p1, p2, totaltime, peopleTimes, rightSide):
    if p1 > p2:
        #totaltime = totaltime + p1
        rightSide.append(p1)
        rightSide.append(p2)
    else:
        #totaltime = totaltime + p2
        rightSide.append(p1)
        rightSide.append(p2)
    print(rightSide)
    print(totaltime)
    """x = random.randrange(1, 5)
    if x == 1:
        print("A person is coming back")
        totaltime = totaltime + p1
        rightSide.append(p2)
        choose3(peopleTimes, totaltime)
    elif x == 2:
        print("A person is coming back")
        totaltime = totaltime + p2
        rightSide.append(p1)
        choose3(peopleTimes, totaltime)
    elif x == 3:
        print("A person is coming back")
        totaltime = totaltime + rightSide[0]
        rightSide.remove(rightSide[0])
        rightSide.append(p1)
        rightSide.append(p2)
        choose3(peopleTimes, totaltime)
    else:
        print("A person is coming back")
        totaltime = totaltime + rightSide[1]
        rightSide.remove(rightSide[1])
        rightSide.append(p1)
        rightSide.append(p2)
        choose3(peopleTimes, totaltime)"""

#def choose3(peopleTimes, totaltime):
    #print(rightSide)
    """if (rightSide[0] == 1 and rightSide[1] == 2 and rightSide[2] == 5) or (rightSide[0] == 1 and rightSide[1] == 5 and rightSide[2] == 2) or (rightSide[0] == 2 and rightSide[1] == 1 and rightSide[2] == 5) or (rightSide[0] == 2 and rightSide[1] == 5 and rightSide[2] == 1) or (rightSide[0] == 5 and rightSide[1] == 1 and rightSide[2] == 2) or (rightSide[0] == 5 and rightSide[1] == 2 and rightSide[2] == 1):
        print(peopleTimes[2], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[2], peopleTimes[3], totaltime, peopleTimes)
    elif (rightSide[0] == 1 and rightSide[1] == 2 and rightSide[2] == 5) or (rightSide[0] == 1 and rightSide[1] == 5 and rightSide[2] == 2) or (rightSide[0] == 2 and rightSide[1] == 1 and rightSide[2] == 5) or (rightSide[0] == 2 and rightSide[1] == 5 and rightSide[2] == 1) or (rightSide[0] == 5 and rightSide[1] == 1 and rightSide[2] == 2) or (rightSide[0] == 5 and rightSide[1] == 2 and rightSide[2] == 1):
        # still need to fix the elif
        print(peopleTimes[1], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[1], peopleTimes[3], totaltime, peopleTimes)
    elif (rightSide[0] == 1 and rightSide[1] == 10) or (rightSide[0] == 10 and rightSide[1] == 1):
        # still need to fix the elif
        print(peopleTimes[1], "and", peopleTimes[2], "go across")
        totaltime = totaltime + peopleTimes[2]
        coming_back_choose4(peopleTimes[1], peopleTimes[2], totaltime, peopleTimes)
    elif (rightSide[0] == 2 and rightSide[1] == 5) or (rightSide[0] == 5 and rightSide[1] == 2):
        print(peopleTimes[0], "and", peopleTimes[3], "go across")
        totaltime = totaltime + peopleTimes[3]
        coming_back_choose4(peopleTimes[0], peopleTimes[3], totaltime, peopleTimes)
    elif (rightSide[0] == 2 and rightSide[1] == 10) or rightSide[0] == 10 and rightSide[1] == 2:
        print(peopleTimes[0], "and", peopleTimes[2], "go across")
        totaltime = totaltime + peopleTimes[2]
        coming_back_choose4(peopleTimes[0], peopleTimes[2], totaltime, peopleTimes)
    elif (rightSide[0] == 5 and rightSide[1] == 10) or (rightSide[0] == 10 and rightSide[1] == 5):
        print(peopleTimes[0], "and", peopleTimes[1], "go across")
        totaltime = totaltime + peopleTimes[1]
        coming_back_choose4(peopleTimes[0], peopleTimes[1], totaltime, peopleTimes)"""

peopleTimes = [1, 2, 5, 10]
i = 100
while i != 0:
    brute_force(peopleTimes)
    i = i - 1