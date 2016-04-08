import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

stations = np.genfromtxt("stationListFrom2005.csv",
                         delimiter=',', 
                         dtype=[('lat', np.float32), ('lon', np.float32)], 
                         usecols=(0, 1))

fig = plt.figure()


themap = Basemap(projection='gall',
              llcrnrlon = -92,              # lower-left corner longitude
              llcrnrlat = 35,               # lower-left corner latitude
              urcrnrlon = -85,               # upper-right corner longitude
              urcrnrlat = 44,               # upper-right corner latitude
              resolution = 'l',
              area_thresh = 100000.0,
              )
themap.drawcoastlines()
themap.drawstates()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

x, y = themap(stations['lon'], stations['lat'])
themap.plot(x, y, 
            'o',                    # marker shape
            color='Green',         # marker colour
            markersize=4            # marker size
            )

plt.show()