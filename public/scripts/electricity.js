(function($) {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
		jQuery('a[href="#lastMonth"]').click(function () {
			jQuery('#loading').addClass('modal');
			$.getJSON("/powerConsumptionLastMonth", function(data) {
			    showChart(data, 'Dane z ostatniego miesiąca');
			    jQuery('div.insertBody').addClass('hidden');
			});
		});
	
		jQuery('a[href="#twoMonths"]').click(function () {
			jQuery('#loading').addClass('modal');
			jQuery.getJSON("/powerConsumptionLastTwoMonth", function(data) {
			    showChart(data, 'Dane z ostatniego miesiąca');
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
		    showChart(data, 'Dane z ostatniego miesiąca');
		    jQuery('div.insertBody').addClass('hidden');
		});
    }

    function convertToDateTime(dateString) {
	var reggie = /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/;
	var dateArray = reggie.exec(dateString); 
	return new Date(
		(+dateArray[1]),
		(+dateArray[2])-1, // Careful, month starts at 0!
		(+dateArray[3]),
		(+dateArray[4]),
		(+dateArray[5]),
		(+dateArray[6])
	);
    }

    function showChart(data, title) {
		var powerUsage = [];
		var readingDate = [];
		var powerConsumptionArray = [];

		jQuery.each(data, function(index, value) {
			powerUsage.push(value.readingValue);
			readingDate.push(value.readingDate);
			powerConsumptionArray.push([convertToDateTime(value.readingDate), value.readingValue]);
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
		chartData.addColumn('number', 'kWh');

		chartData.addRows(powerConsumptionArray);
		
		var options = {
		    	title: title,
			legend: { position: 'bottom' },
			pointSize: 7,
			height: 700,
			hAxis: { title: 'Czas' },
			vAxis: { title: 'Zużycie energii [kWh]', minValue: lowestUsage, maxValue: highestUsage, ticks: ticksArray },
			trendlines: {
			    0: {
				opacity: 1,
				color: 'red',
				pointSize: 0
			    },
			}
		};

		var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
		chart.draw(chartData, options);

		jQuery('#loading').removeClass('modal');
    }

})(jQuery);
