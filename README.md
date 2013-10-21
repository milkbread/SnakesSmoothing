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
* *smooth.py* - exemplary script to call the algorithm from python
	´´´sh
	python smooth.py
	´´´
* *smoothToFeatClass.py* - complex script that works uses dynamic input-parameters and saves the resulting geometry to a GeoJSON-FeatureClass
	´´´sh
	python smoothToFeatClass.py -i in.json -o outFeatClass.json -t 0.05
	´´´

***You can view the resulting GeoJSON-File directly on GitHub!!!***


	




