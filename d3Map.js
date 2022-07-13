// const data = fetch('results/entities_100k.tsv')

const svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

// Map and projection
const projection = d3.geoMercator()
    .center([0, 0]) // GPS of location to zoom on
    .scale(200) // This is like the zoom
    .translate([width / 2, height / 2])

Promise.all([
    d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"),
    d3.tsv("results/entities_100k.tsv")
]).then(function (initialize) {

    let dataGeo = initialize[0]
    let data = initialize[1]

    // Draw the map
    svg.append("g")
        .selectAll("path")
        .data(dataGeo.features)
        .join("path")
        .attr("fill", "#b8b8b8")
        .attr("d", d3.geoPath()
            .projection(projection)
        )
        .style("stroke", "none")
        .style("opacity", .3)

    // Add circles:
    svg.selectAll("myCircles")
        .data(data)
        .join("circle")
        .attr("cx", d => projection([+d.longitude, +d.latitude])[0])
        .attr("cy", d => projection([+d.longitude, +d.latitude])[1])
        .attr("r", d => 1) // radio
        .attr("fill-opacity", .4)



})