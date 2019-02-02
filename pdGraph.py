import sys
import ROOT
import pandas as pd
import numpy as np


if __name__=="__main__":
	args=sys.argv
	filename=args[1]
	data=[]
	data=pd.read_csv(filename,delimiter=',',dtype=None,skiprows=0)

##Make Graph Data
#	data.columns['','','']
	x=data["1"]
	y=data["2"]
	n=data.shape[0]
	g1=ROOT.TGraph(n,x,y)
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
