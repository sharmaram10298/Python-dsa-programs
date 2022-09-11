"""Iterator in python is an object that is used to iterate over iterable objects like
lists, tuples, dicts, and sets. The iterator object is initialized using the iter()
method. It uses the next() method for iteration.
 
__iter(iterable)__ method that is called for the initialization of an iterator.
This returns an iterator object
next ( __next__ in Python 3) The next method returns the next value for the iterable.
When we use a for loop to traverse any iterable object, internally it uses the iter()
method to get an iterator object which further uses next() method to iterate over.
This method raises a StopIteration to signal the end of the iteration."""

iterable_value = 'Virash'
iterable_obj = iter(iterable_value)
 
while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        # exception will happen when iteration will over
        break
    # item = next(iterable_obj)
    # print(item)
 		
# Sample built-in iterators
 
# Iterating over a list
print("List Iteration")
l = ["virash", "training", "institute"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("virash", "training", "institute")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")   
s = "Virash"
for i in s :
    print(i)
