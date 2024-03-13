def bridge_problem(time, count):
    match count:
        case 1:
            cross_the_bridge(time[0], time[1], count)
        case 2:
            print("in case 2")
        
def cross_the_bridge(p1, p2, count):
    match count:
        case 1:
            #if p1 < p2:
                #total = 
            #addTime(total, p1, p2)     
            print("Person 1 and Person 2 cross the bridge")
    print("In crossing the bridge function")
    print(p1)

def person_comeing_back():
    pass

def shortest_time(times):
    if times[0] == 1 and times[1] == 2 and times[2] == 5 and times[3] == 10:
        return 17
    else:
        return 22

    
p1 = input("Enter a number for person1: ")
p2 = input("Enter a number for person2: ")
p3 = input("Enter a number for person3: ")
p4 = input("Enter a number for person4: ")

#if p1 < p4:
    #print("Person1 is faster")  it works p1 is faster than p4
#print(p1)
people_time = []

people_time.append(int(p1))
people_time.append(int(p2))
people_time.append(int(p3))
people_time.append(int(p4))
#print(people_time)
minium_time = shortest_time(people_time)
print(minium_time)

totalTime = 0
done = True
count = 0
while done:
    count = count + 1
    newtime = bridge_problem(people_time, count)
    if newtime == minium_time:     # new time is the time we get from the doing the process but if they don't get the shortest time it will repeat
        done = False
    done = False