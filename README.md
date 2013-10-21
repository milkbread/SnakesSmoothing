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

***Such a pure LineString can be used directly from commandline:***

```sh
SnakesLineSmoothing.jar <inFile> <outFile> <tolerance>'
```
	
--> e.g.: 	

```sh
java -jar SnakesLineSmoothing.jar in.json out.json 0.05
```
	




