#!/usr/bin/python
#This script was written by Ralf Klammer, 22.10.2013
################################
#It demonstrates how to get more control of TopoJSON-geometries by 
#manipulating the single arc-geometries and use them directly to build the GeoJSON-features

import json
import urllib
import subprocess
import time
import classes.topojson_rk as topojson
from classes.visvalingam import VisvalingamSimplification

#topology = topojson.openTopoJSON('https://gist.github.com/milkbread/5957651/raw/81e3b548ab7873f3f80829e918ac5bd0da083a72/vg250_bld_krs_topo.json')
topology = topojson.openJSON('data/vg250_states_topo.json')
arcs = topology['arcs']
objects = topology['objects']

topoTrans = topojson.Transformation(topology['transform'])
arcGeometries = topoTrans.getArcGeometries(arcs)

#test on smoothing the arcs
start = time.time()
'''smoothedArcGeometries = []
for arcGeom in arcGeometries:
	print '***Smooth Arc***'
	feature = {}
	feature['type']='LineString'
	feature['coordinates']=arcGeom
	topojson.saveGeoJSON(feature, 'test.geojson')
	subprocess.call(['java',  '-jar', 'SnakesLineSmoothing.jar', 'test.geojson', 'testoutput.geojson', '0.1'])
	smoothedArcGeometries.append(topojson.openJSON('testoutput.geojson')['coordinates'])

print 'Smoothing all ArcGeometries took:', (time.time() - start)/60, 'minutes'

subprocess.call(['rm', '-rf', 'test.geojson'])
subprocess.call(['rm', '-rf', 'testoutput.geojson'])
'''

topoGeomBuilder = topojson.BuildGeometries(arcGeometries)#smoothedArcGeometries)

geoJSON = topoGeomBuilder.buildFeatures(objects['vg250_bld']['geometries'])
topojson.saveGeoJSON(geoJSON, 'result.geojson')

