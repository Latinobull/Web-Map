import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(
    location=[37.97257545638386, -98.89051431454878],
    zoom_start=5,
    tiles="OpenStreetMap",
)

fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm, el in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    color = ""
    if el < 1000:
        color = "green"
    elif 1000 <= el < 3000:
        color = "orange"
    else:
        color = "red"
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(color=color),
        )
    )

map.add_child(fg)
map.save("Map1.html")
