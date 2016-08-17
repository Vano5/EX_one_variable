import sys
import scipy.optimize, scipy.special
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py




data=scipy.genfromtxt('F:\EPAM\coursera\ML_COURSERA_GARVARD\machine-learning-ex2\ex2\ex2data2.txt',delimiter=',')

def plotData(data):
    
    pozitive=data[data[:,2]==1]
    negative=data[data[:,2]==0]
    plt.scatter( negative[:, 0], negative[:, 1], c='y', marker='o', s=40, linewidths=1, label="Not admitted" ) 
    plt.scatter( pozitive[:, 0], pozitive[:, 1], c='b', marker='+', s=40, linewidths=2, label="Admitted" ) 
    plt.legend() 
    

def segmoid (z):
    return scipy.special.expit(z)
    
    
def mapFeature(x1,x2):
    degree=6
    out=np.ones( (np.shape(x1)[0],1) )
    c=0   
    for i in range(1,degree+1):
        for j in range(0,i+1):
            c=c+1
            val1=x1**(i-j)
            val2=x2**(j)
            #val0=(val1*val2)
            val=(val1*val2).reshape(np.shape(val1)[0],1)
            out   = np.hstack(( out, val ))
    return out
def computeCost(x,y,theta,lamda):
    m=np.shape(x)[0]
    h=segmoid(x.dot(theta))
    val1=-np.log(h).dot(y)
    val2=
    
    
    
    
    
    
    
    
print mapFeature(np.array([2,3]),np.array([3,4]))
                     
    
    
          
print    plotData(data) 