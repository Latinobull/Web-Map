import folium

map = folium.Map(
    location=[40.639050998016664, -73.92169274478333],
    zoom_start=6,
    tiles="OpenStreetMap",
)
map.save("Map1.html")
