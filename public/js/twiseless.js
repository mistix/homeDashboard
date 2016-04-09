(function($) {
	google.charts.load('current', {'packages': ['corechart']});
	google.charts.setOnLoadCallback(drawChart);

	function drawChart() {
		$.getJSON("/last_24_hours", function(data) {
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
				title: 'Temperatura z 24 godzin',
				curveType: 'function',
				legend: { position: 'bottom' },
				width: 1400,
				height: 700,
				vAxis: { minValue: lowestTemperature, maxValue: highestTemperature, ticks: ticksArray },
			};

			var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
			chart.draw(chartData, options);
		});
	}

})(jQuery);
