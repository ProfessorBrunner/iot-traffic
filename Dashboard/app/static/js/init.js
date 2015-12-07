// var map, heatmap, carData, weatherData ;
var multipleMarkers = [];
var markers = [
    [40.12008951,-88.23704624],
    [40.125,-88.235]
];

var carLocData, numCars, numPoints, counter = 0;

$.ajax({
    type: "GET",
    // url: "../static/data/data_for_5_cars_2.json",
    url: "../static/data/data_for_21_cars.json",
    dataType: "json",
    success: function (data) {
        carLocData = data;
        numCars = data.length;
        numPoints = data[0].length;
        console.log("num cars "+numCars+", num points "+numPoints);
    }
});

function startData(){
        // displayMarkers();

        displayHeatmap();
        showAccidentZones();
        showConstructionZones();
        // calls the getCarData function every 1000 milliseconds
        carData = setInterval(getCarData, 1000);
        // get weather data every 30 mins
        weatherData = setInterval(getWeatherData, 1800000);


}

function showAccidentZones(){
  // JSON object containing the start and end cooordinates of the accident zones
    var accidents = [
      {
        "accident":
        [
          {lat: 40.12214, lng: -88.24680},
          {lat: 40.12212, lng: -88.24354}
        ]
      },
      {
        "accident":
        [
          {lat: 40.11021, lng: -88.23352},
          {lat: 40.10909, lng: -88.23352}
        ]
      },
      {
        "accident": [
          {lat: 40.11266, lng: -88.23547},
          {lat: 40.11273, lng: -88.22892}
        ]
      }
    ];
    // draw a polyline on the google map for each point in the JSON object
    for(var a = 0; a < accidents.length; a++){
      var accidentPath = new google.maps.Polyline({
        path: accidents[a].accident,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
      });
      accidentPath.setMap(map);
    }
}

function showConstructionZones(){
  //JSON contianing the start and end cocordinates of each construction area
    var accidents = [
      {
        "accident":
        [
          {lat: 40.11825, lng: -88.25613},
          {lat: 40.11825, lng: -88.24802}
        ]
      },
      {
        "accident":
        [
          {lat: 40.11994, lng: -88.24154},
          {lat: 40.11994, lng: -88.23908}
        ]
      }
    ];

    // draw a polyline with a blue color on the road for each point in the JSON object
    // add an image depicting road construction at the start point
    for(var a = 0; a < accidents.length; a++){
      var accidentPath = new google.maps.Polyline({
        path: accidents[a].accident,
        geodesic: true,
        strokeColor: '#0000FF',
        strokeOpacity: 1.0,
        strokeWeight: 2
      });
      accidentPath.setMap(map);
      var constructionMarker = new google.maps.Marker({
          position: accidents[a].accident[0],
          map: map,
          icon: '../static/images/construction.png'
      });
    }
}

function displayHeatmap(){
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map
  });
};

// stop car and weather data from kafka
function stopData() {
  console.log("stopping data...")
  clearInterval(carData);
  clearInterval(weatherData);
  counter = 0;
}
