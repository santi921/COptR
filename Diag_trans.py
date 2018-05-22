
import numpy as np

#all energies are in ghz
class trans:
	# task: recreate plot from koch paper  
	def __init__(self, nMax=20,Ec=1,Ej=1):
		self.nMax=nMax
		self.Ec=Ec
		self.Ej=Ej

	def energies(self, terms=20, ng_in=0.1):
		#here terms arent the energy levels but the number of the ng steps you 
		#want to take in either direction. To be made more generalizable

		terms=terms
		ng=ng_in
		temp=[]

		E0=[]
		E1=[]
		E2=[]

		for j in range(-terms,terms,1):

			temp=[]

			for i in range(-self.nMax-1,self.nMax+2):
				
				temp.append((i- ng * j )**2)

			temp=np.array(temp)

			diag=np.diag(temp)

			diag=self.Ec*diag

			off_elements=-self.Ej*(np.diag(np.ones(2*self.nMax+2),1)+np.diag(np.ones(2*self.nMax+2),-1))/2
			#print(off_elements)
			H=off_elements+diag

			val,vector=np.linalg.eigh(H)

			E0.append(val[-1])

			E1.append(val[-2])
			
			E2.append(val[-3])
			
		return np.array(E0), np.array(E1), np.array(E2)
