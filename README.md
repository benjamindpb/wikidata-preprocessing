# Wikidata Preprocessing

## Descripción
Este mini proyecto tiene por objetivo hacer un preprocesamiento y analisis de la data que posee la base de datos de Wikidata.

## Objetivo
El principal objetivo fue georreferenciar las entidades de Wikidata usando la propiedad **P625** (*coordinate location*) en un mapa mundial.

## Analisis de Datos
Una vez obtenida la geolocalización de las entidades se realizó un analisis de los **tipos** de entidades usando la propiedad **P31** (*instance of*) de Wikidata que indica a que tipo de ejemplar corresponde una entidad. Cabe destacar que una entidad puede tener más de una propiedad P31, por ejemplo las propiedades P31 de la Universidad de Chile son que es una universidad publica, editor de libre acceso e instituto de investigación.

## Resultados
Para realizar las visualizaciones se utilizaron las herramientas [D3.js](https://d3js.org/) y [Folium](https://python-visualization.github.io/folium/). 

Las siguiente imagenes muestran la geolocalización de 500 mil entidades de Wikidata usando d3.js y Folium respectivamente.

![d3_500k](https://user-images.githubusercontent.com/48598318/184800667-672df18e-0a3c-408e-94d6-a01e567189a2.png)
![folium_500k](https://user-images.githubusercontent.com/48598318/184800687-d937c4b2-5903-4f9d-980c-b69259d709c0.png)

La siguiente tabla muestra los 25 tipos de entidades que más se repiten en Wikidata:

| entity_type                             |   count |
|:----------------------------------------|--------:|
| https://www.wikidata.org/wiki/Q8502     |  519904 |
| https://www.wikidata.org/wiki/Q486972   |  418608 |
| https://www.wikidata.org/wiki/Q79007    |  406014 |
| https://www.wikidata.org/wiki/Q4022     |  366991 |
| https://www.wikidata.org/wiki/Q54050    |  321257 |
| https://www.wikidata.org/wiki/Q41176    |  259995 |
| https://www.wikidata.org/wiki/Q23397    |  257618 |
| https://www.wikidata.org/wiki/Q3947     |  193489 |
| https://www.wikidata.org/wiki/Q16970    |  191711 |
| https://www.wikidata.org/wiki/Q532      |  176979 |
| https://www.wikidata.org/wiki/Q355304   |  173187 |
| https://www.wikidata.org/wiki/Q23442    |  148484 |
| https://www.wikidata.org/wiki/Q27686    |  121843 |
| https://www.wikidata.org/wiki/Q47521    |  121753 |
| https://www.wikidata.org/wiki/Q9842     |  107988 |
| https://www.wikidata.org/wiki/Q811979   |  101900 |
| https://www.wikidata.org/wiki/Q55488    |   98867 |
| https://www.wikidata.org/wiki/Q39816    |   95799 |
| https://www.wikidata.org/wiki/Q22698    |   81944 |
| https://www.wikidata.org/wiki/Q39614    |   81427 |
| https://www.wikidata.org/wiki/Q12323    |   73837 |
| https://www.wikidata.org/wiki/Q67383935 |   73757 |
| https://www.wikidata.org/wiki/Q124714   |   69248 |
| https://www.wikidata.org/wiki/Q19855165 |   68024 |
| https://www.wikidata.org/wiki/Q55659167 |   66348 |
