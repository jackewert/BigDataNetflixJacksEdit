"""
Timer Class for us to see how fast a process is
https://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python

After importing this module, you can use it using the following code:

t = time.time()
# do stuff
elapsed = time.time() - t

OR

with Timer('foo_stuff'):
   # do some foo
   # do some stuff

"""
import time
class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print '[%s]' % self.name,
        print 'Elapsed: %s' % (time.time() - self.tstart)