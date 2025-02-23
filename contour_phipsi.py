#
# countour_phipsi to build 2D histogram Ramachandran plots
# usage python countour_phipsi.py [filewith dihedral angles from MD sim] phi_column_name psi_column name
#
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
plt.close("all")

# Get filenames and path from commandline arguments
phipsi_file = sys.argv[1]

# Load in file with mulitple space separation and column naming to remove #Acceptor that messes up pandas column naming
phipsi = pd.read_csv(phipsi_file, sep="\s+")
#psi = pd.read_csv(phipsi_file, sep="\s+")
phi_column = sys.argv[2]
psi_column = sys.argv[3]

phi = phipsi[phi_column]
psi = phipsi[psi_column]

# combine process data
#hbond_corr = dist_YH
#hbond_corr["HSdist"] = dist_HS["HisND1SerOG"]

# plot
fig, ax = plt.subplots()
ax.set_title("Ramachandran Plot")
ax.set_xlabel(phi_column)
ax.set_ylabel(psi_column)
ax.set_ylim(-180,180)
ax.set_xlim(-180,180)
ax.hist2d(phi,psi, range=[[-180,180],[-180,180]], bins=[36,36], cmap=plt.cm.Greys) 
#ax.plot(hbond_corr["TyrO-HisND1"],hbond_corr["HSdist"], color = "b")
plt.show()
fig.savefig("phipsi.png")
