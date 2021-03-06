#!/usr/bin/python

import json
import os
import subprocess
import time
from classes import checkArguments as check

input, output, threshold = check.getIOFilesThreshold();
#print(input, output, threshold);

print 'Begin to smooth geometry!'
print '***************************'
start = time.time()
subprocess.call(['java',  '-jar', 'SnakesLineSmoothing.jar', input, 'cache.json', threshold])
print '***************************'
print 'Finished smoothing!'
print 'Smoothing took:', time.time() - start, 'seconds'

print 'Build FeatureCollection and write to', output
#open a file, containing a pure GeoJSON-geometry
json_data=open('cache.json','r')
data = json.load(json_data)	#parse JSON-content
json_data.close()

#define a new Featurecollection
geoJson = dict();
geoJson["type"] = "FeatureCollection"
geoJson["features"] = [];

#define a new geometry...and...
geom = {};
#...add the pure GeoJSON-geometry
geom["geometry"]=data;
geom["type"]="Feature";
props = {};
props["threshold"] = threshold;
geom["properties"] = props;
#insert the geometry to the featureclass
geoJson["features"].insert(0,geom)

subprocess.call(['rm', '-rf', 'cache.json'])

#write the resulting GeoJSON-file
json_file=open(output,'w');
json.dump(geoJson, json_file);
json_file.close();
