#Python libraries for math and graphics
import numpy as np
import math 
import matplotlib.pyplot as plt
from numpy import linalg as LA
from scipy.integrate import quad
import math as mp
import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/Line/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if
# input parameter
a=input("enter X^2 coordinate")
b=input("enter y^2 coordinate")
c=input("enter x coordinate")
d=input("enter y coordinates:")
f=input("enter constant")
#generating directrix
Y=np.array(([1,0]))
#c=-2
c=-p/2
e1=np.array(([1,0]))
#points on the line
x1=c/(Y@e1)
A1=x1*e1
#direction vectors
m1=omat@Y
#generation of line
k1=-4
k2=4
X_EF=line_dir_pt(m1,A1,k1,k2)
#generating circle
#Input parameters
#p = 4
#r2 = 2*r1
O = np.array(([p/2,0]))

theta = mp.pi/2
A = p*(np.array(([mp.cos(theta/3),mp.sin(theta/3)])))
B = p*(np.array(([-mp.cos(theta/3),mp.sin(theta/3)])))

##Generating all lines
x_circ1 = circ_gen(O,p)

#Points of intersection of a conic section with a line
m=np.array(([0,1]))
V=np.array(([a,0],[0,b]))
u=np.array(([c/2,d/2]))
f=f
D_val,P=eigen(V)
q=np.array(([b,d]))
p1,p2=inter_pt(m,q,V,u,f)
print(p1)
print(p2)


##Plotting all lines
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(X_EF[0,:],X_EF[1,:],label='$directrix$')
#  plotting parabola
simlen=100
a=8
y= np.linspace(-5,5,simlen)
x = (y**2)/8
plt.plot(x, y, label='Parabola')
#Labeling the coordinates
tri_coords = np.vstack((O.T,p1.T,p2.T))
plt.scatter(tri_coords[:,0], tri_coords[:,1])   
vert_labels = ['O','p1','p2']
for i,  txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[i,0], tri_coords[i,1]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#if using termux
plt.savefig('/sdcard/Download/Conic/figure1/fig8.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/Conic/figure1/fig8.pdf"))
plt.show()
