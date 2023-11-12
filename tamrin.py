from traceback import print_list
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
 
df = pd.read_csv(r"smartphones.csv")
country = pd.read_csv(r"country.csv")

# sb.swarmplot(x='OS',y="Capacity",data=df,size=15,hue="Company")
# plt.show()

# sb.pairplot(df,hue="Name",palette='hls',plot_kws={'s':100})
# plt.show()
country.rename(index=country.Name,inplace=True)
country.drop('Name',axis=1,inplace=True)
country.drop('Code',axis=1,inplace=True)

imp=SimpleImputer(strategy="mean",missing_values=np.nan)
imp.fit(country)
new_dataset=imp.transform(country)
print(new_dataset)
