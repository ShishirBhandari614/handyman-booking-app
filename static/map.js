var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([customerLocation.longitude, customerLocation.latitude]),
        zoom: 5
    })
});

var vectorSource = new ol.source.Vector();
var extent = ol.extent.createEmpty();

serviceProviders.forEach(function(provider) {
    var marker = new ol.Feature({
        geometry: new ol.geom.Point(ol.proj.fromLonLat([provider.longitude, provider.latitude])),
        name: provider.name
    });

    marker.setStyle(new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [0.5, 1],
            scale: 0.8,
            src: 'https://cdn-icons-png.flaticon.com/32/149/149059.png'
        }),
        text: new ol.style.Text({
            text: provider.name,
            offsetY: -25,
            font: '12px Arial',
            fill: new ol.style.Fill({ color: 'black' }),
            stroke: new ol.style.Stroke({ color: 'white', width: 2 })
        })
    }));

    vectorSource.addFeature(marker);
    ol.extent.extend(extent, marker.getGeometry().getExtent());
});

var customerMarker = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([customerLocation.longitude, customerLocation.latitude])),
    name: "You"
});

customerMarker.setStyle(new ol.style.Style({
    image: new ol.style.Icon({
        anchor: [0.5, 1],
        scale: 0.8,
        src: 'https://cdn-icons-png.flaticon.com/32/149/149060.png'
    }),
    text: new ol.style.Text({
        text: "You",
        offsetY: -25,
        font: '12px Arial',
        fill: new ol.style.Fill({ color: 'blue' }),
        stroke: new ol.style.Stroke({ color: 'white', width: 2 })
    })
}));

vectorSource.addFeature(customerMarker);
ol.extent.extend(extent, customerMarker.getGeometry().getExtent());

var markerLayer = new ol.layer.Vector({
    source: vectorSource
});
map.addLayer(markerLayer);

if (serviceProviders.length > 0) {
    map.getView().fit(extent, {
        padding: [50, 50, 50, 50],
        maxZoom: 14,
        duration: 1000
    });
}

map.on('click', function(event) {
    map.forEachFeatureAtPixel(event.pixel, function(feature) {
        alert('Service Provider: ' + feature.get('name'));
    });
});
