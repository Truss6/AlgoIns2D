##### Plotting presets
import matplotlib as mpl
mpl.rcParams['figure.figsize']=[6,4] # set fig size (in inches)
mpl.rcParams['figure.dpi']=300 # set resolution (debugging: 100, draft: 300, final: 900)
mpl.rcParams['font.size']=12 # set global font size
mpl.rcParams['font.family']='times new roman' # set global font
# in a linux OS, this may throw an error, consider changing to 'FreeSerif'
mpl.rcParams['legend.fontsize']=12 # decrease legend font size
mpl.rcParams['lines.markersize']=10 # increase default marker size
mpl.rcParams['mathtext.fontset'] = 'cm' # set math font to computer-modern
from matplotlib import pyplot as plt

from matplotlib.patches import Polygon as poly
# import multiprocessing as mpi
# Pool=mpi.Pool(4)
# from numba import jit,njit
from random import random as rand
'''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |   _____      | || |    ______    | || |     ____     | || |  _______     | || |     _____    | || |  _________   | || |  ____  ____  | || | ____    ____ | || |     _____    | || |     ______   | |
| |     /  \     | || |  |_   _|     | || |  .' ___  |   | || |   .'    `.   | || | |_   __ \    | || |    |_   _|   | || | |  _   _  |  | || | |_   ||   _| | || ||_   \  /   _|| || |    |_   _|   | || |   .' ___  |  | |
| |    / /\ \    | || |    | |       | || | / .'   \_|   | || |  /  .--.  \  | || |   | |__) |   | || |      | |     | || | |_/ | | \_|  | || |   | |__| |   | || |  |   \/   |  | || |      | |     | || |  / .'   \_|  | |
| |   / ____ \   | || |    | |   _   | || | | |    ____  | || |  | |    | |  | || |   |  __ /    | || |      | |     | || |     | |      | || |   |  __  |   | || |  | |\  /| |  | || |      | |     | || |  | |         | |
| | _/ /    \ \_ | || |   _| |__/ |  | || | \ `.___]  _| | || |  \  `--'  /  | || |  _| |  \ \_  | || |     _| |_    | || |    _| |_     | || |  _| |  | |_  | || | _| |_\/_| |_ | || |     _| |_    | || |  \ `.___.'\  | |
| ||____|  |____|| || |  |________|  | || |  `._____.'   | || |   `.____.'   | || | |____| |___| | || |    |_____|   | || |   |_____|    | || | |____||____| | || ||_____||_____|| || |    |_____|   | || |   `._____.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || | ____  _____  | || |    _______   | || |  _________   | || |  _______     | || |  _________   | || |     _____    | || |     ____     | || | ____  _____  | |
| |    |_   _|   | || ||_   \|_   _| | || |   /  ___  |  | || | |_   ___  |  | || | |_   __ \    | || | |  _   _  |  | || |    |_   _|   | || |   .'    `.   | || ||_   \|_   _| | |
| |      | |     | || |  |   \ | |   | || |  |  (__ \_|  | || |   | |_  \_|  | || |   | |__) |   | || | |_/ | | \_|  | || |      | |     | || |  /  .--.  \  | || |  |   \ | |   | |
| |      | |     | || |  | |\ \| |   | || |   '.___`-.   | || |   |  _|  _   | || |   |  __ /    | || |     | |      | || |      | |     | || |  | |    | |  | || |  | |\ \| |   | |
| |     _| |_    | || | _| |_\   |_  | || |  |`\____) |  | || |  _| |___/ |  | || |  _| |  \ \_  | || |    _| |_     | || |     _| |_    | || |  \  `--'  /  | || | _| |_\   |_  | |
| |    |_____|   | || ||_____|\____| | || |  |_______.'  | || | |_________|  | || | |____| |___| | || |   |_____|    | || |    |_____|   | || |   `.____.'   | || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''
tx=[[0,0.5,0],[0.5,0.5,0],[0.5,1,0.5],[0.5,1,1],[0.5,1,0.5],[1,1,0.5],[0,0.5,0],[0,0.5,0.5]]
ty=[[0,0,0.5],[0,0.5,0.5],[0,0.5,0.5],[0,0,0.5],[0.5,0.5,1],[0.5,1,1],[0.5,1,1],[0.5,0.5,1]]
tri=lambda i,x,y,lx,ly: {'x':[x+lx*TX for TX in tx[i]],'y':[y+ly*TY for TY in ty[i]],'clr':[rand() for _ in range(3)]}
def A(x,y): return []#[{'x':x,'y':y}] # empty
def B(x,y): # full
# 	lx=x[2]-x[0];ly=y[2]-y[0]
 	# result=[tri(i,x[0],y[0],lx,ly) for i in range (8)]
 	# return result
 	return [{'x': x,'y': y,'clr':[rand() for _ in range(3)]}]
def gamma(bools,x,y):
	# all but the corner
	lx=x[2]-x[0];ly=y[2]-y[0]
	
# 	dx=[[0,0.5,0],[0,0.5,0.5],[0.5,1,0.5],[0.5,1,1],[0.5,1,1],[0.5,1,0.5],[0,0.5,0.5]]
# 	dy=[[0,0.5,0.5],[0,0,0.5],[0,0.5,0.5],[0,0,0.5],[0.5,0.5,1],[0.5,1,1],[0.5,0.5,1]]
	results=[]
	for i in [1,2,4,7]:
		results.append(tri(i,x[0],y[0],lx,ly))
	if bools[0]:
		results.append(tri(0,x[0],y[0],lx,ly))
	if bools[1]:
		results.append(tri(3,x[0],y[0],lx,ly))
	if bools[2]:
		results.append(tri(5,x[0],y[0],lx,ly))
	if bools[3]:
		results.append(tri(6,x[0],y[0],lx,ly))
	return results

def epsilon(bools,x,y):
	# just the corner
	lx=x[2]-x[0];ly=y[2]-y[0]	
	results=[]
	if bools[0]:
		results.append(tri(0,x[0],y[0],lx,ly))
	if bools[1]:
		results.append(tri(3,x[0],y[0],lx,ly))
	if bools[2]:
		results.append(tri(5,x[0],y[0],lx,ly))
	if bools[3]:
		results.append(tri(6,x[0],y[0],lx,ly))
	return results
def delta(bools,x,y): # half
	lx=x[2]-x[0];ly=y[2]-y[0]
	results=[]
	if bools[0]:
		results.append(tri(0,x[0],y[0],lx,ly))
		results.append(tri(1,x[0],y[0],lx,ly))
	if bools[1]:
		results.append(tri(3,x[0],y[0],lx,ly))
		results.append(tri(2,x[0],y[0],lx,ly))
	if bools[2]:
		results.append(tri(5,x[0],y[0],lx,ly))
		results.append(tri(4,x[0],y[0],lx,ly))
	if bools[3]:
		results.append(tri(6,x[0],y[0],lx,ly))
		results.append(tri(7,x[0],y[0],lx,ly))
# 	print(results)
	return results	
def khaa(bools,x,y): # all but two opposite coners
	lx=x[2]-x[0];ly=y[2]-y[0]
	results=[]
	
	for i in [1,2,4,7]:
		results.append(tri(i,x[0],y[0],lx,ly))
	if bools[0]:
		results.append(tri(0,x[0],y[0],lx,ly))
		results.append(tri(5,x[0],y[0],lx,ly))
	if bools[1]:
		results.append(tri(3,x[0],y[0],lx,ly))
		results.append(tri(7,x[0],y[0],lx,ly))
	return results
def haa(bools,x,y): # two opposite corners
	lx=x[2]-x[0];ly=y[2]-y[0]
	results=[]
	if bools[0]:
		results.append(tri(0,x[0],y[0],lx,ly))
		results.append(tri(5,x[0],y[0],lx,ly))
	if bools[1]:
		results.append(tri(3,x[0],y[0],lx,ly))
		results.append(tri(7,x[0],y[0],lx,ly))
	return results
def det_delta_khaa_haa(bools,F,x,y): # two corners, figure out is delta, haa, or khaa
	if bools in [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]:
# 		result=delta(bools,x,y)
# 		print(result)
# 		return result
		return delta(bools,x,y)
	else:
		print('Suggest increasing subdivisions')
		if F(0.5*(x[2]+x[0]),0.5*(y[2]+y[0])):
			return khaa(bools,x,y)
		else:
			return haa(bools,x,y)
def det(bools,F,x,y):
	bsum=sum(bools)
	if bsum==0: return (x,y)
	elif bsum==4: return B(x,y)
	elif bsum==1: return epsilon(bools,x,y)
	elif bsum==3: return gamma(bools,x,y)
	elif bsum==2:
		return det_delta_khaa_haa(bools,F,x,y)

dx=[[0,0.5,0.5,0],[0.5,1,1,0.5],[0.5,1,1,0.5],[0,0.5,0.5,0]]
dy=[[0,0,0.5,0.5],[0,0,0.5,0.5],[0.5,0.5,1,1],[0.5,0.5,1,1]]
# @njit
def subdiv(F,x,y,N,n=0):
	triangles=[]
	if n==0:
		bools=[F(X,Y) for (X,Y) in zip (x,y)]
		
		if sum(bools)==0:
			result = A(x,y)
			for trngl in result: triangles.append(trngl)
		elif sum(bools)==4: 
			result = B(x,y)
			for trngl in result: triangles.append(trngl)
		elif N<=0: 
			result = det(bools,F,x,y)
			for trngl in result: triangles.append(trngl)
		else: # subdivide
			lx=x[2]-x[0];ly=y[2]-y[0]
			X=[[x[0]+lx*dx2 for dx2 in dx1] for dx1 in dx]
			Y=[[y[0]+ly*dy2 for dy2 in dy1] for dy1 in dy]
			
			for (bx,by) in zip(X,Y):
				result = subdiv(F,bx,by,N-1)
				for trngl in result: triangles.append(trngl)
	else: # subdivide
		lx=x[2]-x[0];ly=y[2]-y[0]
		X=[[x[0]+lx*dx2 for dx2 in dx1] for dx1 in dx]
		Y=[[y[0]+ly*dy2 for dy2 in dy1] for dy1 in dy]
		
		for (bx,by) in zip(X,Y):
			result = subdiv(F,bx,by,N-1,n=n-1)
			for trngl in result: triangles.append(trngl)
# 		plot(triangles)
# 	plot(triangles)
	return triangles
def plot(triangles):
	plt.figure()
	for tri in triangles:
		if not tri==None:
			#print(tri)
			patch=poly([[x,y] for x,y in zip(tri['x'],tri['y'])],ec=[0 for _ in range(3)],fc=[0.75 for _ in range(3)])#fc=tri['clr'])
# 			patch=poly([[x,y] for x,y in zip(tri['x'],tri['y'])],ec=None,fc=[0.75 for _ in range(3)])#fc=tri['clr'])
			plt.gca().add_patch(patch)
def write(triangles,fname='tets.csv'):
	with open(fname,'w') as O:        
		for i in range(4):
			O.write(f'x{i}\ty{i}\t')
		O.write('\n')
		for tri in triangles:
			for i in range(3):
				O.write(f"{tri['x'][i]}\t")
				O.write(f"{tri['y'][i]}\t")
			if len(tri['x'])==4:
				O.write(f"{tri['x'][3]}\t")
				O.write(f"{tri['y'][3]}\n")
			else:
				O.write('\n')

from random import random as rand
from math import sin,cos,pi
if __name__=='__main__':
# 	F=lambda x,y: ((x**2+2*y**2)<1)
	#F=lambda x,y: abs(sin(x*2*pi)*sin(y*2*pi))<0.5
	F=lambda x,y: abs(cos(1*x*2*pi)+cos(2*y*2*pi))<1.25 # p
	#F=lambda x,y: abs(cos(y*2*pi)*cos(y*2*pi)-sin(x*2*pi)*sin(y*2*pi))<0.5 # D
	#F=lambda x,y: abs(sin(x*2*pi)*cos(y*2*pi)+cos(x*2*pi)*sin(y*2*pi))<0.5 # G
	
	result=subdiv(F,[0,1,1,0],[0,0,1,1],8,n=3)
	print(f'{len(result)} polygons generated')
	#print(result)
# 	f=plt.figure()
	write(result)
	plot(result)