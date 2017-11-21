<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Acquittal Search</title>
	 <link rel="icon" href="images/logo.png">	  
      <link rel="stylesheet" href="	css/style.css">


	<script type="text/javascript">
 function redirect_cases(){
	window.location="get_cases.php";
};
function redirect_lawyers(){
	window.location="get_lawyers.php";
};
function redirect_ngo(){
	window.location="get_ngo.php";
};


</script>
  
</head>

<body>

	<div id="logo_title">
			<div id="image_desc">
				<img src="images/logo.png">
			</div>
			<div id="text_desc">
			Acquittal Search
			</div>
		
	</div>
  <form method="GET" accept="#">
	  <input type="search" id="sbx" name="searchbox" placeholder="                 Search the Law..."/>
	  <input type="submit" id="btn" class="material-icons" value="send" name="button"/>
	  <span id="line"></span>
  </form>


  <div id="result_container">
	<h2><b>Result will be here .... </b></h2>
  </div>
  
	<div id="more_search">
		<b>More Search :</b>

		
		  <input type="radio"  onclick="redirect_cases()"    name="search" value="cases">Cases
		  <span class="checkmark"></span>
		
		
		  <input type="radio"  onclick="redirect_lawyers()" name="search" value="lawyers">Lawyers
		  <span class="checkmark"></span>
		
		
		  <input type="radio" onclick="redirect_ngo()" name="search" value="ngo">NGO
		  <span class="checkmark"></span>
		
		  <input type="radio" onclick="redirect()" name="search" value="constitution">Constitution
		  <span class="checkmark"></span>
		


	</div>


  <div id="new_features">
	<b>New Features</b> : Index contains <u><b>~ 1,00,000 cases </b></u> &  <u><b> ~40,000 lawyers</b></u> details <i>(Soon going more bigger) </i>.
  </div>

	<div id="copyright">	
			Copyright © 2017 Acquittal Search.
	</div>
 
    

</body>
</html>
