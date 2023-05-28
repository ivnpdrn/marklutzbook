# File person.py (start)

# uvicorn main:person --reload

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

 # Add customization of one behavior in a subclass

class Manager(Person):     # Inherit Person attrs, Define a subclase of Person, which inherits from, and add customizations to the superclass Person
    def __init__(self, name, pay):
#   Redefine constructor
        Person.__init__(self, name, 'mgr', pay)    #   Run original with 'mgr'
#   Inherit
    def giveRaise(self, percent, bonus=.10):     # Redefine at this value
        Person.giveRaise(self, percent + bonus)     # Call Person's version
# Customize
#       def someThingElse(self,...):...
# Extend



#       def someThingElse(self, ...): ...               # Extend
# tom.someThingElse(
# Extra methods like this code's someThingElse extend the existing software and are
# ...available on Manager objects only, not on Persons.

# instances.method(args...) translated by Python into this equivalent form:
# class.method(instance, args ...)            


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
