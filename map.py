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
    new_color = ""
    if el < 1000:
        new_color = "green"
    elif 1000 <= el < 3000:
        new_color = "orange"
    else:
        new_color = "red"
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=9,
            popup=folium.Popup(iframe),
            fill_color=new_color,
            color="black",
            fill_opacity=1,
        )
    )

fg.add_child(
    folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()))
)
map.add_child(fg)
map.save("Map1.html")
