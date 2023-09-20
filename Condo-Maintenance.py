# first install SimPy
# define the models
# define the roles, activities
# cardinality of agents
# cardinality of average events
# see attached simulation events

import random

startingPopulation = 50
infantMortality = 25
agriculture = 5
disasterChance = 10
food = 0
fertilityx = 18  # fertility range from 18 to 35
fertilityy = 35

peopleDictionary = []

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age
        
        
def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople +=1
    food += ablePeople * agriculture
    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary)-food)]
        food = 0
    else:
        food -= len(peopleDictionary)
 
def reproduce(fertilityx, fertilityy):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0,5)==1:
                        peopleDictionary.append(Person(0))
                        
  
  def beginSim():
    for x in range(startPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))
  
  beginSim()
  
  def runYear(food, agriculture, fertilityx, fertilityy):
    harvest(food, agriculture)
    reproduce(fertilityx, fertilityy)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age +=1
    
    print(len(peopleDictionary))
    
    
    while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    runYear(food, agriculture, fertilityx, fertilityy)
    
    
    
  
  
  
