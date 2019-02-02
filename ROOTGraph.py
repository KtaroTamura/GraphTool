import sys
import ROOT
import numpy as np


if __name__=="__main__":
	args=sys.argv
	filename=args[1]
	data=[]
	data=np.loadtxt(filename,delimiter=',',dtype=None,skiprows=0)

##Make Graoph Data
	x=data[:,0].flatten()
	y=data[:,4].flatten()
	n=data.shape[0]
	g1=ROOT.TGraph(n,x,y)


##Graph Details
	g1.SetMarkerColor(2)
	g1.SetLineColor(2)
	g1.SetTitle("")
	g1.GetXaxis().SetTitle("")
	g1.GetYaxis().SetTitle("")
	g1.Draw()

def stop(self):
	sys.stderr.write('[Read]\tstop.\tPress "q"to quit>')
	ans=raw_input ('>')
	if ans in ['q','Q']:
		g1.IsA().Destructor(g1)
		sys.exit(-1)
	elif ans in ['.','q','Q']:
		return -1
