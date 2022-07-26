import gzip
import time
import pandas as pd
import pandas as pd
import folium as fo
import sys
import pickle

from regex import P

DUMP_TRUTHY = 'latest-truthy.nt.gz'
P625_TSV = "results/entities/entities_100k.tsv"
P31_TSV = "results/types/entity_types.tsv"
PICKLE_ENTITIES = "bin/entities_dict.bin"
PICKLE_TYPES = "bin/entities_types.bin"

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def get_entities_coords(n=10**7):
    """
        This function 
    """
    start = time.time()
    n_entities = 0
    n_errors = 0
    total_ntriples = 0
    with gzip.open(DUMP_TRUTHY, 'rt', encoding='utf8') as f, open("results/entities/entities.tsv", 'w') as entities:
        print('Reading file...')
        entities.write('entity_url\tlatitude\tlongitude\n')
        for line in f:
            total_ntriples += 1
            if n==n_entities: break
            if '/P625>' in line: 
                try:
                    n_entities += 1
                    split = line.split(' ')
                    entity = split[0].split('Q')[1][:-1] # '<https://www.wikidata.org/wiki/Q5>' -> 5
                    # Las sgtes lineas rescatan las coord pero se piensa hacer mejor con regex
                    lon = split[2].split('(')[1]
                    lat = split[3].split(')"^^')[0]
                    entities.write('{}\t{}\t{}\n'.format(entity, lat, lon))

                    print(f'Found {n_entities} entities with geo coord and {n_errors} errors', end="\r")
                except: 
                    n_errors += 1
                    n_entities -= 1
                    
    end = time.time()
    print(f'\nTotal of N-Triples: {total_ntriples}')
    print('\nTime working: {}'.format(convert(end - start)))

def entities_dict():
    print("* Getting pair {entity:1} dictionary.")
    start = time.time()
    D = {}
    n_entities = 0
    with open(P625_TSV, "r") as f, open(PICKLE_ENTITIES, 'wb') as p:
        for line in f:
            key, _, _ = line.split() # entity url, key, and geo coords (lat, lon)
            D[key] = 1
            n_entities += 1
            print(f"Number of entitites added to dict: {n_entities}", end="\r")
        end = time.time()
        print(f"\nTime working getting the dict: {convert(end-start)}")
        pickle.dump(D, p)

def count_types():
    start = time.time()
    types_dict = {}
    with gzip.open(DUMP_TRUTHY, 'rt', encoding='utf8') as f, open(PICKLE_ENTITIES, 'rb') as pe:
        # Load dict from created binary pickle file
        d = pickle.load(pe)
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
    pt = open(PICKLE_TYPES, 'wb')
    pickle.dump(types_dict, pt)
    pt.close()
    end = time.time()
    print(f"\nTime working getting the types count dict: {convert(end-start)}")

def get_types_count():
    start = time.time()
    n_type = 0
    print('Adding types and count in tsv file.\n')
    with open(P31_TSV, "w", encoding='utf8') as t, open(PICKLE_TYPES, 'rb') as pt:
        d = pickle.load(pt)
        t.write("entity_type\tcount\n")
        for k in d:
            try:
                type_key = k.split('Q')[1][:-1] 
                t.write(f'{type_key}\t{d[k]}\n')
                n_type += 1
                print(f'Type {n_type} added to the file', end='\r')
            except:
                pass
        
    end = time.time()
    print(f'\nTime working getting the tsv file of the types count: {convert(end-start)}')

def types_count_to_md():
    df = pd.read_csv("data/entity_types.tsv", sep="\t")
    sort_df = df.sort_values(by='count', ascending=False)
    sort_df['entity_type'] = 'https://www.wikidata.org/wiki/Q'+sort_df['entity_type'].astype(str)
    print(sort_df[:25].to_markdown(index=False))

def types_count_to_html():
    df = pd.read_csv("data/entity_types.tsv", sep="\t")
    sort_df = df.sort_values(by='count', ascending=False)
    sort_df['entity_type'] = 'https://www.wikidata.org/wiki/Q'+sort_df['entity_type'].astype(str)
    # sort_df.reset_index(drop=True)
    sort_df[:25].to_html('entity_list.html', index=False)

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('Usage error.')
    else:
        if args[1] == '-ec':
            if args[2]:
                get_entities_coords(args[2])
            else:
                get_entities_coords()
        elif args[1] == '-et':
            entities_dict()
            count_types()
            get_types_count()


            










