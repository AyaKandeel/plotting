import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([909976, 8615246, 2872086, 2273305]) 
s.index = ["pasion", "hope", "patience", "pain"]
s.name = "life"
print(s) 
print(s.index)
print(s.values )
print(s["hope"] )
print(s.pain)
print(s[["pasion", "patience"]])
print(s.median(), s.mean(), s.std() )
print(s.min(), s.max() )
print(s.quantile(q=0.25), s.quantile(q=0.5), s.quantile(q=0.75))
print(s.describe())
fig, axes = plt.subplots(1, 2, figsize=(12, 3)) 
s.plot(ax=axes[0], kind='bar', title='bar')    
s.plot(ax=axes[1], kind='pie', title='pie')