#practical 13

#importing pandas numpy and scipy

import pandas as pd
import numpy as np
from scipy import stats

#reading csv file
pf=pd.read_csv("D:\machine Learning\Csv files\data1.csv")

#printing data of csv file
print(pf)

#calculating mean
mean=np.mean(pf)
print(mean)

#calculating median
median = np.median(pf)
print(median)

#calculating mode
mode = stats.mode(pf)
print(mode)
