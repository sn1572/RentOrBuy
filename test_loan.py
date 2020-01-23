# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:43:52 2020

@author: mbolding3
"""


import RentOrBuy as rob
import datetime
from numpy import testing


class TestGlobalImports:

    def test_propertyTaxes_import(self):
        taxes = rob.propertyTaxes
        assert type(taxes) == dict


class TestHistoricalPropertyTax:

    prop = rob.OwnedProperty(30308, datetime.date(2019,9,13))
    tax = rob.HistoricalPropertyTax([datetime.date(2020,1,1)], prop)

    def test_instantiation(self):
        assert type(self.tax) == rob.HistoricalPropertyTax

    def test_call_zero(self):
        assert self.tax(datetime.date(2020,12,25)) == 0

    def test_call_nonzero(self):
        assert self.tax(datetime.date(2020,1,1)) == rob.propertyTaxes[30308][2020]


class TestInterest:

    loan = rob.MonthlyLoan(1000)
    interest = rob.Interest([datetime.date(1990,1,1)], 0.1, loan)

    def test_call_zero(self):
        assert self.interest(datetime.date(1989,1,1)) == 0

    def test_call_nonzero(self):
        assert self.interest(datetime.date(1990,1,1)) == 0.1*1000


if __name__ == '__main__':
    testing.run_module_suite()
