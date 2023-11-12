from traceback import print_list
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import scale,normalize
import numpy as np
 
sm = pd.read_csv(r"C:\Users\Site\Desktop\AzHoosh\AzHoosh\smartphones.csv")
print(sm.Capacity.value_counts())
sm.rename(index=sm.Name,inplace=True)
sm.drop(['Name','Company'],axis=1,inplace=True)
sm=pd.get_dummies(sm)
scaled_data=scale(sm)
print (scaled_data)

 