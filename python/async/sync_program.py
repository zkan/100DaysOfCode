import random
import time

import colorama


def process():
    time.sleep(random.random() + .5)
    print(colorama.Fore.CYAN + 'Processing..')


for _ in range(10):
    process()
