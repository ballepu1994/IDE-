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
from sympy import *
#if using termux
import subprocess
import shlex
#end if
# input parameter
p=4
#parabola Conic parameters
V=np.array(([0,0],[0,1]))
u=np.array(([-p],[0]))
f=0
D_val,P=LA.eig(V)
lam1=D_val[0]
lam2=D_val[1]
P1=P[:,0].reshape(2,1)
P2=P[1,:].reshape(2,1)
e=np.sqrt(1-(lam1/lam2))
n=np.sqrt(lam2)*P1
c=(LA.norm(u)**2-lam2*f)/(2*u.T@n)
F=(c*e**2*n-u)/(lam2)

##for circle
V1=np.eye(2)
u1=-F
r=(n.T@F-c)/LA.norm(n)
f1=LA.norm(u1)**2-r**2

#for conics point of contact
mu1=symbols(('mu1'))
V2=np.add(V1,mu1*V)
u2=np.add(u1,mu1*u)
f2=np.add(f1,mu1*f)
A=np.block([[V2],[u2]])
A1=np.block([[u2.T],[f2]])
A2=np.block([[A],[A1]])
A3=Matrix(A2)
eq=A3.det()
eq1=Eq(eq,0)
A4=solve(eq1,mu1)
mu2=A4[0]

V2=np.add(V1,mu2*V)
u2=np.add(u1,mu2*u)
f2=np.add(f1,mu2*f)

q=np.array([p/2,-3*p/2]).reshape(2,1)
m=np.array([0,1]).reshape(2,1)

kk2=m.T@V1@m
kk1=m.T@(V1@q+u2)
kk=(kk1**2-(q.T@V1@q+2*u1.T@q+f1)*(kk2))
kk=np.sqrt(float(kk[0]))
k1=(-kk1+kk)/kk2
k2=(-kk1-kk)/kk2

Aa=q+k1*m
Bb=q+k2*m
print(Aa,Bb)

def parab_gen(y,p):
	x = y**2/(2*p)
	return x

y=np.linspace(-5,5,100)
x=parab_gen(y,p)
E1=np.array([-p/2,0]).reshape(2,1)
x1=line_dir_pt(omat@n,E1,-5,5)
x_circ=circ_gen(F.T,r)
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')
plt.plot(x,y)
plt.plot(x1[0,:],x1[1,:]) 
#Labeling the coordinates
tri_coords = np.vstack((F.T,Aa.T,Bb.T)).T
#print(tri_coords)
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['F','A','B']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('/sdcard/Download/Conic/figure1/fig6.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/Conic/figure1/fig6.pdf"))
plt.show()
