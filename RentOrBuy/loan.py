# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:06:27 2020

@author: mbolding3
"""


import RentOrBuy.interface as interface
import RentOrBuy as rob
import datetime


class PropertyTax(interface.ExpenseGenerator):
    '''
    A concrete implementation of a property tax.
    '''

    def __init__(self, dueDates, ownedProperty):
        dateMsg = 'dueDates must be a list of datetime.date objects.'
        assert type(dueDates) == list, dateMsg
        for date in dueDates:
            assert type(date) == datetime.date, dateMsg
        self.dueDates = dueDates
        self.property = ownedProperty

    def __call__(self, date):
        if date in self.dueDates:
            return(rob.propertyTaxes[self.ownedProperty.zipcode][date.year])