# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:27:05 2019

@author: ILYAS
"""
print('Good morning! Welcome to the national Cheese Emporium!')
cheeses = ['Muenster','Cheddar','Red Leicester']

def change_cheese():
    input_cheese = input('What would you like?')
    for cheese in cheeses:
        if cheese == input_cheese:
             print('We have {}, yessir.'.format(input_cheese))
             return
    if '?' in input_cheese:
        print("""We have 3 cheese(s)!
              Muenster
              Cheddar
              Red Leicester""")
        change_cheese()
    else:
        print("I'm afraid we don't have any {}.".format(input_cheese))
        change_cheese()
change_cheese()



