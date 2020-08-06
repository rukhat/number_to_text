# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 02:22:00 2020

@author: rukhat
"""

digits = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

ten_plus = {
        11: 'elevn',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

tens = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

class Check:
    def __init__(self, n):
        self.n = n
        
    def single_digit(self):
        print(digits[self.n].title())
        
    def tens(self):
        print(tens[self.n].title())
        
    def hundreds(self):
        temp = self.n / 100
        print(digits[temp].title(), "hundred")
        
def convert(n):
    temp = Check(n)
    if n in range(0, 10):
        temp.single_digit()
    elif n % 10 == 0:
        if n % 100 != 0:
            temp.tens()
        elif n % 100 == 0:
            temp.hundreds()
        
        
convert(300)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        