import pandas as pd
import folium as fo
import time
from entity_analysis import convert

def world_map():
    start = time.time()
    print("Reading total of entities...")
    data = pd.read_csv('results/entities_total.tsv', sep='\t')
    # Creating map
    m = fo.Map(
        tiles="CartoDB dark_matter",
        location=[0, 0],
        max_bounds=True,
        zoom_control=False,
        prefer_canvas=True,
        min_zoom=2,
        max_zoom=2,
        zoom_start=2
        )
    lat = data['latitude']
    lon = data['longitude']
    print("Generating map...", end="\r")
    for a, b in zip(lat, lon):
        fo.CircleMarker(
            location=[float(a), float(b)],
            color="#fc2ac1",
            fill=False,
            weight=0.1,
            radius=0.5
        ).add_to(m)
    
    print('\nSaving html file...')
    
    m.save("map.html")
    end = time.time()
    print(f'Time working: {convert(end-start)} (h:m:s)')


world_map()