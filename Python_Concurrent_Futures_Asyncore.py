# Python Concurrent Futures
# concurrent.futures — Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
#
# asyncore — Asynchronous socket handler
#
# Note:
# 
# This module exists for backwards compatibility only. For new code we recommend using asyncio. 
# This module provides the basic infrastructure for writing asynchronous socket service clients and servers.
# There are only two ways to have a program on a single processor do “more than one thing at a time.” Multi-threaded programming is the
# simplest and most popular way to do it, but there is another very different technique, that lets you have nearly all the advantages of
# multi-threading, without actually using multiple threads. It’s really only practical if your program is largely I/O bound.
# If your program is processor bound, then pre-emptive scheduled threads are probably what you really need.
# Network servers are rarely processor bound, however.
#
# Here is a very basic HTTP client that uses the dispatcher class to implement its socket handling:
# 

import asyncore

class HTTPClient(asyncore.dispatcher):

    def __init__(self, host, path):

        asyncore.dispatcher.__init__(self)
        self.create_socket()

        self.connect( (host, 80) )
        self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %
                            (path, host), 'ascii')

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


client = HTTPClient('www.python.org', '/')

asyncore.loop()
