"""
Aramis Birkhimer
Hw 4
09/06/2024
"""

#import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import random
from astropy.io import fits


#import custom functions
from module_template_with_docstring import square
from module_template_with_docstring import squareplot


print("\nProblem 2h: \n")

#make test list containing integers from 1-9
test_square_1 = [i for i in range(1, 10, 1)]

#pass test list to function and assign return value to variable x
x = square(test_square_1)

#print x
print(x)
print("\n")

print("\nProblem 2i: ")

#make second test variable, generate 5x5 array of floats from 0-25
test_square_2 = np.linspace(0,25,25).reshape(5,5)

#pass test_square_2 to function square and assign return value to x
x = square(test_square_2)

#print x
print(x)
print("\n")


print("\nProblem 3: see plot\n")

#call squareplot
squareplot(1, 7, 5, "SquarePlot.pdf")

print("\nProblem 4: \n")

# Step 1: Create the 300x200 Float64 array with y-coordinate values
rows, cols = 300, 200
array = np.arange(rows, dtype=np.float64).reshape(rows, 1) * np.ones(cols, dtype=np.float64)
print("Array Dimensions:", array.shape)
print("Array data type:", array.dtype)
print("\n")

# Step 2: Display the array using matplotlib with 'gray' colormap
plt.imshow(array, cmap='gray', origin='lower')
plt.show()

# Print random elements for verification
for i in range(5):
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    print(f"Value at ({row}, {col}):", array[row, col])
    
print("\nProblem 5:\n")

with fits.open('m42_40min_ir.zip') as hdul:
    hdul.info()
    
    primary = hdul[0]
    
    print(primary.header)
    
    data = primary.data
    print("data dimensions:", data.shape)
    
    plt.imshow(data, cmap='gray')
    plt.title('M42 - ABIRK')
    plt.savefig("m42 Image.png", format = "png")
    plt.show()
    