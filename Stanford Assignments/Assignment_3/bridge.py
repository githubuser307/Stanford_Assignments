# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 23:17:33 2019

@author: ILYAS
"""
import random
def bridge_of_death(text):
    print('KEEPER: STOP!' + text) 
    finish = False
    while finish == False:
        name = input('KEEPER: What is ' + questions[0] + ' ')
        if not name.upper() in answers[0].upper():
            key = 1
            break
        quest = input('KEEPER: What is ' + questions[1] + ' ')
        if not quest.upper() in answers[1].upper():
            key = 1
            if '?' in quest:
                key = 2
            finish = True
            break
        num_question = random.randint(2, 5)
        last_question = input('KEEPER: What is ' + questions[num_question] + ' ')
        if not last_question.upper() in answers[num_question].upper():
            key = 1
            if '?' in last_question:
                key = 2
        finish = True
            
    show(name, key)
    
def show(name, key):
    if key == 1:
        print('{} : Auuuuuuuugh!'.format(name.upper()))
    elif key == 2:
        print('KEEPER: What? I don\'t know that! Auuuuuuuuuuugh!"')
    else:
        print('KEEPER: Right. Off you go.')

questions = []
answers = []

with open("answers.txt", "r") as file_answers:
    for line in file_answers:
        temp = line.split('?')
        questions.append(temp[0])
        answers.append(temp[1])
text = 'Who would cross the Bridge of Death must answer me these questions three, \'ere the other side he see.'
bridge_of_death(text)
bridge_of_death(text)
bridge_of_death(' ')
bridge_of_death(' ')