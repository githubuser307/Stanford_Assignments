# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:58:02 2019

@author: ILYAS
"""
def calc_can_carry(num_of_ounces, num_of_coconuts):
    if float(num_of_ounces) / float(num_of_coconuts) >= 5.5:
        print('Yes! Carrying the coconuts in possible.')
    else:
        print('No. Carrying the coconuts is impossoble.')

num_of_ounces = input('How many ounces of swallows are carrying the coconuts?')
num_of_coconuts = input('How many pounds of coconuts are there?')

calc_can_carry(num_of_ounces, num_of_coconuts)
    
with open('coconuts-input.txt', 'r') as file:
    num_of_ounces = file.readline()
    num_of_coconuts = file.readline()
file.close()
print('number of ounces = {}'.format(num_of_ounces))
print('number of coconuts = {}'.format(num_of_coconuts))
calc_can_carry(num_of_ounces, num_of_coconuts)