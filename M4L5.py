import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium as flm


#import document

file_path = "C:/Users/shado/Downloads/MODIS_C6_1_Global_24h.csv"
df = pd.read_csv(file_path)

#convert data frame to geodata frame

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df["longitude"], df["latitude"]), crs="EPSG:4326"
)


#scale size of markers based on magnatude of earthquake

gdf["size"] = gdf["brightness"]/ 50

#create the plot

fig, ax = plt.subplots(1,1,figsize=(12,8))
gdf.plot(
    ax = ax,
    markersize=gdf["size"],
    color= "orange",
    alpha = .6,
    legend=True
)

#add labels and grid to the plot

plt.title("Global Fire Activity in the past 24 hours")
plt.xlabel("Logitude")
plt.ylabel("Latitude")
plt.grid(True)

#show plot

plt.show()