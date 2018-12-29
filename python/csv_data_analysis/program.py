import collections
import csv
from pathlib import Path


Record = collections.namedtuple(
    'Record',
    'airline, avail_seat_km_per_week, incidents_85_99,'
    'fatal_accidents_85_99, fatalities_85_99, incidents_00_14,'
    'fatal_accidents_00_14, fatalities_00_14'
)


def parse_row(row):
    record = Record(**row)
    return record


def main():
    base_path = Path('.')
    filename = base_path / 'data' / 'airline-safety.csv'
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            record = parse_row(row)
            print(record)


if __name__ == '__main__':
    main()
