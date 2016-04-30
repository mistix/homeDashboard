(function($) {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
	jQuery('a[href="#last24h"]').click(function () {
	    jQuery('#loading').addClass('modal');
	    $.getJSON("/last_24_hours", function(data) {
		showTemperatureChart(data, 'Dane z ostatnich 24 godzin');
	    });
	});
	
	jQuery('a[href="#last48h"]').click(function () {
	    jQuery('#loading').addClass('modal');
	    $.getJSON("/last_48_hours", function(data) {
		showTemperatureChart(data, 'Dane z ostanich 48 godzin');
	    });
	});

	$.getJSON("/last_24_hours", function(data) {
	    showTemperatureChart(data, 'Dane z ostatnich 24 godzin');
	});
    }

    function showTemperatureChart(data, chartTitle) {
	var temperatureArray = [];
	var heaterTemperature = [];
	var airTemperature = [];

	jQuery.each(data, function(index, value) {
		heaterTemperature.push(value.heaterTemperature);
		airTemperature.push(value.airTemperature);
		temperatureArray.push([value.readingDateTime, value.airTemperature, value.heaterTemperature]);
	});

	var lowestAirTemperature = Math.min.apply(Math, airTemperature);
	var highestAirTemperature = Math.max.apply(Math, airTemperature);

	var lowestHeaterTemperature = Math.min.apply(Math, heaterTemperature);
	var highestHeaterTemperature = Math.max.apply(Math, heaterTemperature);

	var lowestTemperature = lowestAirTemperature > lowestHeaterTemperature ? lowestHeaterTemperature - 2 : lowestAirTemperature - 2;
	var highestTemperature = highestAirTemperature > highestHeaterTemperature ? highestAirTemperature + 2 : highestHeaterTemperature + 2;

	var ticksArray = [];
	for(var i=lowestTemperature; i<=highestTemperature; i++) {
		ticksArray.push(i);
	}

	var chartData = new google.visualization.DataTable();
	chartData.addColumn('string', 'Data');
	chartData.addColumn('number', 'Temperatura powierza');
	chartData.addColumn('number', 'Temperatura grzejnika');

	chartData.addRows(temperatureArray);
	
	var options = {
	    	title: chartTitle,
		curveType: 'function',
		legend: { position: 'bottom' },
		height: 700,
		hAxis: { title: 'Czas' },
		vAxis: { title: 'Temperatura [C]',  minValue: lowestTemperature, maxValue: highestTemperature, ticks: ticksArray },
	};

	var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
	chart.draw(chartData, options);

	jQuery('#loading').removeClass('modal');
    }

})(jQuery);
