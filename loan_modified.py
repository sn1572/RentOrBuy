# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:54:14 2018

@author: User68
"""

import numpy as np

class time_func:

    def __init__(self, function=None):
        self.function = function
        self.time = 0
        
    def set_function(function):
        self.function = function

    def value(self):
        val = self.function.iterate(self.time)
        self.time += 1
        return(val)

class const_rate:

    def __init__(self, rate):
        self.rate = rate

    def iterate(self, time):
        return(self.rate)
        

def loan_any_length(loan_amt, down_payment, payment, interest_rate, rent, housing_market_growth, investment_growth):
    capital_gains = .15; property_tax = .0078
    principle = loan_amt-down_payment
    home_value = loan_amt
    alternative = 0
    time = 0
    paid = 0
    taxes = 0
    while principle >0:
        pay = payment.value()
        ren = rent.value()
        paid += pay + property_tax*home_value/12
        taxes += property_tax*home_value/12
        principle = (1+interest_rate.value())*principle-pay
        home_value = (1+housing_market_growth.value())*home_value
        alt_val = pay-ren
        if time == 0:
            alternative = down_payment+alt_val
            assert (pay >= ren), "Housing payment must be greater than rent payment."
        else:
            alternative = (1+investment_growth.value())*alternative+alt_val
        time += 1
    print("Loan: "+str(loan_amt)+" Down payment: "+str(down_payment))
    print("Duration: "+str(time)+" months.")
    print("Total amount paid with down payment: "+str(paid+down_payment))
    print("Buy home - Appreciation of home minus taxes paid: "+str(home_value-loan_amt-taxes))
    print("Rent - Appreciated investments minus capital gains: "+str((1-capital_gains)*alternative))
    if home_value-loan_amt >= alternative:
        print("Conclusion: home loan is a better deal.")
    else:
        print("Renting is a better deal.")
        
def bank_loan_any_length(loan_amt, down_payment, payment, interest_rate, rent, housing_market_growth, investment_growth, term):
    #capital_gains = .15; property_tax = .0078
    capital_gains = .15; property_tax = 0
    init_principle = (1+interest_rate.value()*12)**(term-1)*(loan_amt-down_payment)
    principle = init_principle
    home_value = loan_amt
    alternative = 0
    time = 0
    paid = 0
    taxes = 0
    while principle >0:
        if time > term*12:
            print("Time has exceeded term.")
            print(principle)
            return(None)
        pay = payment.value()
        ren = rent.value()
        paid += pay + property_tax*home_value/12
        taxes += property_tax*home_value/12
        principle -= pay
        home_value = (1+housing_market_growth.value())*home_value
        alt_val = pay-ren
        if time == 0:
            alternative = down_payment+alt_val
            assert (pay >= ren), "Housing payment must be greater than rent payment."
        else:
            alternative = (1+investment_growth.value())*alternative+alt_val
        time += 1
    print("Loan: "+str(loan_amt)+" Down payment: "+str(down_payment)+" Monthly payment: "+str(pay))
    print("Duration: "+str(time)+" months.")
    print("Total amount paid with down payment: "+str(paid+down_payment))
    print("Buy home - Appreciation of home minus taxes paid: "+str(home_value-init_principle-taxes))
    print("Rent - Appreciated investments minus capital gains: "+str((1-capital_gains)*alternative))
    if home_value-init_principle-taxes >= ((1-capital_gains)*alternative):
        print("Conclusion: home loan is a better deal.")
    else:
        print("Renting is a better deal.")
    
loan_amt = 200000
down_payment = 50000
payment = time_func(const_rate(2000))
interest_rate = time_func(const_rate(.0425/12))
housing_market_growth = time_func(const_rate(.054/12))
investment_growth = time_func(const_rate(.054/12))
rent = time_func(const_rate(1250))

print(bank_loan_any_length(loan_amt, down_payment, payment, interest_rate, rent, housing_market_growth, investment_growth, term=15))
#print(loan_any_length(loan_amt, down_payment, payment, interest_rate, rent, housing_market_growth, investment_growth))