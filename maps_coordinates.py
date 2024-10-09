import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic


ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

plt.show()
#changing the coordinate system? 
ccrs.Globe(datum=None, ellipse='WGS84', semimajor_axis=None, semiminor_axis=None, flattening=None, inverse_flattening=None, towgs84=None, nadgrids=None)
Geodesic.circle(lon=52.00667, lat=4.35556, radius=2500.)

# Add the circle to the map
ax.add_patch()

# Add coastlines for reference
ax.coastlines()

plt.show()