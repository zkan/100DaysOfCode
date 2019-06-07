import asyncio
import datetime
import random

import colorama


async def process(number):
    print(colorama.Fore.CYAN + f'Processing.. {number}')
    await asyncio.sleep(random.random() + .5)


async def run(number):
    for _ in range(10):
        await process(number)


t0 = datetime.datetime.now()

loop = asyncio.get_event_loop()
task1 = loop.create_task(run(1))
task2 = loop.create_task(run(2))

final_task = asyncio.gather(task1, task2)
loop.run_until_complete(final_task)

dt = datetime.datetime.now() - t0

print(
    colorama.Fore.WHITE + f'App exiting, total time: {dt.total_seconds()}',
    flush=True
)
