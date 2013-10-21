#!/usr/bin/python

import json
import subprocess
from classes import checkArguments as check

output, start_coords, end_coords = check.getIOFilesRoute();

type = 'shortest.js';
outFile='route.js'
subprocess.call(['wget', 'http://routes.cloudmade.com/969868da48384c2d8e138511ee807367/api/0.3/'+start_coords+','+end_coords+'/car/'+type, '-O'+outFile])

route_data=open(outFile,'r')
route = json.load(route_data);
route_data.close();

#sadly...cloudmade mixes longi- and latitude...we have to correct that
geom = route['route_geometry'];
for i in range(len(geom)):
	geom[i] = [geom[i][1],geom[i][0]];

#make a GeoJSON-LineString-geometry-object
json_in = {};
json_in["type"]='LineString';
json_in["coordinates"]=geom;

#write GeoJSON-geometry to file
in_cache=open(output,'w');
json.dump(json_in, in_cache);
in_cache.close();

#clean up
subprocess.call(['rm', '-rf', outFile])

