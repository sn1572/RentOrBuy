'''
Trying to decide on a design paradigm. Trying also
to be as explicit as possible regarding class method
design decisions.
'''


import abc


class ExpenseGenerator(abc.ABC):
    '''
    This class encapsulates the callable that will
    generate expenses on a daily basis.
    For example, if a bill is due on the eleventh
    of every month and a simulation starts on Jan 1,
    then the bill's class should return the value
    of the bill on day 11 and then on day 42 (the
    eleventh of Feb).
    '''

    @abc.abstractmethod
    def __call__(self, day):
        pass


class RecordKeeper(abc.ABC):
    '''
    This one stores the value of things like
    home equity, loan principal, or stock holdings.
    Must implement __call__ for getting the value
    of the record, and further child classes will
    be used to identify the kind of record.
    '''
    
    @abc.abstractmethod
    def __call__(self):
        pass


class MonthlyLoan(RecordKeeper):
    '''
    A loan with interest compounded monthly. It
    receives a special class because Simulators
    will need some means of finding loans which
    need to be paid off.
    '''
    pass


class OwnedProperty(abc.ABC):
    '''
    Class for properties that are owned.
    Will be the child of potentially many
    objects, such as a property tax, which
    will want to access the OwnedProperty's
    zip code for determination fo tax amounts.
    '''

    @abc.abstractmethod
    def __init__(self, zipCode, purchaseDate):
        pass

    @abc.abstractmethod
    def zipCode(self):
        pass

    @abc.abstractmethod
    def purchaseDate(self):
        pass


class Simulator(abc.ABC):
    '''
    To actually run a simulation, we want to pass a
    collection of ExpenseGenerator and RecordKeeper 
    functions as args and then let the sim call them 
    every day and examine the output. A very general
    way of doing things that lets one easily include
    more and more detail by just including more and
    more expenses and records.
    '''
    
    @abc.abstractmethod
    def __init__(self, *args):
        pass