# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYAGLEL_zHz9AfMLG9xUbEYvRsDG-n58
"""

#plotting the triangle
import matplotlib.pyplot as plt 
x = [0,2,4,0,1,3]
y = [0,4,0,0,2,2]
plt.style.use("seaborn-whitegrid")
plt.plot(x,y, color="black")
#marking points on the triangle
plt.annotate("A",(2,4),weight='bold',horizontalalignment='right',verticalalignment='bottom')
plt.annotate("B",(0,0),weight='bold',horizontalalignment='right',verticalalignment='bottom')
plt.annotate("C",(4,0),weight='bold',horizontalalignment='left',verticalalignment='bottom')
plt.annotate("D",(1,2),weight='bold',horizontalalignment='right',verticalalignment='bottom')
plt.annotate("E",(3,2),weight='bold',horizontalalignment='left',verticalalignment='bottom')
plt.show()
plt.savefig("triangle.png")

