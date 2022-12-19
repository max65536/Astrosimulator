from positions import Stars
from skyfield.api import N, W, wgs84, load
from IPython import embed

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

shanghai = wgs84.latlon(31.256 * N, 121.547 * W)
ts = load.timescale()
t = ts.utc(2003, 8, 29)

stars = Stars(time=t, observer=shanghai)
# embed()


r = np.ones(6) 
# size = 6 * r**2 # Size of plot
colors = stars.colors
ax = plt.subplot(projection='polar')
# ax = plt.subplot()

#projection为画图样式，除'polar'外还有'aitoff', 'hammer', 'lambert'等
c = ax.scatter(stars.positions, y=r, c=stars.colors, s=stars.sizes, cmap='cool', alpha=0.75)
ax.text(3.14,1,"test")
plt.show()
#ax.scatter为绘制散点图函数