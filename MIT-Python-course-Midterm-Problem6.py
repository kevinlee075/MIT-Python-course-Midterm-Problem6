# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:48:36 2021

@author: Lenovo
"""

#Implement a function that meets the specifications below.
#For example,
#max_val((5, (1,2), [[1],[2]])) returns 5.
#max_val((5, (1,2), [[1],[9]])) returns 9.

def max_val(t): 
    """
    t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t
    """
    