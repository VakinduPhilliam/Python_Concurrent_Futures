# Python Concurrent Futures
# concurrent.futures — Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
# ThreadPoolExecutor.
# ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
# Deadlocks can occur when the callable associated with a Future waits on the results of another Future.
#
# For example:
# 

import time

def wait_on_b():
    time.sleep(5)

    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)

    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)

a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

#
# And:
# 

def wait_on_future():
    f = executor.submit(pow, 5, 2)

    # This will never complete because there is only one worker thread and
    # it is executing this function.

    print(f.result())

executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)
