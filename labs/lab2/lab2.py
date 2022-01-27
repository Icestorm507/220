"""
Dylan Benton Embrey
1/26/2022
Computer Programming Labs 2: Means
This is my work.
"""
# This will import math functions
import math


# function definition to find the root-mean-square value
def findrms(num_list):
    length = len(num_list)
    square = 0
    mean = 0.0
    root = 0.0
    # Calculate square
    for i in range(0, length):
        square = square + (num_list[i] ** 2)
    # Calculate Mean
    mean = (square / float(length))
    # Calculate Root
    root = math.sqrt(mean)
    return root


# Function Definition to find the Geometric mean
def findgm(num_list):
    length = len(num_list)
    # declare product variable and initialize it to 1.
    product = 1
    # Compute the product of all the elements in the array.
    for i in range(0, length):
        product = product * num_list[i]
    # compute geometric mean through formula pow(product, 1/n)
    GM = float(math.pow(product, (1 / length)))
    return float(GM)


# function Definition to find the Harmonic mean
def findhm(num_list):
    length = len(num_list)
    # Declare sum variables and initialize with zero.
    add = 0
    for i in range(0, length):
        add = add + 1 / num_list[i]
    return length / add


# Driver Code
if __name__ == '__main__':
    num_list = []
    # Input the total number of values
    number = int(input("Enter the values to be entered: "))
    # Input the elements
    for i in range(0, number):
        element = int(input("Enter Value: "))
        num_list.append(element)
    # Function calling for RMS
    RMS = findrms(num_list)
    # Function Calling for GM
    GM = findgm(num_list)
    # Function Calling for HM
    HM = findhm(num_list)
    # Print the RMS,GM and HM unto 3 decimal places
    print("Root Mean Square : ", round(RMS, 3))
    print("Harmonic Mean : ", round(HM, 3))
    print("Geometric Mean : ", round(GM, 3))
