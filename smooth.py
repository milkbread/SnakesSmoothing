#!/usr/bin/python

import subprocess
import time

print 'Begin to smooth geometry!'
print '***************************'
start = time.time()
subprocess.call(['java',  '-jar', 'SnakesLineSmoothing.jar', 'in.json', 'outGeom.json', '0.05'])
print '***************************'
print 'Finished smoothing!'
print 'Smoothing took:', time.time() - start, 'seconds'