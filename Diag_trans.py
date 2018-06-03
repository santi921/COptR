
import numpy as np

#all energies are in ghz
class trans:
	# task: recreate plot from koch paper  

	#here the circuit is initalized for EC, EJ values
	def __init__(self, nMax=20,Ec=1,Ej=1):
		#nmax is the number of charge states considered, here -20 to 20 are considered
		self.nMax=nMax
		self.Ec=Ec
		self.Ej=Ej
	#method to update values of Ec, Ej
	def update_val(self,Ec, Ej):
		self.Ec=Ec
		self.Ej=Ej

	def energies(self, terms=10, ng_in=0.1):
		#here terms arent the energy levels but the number of the ng steps you 
		#want to take in either direction. 

		#make ng consistent from -1 to 1, just allow the user to custojmize the number of sample
		#more descriptive-ng array perphaps
		terms=terms
		ng=ng_in
		temp=[]
		#ground, 1st excited, and 2nd excited states
		E0=[]
		E1=[]
		E2=[]
		#iterate across term space
		for j in range(-terms,terms,1):

			temp=[]
			#iterate across offset space
			for i in range(-self.nMax-1,self.nMax+2):
				#first diagonal terms are added
				temp.append((i- ng * j )**2)

			temp=np.array(temp)

			diag=np.diag(temp)
			#ec coeffecient added
			diag=self.Ec*diag
			#offdiagonal, junction energies are added to the hamiltonian
			off_elements=-self.Ej*(np.diag(np.ones(2*self.nMax+2),1)+np.diag(np.ones(2*self.nMax+2),-1))/2
			
			H=off_elements+diag
			#eigenenergies are calculated
			val,vector=np.linalg.eigh(H)

			E0.append(val[0])
			E1.append(val[1])
			E2.append(val[2])

		return np.array(E0), np.array(E1), np.array(E2)


