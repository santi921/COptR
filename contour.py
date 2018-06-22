from optimizer import loss
import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':
	
	X=np.arange(5.0,25.0,1)
	Y=np.arange(0.1,2.5,0.1)
	Z=np.zeros([np.shape(X)[0],np.shape(Y)[0]])
	trackX=-1
	trackY=-1
	
	#test_X=np.arange(5.0,25.0,0.1)
	#test_Y=np.arange(0.0,2.0,0.01)
	"""print(loss(np.array([20,0.45])))
				print(loss(np.array([20,0.4])))
				print(loss(np.array([19.5,0.4])))
				print(loss(np.array([19.5,0.45])))
				print(loss(np.array([19.718,0.428])))
				"""
	for i in X:
		trackX+=1
		trackY=-1
		
		for j in Y:
			
			trackY+=1

			Z[trackX,trackY]=loss(np.array([i,j]))

			if np.isfinite(Z[trackX,trackY])==False:

				Z[trackX,trackY]=20
	
	print(" min ind: "+str(np.argmin(Z)))
	print("loss at these points"+""+"" )
	print("Max: "+str(np.amax(Z))+"Min: "+str(np.amin(Z)))
	plt.figure()
	print("X:",np.shape(X))
	print("Y:",np.shape(Y))
	print("Z:",np.shape(Z))
	
	plt.xlabel("Energy of Capacitor (Ghz)")
	plt.ylabel("Energy of Junction (Ghz)")
	plt.contourf(Y,X,Z,25,cmap=plt.cm.bone)	
	pointX=np.array([19.718762221])
	#19.5,20,20,19.5])
	pointY=np.array([0.42834373])
	#,0.45,0.45,0.4,0.4])
	plt.scatter(pointY,pointX,color='r',marker="+", s=100)
	
	#plt.title()
	#plt.plot()
	#plt.subplot(122)
	#length=np.size(X)*np.size(Y)
	#box=np.reshape(Z,-1)
	#plt.boxplot(box)
	
	plt.show()
