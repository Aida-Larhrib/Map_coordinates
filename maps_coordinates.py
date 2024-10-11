import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
import pandas as pd
import matplotlib.patches as mpatches
import cartopy.feature as cfeature

#draw out the map and chose the variable that I want to be in there:
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

#giving values to the lat and the lon: 
longitude = 52.00667
latitude = 4.3556
radius = 0.15

#Plotting the circle
ax.add_patch(mpatches.Circle(xy=[longitude, latitude], radius=r, color='red', alpha=0.3, transform=ccrs.PlateCarree(), zorder=30))
ax.set_xlim([-latitude-5, latitude+5])
ax.set_ylim([-longitude-5, longitude+5])

#plt. save and show the figure
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')
plt.show()