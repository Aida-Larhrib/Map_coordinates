import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

plt.show()

from matplotlib.patches import Circle
circle = Circle((52.00667, 4.35556), radius=5, edgecolor='blue', facecolor='none', transform=ccrs.PlateCarree())

# Add the circle to the map
ax.add_patch(circle)

# Add coastlines for reference
ax.coastlines()

plt.show()