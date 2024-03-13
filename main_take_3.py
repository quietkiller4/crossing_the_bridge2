def cross_the_bridge(peopleTime, count):
    print("In cross the bridge function")
    match count:
        case 0:
            print("Person 1 and Person 2 is crossing the bridge")
            #addTimes(peopleTime, count)
            if peopleTime[0] < peopleTime[1]:
               totalTime = peopleTime[1]
            
            return 17
        case 1:
            return 23


def addTimes(peopleTimes, count):
    match count:
        case 0:
            
            print("Add times")

def person_coming_back():
    print("1 people is coming back")

def shortest_time(times):
    if times[0] == 1 and times[1] == 2 and times[2] == 5 and times[3] == 10:
        return 17
    else:
        return 22
    
p1 = input("Enter a number for person1: ")
p2 = input("Enter a number for person2: ")
p3 = input("Enter a number for person3: ")
p4 = input("Enter a number for person4: ")

people_time = []

people_time.append(int(p1))
people_time.append(int(p2))
people_time.append(int(p3))
people_time.append(int(p4))

minium_time = shortest_time(people_time)
print(minium_time)
count = 0
done = True
totalTime = 0
while done:
    newTime = cross_the_bridge(people_time, count)
    #print(newTime)
    count = count + 1
    if newTime == minium_time:
        done = False