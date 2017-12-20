import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from collections import Counter

#Problem: completar o vetor mais curto com 1s

def plot_pdf(expectedMutations,observedMutations,lamb,log_location):

    x_axis=[]
    y_axis=[]
    observed = Counter(observedMutations)
    for item in observed:
        x_axis.append(item)
        y_axis.append(float(observed[item])/len(observedMutations))

    u_axis=[]
    v_axis=[]
    expected = Counter(expectedMutations)
    for item in expected:
        u_axis.append(item)
        v_axis.append(float(expected[item])/len(expectedMutations)) 

    p1=plt.step(x_axis,y_axis,linestyle='-',color='k',linewidth=1.5,label='Observed')
    p2=plt.step(u_axis,v_axis,linestyle='--',color='k',linewidth=1.5,label='Expected')
    plt.xlabel("Number of Substitutions")
    plt.ylabel("Frequency")
    plt.title("Expected And Observed Frequencies")
    plt.axvline(x = lamb,color='k',linewidth=1.5,linestyle='-')
    plt.grid()
    plt.legend(loc='upper right')
    pl.savefig(log_location + 'plot.png', bbox_inches='tight')
    plt.clf()

def plot_cdf(expectedMutations,observedMutations,lamb,log_location):

    x_axis=[]
    y_axis=[]
    x_axis.append(-1)
    y_axis.append(0)
    observed = Counter(observedMutations)
    for item in observed:
        x_axis.append(item)
        y_axis.append(float(observed[item])/len(observedMutations))

    u_axis=[]
    v_axis=[]
    u_axis.append(-1)
    v_axis.append(0)
    expected = Counter(expectedMutations)
    for item in expected:
        u_axis.append(item)
        v_axis.append(float(expected[item])/len(expectedMutations)) 

    max_value=max([max(x_axis),max(u_axis)])
    p1=plt.step(x_axis,np.cumsum(y_axis),linestyle='-',color='b',linewidth=1.5,label='Observed')
    p2=plt.step(u_axis,np.cumsum(v_axis),linestyle='--',color='r',linewidth=1.5,label='Expected')
    plt.xlabel("Number of Substitutions")
    plt.ylabel("Cumulative Frequency")
    plt.xlim([-0.5,max_value])
    plt.ylim([-0.05, 1.05])
    plt.title("Expected And Observed Cumulative Frequencies")
    plt.axvline(x = lamb,color='k',linewidth=1.5,linestyle='-')
    plt.grid()
    plt.legend(loc='lower right')
    pl.savefig(log_location + 'plot.png', bbox_inches='tight')
    plt.clf()

