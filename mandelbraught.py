#####
import numpy as np
from math import *
##### Plotting presets
import matplotlib as mpl
mpl.rcParams['figure.figsize']=[6,4] # set fig size (in inches)
N=900
mpl.rcParams['figure.dpi']=N # set resolution (debugging: 100, draft: 300, final: 900)
mpl.rcParams['font.size']=12 # set global font size
mpl.rcParams['font.family']='times new roman' # set global font
# in a linux OS, this may throw an error, consider changing to 'FreeSerif'
mpl.rcParams['legend.fontsize']=12 # decrease legend font size
mpl.rcParams['lines.markersize']=10 # increase default marker size
mpl.rcParams['mathtext.fontset'] = 'cm' # set math font to computer-modern
from matplotlib import pyplot as plt
#####
from AlgorithmicInsertion import *
#####

# class complex:
# 	re=0;im=0;
# 	def __init__(self,re,im):
# 		self.re=re;self.im=im;
# 		return self
#	complex={'r':re,'i':im}
one={'r':1,'i':0}
two={'r':2,'i':0}
def addc(a,b):
	return {'r':a['r']+b['r'],'i':a['i']+b['i']}
def subc(a,b):
	return {'r':a['r']-b['r'],'i':a['i']-b['i']}
def multc(a,b):
# 	print(b)
	return {'r':a['r']*b['r']-a['i']*b['i'],'i':a['r']*b['i']+a['i']*b['r']}
	
def powerc(a,n):
	if n==0:
		return one
	else:
		return multc(a,powerc(a,n-1))
def mag(a):
	a_star={'r':a['r'],'i':-1*a['i']}
	
	mgsq=multc(a,a_star)
	
	return sqrt(mgsq['r'])
def function(c,z,n):
	z=addc(powerc(z,2),c)
# 	print(z)
	if n==0:
		return z
	else:
		return function(c,z,n-1)
def F(x,y):
	c={'r':x,'i':y}
	z={'r':0,'i':0}
	return mag(function(c,z,25))<1

if __name__=='__main__':
	result=subdiv(F,[-2,1,1,-2],[-1.5,-1.5,1.5,1.5],11,n=8)
	print(f'{len(result)} polygons generated')
	#print(result)
# 	f=plt.figure()
	write(result)
	plot(result)
	plt.ylim([-1.5,1.5])
	plt.xlim([-2,1])