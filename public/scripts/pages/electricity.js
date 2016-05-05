define(['jquery', 'tools'], function(jQuery, tools) {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
	    jQuery('a[href="#lastMonth"]').click(function () {
		    jQuery('#loading').addClass('modal');
		    jQuery.getJSON("/powerConsumptionLastMonth", function(data) {
				showChart(data.powerConsumption, 'Dane z ostatniego miesiąca');
				jQuery('div.insertBody').addClass('hidden');
		    });
	    });
    
	    jQuery('a[href="#twoMonths"]').click(function () {
		    jQuery('#loading').addClass('modal');
		    jQuery.getJSON("/powerConsumptionLastTwoMonth", function(data) {
				showChart(data.powerConsumption, 'Dane z ostatnich dwóch miesiący');
				jQuery('div.insertBody').addClass('hidden');
		    });
	    });

	    jQuery('a[href="#addNewValue"]').click(function () {
		jQuery('#loading').addClass('modal');
		jQuery.getJSON("/getAllMeters", function(data) {
		    var meterPicker = jQuery('#meterPicker');
		    jQuery.each(data, function(index, item) {
			meterPicker.append("<option value='" + item.id + "'>" + item.meterNumber + "</option>");
		    });

		    jQuery('div.insertBody').removeClass('hidden');
		    jQuery('#loading').removeClass('modal');
		});
	    });

	    jQuery('#addNewReading').click(function () {
		var meterValue = jQuery('#meterValue').val();
		var selectedMeter = jQuery('#meterPicker').find(':selected').val();

		jQuery.ajax("/addNewReading", {
		    data: JSON.stringify({ "meterId": selectedMeter, "meterValue": meterValue }),
		    contentType: 'application/json',
		    type: 'POST',
		    success: function () {
			jQuery('div.insertBody').addClass('hidden');
		    },
		});
	    });

	    jQuery.getJSON("/powerConsumptionLastMonth", function(data) {
			showChart(data.powerConsumption, 'Dane z ostatniego miesiąca');
			jQuery('div.insertBody').addClass('hidden');
	    });
    }

    function showChart(data, title) {
	    var powerUsage = [];
	    var readingDate = [];
	    var powerConsumptionArray = [];

	    if (data.length == 0) {
			var chartArea = jQuery('#curve_chart');
			chartArea.empty();
			chartArea.append("<span>Brak danych</span>");
			jQuery('#loading').removeClass('modal');
			return;
	    }

	    jQuery.each(data, function(index, value) {
		    powerUsage.push(value.readingValue);
		    readingDate.push(value.readingDate);
		    powerConsumptionArray.push([tools.convertToDateTime(value.readingDate), value.readingValue]);
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
	    chartData.addColumn('datetime', 'Data');
	    chartData.addColumn('number', 'Zużycie energii elektrycznej');

	    chartData.addRows(powerConsumptionArray);
	    
	    var options = {
		    title: title,
		    legend: { position: 'bottom' },
		    pointSize: 7,
		    height: 700,
		    hAxis: {
				title: 'Czas',
				format: 'dd/MM HH:mm'
		   	},
		    vAxis: { title: 'Zużycie energii [kWh]', minValue: lowestUsage, maxValue: highestUsage, ticks: ticksArray },
		    trendlines: {
			0: {
			    opacity: 1,
			    color: 'red',
			    pointSize: 0,
			    labelInLegend: 'Trend zużycia energii'
			},
		    }
	    };

	    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
	    chart.draw(chartData, options);

	    jQuery('#loading').removeClass('modal');
    }

});