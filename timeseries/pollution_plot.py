# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt

RS_df=pd.read_csv('pollution_RusselSquare.csv', encoding='utf-8', header=0, index_col=0, parse_dates=['timestamp'])
ER_df=pd.read_csv('pollution_EustonRoad.csv', encoding='utf-8', header=0, index_col=0, parse_dates=['timestamp'])
H_df=pd.read_csv('pollution_Holborn.csv', encoding='utf-8', header=0, index_col=0, parse_dates=['timestamp'])

#box chart and histogram
#plt.figure()
#RS_df.plot.box()
#ER_df.plot.box()
#H_df.plot.box()

#RS_df.plot.hist()
#ER_df.plot.hist()
#H_df.plot.hist()

#resampling and exporting


plt.show()