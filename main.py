# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 02:22:00 2020

@author: rukhat
"""

digits = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }

ten_plus = {
        15: 'fifteen',
        16: 'sixteen',
        19: 'nineteen'
    }

tens = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        10: 'Ten',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }

class Check:
    def __init__(self, n):
        self.n = n
        
    def single_digit(self):
        print(digits[self.n].title(), end=" ")
        
    def tens(self):
        print(tens[self.n].title(), end=" ")
        
    def hundred(self):
        print("Hundred", end=" ")        
    
    def thousand(self):
        print("Thousand", end=" ")
    
    def million(self):
        print("Million", end=" ")
    def billion(self):
        print("Billion", end=" ")        



def convert(n):
    num = Check(n)
    if n in range(0, 10):
        num.single_digit()
    elif n % 10 == 0:
        if n % 100 != 0:
            num.tens()
        elif n % 1000 != 0:
            n = n / 100
            temp = Check(n)
            temp.single_digit()
            temp.hundred()
        elif n % 10000 != 0:
            n = n / 1000
            temp = Check(n)
            temp.single_digit()
            temp.thousand()
        elif n % 100000 != 0:
            n = n / 1000
            temp = Check(n)
            temp.tens()
            temp.thousand()
        elif n % 1000000 != 0:
            n = n / 100000
            temp = Check(n)
            temp.single_digit()
            temp.hundred()
            temp.thousand()
        elif n % 10000000 != 0:
            n = n / 1000000
            temp = Check(n)
            temp.single_digit()
            temp.million()
        elif n % 100000000 != 0:
            n = n / 1000000
            temp = Check(n)
            temp.tens()
            temp.million()
        elif n % 1000000000 != 0:
            n = n / 100000000
            temp = Check(n)
            temp.single_digit()
            temp.hundred()
            temp.million()
        elif n % 10000000000 != 0:
            n = n / 1000000000
            temp = Check(n)
            temp.single_digit()
            temp.billion()
            
convert(2000000000)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        