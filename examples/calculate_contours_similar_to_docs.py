import matplotlib.pyplot as plt

from viroconcom.params import ConstantParam, FunctionParam
from viroconcom.distributions import WeibullDistribution, LognormalDistribution, \
    MultivariateDistribution
from viroconcom.contours import IFormContour, HighestDensityContour
from viroconcom.plot import plot_contour


# Define a Weibull distribution representing significant wave height.
shape = ConstantParam(1.5)
loc = ConstantParam(1)
scale = ConstantParam(3)
dist0 = WeibullDistribution(shape, loc, scale)
dep0 = (None, None, None) # All three parameters are independent.

# Define a Lognormal distribution representing spectral peak period.
my_sigma = FunctionParam('exp3', 0.05, 0.2, -0.2)
my_mu = FunctionParam('power3', 0.1, 1.5, 0.2)
dist1 = LognormalDistribution(sigma=my_sigma, mu=my_mu)
dep1 = (0, None, 0) # Parameter one and three depend on dist0.

# Create a multivariate distribution by bundling the two distributions.
distributions = [dist0, dist1]
dependencies = [dep0, dep1]
mul_dist = MultivariateDistribution(distributions, dependencies)

# Compute an IFORM contour with a return period of 25 years and a sea state
# duration of 3 hours.
iform_contour = IFormContour(mul_dist, 25, 3)

# Compute a highest density contour with the same settings (25 years return
# period, 3 hour sea state duration).
limits = [(0, 20), (0, 20)] # The limits of the computational domain.
deltas = [0.4, 0.4] # The dimensions of the grid cells.
hdens_contour = HighestDensityContour(mul_dist, 25, 3, limits, deltas)

# Plot the two contours.
plt.scatter(iform_contour.coordinates[1], iform_contour.coordinates[0],
            label='IFORM contour')
plt.scatter(hdens_contour.coordinates[1], hdens_contour.coordinates[0],
            label='Highest density contour')
plt.xlabel('Spectral peak period, Tp (s)')
plt.ylabel('Significant wave height, Hs (m)')
plt.legend()
plt.show()

plot_contour(iform_contour.coordinates[1], iform_contour.coordinates[0],
             x_label='Tp (s)', y_label='Hs (m)')
plt.show()
