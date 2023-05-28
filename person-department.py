# Aggregate embedded objects into a composite

class Person:
    def __init__(self, name, job=None, pay=0):  # Constructor takes three arguments
        self.name = name   # fill out fields when created 
        self.job = job     # self is the new instance object
        self.pay = pay
    def lastName(self):    # Behavior methods
        return self.name.split()[-1]     # self is implied subject
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))   # Must change here only
    def __repr__(self):                # Add method  __repr__overload method for printing objects
        return '[Person: %s, %s]' %(self.name, self.pay)     # String to print
    
class Manager:
    def __init__ (self, name, pay):
        self.person = Person(name, 'mgr', pay)        #  Embed a person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)         # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr)     # Delegate all other attrs
    def __repr__(self):
        return str(self.person)
    
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember (self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__=='__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay= 100000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)

#   Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10)

#   Runs embedded objects' giveRaise
    development.showAll()
#   Runs embedded objects' __repr__



    