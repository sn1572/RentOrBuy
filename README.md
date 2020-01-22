# RentOrBuy
Python code base to decide if you should rent or buy.

Code organization: Data, both historical and forecast, is stored in .pkl files that belong to the module.

There is an interface.py file that specifies essential methods belonging to various classes.
Generally speaking, if you are implicitly relying on a given class possessing a given method,
then go put it in the interface file.

Simulator class objects will receive an unsorted list of callables of various types.
The simulator steps through days starting with some arbitrary start date.
On each day, the simulator calls each member of its args list to determine what
payments need to be made on that day, what records need to be updated, and so on.
