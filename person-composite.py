
# uvicorn main:person-composite --reload


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

if __name__ == '__main__':
    bob = Person('Bob Smith')          # Test the class
    sue = Person('Sue Jones', job='dev', pay=1000000)  # Runs _init_ automatically
    print (bob)
    print (sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
#   tom = Manager('Tom Jones', 'mgr', 50000)   # Make a Manager: __init__
    tom = Manager('Tom Jones', 50000)          # Job name not need:   
# Manager:__init__
# Job name not needed:
    tom.giveRaise(.10)
# Runs custom version
    print(tom.lastName())
# Runs inherited method
    print(tom)
# Runs inherited __repr__

    # tom.giveRaise(.10)          # Runs custom version. This is the traditional and simplest scheme 
    # print(tom.lastName())       # Runs inherit method
    # print(tom)                  # Runs inherits __repr__
        
 #  print('--All three--')          # Polymorphism 
 #  for obj in (bob, sue, tom):     # Process objects generically
 #      obj.giveRaise(.10)          # Run this object's giveRaise
 #      print (obj)                 # Run the common __repr__


    # print(bob.name, bob.pay) # Fetch attached attributes
    # print(sue.name, sue.pay) # sue's and bob's attrs differ
    # print(bob.lastName(), sue.lastName())    # Use the methods
    # sue.giveRaise(.10)                       # instead of hardcoding
    # print(sue.pay)                           

