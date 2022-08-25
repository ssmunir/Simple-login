# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:37:01 2022

@author: ACER
"""

username = input("What is your name?\n")
allowedUsers = {'Munir'}
allowedPassword = "1234"

if (username in allowedUsers):
    password = input("Your Password\n")
    
    if(password == allowedPassword):
        print("Welcome Munir")
        print("These are your available python files:")
        print("1. whirlwind_tour.py")
        print("2. PDSH.py")
        print("3. functions.py")
        print("4. Wanna do something else?")
        
        selectedOptions = int(input("Please select an option \n"))
        
        if (selectedOptions == 1):
            print("1. Read this file?")
            print("2. Edit this file?")
            
            choice = int(input("Make a choice \n"))
            
            if (choice == 1):
                open(file = "whirlwind_tour.py", mode='r')
            else:
                open(file = "whirlwind_tour.py", mode = 'a')
        elif(selectedOptions == 2):
            print("1. Read this file?")
            print("2. Edit this file?")
            
            choice = int(input("Make a choice \n"))
            
            if (choice == 1):
                open(file = "PDSH.py", mode='r')
            else:
                open(file = "PDSH.py", mode = 'a')
        elif(selectedOptions == 3):
            print("1. Read this file?")
            print("2. Edit this file?")
            
            choice = int(input("Make a choice"))
            
            if (choice == 1):
                open(file = "functions.py", mode='r')
            else:
                open(file = "functions.py", mode = 'a')
        elif(selectedOptions == 4):
            print("1. Calculate Binomial Probability?")
            print("2. Get help docstring on any function?")
            print("More options coming soon")
            
            choice = int(input("Make a choice\n"))
            
            if (choice == 1):
                value = int(input("Number of trials\n"))
                value1 = int(input("Value of x\n"))
                value2 = float(input("Probability of success\n"))
                value3 = float(input("Probability of failure\n"))
                
                from math import factorial

                def comb(n, k):
                    if n < 0:
                        raise ValueError("n must be positive")
                    elif k < 0:
                        raise ValueError("k must be positive")
                    combination = factorial(n)/(factorial(k)*factorial(n-k)) 
                    return combination

                def binom(n, k, p, q):
                    binomial = comb(n, k) * (p**k) * (q**(n-k))
                    mean = n * p
                    var = n * p * q
                    """ 
    Funtion BINOM(): 
        Gives the binomial probability of k successes
    args:
        n: number of trials 
        k: value of x
        p: probability of success
        q: probability of failure
    return:
        int
        """
                    print(binomial, "is the probability")
                    print(mean, "is the mean")
                    print(var, "is the variance")
                pass
                b = binom(value, value1, value2, value3)
                print(b)
            elif (choice == 2):
                print('Please enter function name')
                
                import inspect 
                def tooltip(function):
                    docstring = inspect.getdoc(function)
                    border = '#' * 28 
                    """ Create a tooltip for any function that shows the function's docstring.
    
    Args:
        function (callable): The function we want a tooltip for.
        
    Returns:
        str
    """
                    return '{}\n{}\n{}'.format(border, docstring, border)
                pass
                print(tooltip(input()))
                    
        else:
            print("Invalid option selected")
            
            
    else:
        print("Password incorrect, please try again")
else:
    print("Name not found, please try again")
       