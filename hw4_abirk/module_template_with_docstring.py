"""

This is the docustring for the module template. I am editing it to be more
appropriate for my current assignment. I only need to find the square of 
an integer, so I don't need many modules. 

"""

import os # standard library imports first
import numpy as np

#then write your functions
def square(x) :
    #this is our function's docstring!
    
    #begin testing input and operating on the input if it is suitable.
    
    #if input is an integer
    if isinstance(x, int):
        
        #return square of integer
        return x * x
    
    #if input is list, and all items in the list are integers
    elif isinstance(x, list) and all(isinstance(i, (int, float)) for i in x):
        
        #square and return all items in list 
        return [i * i for i in x]
    
    #if neither instance is satisfied
    else:
        
        #raise error message about incorrect input
        raise TypeError("Input must be integer or list")
        
    """
    Example
    -------
    
    >>>print(square(9))
    81
    
    >>>print(square([2,4,6]))
    [4, 16, 36]
    
    >>>print(square([2.5, 4.5, 6.5, 8.5]))
    [6.25, 20.25, 42.25, 72.25]
    
    >>>print(square("notanum"))
    TypeError: Input must be integer or list
    
    """
        
    #close function    
    pass
