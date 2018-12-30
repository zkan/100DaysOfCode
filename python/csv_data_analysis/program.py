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
    for k, v in row.items():
        if k != 'airline':
            row[k] = int(v)

    record = Record(**row)
    return record


def main():
    base_path = Path('.')
    filename = base_path / 'data' / 'airline-safety.csv'
    records = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            record = parse_row(row)
            print(record)
            records.append(record)

    print()

    max_fatal_accidents_85_99 = max(
        records,
        key=lambda x: x.fatal_accidents_85_99
    )
    print('Max fatal accidents in 85-99: ', max_fatal_accidents_85_99)
    max_fatalities_85_99 = max(
        records,
        key=lambda x: x.fatalities_85_99
    )
    print('Max fatalities in 85-99: ', max_fatalities_85_99)

    max_fatal_accidents_00_14 = max(
        records,
        key=lambda x: x.fatal_accidents_00_14
    )
    print('Max fatal accidents in 00-14: ', max_fatal_accidents_00_14)
    max_fatalities_00_14 = max(
        records,
        key=lambda x: x.fatalities_00_14
    )
    print('Max fatalities in 00-14: ', max_fatalities_00_14)


if __name__ == '__main__':
    main()
