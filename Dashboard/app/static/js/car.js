// get car data from kafka
function getCarData() {
  // console.log("getting car data...");
  if(counter != numPoints)
    clearMarkers();
  displayMarkers();
  // console.log(multipleMarkers.length);
}

function displayMarkers(){
  // Loop through our array of markers & place each one on the map
  if(counter < numPoints){
      for(var i = 0; i < numCars; i++){
        if(counter == 0)
          console.log(carLocData[i][counter].latitude+", "+ carLocData[i][counter].longitude);
          var carIcon;
        if(i % 8 != 0){
          carIcon = '../static/images/car.png';
        }
        else{
          carIcon = '../static/images/truck.png'
        }
        var position = new google.maps.LatLng(carLocData[i][counter].latitude, carLocData[i][counter].longitude);
        marker = new google.maps.Marker({
            position: position,
            map: map,
            icon: carIcon
            // icon: '../static/images/car.png'
        });



        // console.log( circle.getBounds().contains( marker.getPosition() ) );
        // if the circle is made visible, for each car wiithin the circular alert area connect to the Firebase app and send out the message
        if(circle.visible){
          if(circle.getBounds().contains( marker.getPosition() ) ){

            var ref = new Firebase("https://trafficiot.firebaseio.com/demo/data");
            var message = "Alert! You are in an accident zone, please proceed with caution";
            var newPostRef = ref.push();

            if (message != null) {
              newPostRef.set({
                      traffic_message: {
                        message_details: message
                  }
                });
            }
          }
        }
        // message sending for individual cars
        // if the vehicle is clicked on, connect to the firebase app to send out the typed message
        marker.addListener('click', function() {
            // infowindow.open(map, marker);
            var ref = new Firebase("https://trafficiot.firebaseio.com/demo/data");
            var message = prompt("Please enter the message");
            var newPostRef = ref.push();

            if (message != null) {
              newPostRef.set({
                      traffic_message: {
                        message_details: message
                  }
                });
            }

        });
        multipleMarkers.push(marker);
    }

      counter++;
    }
  };


// remove all markers
function setMapOnAll(map) {
  for (var i = 0; i < multipleMarkers.length; i++) {
    multipleMarkers[i].setMap(map);
  }
  multipleMarkers.length = 0;
}

// Removes the markers from the map
function clearMarkers() {
  setMapOnAll(null);
}

function toggleMarkers() {
  for (var i = 0; i < multipleMarkers.length; i++) {
    multipleMarkers[i].setMap(multipleMarkers[i].getMap() ? null : map);
  }
}
