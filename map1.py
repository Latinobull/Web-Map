import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])

map = folium.Map(
    location=[40.639050998016664, -73.92169274478333],
    zoom_start=10,
    tiles="OpenStreetMap",
)
fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon):

    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Hi I am a Marker",
            icon=folium.Icon(color="red"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
