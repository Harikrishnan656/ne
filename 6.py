import folium 
import pandas as pd 
data = { 
  'City': ['New York', 'San Francisco', 'Los Angeles'], 
  'Population': [8175133, 884363, 3906772], 
  'Latitude': [40.7128, 37.7749, 34.0522], 
  'Longitude': [-74.0060, -122.4194, -118.2437] 
}
df = pd.DataFrame(data)  
map_center = [37.7749, -122.4194] 
map_obj = folium.Map(location=map_center, zoom_start=5)
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']], 
        popup=f"City: {row['City']} \nPopulation: {row['Population']}", 
        tooltip=row['City']
    ).add_to(map_obj)
map_obj.save('interactive_map.html')
print(data)
xport USERNAME_2=student-00-9870a7cf2123@qwiklabs.net


curl -LO
e raw.githubusercontent.com/quiccklabs/Labs_solutions/master/Cloud%20IAM%20Qwik%20Start/quicklabgsp064.sh

sudo chmod +x quicklabgsp064.sh

./quicklabgsp064.sh
