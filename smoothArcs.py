#!/usr/bin/python
#This script was written by Ralf Klammer, 22.10.2013
################################
#It demonstrates how to get more control of TopoJSON-geometries by 
#manipulating the single arc-geometries and use them directly to build the GeoJSON-features

import json
import urllib
import classes.topojson_rk as topojson

#topology = topojson.openTopoJSON('https://gist.github.com/milkbread/5957651/raw/81e3b548ab7873f3f80829e918ac5bd0da083a72/vg250_bld_krs_topo.json')
topology = topojson.openJSON('data/vg250_bld_krs_topo.json')
arcs = topology['arcs']
objects = topology['objects']

topoTrans = topojson.Transformation(topology['transform'])
arcGeometries = topoTrans.getArcGeometries(arcs)

topoGeomBuilder = topojson.BuildGeometries(arcGeometries)

#test on smoothing the arcs
smoothedArcGeometries = []
for arcGeom in arcGeometries:
	feature = {}
	feature['type']='LineString'
	feature['coordinates']=arcGeom
	topojson.saveGeoJSON(feature, 'test.geojson')
	import subprocess
	subprocess.call(['java',  '-jar', 'SnakesLineSmoothing.jar', 'test.geojson', 'testoutput.geojson', '0.1'])
	smoothedArcGeometries.append(topojson.openJSON('testoutput.geojson'))
	
subprocess.call(['rm', '-rf', 'test.geojson'])
subprocess.call(['rm', '-rf', 'testoutput.geojson'])


geoJSON = topoGeomBuilder.buildFeatures(objects['vg250_bld']['geometries'])
topojson.saveGeoJSON(geoJSON, 'result.geojson')


#test = objects['vg250_bld']['geometries'][11]
#print test.keys()
#print test['type']
#buildGeoSONGeometry(test)
#print test['properties']['GEN']
