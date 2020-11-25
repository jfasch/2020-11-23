import json
import sys


inputfile = sys.argv[1]
outputfile = sys.argv[2]

records = []
with open(inputfile) as fin:
    for line in fin:
        fields = line.split(':')
        record = {
            'name': fields[0],
            'birthday': fields[1],
            'birthplace': fields[2],
        }
        records.append(record)

with open(outputfile, 'x') as fout:
    json.dump(records, fout)

