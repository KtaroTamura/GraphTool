# GraphTool
# Overview
* MinFit.py \
iMinuitによる誤差付き最小二乗法フィッティング用コード \
実行のソースコードはMinmain.py 

* pdGraph.py \
pandasとROOTによるグラフ表示。CERNのpyROOT環境が必要。

* matGraph.py \
matplotlibによるグラフ表示。純pythonで実行可能。

# Usage
* MinFit.py \
import MinFit.py as MiF   
最初に使うデータセット等を宣言  
MiF.Setup(data_x,data_y,x_err,y_err,fit func,ax)
data_x,data_y フィット用のデータセット  
x_err,y_err   データセットの誤差。ゼロの場合も０を入力  
func          フィット関数
ax            結果表示用のグラフオブジェクト

### option
* MiF.SetRange(X_min,X_max)
* MiF.SetLimit(lim_par=[par_min,par_max])

MiF.chisquare(init_par)
