# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:18:52 2019

@author: ILYAS
"""
import numpy as np
import math
import random

def encrypt_caesar(plaintext):
    ciphertext = []
    for i in plaintext:
        character = ord(i.upper())
        if character >= 65 and character <= 87:
            ciphertext.append(chr(character + 3))
        elif character == 88:
            ciphertext.append('A')
        elif character == 89:
            ciphertext.append('B')
        elif character == 90:
            ciphertext.append('C')
        else:
            ciphertext.append(chr(character))
            
    return ciphertext


def decrypt_caesar(ciphertext):
    plaintext = []
    for i in ciphertext:
        character = ord(i.upper())
        if character >= 68 and character <= 90:
            plaintext.append(chr(character - 3))
        elif character == 65:
            plaintext.append('X')
        elif character == 66:
            plaintext.append('Y')
        elif character == 67:
            plaintext.append('Z')
        else:
            plaintext.append(chr(character))
    return plaintext

def encrypt_vigenere(plaintext, keyword):
    """asdfghjk"""
    full_keyword = []
    for i in range(len(plaintext)):
        full_keyword.append(keyword[i%len(keyword)])
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append(((ord(plaintext[i].upper()) - 65) + (ord(full_keyword[i].upper()) - 65)) % 25)
    return_ciphertext = []
    for i in ciphertext:
        return_ciphertext.append(chr(i + 65))
    
    return return_ciphertext
    
def decrypt_vigenere(ciphertext, keyword):
    """yuikjhg"""
    full_keyword = []
    for i in range(len(ciphertext)):
        full_keyword.append(keyword[i%len(keyword)])
    dig_ciphertext = []
    dig_full_keyword = []
    for i in range(len(ciphertext)):
        dig_ciphertext.append(ord(ciphertext[i].upper()) - 65)
        dig_full_keyword.append(ord(full_keyword[i].upper()) - 65)
    plaintext = []
    for i in range(len(dig_ciphertext)):
        if dig_ciphertext[i] < dig_full_keyword[i]:
            plaintext.append(chr((25 - abs(dig_ciphertext[i] - dig_full_keyword[i])) + 65))
        else:
            plaintext.append(chr((dig_ciphertext[i] - dig_full_keyword[i]) + 65))

    return plaintext
"""define for receive type cryptosystemfrom user"""
def receive_cryptosystem():
    print('* Cryptosystem *')
    crypto_set = set('cCvVmM')
    keyword = 'a'
    crypto_print = ''
    cryptosystem = input('(C)aesar, (V)igenere or (M)erkle-Hellman?')
    if cryptosystem in crypto_set:
        if cryptosystem == 'c' or cryptosystem =='C':
            crypto_print = 'Caesar'
        elif cryptosystem == 'v' or cryptosystem == 'V':
            crypto_print = 'Vigenere'
            keyword = input('Keyword? ')
        else:
            crypto_print = 'Merkle-Hellman'
    else:
        print('Please choose a correct type cryptosystem:')
        return cryptosystem, crypto_print, keyword, 0
    return cryptosystem, crypto_print, keyword, 1
"""define for receive action(Encrypt or Decrypt) from user"""
def receive_action():
    print('* Action *')
    action_set = set('eEdD')
    action_print = ''
    action = input('(E)ncrypt or (D)ecrypt?')
    if action in action_set:
        if action == 'e' or action == 'E':
            action_print = 'Encrypt'
        else:
            action_print = 'Decrypt'
    else:
        print('Please choose a correct type action:')
        return action, action_print, 0
    return action, action_print, 1
""" define for call type cryptosystem and action and after return result (decrypt string or encrypt string)"""
def call_cipher(text, cryptosystem, action, keyword):
    if cryptosystem.upper() == 'C' and action.upper() == 'E':
        return encrypt_caesar(text)
    elif cryptosystem.upper() == 'C' and action.upper() == 'D':
        return decrypt_caesar(text)
    elif cryptosystem.upper() == 'V' and action.upper() == 'E':
        return encrypt_vigenere(text, keyword)
    else:
        return decrypt_vigenere(text, keyword)

from utils import coprime
from utils import bits_to_byte
from utils import byte_to_bits
from utils import is_superincreasing

""" define for generate private key, we use for Merkle-hellman cryptosystem"""
def generate_private_key(n=8):
    total = 0
    seq = [1]
    for i in range(8):
        total = total + seq[i]
        seq.append(random.randint((total + 1), (2 * total)))
    q = random.randint((total + 1),(2 * total))
    r = 0
    while not coprime(r,q):
        r = random.randint(2,(q - 1))        
    return seq, q, r    

def create_public_key(private_key):
    beta = []
    for i in range(len(private_key[0])):
        beta.append(private_key[2] * private_key[0][i] % private_key[1])
    return beta

private_key = generate_private_key(8)
public_key = create_public_key(private_key)   
 
def chunk_it(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out
def encrypt_mh(message, public_key):
    split_message = chunk_it(message, len(public_key))
    split_message_bytes = []
    for chunk in split_message:
        for byte in chunk:
            split_message_bytes.append(byte_to_bits(ord(byte)))
    print(split_message_bytes)
encrypt_mh('as sdfgsd asdhdgfgfrehfghrefhgfhghdhdhghdg', public_key)    
    
    
    
"""Console menu"""
print('Welcome to the Criptography Suite!')
print('----------------------------------')
close_program = 'Yr'
while close_program == 'Y':
    auth = 0
    while auth == 0:
        cryptosystem, crypto_print, keyword, auth = receive_cryptosystem()
    auth = 0
    while auth == 0:
        action, action_print, auth = receive_action()
    
    input_data = input('Enter a string: ')
    output_data = call_cipher(input_data, cryptosystem, action, keyword)
    print('{}ing "{}" using {} cipher...\nand result {}'.format(action_print, input_data, crypto_print, output_data))
    close_program = input('Again? ').upper()


"""write encrypt and decrypt in files"""
with open('tests/caesar_tests.txt', 'w') as file:
    file.write('encrypt_caesar(\'python\')' + str(encrypt_caesar('python')))
    file.write('\ndecrypt_caesar "sbwkrq" ' + str(decrypt_caesar('sbwkrq')))
    file.write('\nencrypt_caesar "ilyas" ' + str(encrypt_caesar('ilyas')))
    file.write('\ndecrypr_caesar "ddccbbaa" ' + str(decrypt_caesar('ddccbbaa')))

with open('tests/vigenere_tests.txt', 'w') as file:
    file.write('\nencrypt_vigenere("ATTACKATDAWN" with key "LEMON")' + str(encrypt_vigenere('ATTACKATDAWN', 'LEMON')))
    file.write('\ndecrypt_vigenere "lxgopvegrnir", with key "LEMON")' + str(decrypt_vigenere('lxgopvegrnir', 'LEMON')))
    file.write('\nencrypt_vigenere("ilyas" with key "n")' + str(encrypt_vigenere('ilyas', 'n')))
