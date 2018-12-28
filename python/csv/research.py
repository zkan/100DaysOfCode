import collections
import csv
import os


data = []
Record = collections.namedtuple(
    'Record',
    'actual_mean_temp,actual_min_temp',
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            record = parse_row(row)
            print(record)



def parse_row(row):
    record = Record(
        actual_mean_temp=row.get('actual_mean_temp'),
        actual_min_temp=row.get('actual_min_temp')
    )
    return record
