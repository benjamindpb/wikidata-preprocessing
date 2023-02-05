# Wikidata Preprocessing

## Objective
The main objective of this work is to carry out a preprocessing and subsequent analysis of the Wikidata database to see the feasibility of its use as a potential data source for carrying out an entity geolocation project. In addition, once the data source is obtained, the aim is to analyze the performance of generating a world map with georeferenced instances.

## Preprocessing
To carry out the preprocessing of the Wikidata database, the [truthy dump](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format#Truthy_statements) is first downloaded and read to obtain all the triples that contain the property [P625](https://www.wikidata.org/wiki/Property:P625) (*coordinate location*) as a predicate. In this way, all the Wikidata entities that are potentially georeferenceable on a world map are obtained. These are saved in a tsv file for later analysis.

## Data analysis
Once the georeferenced entities were obtained, an analysis of the **types** to which these entities correspond was carried out. For this, the same previous procedure of reading the dump was repeated and for each triple that had the property [P31](https://www.wikidata.org/wiki/Property:P31) (*instance of*) as a predicate, the type was saved in a dictionary as *key* and the count as *value*. It should be noted that an entity may have more than one P31 property, for example the P31 properties of the University of Chile are that it is a public university, open access publisher and research institute.

## Results
To perform the visualizations, the [D3.js](https://d3js.org/) and [Folium](https://python-visualization.github.io/folium/) tools were used. 

The following images show the geolocation of 500 thousand Wikidata entities using d3.js and Folium respectively.

![d3_500k](https://user-images.githubusercontent.com/48598318/184800667-672df18e-0a3c-408e-94d6-a01e567189a2.png)
![folium_500k](https://user-images.githubusercontent.com/48598318/184800687-d937c4b2-5903-4f9d-980c-b69259d709c0.png)

As explained above, from the analysis of the data it was possible to obtain the distribution of the types of georeferenced entities.
The following table shows the 25 types of entities that are most repeated in Wikidata:

| Entity URL                              |   label     |   count |
|:----------------------------------------|-------------|--------:|
| https://www.wikidata.org/wiki/Q8502     |mountain|  519904 |
| https://www.wikidata.org/wiki/Q486972   |human settlement|  418608 |
| https://www.wikidata.org/wiki/Q79007    |street|  406014 |
| https://www.wikidata.org/wiki/Q4022     |river|  366991 |
| https://www.wikidata.org/wiki/Q54050    |hill|  321257 |
| https://www.wikidata.org/wiki/Q41176    |building|  259995 |
| https://www.wikidata.org/wiki/Q23397    |lake|  257618 |
| https://www.wikidata.org/wiki/Q3947     |house|  193489 |
| https://www.wikidata.org/wiki/Q16970    |church building|  191711 |
| https://www.wikidata.org/wiki/Q532      |village|  176979 |
| https://www.wikidata.org/wiki/Q355304   |watercourse|  173187 |
| https://www.wikidata.org/wiki/Q23442    |island|  148484 |
| https://www.wikidata.org/wiki/Q27686    |hotel|  121843 |
| https://www.wikidata.org/wiki/Q47521    |stream|  121753 |
| https://www.wikidata.org/wiki/Q9842     |primary school|  107988 |
| https://www.wikidata.org/wiki/Q811979   |architectural structure|  101900 |
| https://www.wikidata.org/wiki/Q55488    |railway station|   98867 |
| https://www.wikidata.org/wiki/Q39816    |valley|   95799 |
| https://www.wikidata.org/wiki/Q22698    |park|   81944 |
| https://www.wikidata.org/wiki/Q39614    |cemetery|   81427 |
| https://www.wikidata.org/wiki/Q12323    |dam|   73837 |
| https://www.wikidata.org/wiki/Q67383935 |co-educational school|   73757 |
| https://www.wikidata.org/wiki/Q124714   |spring|   69248 |
| https://www.wikidata.org/wiki/Q19855165 |rural school|   68024 |
| https://www.wikidata.org/wiki/Q55659167 |natural watercourse|   66348 |

---
[![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Wikidata_Stamp_Rec_Dark.svg/200px-Wikidata_Stamp_Rec_Dark.svg.png "Powered by Wikidata")](https://www.wikidata.org/wiki/Wikidata:Main_Page)
