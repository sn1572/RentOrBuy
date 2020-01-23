# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:06:27 2020

@author: mbolding3
"""


import RentOrBuy as rob
import datetime
from RentOrBuy import interface


class OwnedProperty(interface.OwnedProperty):
    '''
    A concrete implementation of an owned property.
    '''

    def __init__(self, zipcode, purchaseDate):
        zipMsg = 'zipcode must be an int.'
        assert type(zipcode) == int, zipMsg
        dateMsg = 'purchase date must be a datetime.date object.'
        assert type(purchaseDate) == datetime.date, dateMsg

        self.zipcode = zipcode
        self.purchaseDate = purchaseDate


class HistoricalPropertyTax(interface.ExpenseGenerator):
    '''
    A concrete implementation of a property tax, 
    meant for pasing historical data.
    '''

    def __init__(self, dueDates, ownedProperty):
        dateMsg = 'dueDates must be a list of datetime.date objects.'
        assert type(dueDates) == list, dateMsg
        for date in dueDates:
            assert type(date) == datetime.date, dateMsg
        propertyMsg = 'ownedProperty must be a single OwnedProperty object.'
        assert type(ownedProperty) == rob.OwnedProperty, propertyMsg

        self.dueDates = dueDates
        self.property = ownedProperty

    def __call__(self, date):
        if date in self.dueDates:
            return(rob.propertyTaxes[self.property.zipcode][date.year])
        return(0)


class MonthlyLoan(interface.MonthlyLoan):
    '''
    Basic record keeper holding a monthly loan
    '''

    def __init__(self, principle):
        msg = 'principle must be an integer'
        assert type(principle) == int, msg
        self.principle = principle


class Interest(interface.ExpenseGenerator):
    '''
    Compounds interest on a monthly loan.
    '''

    def __init__(self, dueDates, rate, monthlyLoan):
        dateMsg = 'dueDates must be a list of datetime.date objects.'
        assert type(dueDates) == list, dateMsg
        for date in dueDates:
            assert type(date) == datetime.date, dateMsg
        rateMsg = 'rate must be a float.'
        assert type(rate) == float, rateMsg
        loanMsg = 'monthlyLoan must be a MonthlyLoan object.'
        assert type(monthlyLoan) == rob.MonthlyLoan, loanMsg

        self.dueDates = dueDates
        self.rate = rate
        self.monthlyLoan = monthlyLoan

    def __call__(self, date):
        if date in self.dueDates:
            return(self.rate*self.monthlyLoan.principle)
        return(0)