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

#x (xpoints) to the power of 3 using pow REF: https://www.geeksforgeeks.org/python-pow-function/
ypoints = pow(xpoints, 3,)

#CUSTOMISING PLOT CODE BELOW]
#REF https://medium.com/@arseniytyurin/how-to-make-your-histogram-shine-69e432be39ca

plt.figure(figsize=(14,7)) # size of fig 14x7
plt.style.use('seaborn-whitegrid') #grid style
plt.title("Plotting Plot")

plt.hist(x, facecolor="cyan", edgecolor="white", label="X Data") # draw solid white grid lines
plt.plot(xpoints, ypoints, linewidth=5.0, color="pink", label="Y Data") #https://www.statology.org/matplotlib-line-thickness/
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=2.)
#REF: https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html


#shows the plots
# saves the plot into an image file as seen in plotted.png 
#plt.savefig("plottask.png")
# REF https://towardsdatascience.com/save-plots-matplotlib-1a16b3432d8a

#shows plot
plt.show()


