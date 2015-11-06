ParkMe.controller('batchDailyController', function($scope, $http, $rootScope, getParkingSpots){
    $scope.dayValue = "20150926";

    $scope.displayDailyStats = false;

    //var initial_latitude = 37.7568400419;
    //var initial_longitute = -122.4204335636;
    var initial_latitude = 40.12008951;
    var initial_longitute = -88.23704624;
    $scope.map = { center: { latitude: initial_latitude, longitude: initial_longitute}, zoom: 14 };

    $scope.marker = {
        id: 0,
        coords: {
            latitude: initial_latitude,
            longitude: initial_longitute
        },
        options:{
            //icon:'../css/parking_marker.png'
            icon:'../css/car.png'
        }
    };

    $rootScope.dailyMarkers = [];


    var car1, car2, car3, myVar;

    $scope.stopStats = function(){
        clearInterval(myVar);
    };

    $scope.getDailyStats = function() {
        $.ajax({
            type: "GET",
            url: "../data/coordinatedata2.csv",
            dataType: "text",
            success: function (data) {
                car1 = data;
            }
        });
        $.ajax({
            type: "GET",
            url: "../data/coordinatedata0_2.csv",
            dataType: "text",
            success: function (data) {
                car2 = data;
            }
        });
        $.ajax({
            type: "GET",
            url: "../data/coordinatedata88_2.csv",
            dataType: "text",
            success: function (data) {
                car3 = data;


                var car1_data = $.csv.toObjects(car1);
                var car2_data = $.csv.toObjects(car2);
                var car3_data = $.csv.toObjects(car3);
                var carCount = 0;
                //var myVar = setInterval(function(){
                myVar = setInterval(function(){
                    $rootScope.dailyMarkers = [];
                    //$scope.map = { center: { latitude: car1_data[carCount].lat, longitude: car1_data[carCount].lon}, zoom: 14 };
                    //$scope.$apply();
                    getParkingSpots.getDailyAggregate(car1_data[carCount].lat, car1_data[carCount].lon, car2_data[carCount].lat, car2_data[carCount].lon, car3_data[carCount].lat, car3_data[carCount].lon);
                    //console.log(result[carCount].lat+", "+result[carCount].lon);
                    carCount++;
                    if(carCount == 100)
                        clearInterval(myVar);
                }, 1000);
            }
        });
    };
        //var carCount = 0;


    //    function processData(allText) {
    //        var result = $.csv.toObjects(allText);
    //
    //        var myVar = setInterval(function(){
    //            $rootScope.dailyMarkers = [];
    //            $scope.map = { center: { latitude: result[carCount].lat, longitude: result[carCount].lon}, zoom: 14 };
    //            $scope.$apply();
    //            getParkingSpots.getDailyAggregate(result[carCount].lat, result[carCount].lon);
    //            console.log(result[carCount].lat+", "+result[carCount].lon);
    //            carCount++;
    //            if(carCount == 1000)
    //                clearInterval(myVar);
    //        }, 1000);
    //
    //    }
    //
    //};

    //$scope.getDailyStats = function(){
    //    $.ajax({
    //        type: "GET",
    //        url: "../data/coordinatedata2.csv",
    //        dataType: "text",
    //        success: function(data) {processData(data);}
    //    });
    //    var carCount = 0;
    //
    //
    //    function processData(allText) {
    //        var result = $.csv.toObjects(allText);
    //
    //        var myVar = setInterval(function(){
    //            $rootScope.dailyMarkers = [];
    //            $scope.map = { center: { latitude: result[carCount].lat, longitude: result[carCount].lon}, zoom: 14 };
    //            $scope.$apply();
    //            getParkingSpots.getDailyAggregate(result[carCount].lat, result[carCount].lon);
    //            console.log(result[carCount].lat+", "+result[carCount].lon);
    //            carCount++;
    //            if(carCount == 1000)
    //                clearInterval(myVar);
    //        }, 1000);
    //
    //    }
    //
    //};

});