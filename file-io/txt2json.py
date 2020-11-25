import json
import sys


inputfile = sys.argv[1]
outputfile = sys.argv[2]

# read input file into list of records
# ------------------------------------

# TODO:

# records = read_records_from_txt_file(inputfile)

records = []
with open(inputfile) as fin:
    for line in fin:
        if line.isspace():
            continue

        fields = line.rstrip('\n').split(':')
        record = {
            'name': fields[0],
            'birthday': fields[1],
            'birthplace': fields[2],
        }
        records.append(record)

# write records into json output file
# -----------------------------------

# TODO:

# write_records_to_json_file(records, outputfile)

with open(outputfile, 'x') as fout:
    json.dump(records, fout)

