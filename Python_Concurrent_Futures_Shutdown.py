# Python Concurrent Futures
# concurrent.futures — Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
#
# shutdown(wait=True) 
# Signal the executor that it should free any resources that it is using when the currently pending futures are done executing.
# Calls to Executor.submit() and Executor.map() made after shutdown will raise RuntimeError.
#
# You can avoid having to call this method explicitly if you use the with statement, which will shutdown the Executor (waiting as if Executor.shutdown()
# were called with wait set to True):
# 

import shutil

with ThreadPoolExecutor(max_workers=4) as e:

    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')

    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

