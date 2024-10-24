#map_coordinates project by Aïda Larhrib, student 5854261.
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
import matplotlib.patches as mpatches
import cartopy.feature as cfeature

#draw out the map and chose the variable that I want to be in there:

def map_generation(ax=None):
    """This function genrates a map, according to the chosen parameters.

    Args:
        ax (_type_, optional): the features of the map can be specified.

    Returns:
        The output is a map, with coastlines and other features that were asked for.
    """
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
    """This function plots a circle at the coordinates that were chosen by the user.

    Args:
        ax (_type_): the map that we generated using the previous function.
        longitude (float, optional): the value of the longitude which can be changed.
        latitude (float, optional): the value of the latitude which can also be changed.

    Returns:
        The output is a circle that is drawn up on the map previously plotted at the demanded coordinates.
    """
    r = 0.15
    circle = ax.add_patch(mpatches.Circle(xy=[longitude, latitude], radius=r, color='red', alpha=0.3, transform=ccrs.PlateCarree(), zorder=30))
    return circle

#This defines the bounding box around the coordinates

def zoom(ax, degree, longitude= -7.603869, latitude= 33.589886):
    """This function redefines the boundary of the image we get as the ouptut, it makes it smaller so that we do not have to manually zoom into the map to see the circle.

    Args:
        ax (_type_): the map that was plotted in the first function.
        degree (_type_): by how much I want the boundaries of the image to extend using the longitude and latitude as origine
        longitude (float, optional): the value of the longitude which can be changed.
        latitude (float, optional): the value of the latitude which can also be changed.

    Returns:
        _type_: the output is an image of the circle in the map we previously plotted that is zoomed in, centered into the circle.
    """
    zoom_radius = 5
    frame = ax.set_extent([longitude - degree, longitude + zoom_radius, latitude - zoom_radius, latitude + zoom_radius], crs=ccrs.PlateCarree())
    return frame

ax = map_generation()
circle = plot_circle(ax=ax)
frame = zoom(ax=ax,degree=5)

plt.show()