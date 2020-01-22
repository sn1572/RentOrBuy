# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:43:52 2020

@author: mbolding3
"""


import RentOrBuy as rob
from numpy import testing


def test_global_imports():
    _ = rob.propertyTaxes
    assert _ != None


if __name__ == '__main__':
    testing.run_module_suite()
