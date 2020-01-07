import random

def RandomEventsGenerator(n):
    #This function is created for basic testing.
    eventsList = []
    for i in range(n):
        eventsList.append(Event(str(i) + "Course", random.randint(1, 6), random.randint(1, 12), str(random.randint(1,10))+ "Teacher"))
    return eventsList

class Event:
    def __init__(self, name, room, timeslot, teacher):
        self.name = name # "Advance algorithms"
        self.room = room # 411
        self.timeslot = timeslot # Value of 1 to 30, 1 meaning monday morning 08.15 and 30 friday 18.15.
        self.teacher = teacher # "Jaak Vilo"
        
    def EventPrint(self):
        #Prints the event values
        print(str(self.name) + " " + str(self.room) + " " + str(self.timeslot) + " " + str(self.teacher))

class Timetable:
    def __init__(self, events, valid, fitness):
        self.valid = valid
        self.events = events
        self.fitness = fitness
        #self.fitness = fitness
        
    def CalculateFitness(self):
        #This function calculates the fitness value of a timetable.
        fitness = 0
        #Penalyse for every course at  0815 and 1815.
        for e in self.events:
            if e.timeslot == 1:
                fitness = fitness -1
            elif e.timeslot == 12:
                fitness = fitness -1
            else:
                fitness = fitness + 1
        return fitness
    
    def IsFeasible(self):
        #Tests if Timetable has no clashes
        #Roomclashes
        roomstimes = []
        teachertimes = []
        roomvalid = False
        teachervalid = False
        for e in self.events:
            roomstimes.append(e.timeslot*10000 + e.room) #Hashfunction
            teachertimes.append(str(e.timeslot) + e.teacher)
        if len(roomstimes) == len(set(roomstimes)):
            roomvalid = True
        if len(teachertimes) == len(set(teachertimes)):
            teachervalid = True
        if roomvalid == True and teachervalid == True:
            self.valid = True
        return self.valid
        #Teacherclashes
    
    def PrintTable(self):
        #Prints the timetable
        tableoftimes = {}
        for i in range(12):
            tableoftimes[i+1] = []
        
        for e in self.events:
            tableoftimes[e.timeslot].append([e.room, e.teacher])
        return tableoftimes
