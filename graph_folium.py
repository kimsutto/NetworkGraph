import pandas as pd
import folium
import networkx as nx

nodes = pd.read_csv('./Desktop/location2.csv')
#필요한 컬럼만 추출
nodes = nodes[['NODE_NAME','LATITUDE','LONGITUDE','CATEGORY','NUMBER']] 

G = nx.Graph()

for idx,row in nodes.iterrows():
    # add node to Graph G
    G.add_node(row['NODE_NAME'],Label=row['NODE_NAME'],latitude=row['LATITUDE'], longitude=row['LONGITUDE'], category= row['CATEGORY'])

#center -> seoul 
center = [37.541, 126.986] 

dict={'쇼핑':'red','체험관광지':'blue','역사관광지':'yellow', '자연관광지':'black','휴양관광지':'white','건축/조형물':'purple'}

#tiles 지도 삭제 
map_osm = folium.Map(location=center, zoom_start=13,tiles='Mapbox Bright') 

for ix, row in nodes.iterrows():
    location = (row['LATITUDE'], row['LONGITUDE'])
    folium.Circle(
        location=location,
        radius=row['NUMBER']/2, 
        color='white',
        weight=1,
        fill_opacity=1,
        opacity=1,
        fill_color=dict[row['CATEGORY']],
        fill=True, 
    ).add_to(map_osm)
map_osm