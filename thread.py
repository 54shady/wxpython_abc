#!/usr/bin/env python

import threading
import time, random

class MyConter():
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()

c = MyConter()

class MyWorker(threading.Thread):
    def run(self):
        for i in range(10):
            print self.getName(), c.value
            c.increment()

w = MyWorker()

w.start()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
