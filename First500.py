import folium
import pandas as pd

Westchester = pd.read_csv('First500.csv', encoding = "latin-1") 
myHoodmap = folium.Map(location=[40.8415, -73.8448], zoom_start=14)

for index, row in Westchester.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Complaint Type"]
    folium.CircleMarker(location=[lat,lon], radius=15, popup=name, color='#3186cc',fill_color='#3186cc').add_to(myHoodmap)
   
myHoodmap.save('myHood.html')
