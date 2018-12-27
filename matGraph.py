import sys
import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
##Get Data set 
	args=sys.argv
	filename=args[1]
	data=[]
	data=pd.read_csv(filename,delimiter=',',dtype=None,skiprows=0)

##Make graph data
	data.colums["","",""]
	x=data["1"]
	y=data["2"]
	plt.plot(x,y,label='',color='b')

##plot details
#	plt.title('AAA')
#	plt.xlabel(u'aaa')
#	plt.ylabel(u'bbb')
#	plt.xlim([])
#	plt.ylim([])
#	plt.yscale('log')
#	plt.legend(loc='upper right')
	plt.show(block=False)
