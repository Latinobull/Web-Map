import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])

map = folium.Map(
    location=[37.97257545638386, -98.89051431454878],
    zoom_start=5,
    tiles="OpenStreetMap",
)
fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm in zip(lat, lon, name):

    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Volcano {}".format(nm),
            icon=folium.Icon(color="red"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
