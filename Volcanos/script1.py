import folium, pandas

df=pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[45.372, -121.6972], zoom_start=5,tiles='Stamen Terrain')

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    folium.Marker([lat, lon], popup=name).add_to(map)


map.save('mthood.html')
