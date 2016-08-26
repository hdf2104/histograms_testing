import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm


offset500 = [2.4, 0.2, 0.8, -2.6, -3, -2.7, 0, 0.1, 0.2, 0.3, 0.3, 2.3, 0.1, 0.1, 0.2, 0, 1, 0.4, 2.2, 1.8, 2.6, 2.4, 3.6, 0.3, 0.3, 1.3, 2.7, 2.7, 2.5, 0.3, 2.5, 2.6, 1.8, 2.4, 1.7, 1.1, 1, 1.4, 2, 2.6, 2.3, 2.5, 2.6, 2.6, 1.1, 0.6, 0.4, 0.3, 0.3, 0.3, 0.3, 0.4, 0.5, 0.3, 0.3, 0.4, 0.4, 0.7, 0.4, 0.9, 1.1, 1.3, 0.7, 1, 1.5, 2.9, 1.6, 1.5,1.5, 2.6, 1.8, 2.4, 3.1, 2.8, 1.7, 0.5, 1.1, 0.6, 1.5, 2.6, 2.9, 2.8, 2.8, 2.4, 1.1, 0.6, 3.5, 0.4, 0.4, 0.5, 0.6, 0.4, 0.7, 0.6, 0.5, 0.7, 0.5, 0.7, 0.6, 2.1, 0.6]
offset5002 = [-0.1, -0.1, -1.2, 0, 0.2, 1, -0.1, 1.2, 2.5, 1.2, 0, 1.1, 0.9, 1.6, 0.1, -0.1, 1.5, 2.4, 2.1,2.4, 2.3, 0.1, 2.4, 0.7, 2.3, 2.3, 2.4, 2.4, 2.3, 0.9, 1, 2.5, -0.2, 2.3, 2.2, 2.3, 2.1, 1.6, 0.8, 1.2, 2.2, 2.2, 1.6, 2.4, 2.2, 1.4, 1.9, 0.7, 0.8, 2.2, 2.3, 2.2, 0.8, 2.2, 2, 2.1, 1.2, 2.3, 0.3, 2.3, -0.2, 1, 1, 0.8, 2.2, 0.8,2.1,1.3, 2.2, 2.3,-0.1, 1, 1.8, 0.8, 0.5]
offset500.extend(offset5002)
(mu, sigma) = norm.fit(offset500)
fig500 = plt.figure()

num_bins = 70
n, bins, patches = plt.hist(offset500, num_bins, normed=1, facecolor= 'blue', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)

