""" 
Aramis Birkhimer
Hw 3 - Python refresher 
09/01/2024
"""

#import relevant packages 
import numpy as np
import matplotlib.pyplot as plt

print("Problem 2a: \n")

#make array
x = np.arange(0, 1001)

# print values of x using numpy commands

#array size
print(f"Number of elements: {x.size}")

#array type
print(f"Data type: {x.dtype}")

#min and max values of array
print(f"Min: {x.min()}")
print(f"Max: {x.max()}")

print("\nProblem 2b: \n")

#define variables for resizing formula 
newmin = 0
newmax = 2*np.pi
oldmin = 0
oldmax = 1000

#apply formula to resize array x
x = newmin + (x-oldmin) * (newmax-newmin)/(oldmax-oldmin)

#print resized values of array x
print(f"Resized min: {x.min()}")
print(f"Resized max: {x.max()}")

print("\n problem 2c:\n")

# define array y as the sin() of all x values
y = np.sin(x)

#print new minimum and maximum values
print(f"Min y: {y.min()}")
print(f"Max y: {y.max()}")

print("\nProblem 2d: \n")

#print element 234 of array y. since the first array value is 0 in python we reduce the element number by 1.
print(f"Element 234 of y: {y[233]}")

print("\nProblem 3a: \n")

# Plot the x values vs the y values and add appropriate labels
plt.plot(x,y)
plt.xlabel("X values [0, 2*pi]")
plt.ylabel("Y values: sin(x)")
plt.title("Plot of sin(x); x = [0, 2pi]")

print("\nProblem 3b: \n")

#save figure as PNG (default format)
plt.savefig("hw3_abirk_problem3b_plot1")

print("\nProblem 4a: \n")

#make ramp array with 101 values between -1 and 1
ramp = np.linspace(-1,1,101)

#clip array to values between -.5 and .5
clip = np.clip(ramp, -0.5,0.5)

#print array
print(f"Clipped array: {clip}")

print("\nProblem 4b: \n")

# plot clipped and ramp arrays together with appropriate labels and title
plt.figure()
plt.plot(ramp)
plt.plot(clip)
plt.xlabel("x values")
plt.ylabel("Y values")
plt.title("Plots of ramp and clipped arrays")

#save plot with appropriate file name
plt.savefig("hw3_abirk_problem4b_plot2")

print("\nProblem 5:\n")

print("https://sourceforge.net/projects/spacepy/")
print("https://sourceforge.net/projects/fabs/")

"""
SpacePy: 
    SpacePy is a beta software written in python. The website describes
it as a space science library for python that contains lots of data about space
and space related phenomena such as magnetic field models. 
    
    
FABS: 
    FABS is an open source spectral analysis tool written in python. This 
    package allows for quick and easy analysis of spectra retreived from space
    telemetry to understand the properties of deep space objects. FABS can also
    use data from any video or image file, so you can take spectra using your 
    cell phone. This software is designed for students to help with projects. 
"""
