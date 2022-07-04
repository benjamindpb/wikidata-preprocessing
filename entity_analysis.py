import gzip
import time
from turtle import width
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium as fo
import mpl_toolkits as mpl


BYTES = 10000
dump_truthy = 'latest-truthy.nt.gz'
total_entities = "data/entities_total.tsv"
errors_fn = "data/errors.tsv"


def get_entities_coords(n):
    """
        Esta función se encarga de 
    """
    start = time.time()
    n_entities = 0
    n_errors = 0
    with gzip.open(dump_truthy, 'rt', encoding='utf8') as f, open("entities.tsv", 'w') as entities, open(errors_fn, 'w') as errors:
        print('Reading file...')
        entities.write('entity_url\tlatitude\tlongitude\n')
        for line in f:
            if n==n_entities: break
            if '<http://www.wikidata.org/prop/direct/P625>' in line: 
                try:
                    n_entities += 1
                    split = line.split(' ')
                    entity = split[0].split('Q')[1][:-1] # '<https://www.wikidata.org/wiki/Q5>' -> 5
                    lon = split[2].split('(')[1]
                    lat = split[3].split(')"^^')[0]
                    entities.write('{}\t{}\t{}\n'.format(entity, lat.replace('.',','), lon.replace('.',',')))

                    print(f'Found {n_entities} entities with {n_errors} errors', end="\r")
                except: 
                    n_error += 1
                    n_entities -= 1
                    errors.write(line)
                    
    end = time.time()
    print('\nTime working: {}'.format(convert(end - start)))

def entities_dict():
    print("* Getting pair {entity:1} dictionary.")
    start = time.time()
    D = {}
    n_entities = 0
    with open(total_entities, "r") as f:
        for line in f:
            key, _, _ = line.split() # entity url key and geo coords (lat, lon)
            D[key] = 1
            n_entities += 1
            print(f"Number of entitites added to dict: {n_entities}", end="\r")
    end = time.time()
    print(f"\nTime working getting the dict: {convert(end-start)}")
    return D
"""
    Leer el dum truthy completo  y si el 1er termino está en el diccionario
    de entidades (P625), y si el 2do termino es http://www.wikidata.org/prop/direct/P31

    Esta función retorna un diccionario que contiene la frecuencia de los tipos de 
    entidades del dataset (?)

"""
def count_types():
    start = time.time()
    d = entities_dict()
    types_dict = {}
    with gzip.open(dump_truthy, 'rt', encoding='utf8') as f:
        print("* Reading dump truthy...")
        for line in f:
            if '/P31>' in line:
                split = line.split(' ')[:-1] # ignore last element ("\n") from the list 
                entity = split[0] # entity url
                if entity in d:
                     e_types = split[2:] # list of the types of the entity
                     for et in e_types: # iterate over the entity types. can be more than one per entity
                        if et in types_dict:
                            types_dict[et] += 1
                        else:
                            types_dict[et] = 0 # base case
    end = time.time()
    print(f"\nTime working getting the types count dict: {convert(end-start)}")
    return types_dict

def get_types_count():
    start = time.time()
    d = count_types()
    n_type = 0
    print('Adding types and count in tsv file.\n')
    with open("data/entity_types.tsv", "w", encoding='utf8') as t, open("data/entity_types_errors.tsv", "w", encoding="utf8") as e:
        t.write("entity_type\tcount\n")
        for k in d:
            try:
                type_key = k.split('Q')[1][:-1] # acá hay problemas
                t.write(f'{type_key}\t{d[k]}\n')
                n_type += 1
                print(f'Type {n_type} added to the file', end='\r')
            except:
                e.write(type_key+"\n")
    end = time.time()
    print(f'\nTime working getting the tsv file of the types count: {convert(end-start)}')

def types_count_to_md():
    df = pd.read_csv("data/entity_types.tsv", sep="\t")
    sort_df = df.sort_values(by='count', ascending=False)
    sort_df['entity_type'] = 'https://www.wikidata.org/wiki/Q'+sort_df['entity_type'].astype(str)
    sort_df['title_label'] = [get_title_label(u) for u in sort_df['entity_type']]
    print(sort_df[:25].to_markdown(index=False))

def types_count_to_html():
    df = pd.read_csv("data/entity_types.tsv", sep="\t")
    sort_df = df.sort_values(by='count', ascending=False)
    sort_df['entity_type'] = 'https://www.wikidata.org/wiki/Q'+sort_df['entity_type'].astype(str)
    # sort_df.reset_index(drop=True)
    sort_df[:25].to_html('entity_list.html', index=False)

def world_map():
    data = pd.read_csv('data/entities_total.tsv', sep='\t')   
    m = fo.Map(
        tiles="CartoDB dark_matter",
        location=[0, 0],
        zoom_control=False,
        prefer_canvas=True,
        zoom_start=2
        )
    lat = data['latitude']
    lon = data['longitude']
    for a, b in zip(lat, lon):
        fo.CircleMarker(
            location=[float(a.replace(',', '.')), float(b.replace(',', '.'))],
            color="crimson",
            fill=False,
            weight=0.5,
            radius=0.5
        ).add_to(m)
        
    m.save("map.html")



def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

# get_entities_coords()
# entities_dict()
# get_types_count()
# types_count_to_md()
# world_map()
world_map()


