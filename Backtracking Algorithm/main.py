"""
Project - Backtracking Algorithm
Author - Kushagra Mittal
Date - 8th Febuary 2023

Concepts = Backtracking, iteration, conditionals
"""

import time

string = "Hello World"

words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

new_string = ""
ind = 0
while True:
    if string.lower() == new_string:
        break
    elif string[ind] == ' ':
        new_string += ' '
        ind += 1
    else: 
        for i in words:
            if string.lower() == new_string:
                break
            else:
                print(new_string+i)
                time.sleep(0.02)
                if i == string[ind].lower():
                    new_string += i
                    ind += 1
                    break
