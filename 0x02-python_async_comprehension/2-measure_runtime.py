#!/usr/bin/env python3
'''Task 2: Run time for four parallel comprehensions
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    '''asyncio.gather(): This function is used to concurrently
    run multiple coroutines in an event loop. It takes in one
    or more awaitable objects, and returns a coroutine
    that waits for all of them to complete.
    '''
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
