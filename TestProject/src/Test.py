import numpy as np
'''
@author:                     Jasper van Bemmelen
@studentnumber:     2653840
Created on 18 aug. 2018
'''

x = np.array([[20., 10.], [10., 20.]])
y = np.linalg.inv(x)

print(x@y)

print(np.linalg.solve(x, np.ones((2,2))))