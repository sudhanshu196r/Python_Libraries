'''
@Author: Sudhanshu Kumar
@Date: 10 - 10 - 2024
@Last Modified by: Sudhanshu Kumar
@Last Modified time: 10 - 10 - 2024
@Title: Python program to convert a list of numbers to numpy array

'''


import numpy as np

def convert(lst):
    """
    Description:
        This function will convert list to numpy array
    Parameters:
        lst: a list which has to be converted to numpy array
    Returns: A numpy array
    """
    np_array = np.array(lst)
    return np_array

def main():
    lst = [23, 45, 90.4, 39, 1, 4.5, 3]
print(convert(lst))

if __name__ == "__main__":
    main()