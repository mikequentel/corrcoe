#!/usr/bin/python

# corrcoe.py 
# author Mike Quentel

import csv
from math import sqrt

filename = 'xyvals.csv'

n = 0
sum_x = 0.0
sum_y = 0.0
sum_xy = 0.0
sum_x_squared = 0.0
sum_y_squared = 0.0

print "x" + "\t\t" + "y" + "\t\t" + "xy" + "\t\t" + "x^2" + "\t\t" + "y^2"
print ""

with open(filename, 'rb') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    
    n += 1
    x = float(row[0])
    y = float(row[1])
    xy = x * y
    x_squared = x**2
    y_squared = y**2
    
    sum_x += x   
    sum_y += y
    sum_xy += xy
    sum_x_squared += x_squared
    sum_y_squared += y_squared
    
    print str(round(x, 2)) + "\t\t" + str(round(y, 2)) + "\t\t" + str(round(xy, 2)) + "\t\t" + str(round(x_squared, 2)) + "\t\t" + str(round(y_squared, 2))

r =  ((n * sum_xy) - (sum_x * sum_y))/((sqrt((n * sum_x_squared) - (sum_x**2))) * (sqrt((n * sum_y_squared) - (sum_y**2))))

m = ((n * sum_xy) - (sum_x * sum_y))/((n * sum_x_squared) - (sum_x**2))

b = ((sum_x_squared * sum_y) - (sum_x * sum_xy))/((n * sum_x_squared) - (sum_x**2))

print "------------------------------------------------------------------------------"
print str(round(sum_x, 2)) + "\t\t" + str(round(sum_y, 2)) + "\t\t" + str(round(sum_xy, 2)) + "\t\t" + str(round(sum_x_squared, 2)) + "\t\t" + str(round(sum_y_squared, 2))
print ""
print "NUMBER OF ITEMS n = " + str(n)
print ""
print "CORRELATION COEFFIECIENT r = " + str(r)
print ""
print "SLOPE m = " + str(m)
print ""
print "Y-INTERCEPT b = " + str(b)
print ""
print "LEAST SQUARES EQUATION (y = mx+b) is: \t" + "y = " + str(m) + "x + " + str(b)
