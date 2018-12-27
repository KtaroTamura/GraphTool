import numpy as np
import MinuitFit as MiF
import matplotlib.pyplot as plt
import numpy as np

def func(x, *par):
	a=par[0]
	b=par[1]
	return a*x+b

if __name__=='__main__':
	data_x=np.array([])
	data_y=np.array([])
	x_err=np.array([])
	y_err=np.array([])
	ax=plt.subplot()

	data=np.loadtxt("sample.csv",delimiter=',',skiprows=0)
	data_x=data[:,0]	
	data_y=data[:,1]
	x_err=np.full(data_x.shape[0],1)	
	y_err=np.full(data_x.shape[0],1)	
	MiF.Setup(data_x,data_y,x_err,y_err,func,ax)
#	MiF.SetRange()
#	MiF.SetLimit()
	result=MiF.chisquare(1,1)
#	plt.title()
#	plt.xlabel()
#	plt.ylabel()
	plt.show(block=False)

