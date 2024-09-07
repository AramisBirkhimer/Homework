"""
Aramis Birkhimer
Hw 4
09/06/2024
"""

print("\nProblem 2d: \n")

#import necessary modules
import numpy as np

#import custom functions
from module_template_with_docstring import square
from module_template_with_docstring import squareplot

#make test list containing integers from 1-9
test_square_1 = [i for i in range(1, 10, 1)]

#print test list for clarity
print(test_square_1)
print("\n")

#pass test list to function and assign return value to variable x
x = square(test_square_1)

#print x
print(x)
print("\n")

#make second test variable, generate 5x5 array of floats from 0-25
test_square_2 = np.linspace(0,25,25).reshape(5,5)


#print second test variable for clarity
print(test_square_2)
print("\n")

#pass test_square_2 to function square and assign return value to x
x = square(test_square_2)

#print x
print(x)
print("\n")

#call squareplot
squareplot(1, 7, 5, "SquarePlot.pdf")