fig500 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{500\ SPS\ Returning\ to\ a\ lighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence')
plt.grid(True)
plt.axis([-3, 4, 0, 1])
plt.show()
fig500.savefig('histo500.pdf')

offset200 = [ 1.4, 1.3, 1.2, 1.5, 1.7, 1.2, 1.3, 2.2, 1.8, 3.4, 2.7, 1.3, 1.3, 2.1, 1.4, 1.3, 2.1, 2.2, 3.7, 3.1, 1.3, 2.3, 1.8, 2.9, 2.2, 1.8, 1.9, 3, 1.5, 2.6, 3, 3.6, 1.4, 2.2, 1.5, 2.6, 2.1, 3, 3, 1.9, 3.6, 1.6, 2.1, 3.4, 2.1,2.9, 3.6, 3.5, 1.3, 1.7, 1.6, 3, 2.6, 2.7, 2, 3, 3.6, 3.3, 2.1, 1.9]
(mu, sigma) = norm.fit(offset200)
fig200 = plt.figure()

num_bins = 40
n, bins, patches = plt.hist(offset200, num_bins, normed=1, facecolor= 'blue', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)


fig200 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{200\ SPS\ Returning\ to\ a\ lighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence')
plt.grid(True)
plt.axis([0, 4, 0, 2])

plt.show()
fig200.savefig('histo200.pdf')

offset150= [-2, -0.8, -1.6, -1.2, -1.8, -0.9, -1.7, -1.3, -1, -1, -2.7, -1.3, -2, -2.6, -1.5, -2.5, 0.2, 0, 0.3, 0.3, 0.4, 0.6, 0.5, 0.4, 0.7, 0.5, 0.7, 0.4, 0.7, 0.7, 0.7, -0.5, -0.9, -0.8, 0.5, -0.4, -0.8, -0.1, -0.5, -0.9, -0.5, 1.6, -0.7, 1.6, -0.3, 1.5, 1.6, 0.4, -0.1, 1.6, -0.7, -0.9, -0.2, -0.9, 0.5, 0.1, 1.6, 1.1,1.6,1.7, 1.6, 1.6, 1.7, 1.6, 1.6, 1.8, 2.1, 1.1, 1.9, 1.9, 1.8, 1.9, 1.3, 1.6, -0.8, -0.5, -0.2, -0.8, -0.6, -0.7, -1.2, 0, -0.2, 0.2, -0.9, 0.2, 0.3, -1, 0.2, -0.7, -0.5]
(mu, sigma) = norm.fit(offset150)
fig150 = plt.figure()

num_bins = 60
n, bins, patches = plt.hist(offset150, num_bins, normed=1, facecolor= 'blue', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)

fig150 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{150\ SPS\ Returning\ to\ a\ lighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence')
plt.grid(True)
plt.axis([-3, 3, 0, 2])
plt.show()
fig150.savefig('histo150.pdf')


offset100= [2.6, 3.8, 2.2, 4.2, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.4, 3.7, 4.8, 4.4, 4.5, 4.3, 4.5, 3.1, 4.5, 4.9, 3.7, 3, 4.6, 4.7, 3.1, 4.9, 4.8, 4.6, 6.1, 3.7, 6, 6, 6, 6.2, 6.1, 6.5, 6.2, 6.1, 5.8, 4.7, 5.1, 6.1, 6.1, 6.5, 6.3, 6.3, 6.3, 6.2, 6.2, 6.6, 6.4, 6.1, 6.2, 6.7, 5.4, 6.3, 6.3, 5.6, 6.1, 6.7, 6.6, 5.7, 5.1, 5.3]
(mu, sigma) = norm.fit(offset100)
fig100 = plt.figure()

num_bins = 50
n, bins, patches = plt.hist(offset100, num_bins, normed=1, facecolor= 'blue', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)

fig100 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{100\ SPS\ Returning\ to\ a\ lighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence')
plt.grid(True)
plt.axis([0, 7, 0, 2])
plt.show()
fig100.savefig('histo100.pdf')



offsetreverse500 = [-0.8, -2, -2.1, -2.1, -2.1, -0.5, 0.4, -0.5, -1.2, -0.6, -1.4, -1.9, -1.9, -2, -1.4, -1.8, -1.9, -1.9, -1.9, -1.9, -1.9, -1.9, -1.9, -1.9, -1.8, -1.7, -1.9, -1.9, -1.9, -1.9, -2, -1.9, -1, -1.9, -1.9, -1.8, -1.7, -1.7, -1.7]
(mu, sigma) = norm.fit(offsetreverse500)
fig500rev = plt.figure()

num_bins = 40
n, bins, patches = plt.hist(offsetreverse500, num_bins, normed=1, facecolor= 'yellow', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)

rev500 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{500\ SPS\ Returning\ to\ a\ lighted\ home\ from\ reverse\ side:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence, normalized')
plt.grid(True)
plt.axis([-3, 1, 0, 8])
plt.show()
rev500.savefig('histo_rev500.pdf')



offsetoff500 = [31.6, 31.5, 26.8, 27.3, 31.6, 31.7, 31.6, 31.6, 31.2, 31.3, 31.3, 31.3, 31.3, 31.2, 31.2, 31.1, 31.1, 31.5, 32.1, 30.9, 31.7, 31.7, 31.6, 31.4, 31.5, 31.6, 31.5, 31.6, 31.5, 31.7, 31.2, 31.3, 31.2, 31.2, 31.2, 31.2, 31.3, 31.6, 31.3, 31.3, 30.6, 31.3, 31.2, 31.1, 31.3, 31.4, 31.2, 31.2, 31.6, 31.2, 31.1, 30, 29.7, 31.4, 31.2, 30.1, 30.2, 30, 28.7, 29.5, 28.3, 27.5, 28.2, 28.2,  28.1, 28.2]
(mu, sigma) = norm.fit(offsetoff500)
fig500off = plt.figure()

num_bins = 40
n, bins, patches = plt.hist(offsetoff500, num_bins, normed=1, facecolor= 'green', alpha= 0.5)

#y = mlab.normpdf( bins, mu, sigma)
#l= plt.plot(bins, y, 'r--', linewidth=1)

off500 = plt.gcf()
plt.hold(True)
plt.xlabel(' Offset Distance [microns]')
plt.title(r'$\mathrm{500\ SPS\ Returning\ to\ an\ unlighted\ home:}\ \mu=%.3f, \ \sigma= %.3f$' %(mu, sigma))
plt.ylabel('Occurrence, normalized')
plt.grid(True)
plt.axis([26, 33, 0, 3])
plt.show()
off500.savefig('histo_off500.pdf')