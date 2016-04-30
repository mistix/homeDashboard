define([], function () {
    return {
	convertToDateTime: function(dateString) {
	    var reggie = /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/;
	    var dateArray = reggie.exec(dateString); 
	    return new Date(
		    (+dateArray[1]),
		    (+dateArray[2])-1,
		    (+dateArray[3]),
		    (+dateArray[4]),
		    (+dateArray[5]),
		    (+dateArray[6])
	    );
	}
    };
});
