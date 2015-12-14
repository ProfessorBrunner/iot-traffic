$(function () {
    $('#traffic-density').highcharts({
        chart: {
            type: 'areaspline'
        },
        title: {
            text: 'Average traffic denstiy during one week'
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 150,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        xAxis: {
            categories: [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday'
            ],
            plotBands: [{ // visualize the weekend
                from: 4.5,
                to: 6.5,
                color: 'rgba(68, 170, 213, .2)'
            }]
        },
        yAxis: {
            title: {
                text: 'Number of cars per square kilometer'
            }
        },
        tooltip: {
            shared: true,
            valueSuffix: ' units'
        },
        credits: {
            enabled: false
        },
        plotOptions: {
            areaspline: {
                fillOpacity: 0.5
            }
        },
        series: [{
            name: 'White and Fourth',
            data: [3, 4, 3, 5, 4, 10, 12]
        }, {
            name: 'Wright and Healy',
            data: [1, 3, 4, 3, 3, 5, 4]
        },
        {
            name: 'White and Sixth',
            data: [3, 4, 17,3,4,6, 12]
        }]
    });
});
