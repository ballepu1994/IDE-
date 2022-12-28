import numpy as np
import mpmath as mp
import math as m
import random as r
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sympy as sym
import math
import sympy
import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/sdcard/Download/Line/CoordGeo')


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from sympy import Poly,roots,simplify
from sympy import*
#if using termux
import subprocess
import shlex
#end if

#Defining f(x)
def f(x,b,r):
 return (b*(x**3)*r-(x**4))
b=2
r=0.84
label_str = "$.$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: (6*x**2*r)-(4*x**3)             

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

max_val = f(cur_x,b,r)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(0,2,10)
y=f(x,b,r)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.grid()
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/sdcard/Download/Optia/fig/optia.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/Optia/fig/optia.pdf"))
plt.show()
