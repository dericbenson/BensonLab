import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
plt.close("all")

# Get filenames and path from commandline arguments
YH_file = sys.argv[1]
HS_file = sys.argv[2]

# Load in file with mulitple space separation and column naming to remove #Acceptor that messes up pandas column naming
dist_YH = pd.read_csv(YH_file, sep="\s+")
dist_HS = pd.read_csv(HS_file, sep="\s+")

# combine process data
hbond_corr = dist_YH
hbond_corr["HSdist"] = dist_HS["HisND1SerOG"]

# plot
fig, ax = plt.subplots()
ax.set_title("Correlated Triad Distances")
ax.set_xlabel("TyrO-HisND1")
ax.set_ylabel("HisNE2-SerOG")
ax.set_ylim(2,5)
ax.set_xlim(2,5)
ax.hist2d(hbond_corr["TyrO-HisND1"],hbond_corr["HSdist"], range=[[2,5],[2,5]], bins=[30,30], cmap=plt.cm.Reds)
#ax.plot(hbond_corr["TyrO-HisND1"],hbond_corr["HSdist"], color = "b")
plt.show()
fig.savefig("Triad_corr.png")
