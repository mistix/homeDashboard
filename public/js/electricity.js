(function($) {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
		jQuery('a[href="#lastMonth"]').click(function () {
			jQuery('#loading').addClass('modal');
			jQuery('#chartTitle').text('Dane ostatniego miesiąca');
			$.getJSON("/powerConsumptionLastMonth", showChart);
		});
	
		jQuery('a[href="#twoMonths"]').click(function () {
			jQuery('#loading').addClass('modal');
			jQuery('#chartTitle').text('Dane z ostatnich 2 miesiecy');
			$.getJSON("/powerConsumptionLastTwoMonth", showChart);
		});

		jQuery('#chartTitle').text('Dane z ostatniego miesiąca');
		$.getJSON("/powerConsumptionLastMonth", showChart);
    }

    function showChart(data) {
		var powerUsage = [];
		var readingDate = [];
		var powerConsumptionArray = [];

		jQuery.each(data, function(index, value) {
			powerUsage.push(value.readingValue);
			readingDate.push(value.readingDate);
			powerConsumptionArray.push([value.readingDate, value.readingValue]);
		});

		var lowestReading = Math.min.apply(Math, powerUsage);
		var highestReading = Math.max.apply(Math, powerUsage);

		var lowestUsage = lowestReading - 2;
		var highestUsage = highestReading + 2;

		var ticksArray = [];
		for(var i=lowestUsage; i<=highestUsage; i++) {
			ticksArray.push(i);
		}

		var chartData = new google.visualization.DataTable();
		chartData.addColumn('string', 'Data');
		chartData.addColumn('number', 'kWh');

		chartData.addRows(powerConsumptionArray);
		
		var options = {
			curveType: 'function',
			legend: { position: 'bottom' },
			height: 700,
			vAxis: { minValue: lowestUsage, maxValue: highestUsage, ticks: ticksArray },
		};

		var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
		chart.draw(chartData, options);

		jQuery('#loading').removeClass('modal');
    }

})(jQuery);
