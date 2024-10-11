import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
import shapely.geometry as sgeom
import matplotlib.patches as mpatches
import cartopy.feature as cfeature

# Creating a cartopy, choosing the features I want to be shown on it:
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '50m', edgecolor='black', facecolor=cfeature.COLORS['land']))
ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='black', facecolor='none'))
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='none', facecolor=cfeature.COLORS['water']), alpha=0.5)
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m', edgecolor=cfeature.COLORS['water'], facecolor='none'))
ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces_lines', '50m', edgecolor='gray', facecolor='none'))

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

# Coordinates for the center of the circle
longitude = 4.3556
latitude =52.00667 
r = 0.15


#generate the circle
ax.add_patch(mpatches.Circle(xy=[longitude, latitude], radius=r, color='red', alpha=0.3, transform=ccrs.PlateCarree(), zorder=30))
plt.savefig('CircleTest.png')


# Add coastlines for reference
ax.coastlines()


plt.show()
