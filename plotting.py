#Author: Rebecca Quinn
# plots a line plot and histogram

import numpy as np
import matplotlib.pyplot as plt

#distributuon is normal at 1000, mean is 5 and standard deviation is 2 for this historgram
meanvalue = 5
standard = 2
distrib = 1000
x = np.random.normal(meanvalue, standard, distrib)
plt.hist(x)


xpoints = np.arange(0,11)

#x (xpoints) to the power of 3 using pow REF: https://www.geeksforgeeks.org/python-pow-function/
ypoints = pow(xpoints, 3,)

plt.plot(xpoints, ypoints)
plt.plot(xpoints, color = ("cyan"), edgecolor = ("w"))
plt.plot(ypoints, color = ("magenta"), edgecolor = ("black"))

#CUSTOMISING PLOT CODE BELOW]

plt.title("Plotting Plot")
plt.xlabel("X Data")
plt.ylabel("Y Data")
# draw solid white grid lines
#REF: https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html
plt.grid()

#shows the plots
# saves the plot into an image file as seen in plotted.png plt.savefig("plotted.png")
# REF https://towardsdatascience.com/save-plots-matplotlib-1a16b3432d8a
plt.show()


