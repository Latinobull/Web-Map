import folium

map = folium.Map(
    location=[40.639050998016664, -73.92169274478333],
    zoom_start=10,
    tiles="OpenStreetMap",
)
fg = folium.FeatureGroup(name="My Map")
for coords in [
    [40.64748489005272, -73.88336934270934],
    [40.60204651406353, -73.96563805750966],
]:

    fg.add_child(
        folium.Marker(
            location=coords,
            popup="Hi I am a Marker",
            icon=folium.Icon(color="red"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
