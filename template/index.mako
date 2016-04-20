<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Home Temperature</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <script type="text/javascript" src="/static/js/jquery-1.12.0.min.js"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript" src="/static/js/temperature.js"></script>
    <link rel="stylesheet" type="text/css" href="/static/css/temperature.css">
  </head>
  <body>
      <ul>
	  <li><a class='active' href='#last24h'>Ostatnie 24h</a></li>
	  <li><a href='#last48h'>Ostatnie 48h</a></li>
	  <li><a href='#lastWeek'>Ostatni tydzien</a></li>
      </ul>
      <div id='chartTitle'></div>
      <div id="content-container">
	<div id="curve_chart"></div>
	  <div id='loading' class='modal'></div>
      </div>
  </body>
</html>
