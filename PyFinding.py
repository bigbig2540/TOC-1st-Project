# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:18:02 2017

@author: Malikoto
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt
 
def withinCircle(x,y):
    if(x**2+y**2<1):
        return True
    else:
        return False
 
pi_avg = 0
sampleNumber = 10


fig = plt.figure()
axis = fig.add_subplot(1,1,1)
circle = plt.Circle((0,0), 1)
axis.add_patch(circle)
axis.set_xlim([-1,1])
axis.set_ylim([-1,1])
axis.set_title('GraphSimulator')

#for sample in range(0,sampleNumber):
#    circleArea = 0
#    squareArea = 0
#    pi = 0
#    for i in range(0,500000):
##        x = random.random()
##        y = random.random()
#        x = random.uniform(-1,1)
#        y = random.uniform(-1,1)
#        if(withinCircle(x,y)==1):
#                   circleArea=circleArea+1
#                   plt.plot(x,y,'ro',color = 'red')
#        squareArea=squareArea+1
#        plt.plot(x,y,'ro',color = 'green')
#    pi = 4.0*circleArea/squareArea
#    print ("Approximate value for pi sampleNo. ",sample, " : " , pi)
#    pi_avg = pi_avg + pi
#pi_avg = pi_avg/sampleNumber
#print ("Approximate value for pi: ", pi_avg)
#print ("Exact value of pi: ", math.pi)
#print ("Difference to exact value of pi: ", pi_avg-math.pi)
#print ("Error: (approx-exact)/exact=", (pi_avg-math.pi)/math.pi*100, "%")
    
circleArea = 0
squareArea = 0
pi = 0
for i in range(0,1000000):
#        x = random.random()
#        y = random.random()
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if(withinCircle(x,y)==1):
               circleArea=circleArea+1
               plt.plot(x,y,'ro',color = 'red')
    else:
        plt.plot(x,y,'ro',color = 'green')
    squareArea=squareArea+1
pi = 4.0*circleArea/squareArea
print ("Approximate value for pi sampleNo. : ", pi)


plt.show()


