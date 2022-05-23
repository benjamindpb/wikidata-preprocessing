import gzip
import time

BYTES = 10**8
filename = 'latest-truthy.nt.gz'


def get_entities_and_coord(bytes=-1):
    start = time.time()
    n_entities = 0
    with gzip.open('latest-truthy.nt.gz', 'r') as f, open('entities.tsv', 'w') as e:
        print('Reading file...')
        file_content = f.readlines(bytes)
        e.write('{}\t{}\t{}\n'.format('entity_url', 'latitude', 'longitude'))
        for line in file_content:
            str_line = line.decode()
            if '<http://www.wikidata.org/prop/direct/P625>' in str_line: 
                # print(str_line)
                n_entities += 1
                split = str_line.split(' ')
                # print(split)
                lon = split[2].split('(')[1]
                lat = split[3].split(')"^^')[0]
                e.write('{}\t{}\t{}\n'.format(split[0], lat, lon))
    end = time.time()
    print('Time working: {}'.format(convert(end - start)))
    print('Found entities: {}\n'.format(n_entities))

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

get_entities_and_coord(BYTES)
