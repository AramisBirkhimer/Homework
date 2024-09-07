"""

This is the docustring for the module template. I am editing it to be more
appropriate for my current assignment. I only need to find the square of 
an integer, so I don't need many modules. 

"""

import os # standard library imports first
import numpy as np
import matplotlib.pyplot as plt

#Problem 2d:
#then write your functions
def square(x) :
    #this is our function's docstring!
    
    #convert input to numpy array
    y = np.array(x)
    
    #raise input to second power and return value
    return np.power(y, 2)
        
    """
    Example
    -------
    
    problem 2e: provide examples
    
    >>>print(square(9))
    81
    
    >>>print(square([2,4,6]))
    [4, 16, 36]
    
    >>>print(square([2.5, 4.5, 6.5, 8.5]))
    [6.25, 20.25, 42.25, 72.25]
    
    >>>print(square("notanum"))
    TypeError: Input must be integer or list
    
    >>>test_squre_2 = np.linspace(0,25,25).reshape(5,5)
    >>>print(square(test_square_2))
    [[  0.           1.08506944   4.34027778   9.765625    17.36111111]
     [ 27.12673611  39.0625      53.16840278  69.44444444  87.890625  ]
     [108.50694444 131.29340278 156.25       183.37673611 212.67361111]
     [244.140625   277.77777778 313.58506944 351.5625     391.71006944]
     [434.02777778 478.515625   525.17361111 574.00173611 625.        ]]
    
    
    """
        
    #close function    
    pass




#problem 3:
    
def squareplot(low, high, step, saveplot) :
    
    #import square function
    from module_template_with_docstring import square
    
    """
    make array of values beginning at the low end, that includes the high end
    in the specified number of steps.
    """
    array = np.linspace(low, high, step)
    
    #pass array to square function
    y = square(array)
    
    #plot result with appropriate labels
    plt.plot(array,y, label = "y = x^2")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Square Function")
    plt.grid(True)
    
    #save plot if user asks
    if saveplot:
        plt.savefig(saveplot, format = "pdf")
    
    #display plot
    plt.show()
    
    """
    Example
    -------
    
    >>>squareplot(1, 7, 5, "SquarePlot.pdf")
    <Plot of squared values>
    
    """
    
    
    pass
    