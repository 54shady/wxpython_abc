#!/usr/bin/env python

import threading
import Queue
import time, random

class MyWorker(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                print "reached end of queue"
                break;

            # pretend we're doing something that takes 10-100 ms
            time.sleep(random.randint(10, 100) / 1000.0)
            print "task", item, "finished"

q = Queue.Queue(0)

for i in range(10):
    q.put(i)

# add end-of-queue markers
q.put(None)

MyWorker(q).start()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
