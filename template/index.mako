<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Home Temperature</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script> 
    <script type="text/javascript" src="/static/js/twiseless.js"></script> 
    <script type="text/javascript">
      $(document).ready(function() {
        $("#viz").twiseless("render");
      });
    </script>
  </head>
  <body>
    <div id="container">
      <div id="header">
	<h1>Home Temperature</h1>
      </div>
      <div id="content-container">
	<div id="content">
	</div>
      </div>
    </div>
  </body>
</html>
