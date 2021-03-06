# Python Concurrent Futures
# concurrent.futures � Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
# Executor Objects.
# class concurrent.futures.Executor. 
# An abstract class that provides methods to execute calls asynchronously. It should not be used directly, but through its concrete subclasses.
# submit(fn, *args, **kwargs). 
# Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future object representing the execution of the callable.
 
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)

    print(future.result())
