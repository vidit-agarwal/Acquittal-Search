<?php

	$mysqli = NEW  MySQLi('tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com', 'root', 'Aniket2606' , 'machineLearning') ;
     
    
     
     $query = $mysqli->query("SELECT * FROM legal_crystal LIMIT 30 ; ");

     

     

?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>All Cases</title>
	<link rel="icon" href="images/logo.png">	
	 <!--<link rel="stylesheet" href="table_ui/css/footable.bootstrap.css">
	 <link rel="stylesheet" href="table_ui/css/footable.bootstrap.min.css">-->

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	
	<!--<script type="text/javascript" src="table_ui/js/footable.js"></script>
    <script type="text/javascript" src="table_ui/js/footable.min.js"></script>-->
      <link rel="stylesheet" href="	css/style.css">

      
</head>
<body>
	
<div style="overflow-x:auto;">
	<table class="table" data-paging="true" border=" 1px solid black " border-collapse="collapse " style="width:100% ;">
		<thead>
				<tr>
					<th>Ttile</th>
					<th>Citation</th>
					<th>Subject</th>
					<th >Court</th>
					<th>Decided On</th>
					<th>Case Number</th>
					<th>Judge</th>
						<th>Appellant</th>
						<th>Reported On</th>

						<th>Acts</th>
						<th>Respondent</th>
						<th>Appellant Advocate</th>
						<th>Respondent Advocate</th>
						<th>History</th>
						<th>Excerpt</th>
						

				</tr>
		</thead>
		<tbody>
			<?php
				while($row = mysqli_fetch_row($query))
			     {
			     	echo "<tr>";
			     	echo "<td>".$row[0]."</td>" ;
			     	echo "<td>".$row[1]."</td>" ;
			     	echo "<td>".$row[2]."</td>" ;
			     	echo "<td>".$row[3]."</td>" ;
			     	echo "<td>".$row[4]."</td>" ;
			     	echo "<td>".$row[5]."</td>" ;
			     	echo "<td>".$row[6]."</td>" ;
			     	echo "<td>".$row[7]."</td>" ;
			     	echo "<td>".$row[8]."</td>" ;
			     	echo "<td>".$row[9]."</td>" ;
			     	echo "<td>".$row[10]."</td>" ;
			     	echo "<td>".$row[11]."</td>" ;
			     	echo "<td>".$row[12]."</td>" ;
			     	echo "<td>".$row[14]."</td>" ;
			     	echo "<td>".$row[15]."</td>" ;
			     	
			     	
			  
			     	echo "</tr>" ;
			     }


			?>
		</tbody>

	</table>

</div>

</body>
</html>