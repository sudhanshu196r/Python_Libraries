'''
    @Author: Sudhanshu Kumar
    @Date: 10-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 10-10-2024
    @Title : Python program to create numpy array within particular range

'''

import numpy as np

def createArray(l,h):
    """
    Description:
        This function will create numpy array within particular range
    Parameters:
        l: lower limit
        h: higher limit
    Returns: A numpy array
    """

    np_array = np.arange(l,h+1).reshape(3,3)
    return np_array

def main():
    l = int(input("ENter lower range"))
    h = int(input("Enter higher range"))
    print(createArray(l,h))

if __name__=="__main__":
    main()
