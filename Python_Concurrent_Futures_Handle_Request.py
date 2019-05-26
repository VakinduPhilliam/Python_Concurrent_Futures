# Python Concurrent Futures
# concurrent.futures — Launching parallel tasks.
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
# asynchat — Asynchronous socket command/response handler
#
# Note:
# 
# This module exists for backwards compatibility only. For new code we recommend using asyncio.
# This module builds on the asyncore infrastructure, simplifying asynchronous clients and servers and making it easier to handle protocols
# whose elements are terminated by arbitrary strings, or are of variable length. asynchat defines the abstract class async_chat that you
# subclass, providing implementations of the collect_incoming_data() and found_terminator() methods.
# It uses the same asynchronous loop as asyncore, and the two types of channel, asyncore.dispatcher and asynchat.async_chat, can freely be
# mixed in the channel map. Typically an asyncore.dispatcher server channel generates new asynchat.async_chat channel objects as it receives
# incoming connection requests.
#
# The handle_request() method is called once all relevant input has been marshalled, after setting the channel terminator to None to ensure
# that any extraneous data sent by the web client are ignored.
 
import asynchat

class http_request_handler(asynchat.async_chat):

    def __init__(self, sock, addr, sessions, log):
        asynchat.async_chat.__init__(self, sock=sock)

        self.addr = addr
        self.sessions = sessions
        self.ibuffer = []
        self.obuffer = b""

        self.set_terminator(b"\r\n\r\n")
        self.reading_headers = True
        self.handling = False

        self.cgi_data = None
        self.log = log

    def collect_incoming_data(self, data):
        """Buffer the data"""

        self.ibuffer.append(data)

    def found_terminator(self):

        if self.reading_headers:
            self.reading_headers = False

            self.parse_headers(b"".join(self.ibuffer))
            self.ibuffer = []

            if self.op.upper() == b"POST":
                clen = self.headers.getheader("content-length")
                self.set_terminator(int(clen))

            else:
                self.handling = True
                self.set_terminator(None)
                self.handle_request()

        elif not self.handling:
            self.set_terminator(None)  # browsers sometimes over-send
            self.cgi_data = parse(self.headers, b"".join(self.ibuffer))

            self.handling = True
            self.ibuffer = []
            self.handle_request()
