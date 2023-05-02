#!usr/bin/env python3
'''Task 1: Let's execute multiple coroutines
at the same time'''

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_ramdom


async def wait_n(n: int, max_delsy: int) -> List(float):
    '''returns a list of the result of the delayed float values
    '''
    delay = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delsy). range(n)))
    )

    return sorted(delay)
