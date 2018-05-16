
import numpy as np

#all energies are in ghz

# task: recreate plot from koch paper  

nMax=20

Ec=1

Ej=1

ng=0.1

temp=[]

for i in range(-nMax-1,nMax+2):
	
	temp.append((i-ng)**2)

temp=np.array(temp)

diag=np.diag(temp)

diag=Ec*diag

off_elements=-Ej*(np.diag(np.ones(2*nMax+2),1)+np.diag(np.ones(2*nMax+2),-1))/2
#print(off_elements)
H=off_elements+diag

val,vector=np.linalg.eigh(H)
ts1=val[-2]-val[-1]
ts2=val[-3]-val[-2]
print("ts1: "+str(-ts1)+" ts2: "+str(-ts2))
