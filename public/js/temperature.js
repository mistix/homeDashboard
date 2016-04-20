(function($) {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
	jQuery('a[href="#last24h"]').click(function () {
	    jQuery('#loading').addClass('modal');
	    jQuery('#chartTitle').text('Dane z ostatnich 24 godzin');
	    $.getJSON("/last_24_hours", showTemperatureChart);
	});
	
	jQuery('a[href="#last48h"]').click(function () {
	    jQuery('#loading').addClass('modal');
	    jQuery('#chartTitle').text('Dane z ostatnich 48 godzin');
	    $.getJSON("/last_48_hours", showTemperatureChart);
	});

	jQuery('a[href="#lastWeek"]').on('click', function () {
	    jQuery('#loading').addClass('modal');
	    jQuery('#chartTitle').text('Dane z ostatniego tygodnia');

	    var now = new Date();
	    var weekBeforeNow = now.setDate(now.getDate() - 7);
	    $.ajax({
		type: "POST",
		url: "/reading_in_range",
	        data: JSON.stringify({fromDate: weekBeforeNow, toDate: now }),
		contentType: 'application/json',
		dataType: 'json',
		error: function() { 
		    jQuery('#loading').removeClass('modal');
		},
		success: showTemperatureChart
	    });
	});

	jQuery('#chartTitle').text('Dane z ostatnich 24 godzin');
	$.getJSON("/last_24_hours", showTemperatureChart);
    }

    function showTemperatureChart(data) {
	var temperatureArray = [ ];
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
	chartData.addColumn('number', 'Temperaturza powierza');
	chartData.addColumn('number', 'Temperaturza grzejnika');

	chartData.addRows(temperatureArray);
	
	var options = {
		curveType: 'function',
		legend: { position: 'bottom' },
		height: 700,
		vAxis: { minValue: lowestTemperature, maxValue: highestTemperature, ticks: ticksArray },
	};

	var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
	chart.draw(chartData, options);

	jQuery('#loading').removeClass('modal');
    }

})(jQuery);
