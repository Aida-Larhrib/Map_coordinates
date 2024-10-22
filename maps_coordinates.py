import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
import matplotlib.patches as mpatches
import cartopy.feature as cfeature

#draw out the map and chose the variable that I want to be in there:

def map_generation(ax=None):
    if ax is None : 
        ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '50m', edgecolor='black', facecolor=cfeature.COLORS['land']))
    ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '50m', edgecolor='black', facecolor='none'))
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='none', facecolor=cfeature.COLORS['water']), alpha=0.5)
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m', edgecolor=cfeature.COLORS['water'], facecolor='none'))
    ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces_lines', '50m', edgecolor='gray', facecolor='none'))
    return ax

# plt.savefig( )
# plt.savefig('coastlines.pdf')
# plt.savefig('coastlines.png')

#Defining a function for coordinates and radius of the circle that is to be mapped
def plot_circle(ax, longitude= -7.603869, latitude= 33.589886):
    r = 0.15
    circle = ax.add_patch(mpatches.Circle(xy=[longitude, latitude], radius=r, color='red', alpha=0.3, transform=ccrs.PlateCarree(), zorder=30))
    return circle

#This defines the bounding box around the coordinates

def zoom(ax, degree, longitude= -7.603869, latitude= 33.589886):
    zoom_radius = 5
    frame = ax.set_extent([longitude - degree, longitude + zoom_radius, latitude - zoom_radius, latitude + zoom_radius], crs=ccrs.PlateCarree())
    return frame

ax = map_generation()
circle = plot_circle(ax=ax)
frame = zoom(ax=ax,degree=5)

plt.show()