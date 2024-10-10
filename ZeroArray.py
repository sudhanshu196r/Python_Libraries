'''
    @Author: Sudhanshu Kumar
    @Date: 10-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 10-10-2024
    @Title : Python program to create 

'''

import numpy as np

def create(size,index):
    """
    Description:
        This function will create numpy array with 0 and change value at index
    Parameters:
        size: size of array
        index: index at which value has to be changed
    Returns: numpy array

    """

    np_array = np.zeros(size)
    np_array[index] = 22
    return np_array

def main():
    size = int(input("Enter size of numpy array: "))
    index = int(input("Enter index at which value needs to be changed"))
    print(create(size,index))

if __name__=="__main__":
    main()

