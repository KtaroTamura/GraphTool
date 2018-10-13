import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
	args=sys.argv
	filename=args[1]
	data=[]
	data=np.loadtxt(filename,delimiter=',',dtype=None,skiprows=0)
	x=data[:,0]
	y=data[:,1]
	plt.plot(x,y,label='',color='b')
	plt.title('')
	plt.xlabel(u'')
	plt.ylabel(u'')
#	plt.xlim([])
#	plt.ylim([])
#	plt.legend(loc='upper right')
	plt.show()
