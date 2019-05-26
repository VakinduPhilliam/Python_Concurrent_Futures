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
# asyncore - basic echo server
# 
# Here is a basic echo server that uses the dispatcher class to accept connections and dispatches the incoming connections to a handler:
# 

import asyncore

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):

        data = self.recv(8192)

        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)

        self.create_socket()
        self.set_reuse_addr()

        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):

        print('Incoming connection from %s' % repr(addr))

        handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)

asyncore.loop()
