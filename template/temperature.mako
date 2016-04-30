<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Home Temperature</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" type="text/css" href="/static/css/temperature.css">
  </head>
  <body>
      <ul>
	  <li><a class='active' href='#last24h'>Ostatnie 24h</a></li>
	  <li><a href='#last48h'>Ostatnie 48h</a></li>
	  <li class='floatRight'><a href='/index'>Dashboard</a></li>
      </ul>
      <div id="content-container">
	<div id="curve_chart"></div>
	  <div id='loading' class='modal'></div>
      </div>
  </body>
  <script data-main="/static/scripts/common" src="/static/scripts/require.js"></script>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script>
    require(['common'], function() {
	require(['pages/temperature']);
    });
  </script>
</html>
