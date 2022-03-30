# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Array is:\n",arr)
print("Display all elements excluding first row :\n",arr[1:4])
#print("Display all elements excluding last column:",arr[0:3])
#print("Display all elements excluding last column:",arr[1:3,1:3])
#print("Display all elements excluding last column:",arr[0:4,1:4])
print("Display all elements excluding last column:\n",arr[0:4,0:3])
