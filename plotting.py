#Author: Rebecca Quinn
# plots a line plot and histogram

import numpy as np
import matplotlib.pyplot as plt

#distributuon is normal at 1000, mean is 5 and standard deviation is 2 for this historgram
meanvalue = 5
standard = 2
distrib = 1000
x = np.random.normal(loc = meanvalue , scale = standard, size = distrib)
plt.hist(x)


xpoints = np.array(range(0,11))

#x (xpoints) to the power of 3 using pow REF: https://www.geeksforgeeks.org/python-pow-function/
ypoints = pow(xpoints, 3)

plt.plot(xpoints, ypoints)

x = np.linespace(0,11)
with plt.style.context("Solarize_Light2"):
    plt.plot(x, np.sin(x) + x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 1 + np.random.randn(50))
    plt.plot(x, np.sin(x) + 2 + np.random.randn(50))
    plt.plot(x, np.sin(x) + 3 + np.random.randn(50))
    plt.plot(x, np.sin(x) + 4 + np.random.randn(50))
    plt.plot(x, np.sin(x) + 5 + np.random.randn(50))

    plt.title("h(x)=x^3")
    plt.xlabel("X", fontsize = 14)
    plt.ylabel("Y", fontsize = 14)

#shows the plots
plt.show()


