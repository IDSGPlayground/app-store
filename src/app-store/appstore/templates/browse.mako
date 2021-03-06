<!DOCTYPE html> 
<html>
<head>
    <meta charset="UTF-8">
    <title>BearApps</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="BearApps">
    <meta name="author" content="EECS IDSG">

    <link rel="stylesheet" type="text/css" href="static/css/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="static/css/bootstrap-responsive.css" />
    <link href='http://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>     
    <link href='http://fonts.googleapis.com/css?family=Ubuntu' rel='stylesheet' type='text/css'>
    
    <style type="text/css">
	    .content {
			padding-top: 80px;
			padding-bottom: 40px;
			padding-right: 40px;
			padding-left: 40px;
	    }
    </style>


</head> 

<body>

<div class="navbar navbar-fixed-top">
    <div class="navbar-inner">
		<div class="container-fluid">
			<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</a>

			<a class="brand" href="index.html">BearApps</a>

			<div class="nav-collapse">
				<ul class="nav">
					<li><a href="my-apps.html">My Apps</a></li>
					<li><a href="browse.html">Browse Apps</a></li>
				</ul>
			</div>

			<div class="btn-group pull-right">
				<a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
					<i class="icon-user"></i>
					Username
					<span class="caret"></span>
				</a>
				<ul class="dropdown-menu">
					<li>
						<a href="#">Edit Settings</a>
					</li>
					<li class="divider"></li>
					<li>
						<a href="#">Sign Out</a>
					</li>
				</ul>
			</div>

			<div class="btn-group pull-right">
				<div class="btn btn-danger">
					<i class="icon-bell icon-white"></i> 0
				</div>
			</div>

		</div>
    </div>
</div>

<div class="container-fluid content">
	<div class="row-fluid">
		<h1>BROWSE APPS</h1>
		<div class="pull-right">
			<form class="form-search">
				<input type="text" class="input-medium search-query">
				<button type="submit" class="btn">Search</button>
			</form>
		</div>
	</div>

	<div class="row-fluid">
		<div class="span12">
			<div class="well hero-unit">
				<div class="row-fluid">
					<div class="span3">
						<a href="#matlab" data-toggle="modal" class="app-btn"><h3>MatLab</h3></a>
					<div>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="modal hide" id="matlab">
	<div class="modal-header">
    	<button type="button" class="close" data-dismiss="modal">×</button>
    	<h3><img src="static/img/matlab-icon-small.png" /> MatLab</h3>
  	</div>
  	<div class="modal-body">
    	<p>Description here</p>
  	</div>
</div>

</body>

<!-- Le javascript
================================================== -->
<script src="static/js/jquery.js"></script>
<script src="static/js/bootstrap-transition.js"></script>
<script src="static/js/bootstrap-alert.js"></script>
<script src="static/js/bootstrap-modal.js"></script>
<script src="static/js/bootstrap-dropdown.js"></script>
<script src="static/js/bootstrap-scrollspy.js"></script>
<script src="static/js/bootstrap-tab.js"></script>
<script src="static/js/bootstrap-tooltip.js"></script>
<script src="static/js/bootstrap-popover.js"></script>
<script src="static/js/bootstrap-button.js"></script>
<script src="static/js/bootstrap-collapse.js"></script>
<script src="static/js/bootstrap-carousel.js"></script>
<script src="static/js/bootstrap-typeahead.js"></script>

</html>
