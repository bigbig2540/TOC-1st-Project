# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:21:33 2017

@author: Malikoto
"""
import random
import math
import matplotlib.pyplot as plt

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
circle = plt.Circle((0,0), 1)
axis.add_patch(circle)
axis.set_xlim([-1,1])
axis.set_ylim([-1,1])
axis.set_title('A Circle in a Square')

plt.plot(0.5,0.3,'ro',color = 'red')
plt.plot(0.5,1,'ro',color = 'red')

plt.show()