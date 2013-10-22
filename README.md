## SnakesSmoothing - Exemplary applications of linear smoothing using a java based algorithm
## ===============

### Download the package

* clone the repository (**recommended**)
	
	```sh
	git clone https://github.com/milkbread/SnakesSmoothing.git
	```
	
* download the [zip-file](https://github.com/milkbread/SnakesSmoothing/archive/master.zip)

### Basics

The smoothing algorithm is implemented in Java and compressed into the file 'SnakesLineSmoothing.jar'

It reads only pure LineString-geometries adapted to [GeoJSON-Specification](http://geojson.org/geojson-spec.html)

```json
{ "type": "LineString",
  "coordinates": [ [100.0, 0.0], [101.0, 1.0] ]
}
```

### Process directly from commandline (Java):

```sh
SnakesLineSmoothing.jar <inFile> <outFile> <tolerance>
```
	
--> e.g.: 	

```sh
java -jar SnakesLineSmoothing.jar in.json outGeom.json 0.05
```

*Result:* smoothed pure GeoJSON-LineString-geometry

### Exemplary processing in Python:

Additionally you can write some simple scripts in python...
* *[smooth.py](smooth.py)* - exemplary script to call the algorithm from python
	
	```sh
	python smooth.py
	```
* *[smoothToFeatClass.py](smoothToFeatClass.py)* - complex script that works uses dynamic input-parameters and saves the resulting geometry to a GeoJSON-FeatureClass
	
	```sh
	python smoothToFeatClass.py -i in.json -o outFeatClass.json -t 0.05
	```
	***You can [view the resulting GeoJSON-FeatureClass directly](outFeatClass.json) on GitHub!!!***

### Exemplary workflow:

* Get the navigation route from paris (*48.86,2.33*) to moscow (*55.08,37.57*) *[lat, lng]*

	```sh
	python routeToJson.py -o route.json -s 48.86,2.33 -e 55.08,37.57
	```

* Smooth it and save it as GeoJSON-FeatureCollection

	```sh
	python smoothToFeatClass.py -i route.json -o outFeatClass.json -t 0.05
	```

### Efforts on polygon smoothing

* *[topojson_rk.py](topojson_rk.py)* - provides some classes and function to:
	- read the build the ArcGeometries of a TopoJSON-file and
	- transform (generalise) them occasionally
	- build the geometries from these afterwards

* *[smoothArcs.py](smoothArcs.py)* - testscript that:
	- executes the implemented classes and function
	- smoothes the ArcGeometries


