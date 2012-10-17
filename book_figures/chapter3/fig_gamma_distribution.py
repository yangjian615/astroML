"""
Example of a Gamma distribution
-------------------------------

This shows an example of a gamma distribution with various parameters.
We'll generate the distribution using::

    dist = scipy.stats.gamma(...)

Where ... should be filled in with the desired distribution parameters
Once we have defined the distribution parameters in this way, these
distribution objects have many useful methods; for example:

* ``dist.pmf(x)`` computes the Probability Mass Function at values ``x``
  in the case of discrete distributions

* ``dist.pdf(x)`` computes the Probability Density Function at values ``x``
  in the case of continuous distributions

* ``dist.rvs(N)`` computes ``N`` random variables distributed according
  to the given distribution

Many further options exist; refer to the documentation of ``scipy.stats``
for more details.
"""
# Author: Jake VanderPlas <vanderplas@astro.washington.edu>
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning for Astronomy" (2013)
#   For more information, see http://astroML.github.com
import numpy as np
from scipy.stats import gamma
import pylab as pl

#------------------------------------------------------------
# plot the distributions
k_values = [1, 2, 3, 5]
theta_values = [2, 1, 1, 0.5]
linestyles = ['-', '--', ':', '-.']
x = np.linspace(1E-6, 10, 1000)

#------------------------------------------------------------
# plot the distributions
for k, t, ls in zip(k_values, theta_values, linestyles):
    dist = gamma(k, 0, t)
    pl.plot(x, dist.pdf(x), ls=ls, c='black',
            label=r'$k=%.1f,\ \theta=%.1f$' % (k, t))

pl.xlim(0, 10)
pl.ylim(0, 0.5)

pl.xlabel('$x$', fontsize=14)
pl.ylabel(r'$P(x|\alpha,\beta)$', fontsize=14)
pl.title('Gamma Distribution')

pl.legend(loc=0)
pl.show()
