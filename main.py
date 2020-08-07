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
    if n // 1000 in range(0, 10):
        d3 = n // 1000
        d012 = n % 1000
    
        print(digits[d3], end = " ")
        print("Thousand", end = " ")
        if d012:
            hundreds(d012)
    elif n // 10000 in range(0, 10):
        d34 = n // 1000
        d012 = n % 1000
        
        under_100(d34)
        print("Thousand", end = " ")
        if d012:
            hundreds(d012)
    elif n // 100000 in range(0, 10):
        d345 = n // 1000
        d012 = n % 1000
        
        hundreds(d345)
        print("Thousand", end = " ")
        if d012:
            hundreds(d012)
             
def millions(n):
    if n // 1000000 in range(0, 10):
        d6 = n // 1000000
        d05 = n % 1000000
    
        print(digits[d6], end = " ")
        print("Million", end = " ")
        if d05:
            thousands(d05)
    elif n // 10000000 in range(0, 10):
        d67 = n // 1000000
        d05 = n % 1000000
        
        under_100(d67)
        print("Million", end = " ")
        if d05:
            thousands(d05)
    elif n // 100000000 in range(0, 10):
        d678 = n // 1000000
        d05 = n % 1000000
        
        hundreds(d678)
        print("Million", end = " ")
        if d05:
            thousands(d05)

def billions(n):
    if n // 1000000000 in range(0, 10):
        d9 = n // 1000000000
        d08 = n % 1000000000
    
        print(digits[d9], end = " ")
        print("Billion", end = " ")
        if d08:
            millions(d08)
    elif n // 10000000000 in range(0, 10):
        d910 = n // 1000000000
        d09 = n % 1000000000
        
        under_100(d910)
        print("Billion", end = " ")
        if d08:
            millions(d08)
    elif n // 100000000000 in range(0, 10):
        d91011 = n // 1000000000
        d08 = n % 1000000000
        
        hundreds(d91011)
        print("Billion", end = " ")
        if d08:
            millions(d08)
    
def switch(n):
    l = len(str(n))
    
    if l == 1 or l == 2:
        under_100(n)
    elif l == 3:
        hundreds(n)
    elif l in range (4, 7):
        thousands(n)
    elif l in range (7, 10):
        millions(n)
    elif l in range (10, 13):
        billions(n)
    else:
        print("Range crossed. Sorry! Try again.", end="")

def main():
    while True:
        n = int(input("Enter a number (positive or negative):\n>> "))
    
        if n >= 0:
            switch(n)
        else:
            print("Minus", end = " ")
            switch(abs(n))
        print("\n")
                
if __name__ == "__main__":
    main()