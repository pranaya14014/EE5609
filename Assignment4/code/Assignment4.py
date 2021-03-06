# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10SsWeFWTzbjnejtv0DyEcQJnUZ6UEVSS
"""

import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
# Given pair of straight line equation x**2 + 6xy + 9y**2 + 4x + 12y - 5 = 0
n1 = np.array([1,3])
n2 = np.array([1,3])
l=np.linalg.norm(n1)
m=np.linalg.norm(n2)
n = np.dot(n1,n2)
theta = int(np.arccos(n/(l*m)))  # cos(theta) = (n1.n2)/(||n1||.||n2||)
print("The angle beteen the lines:",theta)
print('Hence the lines are parallel')

# generating the points lying on the given points
# generating the 50 of x-points between -10 to 10
x = np.linspace(-10,10,50)   
y1 = (1/3)*(-x +1) # using (1 3)x=1
y2 = (1/3)*(-x-5)  # using (1 3)x=-5

#Plotting:
plt.style.use("seaborn-whitegrid")
plt.plot(x,y1,label="line 1: (1 3)x=1")
plt.plot(x,y2,label="line 2: (1 3)x= -5")
plt.legend()
plt.show()
plt.savefig('Straight_lines.png')
