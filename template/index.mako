<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Home Dashboard</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
  </head>
  <body>
	  <div class='dashboard'>
		  <div class='row'>
			  <div class='item temperature'>
				  <div class='body'>
					  <div class='image'>
						  <img src='/static/images/tool.png' />
					  </div>
					  <div class='content'>
						  <div class='mesure'>
							  <div class='mesureTitle'>
								  Average air temperature:
							  </div>
							  <div class='mesureValue'>
								  23.6 C
							  </div>
						  </div>
					  </div>
				  </div>
				  <div class='footer'>
					  <div class='footerText'>
					      <span>Click to more</span>
					  </div>
				  </div>
			  </div>
			  <div class='item electricity'>
				  <div class='body'>
					  <div class='image'>
						  <img src='/static/images/electricity.png' />
					  </div>
					  <div class='content'>
						  <div class='mesure'>
							  <div class='mesureTitle'>
								  Average usage:
							  </div>
							  <div class='mesureValue'>
								  16 kWh
							  </div>
						  </div>
					  </div>
				  </div>
				  <div class='footer'>
					  <div class='footerText'>
					      <span>Click to more</span>
					  </div>
				  </div>
			  </div>
		  </div>
	  </div>
  </body>
  <script data-main="/static/scripts/common" src="/static/scripts/require.js"></script>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script>
    require(['common'], function() {
	require(['pages/main']);
    });
  </script>
</html>
