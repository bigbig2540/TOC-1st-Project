# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:29:54 2017

@author: Malikoto
"""

import csv
import numpy as np


#x = np.array([0,1,2,3,4,5])
#
#y = np.array([2.1, 2.9, 4.15, 4.98, 5.5, 6])
#
#z = np.polyfit(x, y, 1)
#p = np.poly1d(z)
#
##plotting
#import matplotlib.pyplot as plt
#xp = np.linspace(-1, 6, 100)
#plt.plot(x, y, '.', xp, p(xp))
#plt.show()

with open('LS.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
  print(your_list)