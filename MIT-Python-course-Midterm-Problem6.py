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
    def next_level_collection(element_t):
        '''
        define another function in which all elements of element_t
        become int
        '''
        comparison_list = []                                                   #use an empty list first
        
        for item in element_t:                                                 #check every element in the variable list
            if type(item) == int:                                              #if a certain element is int, add it to the comparison_list 
                comparison_list.append(item)
                
            else:                                                              #if a certain element is list or other types, use the recursion method for this function
                comparison_list += next_level_collection(item)
                
        return comparison_list
    
    
    new_list = next_level_collection(t)                                        #make t using the next_level_collection function to change all elements to int
    max_elem = max(new_list)                                                   #search the maximal int in the new_list
    
    return max_elem
    
    
    