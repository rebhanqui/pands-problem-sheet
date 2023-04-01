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
ypoints = pow(xpoints, 3)

plt.plot(xpoints, ypoints)


#shows the plots
plt.show()


