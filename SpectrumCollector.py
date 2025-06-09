import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#plt.style.use('seaborn-whitegrid')

# Load the space-delimited file using pandas
file_path = './'
file = input(str("filename in current directory: "))
file = file_path+file
print(file,"being loaded")
data = pd.read_csv(file, sep='\s{1}', header=None, engine='python', index_col=0)

# Convert to a NumPy array if needed
array = data.to_numpy

#print("Data loaded using Pandas:")
#print(data.values[0])
#print(data.T.values[0])
#print(data.index)
px = data.index
py = data.values[:, 2]
py2 = data.values[:,-1]
print(px,py)
x = pd.to_numeric((px[1:-1]), errors='coerce')
y = pd.to_numeric((py[1:-1]), errors='coerce')
y2 = pd.to_numeric((py2[1:-1]), errors='coerce')
print(x,y)

plt.plot(x, y, 'o', color='black');
plt.plot(x, y2, 'o', color='red');
plt.show()
wavelength = str(input("wavelength in nm: "))+".0"
ph = data.values[0]
abs = data.loc[wavelength]
print(ph,abs)
plt.plot(ph, abs, 'o', color='black');
plt.show()





