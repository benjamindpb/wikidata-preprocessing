import gzip
import time

BYTES = 10**8
filename = 'latest-truthy.nt.gz'


def get_entities_and_coord(bytes=-1, filename):
    start = time.time()
    n_entities = 0
    with open(filename, 'r') as f, open('entities.tsv', 'w') as e:
        print('Reading file...')
        file_content = f.readlines(bytes)
        e.write('{}\t{}\t{}\n'.format('entity_url', 'latitude', 'longitude'))
        for line in file_content:
            str_line = line.decode()
            if "P625" in str_line:
                print(str_line)
                n_entities += 1
                split = str_line.split(' ')
                lat = split[2]
                lon = split[3]
                e.write('{}\t{}\t{}\n'.format(split[0], lat, lon))
    end = time.time()
    print('Time working: {}\n'.format(convert(end - start)))
    print('Found entities: {}\n'.format(n_entities))

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

get_entities_and_coord(BYTES, filename)
