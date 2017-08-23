import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 緯度経度で範囲を指定する
north = 46.
#south = 30.
south = 10.
east = 147.
#west = 128.
west = 108.

# 地図の表示('merc"は純粋に緯度経度を直行座標系にplotしている）
#m = Basemap( projection='merc', llcrnrlat=south, urcrnrlat=north, llcrnrlon=west, urcrnrlon=east )
m = Basemap( llcrnrlat=south, urcrnrlat=north, llcrnrlon=west, urcrnrlon=east, resolution='l' )

# 海岸線を引く
m.drawcoastlines()

# 画面に表示
plt.show()
