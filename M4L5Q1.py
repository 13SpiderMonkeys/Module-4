import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


#import document
file_path = "C:/Users/shado/Downloads/significant_month.geojson.customization"

#have geopandas load the GeoJSON file

gdf = gpd.read_file(file_path)

#scale size of markers based on magnatude of earthquake

gdf["size"] = gdf["mag"] * 5

#create the plot

fig, ax = plt.subplots(1,1,figsize=(12,8))
gdf.plot(
    ax = ax,
    markersize=gdf["size"],
    color= "green",
    alpha = .6,
    legend=True
)

#add labels and grid to the plot

plt.title("Earthquake Activty Map")
plt.xlabel("Logitude")
plt.ylabel("Latitude")
plt.grid(True)

#show plot

plt.show()