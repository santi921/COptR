#imiport minimize and the circuit eigenfinder
from Diag_trans import trans
from scipy.optimize import minimize

import numpy as np
import matplotlib.pyplot as plt

#this function creates a loss function and calculates its value for given circuit parameters that are used to calc energies
def loss(x):
	#x is Ec, Ej as an array
	Ej=x[0]
	Ec=x[1]
	#initialize circuit
	test=trans(Ec=Ec,Ej=Ej)
	E0,E1,E2=test.energies()
	
	#these coeffecients tune the sensitivity to each desired parameter
	# a=1, b=1, c=2.55, d=1 <-- this worked beforehand 

	#tune var 1
	a=1.0
	#tune var 2
	b=1.0
	#tune anharmonicity
	c=2.55
	#tune 4 ghz
	d=1

	
	#loss function calculated for variance of E1, E2, and how close the first energy transition is  to 4 ghz 
	#anharmonicity is also calcualted as relative energy transitions between E0-->E1 and E1-->E2
	loss = a * np.var(E1)+ b * np.var(E2) + \
	c * (np.log((np.mean(E2)-np.mean(E1))/(np.mean(E1)-np.mean(E0))-0.8)) +\
	d * abs(abs(np.mean(E1)-np.mean(E0))-4)

	return loss



if __name__=='__main__':
		
	#start values for optimization
	Ec=2
	Ej=20

	x0=np.array([Ej,Ec])

	#as per koch paperzA
	bounds=[(0.01,140),(0.01,140)]
	bounds=bounds

	#gradient-descent Low memory BFGS methods
	res1 = minimize(loss, x0, method='L-BFGS-B',bounds=bounds)
	 
	#create circuit based on optimization to display
	final_cir=trans(Ej=float(res1['x'][0]),Ec=float(res1['x'][1]))

	E0,E1,E2=final_cir.energies()

	#prints parameters of  final circuit

	print(res1)

	print(" var 1: \t"+str(np.var(E1)))

	print(" var 2: \t"+str(np.var(E2)))

	print(" anharm: \t"+str((np.mean(E2)-np.mean(E1))/(np.mean(E1)-np.mean(E0))))

	print(" Ej/Ec: \t"+str(res1['x'][0]/res1['x'][1]))


	print(" t1: \t\t"+ str(np.mean(E1-E0)))

	#display energies
	t=np.arange(-10,10,1)
	fig,ax=plt.subplots()
	plt.subplots_adjust(left=0.25, bottom=0.25)
	plt.xlabel("Charge offset")
	plt.ylabel("Energy(G)")
	E1-=np.mean(E0)
	E2-=np.mean(E0)
	E0-=np.mean(E0)
	l = plt.plot(t, (E0), 'red', t, (E1), 'blue', t, (E2), 'green')
	plt.show()
