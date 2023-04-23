#Author: Rebecca Quinn
# plots a line plot and histogram

import numpy as np
import matplotlib.pyplot as plt

#distributuon is normal at 1000, mean is 5 and standard deviation is 2 for this historgram
meanvalue = 5
standard = 2
distrib = 1000
x = np.random.normal(meanvalue, standard, distrib)

xpoints = np.arange(0,11)

#x (xpoints) to the power of 3 using pow
ypoints = pow(xpoints, 3,)

#CUSTOMISING PLOT CODE BELOW

plt.figure(figsize=(14,7)) # size of fig 14x7
plt.style.use('seaborn-whitegrid') #grid style
plt.title("Plotting Plot")

plt.hist(x, facecolor="cyan", edgecolor="white", label="X Data") # draws solid white grid lines
plt.plot(xpoints, ypoints, linewidth=5.0, color="pink", label="Y Data") 
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=2.)

#shows the plots
# saves the plot into an image file as seen in plotted.png 
#plt.savefig("plottask.png")

#shows plot
plt.show()


