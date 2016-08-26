import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm



offset100= [2.6, 3.8, 2.2, 4.2, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.4, 3.7, 4.8, 4.4, 4.5, 4.3, 4.5, 3.1, 4.5, 4.9, 3.7, 3, 4.6, 4.7, 3.1, 4.9, 4.8, 4.6, 6.1, 3.7, 6, 6, 6, 6.2, 6.1, 6.5, 6.2, 6.1, 5.8, 4.7, 5.1, 6.1, 6.1, 6.5, 6.3, 6.3, 6.3, 6.2, 6.2, 6.6, 6.4, 6.1, 6.2, 6.7, 5.4, 6.3, 6.3, 5.6, 6.1, 6.7, 6.6, 5.7, 5.1, 5.3]

(mu, sigma) = norm.fit(offset100)

fig100 = plt.figure()

#make the histogram
num_bins = 50

n, bins, patches = plt.hist(offset100, num_bins,  facecolor= 'blue', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)


#make the plot
fig100 = plt.gcf()

plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{100\ SPS\ Returning\ to\ a\ lighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence')
plt.grid(True)
plt.axis([0, 7, 0, 8])

plt.show()
fig100.savefig('histo100.pdf')