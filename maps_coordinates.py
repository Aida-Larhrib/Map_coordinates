import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
import matplotlib.patches as mpatches
import cartopy.feature as cfeature

#draw out the map and chose the variable that I want to be in there:
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '50m', edgecolor='black', facecolor=cfeature.COLORS['land']))
ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='black', facecolor='none'))
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='none', facecolor=cfeature.COLORS['water']), alpha=0.5)
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m', edgecolor=cfeature.COLORS['water'], facecolor='none'))
ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces_lines', '50m', edgecolor='gray', facecolor='none'))

plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

#giving values to the lat and the lon as well as the radius: 
longitude = -7.603869
latitude = 33.589886
r = 0.15

#Plotting the circle
ax.add_patch(mpatches.Circle(xy=[longitude, latitude], radius=r, color='red', alpha=0.3, transform=ccrs.PlateCarree(), zorder=30))

#This defines the bounding box around the coordinates
zoom_radius = 2  # degrees to zoom in
ax.set_extent([longitude - zoom_radius, longitude + zoom_radius, latitude - zoom_radius, latitude + zoom_radius], crs=ccrs.PlateCarree())

plt.show()