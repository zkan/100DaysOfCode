import random
import time

import colorama


def process():
    print(colorama.Fore.CYAN + 'Processing..')
    time.sleep(random.random() + .5)


for _ in range(10):
    process()
