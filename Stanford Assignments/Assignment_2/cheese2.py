# -*- coding: utf-8 -*-
"""
@author: Murat
"""
print('Good morning! Welcome to the national Cheese Emporium!')
cheeses = ['Muenster','Cheddar','Red Leicester']

def change_cheese():
    #global cheeses
    input_cheese = input('What would you like?')
    #Check the cheese
    if input_cheese in cheeses:
        print('We have {}, yessir.'.format(input_cheese))
        return
    elif '?' in input_cheese:
        print("We have 3 cheese(s)!")
        [print(ch) for ch in cheeses]
        change_cheese()
    else:
        print("I'm afraid we don't have any {}.".format(input_cheese))
        change_cheese()

change_cheese()
