import json
import sys


def read_records_from_txt_file(filename):
    records = []
    with open(filename) as f:
        for line in f:
            if line.isspace():
                continue

            fields = line.rstrip('\n').split(':')
            record = {
                'name': fields[0],
                'birthday': fields[1],
                'birthplace': fields[2],
            }
            records.append(record)
    return records

def write_records_to_json_file(records, filename):
    with open(filename, 'x') as f:
        json.dump(records, f)


inputfile = sys.argv[1]
outputfile = sys.argv[2]

records = read_records_from_txt_file(inputfile)
write_records_to_json_file(records, outputfile)

