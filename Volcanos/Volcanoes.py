import folium, pandas

df=pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[df['ELEV'].mean(),df['LAT'].mean()], zoom_start=5,tiles='Stamen Terrain')
elev1 = df['ELEV']
step = int(max(elev1)-min(elev1)/3)

def color(elev):
    minimum = int(min(elev1))
    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range (minimum+step,minimum+step*2):
        col='orange'
    else:
        col='red'
    return col

def pop(population):
    if population<=10000000:
        return 'green'
    elif population<=100000000:
        return 'orange'
    else:
        return 'red'


for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker([lat, lon], popup=name,  icon = folium.Icon(color=color(elev))).add_to(map)
"""
folium.GeoJson(data=open('world-geojson-from-ogr.json').decode('utf-8-sig'),name='World Population'
#,style_fnction=lambda x:{'fillCOlor':pop(x['properties']['POP2005'])}
).add_to(map)
"""
map.save('Volcanoes.html')
