# Python Concurrent Futures
# concurrent.futures — Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
# class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())
# An Executor subclass that uses a pool of at most max_workers threads to execute calls asynchronously.
# initializer is an optional callable that is called at the start of each worker thread; initargs is a tuple of arguments passed to the
# initializer. Should initializer raise an exception, all currently pending jobs will raise a BrokenThreadPool, as well as any attempt to
# submit more jobs to the pool.
# ThreadPoolExecutor 

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents

def load_url(url, timeout):

    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

    # Start the load operations and mark each future with its URL

    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]

        try:
            data = future.result()

        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))

        else:
            print('%r page is %d bytes' % (url, len(data)))
