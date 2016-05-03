define(['jquery', 'tools'], function(jQuery, tools) {
    jQuery('.temperature').on('click', function() {
	window.location.href='/temperature';
    });

    jQuery('.electricity').on('click', function() {
	window.location.href='/electricityUsage';
    });
});
