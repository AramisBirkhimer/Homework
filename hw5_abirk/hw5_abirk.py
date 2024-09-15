"""
Homework Assignment 5

Aramis Birkhimer

09/13/2024
"""

#import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.stats import norm
import random

#begin code
print("\nProblem 2a: \n")

"""
Find a Python function that draws a random sample of N draws from
a Gaussian distribution of width σ and mean 𝑥̅ . Use it to make a sample of
10,000-draws (i.e., N=10,000) from a population with width σ = 13 and mean 𝑥̅ =
55.
"""

#use numpy library's random and normal functions to generate an array of 10,000
#random values with mean 55 and std 13
rand_sample = np.random.normal(55, 13, 10000)

#print the mean and std to check the array for accuracy
print(f"\nSample mean: {np.mean(rand_sample)}\n")
print(f"Sample STD: {np.std(rand_sample)}\n")

print("\nProblem 2b: \n")

"""
Plot the histogram of your sample. The histogram should have bins
from 0 to 100 with a width of 1 unit. Make sure to make a publication-ready plot
(with axis labels and a title). Save it as a PNG file using the appropriate Python
command. Remember to name your PNG appropriately.
"""

#plot histogram with data generated in previous question with 100 bins
plt.hist(rand_sample, bins = 100)
#give plot appropriate titles and axis labels
plt.title("Histogram of Gaussian Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
#display plot
plt.show()

print("\nProblem 2c: \n")

"""
Now use the Gaussian function to overplot a Gaussian distribution
with the same 𝑥̅ and σ as your histogram. Approximate the integration between
the bin boundaries by just evaluating the Gaussian at the center of each bin (e.g.,
for bin [-1,-0.8] you will evaluate the Gaussian at x =-0.9).
Remember that the analytic Gaussian distribution, integrated over each bin,
gives you the expected number of draws in each bin for a single draw from the
parent population (i.e., much less than one draw per bin on average, in contrast
to your histogram from parts a and b). If you thus try to plot your function “as is”
versus the histogram you will not see them aligning properly. To fix this, you
need to multiply your function by the total number of draws N to get the expected
number of draws per bin for a larger sample and get the plot correctly.
"""

# Calculate bin edges and centers
bin_edges = np.linspace(0, 100, 101)  
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Compute the Gaussian PDF at the bin centers
pdf_values = norm.pdf(bin_centers, 55, 13)

# Scale the PDF to match the histogram
pdf_values_scaled = pdf_values * 10000 

# Plot histogram and Gaussian PDF
plt.figure()
plt.hist(rand_sample, bins=100)
plt.plot(bin_centers, pdf_values_scaled)

# Add titles and axis labels
plt.title("Histogram with Gaussian Fit")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Save the plot as a PNG file
plt.savefig("hw5_abirk_figure1.png")

# Display the plot
plt.show()

print("\nProblem 3a: \n")
"""
Use your code to create a sample with N=10 random draws. Do this
10 times (remember, don’t repeat the same command!). For each sample, record
the sample number (0 to 9), the sample mean, and the sample standard
deviation in an array with one row per sample. Do not include the actual values of
the samples in your array. At the end you should have a 10 by 3 array with each
line corresponding to one of your samples.

Use the appropriate Python commands to write the array into a text file.
Remember to name the output file following the homework formatting naming
conventions.
In your output file, before the table, include a comment stating the number of
draws in the table. Be careful to not overwrite your previous entries on the file
when you access it to write a new result!
"""

#initialize record
sample_record = []

#start loop
for i in range(10):
    #pick 10 random values with mean 55 and std 13
    rand_sample = np.random.normal(55, 13, 10)
    
    # find mean and std for the random pick
    sample_mean = np.mean(rand_sample)
    sample_std = np.std(rand_sample)
    
    #add data from current pick to sample record
    sample_record.append([i, sample_mean, sample_std])
    
#make sample_record a numpy array
sample_record = np.array(sample_record)

#print sample record and array shape to verify accuracy
print("Sample Record: \n", sample_record)
print(f"\nSample record shape: {np.shape(sample_record)}")

file_name = "hw5_abirk_Problem3a.txt"

with open(file_name, 'a') as file:
    #write comment about sample size
    file.write("Draws/sample (N) = 10\n")
    
    #write data
    np.savetxt(file, sample_record, fmt='%d\t %.4f\t %.4f', header = 'Sample number --> Mean --> Std')
    file.write("\n\n\n-----End Entry\n\n")
    
    #close file
    file.close()
    
print("\nProblem 3b: \n")

"""
Repeat (a) for samples with N=100, 1,000, 10,000, 100,000, and
1,000,000 draws. Remember that you will need to do 10 repetitions for each of
these sample sizes! Record each set of results in a separate 2D array and
append them to the same file as in (a)
"""

# for five iterations
for i in range(5):
    
    #initialize record for each N value
    sample_record = []
    
    #calculate N
    N = 100*10**i
    
    # Generate 10 samples with current N
    for j in range(10):
        # generate N random picks with mean 55 and std 13
        rand_sample = np.random.normal(55, 13, N)
        
        #find mean and std
        sample_mean = np.mean(rand_sample)
        sample_std = np.std(rand_sample)
        
        #append current pick results to record list
        sample_record.append([j, sample_mean, sample_std])

    # Convert record list to numpy array
    sample_record = np.array(sample_record)

    # Write to file with appropriate formatting
    file_name = "hw5_abirk_Problem3b.txt"
    with open(file_name, 'a') as file:
        file.write(f"Draws/sample (N) = {N}\n")
        np.savetxt(file, sample_record, fmt='%d\t %.4f\t %.4f', header='Sample number --> Mean --> Std')
        file.write("\n\n\n-----End Entry\n\n")


        
print("\nProblem 3c: \n")

"""
Now, you will find the standard deviation of the means for each of the
six sample sizes you run in (a) and (b).
To do this, read in the data you generated in (a) and (b) and use an appropriate
Python function to find the standard deviation of the means for each sample size.
Then, print the sample size and its calculated standard deviation both on the
screen and in your .txt (or.dat) file from parts (a) and (b) with an appropriate
comment. Be careful to append the data to the file and not overwrite the existing file!
"""

# Define function to read files and find std of means
def calculate_std_of_means(filename, sample_sizes):
    std_of_means = []

    for N in sample_sizes:
        # Read the data from file
        data = np.loadtxt(filename, skiprows=1, max_rows=10)
        means = data[:, 1]
        std_dev_of_means = np.std(means)
        std_of_means.append((N, std_dev_of_means))

    return std_of_means

std_a = calculate_std_of_means("hw5_abirk_Problem3a.txt", [10])
std_b = calculate_std_of_means("hw5_abirk_Problem3b.txt", [100, 1000, 10000, 100000, 1000000])

with open("hw5_abirk_Problem3a.txt", "a") as file:
    file.write("STD of means: \n")
    for N, std in std_a:
        file.write(f"Draws/sample = {N}, STD of Means: {std:.4f}\n")
    file.close()
    
with open("hw5_abirk_Problem3b.txt", "a") as file:
    file.write("STD of means: \n")
    for N, std in std_b:
        file.write(f"Draws/sample = {N}, STD of Means: {std:.4f}\n")
    file.close()















