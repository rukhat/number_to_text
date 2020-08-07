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
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }

tens = {
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

def under_100(n):
    if n in range(0, 10):
        print(digits[n], end = " ")
    elif n in range(10, 100, 10):
        print(tens[n], end = " ")
    elif n in range(11, 20):
        print(ten_plus[n], end = " ")
    else:
        for i in range(2, 10):
            if n in range((10*i+ 1), (10* (i + 1))):
                d1 = (n // 10) * 10
                d0 = n % 10
                    
                print(tens[d1], end = " ")
                print(digits[d0], end = " ")

def hundreds(n):
    d2 = n // 100
    d01 = n % 100
        
    print(digits[d2], end = " ")
    print("Hundred", end = " ")
    if d01:
        print("and", end = " ")
        under_100(d01)

def thousands(n):
    d3 = n // 1000
    d012 = n % 1000
        
    print(digits[d3], end = " ")
    print("Thousand", end = " ")
    if d012:
        hundreds(d012)        
                
def switch(n):
    l = len(str(n))
    
    if l == 1 or l == 2:
        under_100(n)
    elif l == 3:
        hundreds(n)
    elif l == 4:
        thousands(n)
    
                

def main():
    n = int(input("Enter a number:\n>> "))
    
    if n >= 0:
        switch(n)
    else:
        print("Minus ")
        switch(abs(n))
                
if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        