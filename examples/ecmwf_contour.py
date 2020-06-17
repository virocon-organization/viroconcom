import netCDF4
from viroconcom.dataECMWF import ECMWF
from matplotlib import pyplot as plt
from viroconcom.contours import DirectSamplingContour

# Get the data and write them into a file.
ecmwf = ECMWF()
ecmwf.get_data("2018-09-01/to/2018-09-30", "00:00:00", "0.75/0.75", "75/-20/10/60", "229.140/232.140")
# Open the file for reading.
test_nc_file = '../examples/datasets/ecmwf.nc'
nc = netCDF4.Dataset(test_nc_file, mode='r')

var_s = nc.variables
var = 'swh'
var2 = 'mwp'
data1 = var_s[var][:]
data2 = var_s[var2][:]

dsc = DirectSamplingContour(data1, data2, 1, 0.5, 1)
direct_sampling_contour = dsc.direct_sampling_contour()

# Plot the contour and the sample.
plt.scatter(data1, data2, marker='.')
plt.plot(direct_sampling_contour[0], direct_sampling_contour[1], color='red')
plt.title('Direct sampling contour')
plt.xlabel('Significant wave height (m)')
plt.ylabel('Mean wave period (s)')
plt.show()