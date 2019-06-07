import datetime
import random
import time

import colorama


def process(number):
    print(colorama.Fore.CYAN + f'Processing.. {number}')
    time.sleep(random.random() + .5)


def run(number):
    for _ in range(10):
        process(number)


t0 = datetime.datetime.now()

run(1)
run(2)

dt = datetime.datetime.now() - t0

print(
    colorama.Fore.WHITE + f'App exiting, total time: {dt.total_seconds()}',
    flush=True
)
