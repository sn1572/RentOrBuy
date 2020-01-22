# We're a module now, baby!


import pickle
import os
from RentOrBuy.loan import *


moduleDir = os.path.dirname(os.path.realpath(__file__))
propertyTaxFilename = os.path.join(moduleDir,'propertyTaxData.pkl')
with open(propertyTaxFilename, 'rb') as f:
    propertyTaxes = pickle.load(f)