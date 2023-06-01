# File makedb.py: store Person objects on a shelve database

from person import Person, Manager

# Load our classes

bob = Person('Bob Smith')      # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')       # Filename when objects are stored

try:
    for obj in (bob, sue, tom):    # Use object's name attr as key
        db[obj.name] = obj        # Store object on shelve by key
        print("Stored object:", obj.name)

except Exception as e:
    print("An error ocurred while storing objects:", str(e))

finally:
    db.close()                     # Close after making changespython3



