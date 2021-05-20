import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
elev = list(data["ELEV"])
map = folium.Map(
    location=[37.97257545638386, -98.89051431454878],
    zoom_start=5,
    tiles="OpenStreetMap",
)
fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm, el in zip(lat, lon, name, elev):

    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Volcano {}: Elevation: {}m".format(nm, el),
            icon=folium.Icon(color="red"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
