import optimizer as op

#file was used to test whether Ej and EC values were switched
#in representation

if __name__ =="__main__":
 	
	print(op.loss(op,2*1E9,100*1E9))
	print(op.loss(op,20*1E9,1000*1E9))
	print(op.loss(op,0.2*1E9,10*1E9))
	print(op.loss(op,10*1E9,500*1E9))