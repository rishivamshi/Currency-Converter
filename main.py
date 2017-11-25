# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:08:51 2017

@author: rishi
"""

from currency_converter import CurrencyConverter
c = CurrencyConverter()

print(c.convert(1,'EUR','USD'))

x = list(c.currencies)
print(len(x))

print('Enter the from code')
cfrom = input()
print('enter the to code')
cto = input()

print('enter the amount')
amount = int(input())

print(c.convert(amount,cfrom,cto))