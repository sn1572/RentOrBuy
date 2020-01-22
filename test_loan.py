# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:43:52 2020

@author: mbolding3
"""


import RentOrBuy as rob
import datetime
from numpy import testing


def test_global_imports():
    _ = rob.propertyTaxes
    assert _ != None


class TestPropertyTax:

    prop = rob.OwnedProperty(30308, datetime.date(2019,9,13))
    tax = rob.PropertyTax([datetime.date(2020,1,1)], prop)

    def test_instantiation(self):
        assert type(self.tax) == rob.PropertyTax

    def test_call_zero(self):
        assert self.tax(datetime.date(2020,12,25)) == 0

    def test_call_nonzero(self):
        assert self.tax(datetime.date(2020,1,1)) == rob.propertyTaxes[30308][2020]


if __name__ == '__main__':
    testing.run_module_suite()
