import collections
import cProfile
import csv
from pathlib import Path


profiler = cProfile.Profile()
profiler.disable()

Record = collections.namedtuple(
    'Record',
    'airline, fatal_accidents_85_99, fatalities_85_99, '
    'fatal_accidents_00_14, fatalities_00_14'
)


def parse_row(row):
    record = Record(
        airline=row.get('airline'),
        fatal_accidents_85_99=int(row.get('fatal_accidents_85_99')),
        fatalities_85_99=int(row.get('fatalities_85_99')),
        fatal_accidents_00_14=int(row.get('fatal_accidents_00_14')),
        fatalities_00_14=int(row.get('fatalities_00_14')),
    )
    return record


def main():
    profiler.enable()
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
    profiler.disable()


if __name__ == '__main__':
    for _ in range(500):
        main()

    profiler.print_stats(sort='cumtime')
