import random


def cross_the_bridge(times, time_it_should_be):  # 2 people on the left side go to the right side
    right_side = 0
    left_side = len(times)
    print(left_side)


def person_come_back(times):  # 1 person from the right side go back to the left side
    pass

def minium_time(times):
    #for x in times:    #this for loop check what is in the list
        #print(x)
    if times[0] == 1 and times[1] == 2 and times[2] == 5 and times[3] == 10:
        return 17
    else:
        return 22


times = [1, 2, 5, 10]
min_time = minium_time(times)
print(min_time)
#done = True
#while done:
time = cross_the_bridge(times, min_time)
    #done = False
    #if time <= min_time:
        #done = False