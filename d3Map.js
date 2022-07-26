// The svg
const svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

// Map and projection
const projection = d3.geoMercator()
    .center([0, 0])                // GPS of location to zoom on
    .scale(180)                       // This is like the zoom
    .translate([ width/2, height/2 ])

Promise.all([
d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"),
d3.tsv("results/entities_500k.tsv")
// d3.csv("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/data_gpsLocSurfer.csv")

]).then(function (initialize) {

    let dataGeo = initialize[0]
    let data = initialize[1]

  // Create a color scale
  /* const color = d3.scaleOrdinal()
    .domain(data.map(d => d.homecontinent))
    .range(d3.schemePaired); */

  // Add a scale for bubble size
  /* const valueExtent = d3.extent(data, d => +d.n)
  const size = d3.scaleSqrt()
    .domain(valueExtent)  // What's in the data
    .range([ 1, 50])  // Size in pixel */

  // if (d3.select("svg")) d3.select("svg").remove();

  // Draw the map
  svg.append("g")
      .selectAll("path")
      .data(dataGeo.features)
      .join("path")
        .attr("fill", "#e0e0e0")
        .attr("d", d3.geoPath()
            .projection(projection)
        )
      .style("stroke", "none")
      .style("opacity", 1)

  // Add circles:
  svg
    .selectAll("myCircles")
    .data(data) // .sort((a,b) => +b.n - +a.n).filter((d,i) => i<1000)
    .join("circle")
      .attr("cx", d => projection([+d.longitude, +d.latitude])[0])
      .attr("cy", d => projection([+d.longitude, +d.latitude])[1])
      .attr("r", d => .4).style("fill", d => "black")
      // .style("fill", d => color(d.homecontinent))
      // .attr("stroke", d=> {if (d.n>2000) {return "black"} else {return "none"}  })
      .attr("stroke-width", 3)
      .attr("fill-opacity", .4)



  // Add title and explanation
  /* svg
    .append("text")
      .attr("text-anchor", "end")
      .style("fill", "black")
      .attr("x", width - 10)
      .attr("y", height - 30)
      .attr("width", 90)
      .html("Wikidata georreferenced entities.")
      .style("font-size", 14) */


  // --------------- //
  // ADD LEGEND //
  // --------------- //

  // Add legend: circles
  /* const valuesToShow = [100,4000,15000]
  const xCircle = 40
  const xLabel = 90
  svg
    .selectAll("legend")
    .data(valuesToShow)
    .join("circle")
      .attr("cx", xCircle)
      .attr("cy", d => height - size(d))
      .attr("r", d => size(d))
      .style("fill", "none")
      .attr("stroke", "black") */

  // Add legend: segments
  /* svg
    .selectAll("legend")
    .data(valuesToShow)
    .join("line")
      .attr('x1', d => xCircle + size(d))
      .attr('x2', xLabel)
      .attr('y1', d => height - size(d))
      .attr('y2', d => height - size(d))
      .attr('stroke', 'black')
      .style('stroke-dasharray', ('2,2'))

  // Add legend: labels
  svg
    .selectAll("legend")
    .data(valuesToShow)
    .join("text")
      .attr('x', xLabel)
      .attr('y', d => height - size(d))
      .text(d => d)
      .style("font-size", 10)
      .attr('alignment-baseline', 'middle') */
})