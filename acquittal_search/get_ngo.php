<?php

	$mysqli = NEW  MySQLi('tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com', 'root', 'Aniket2606' , 'machineLearning') ;
     
    
     
     $query = $mysqli->query("SELECT * FROM NGO LIMIT 1000 ; ");

     

     

?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>All NGO</title>
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
					<th>Sno</th>
					<th>Name</th>
					<th>Id</th>
					<th>Cheif Functionary</th>
					<th>Chairman</th>
					<th>Secretary</th>
					<th>Treasurer</th>
						<th>Parent Organisation</th>
						<th>Registered With</th>

						<th>Type</th>
						<th>Registration No</th>
						<th>City Of Registration</th>
						<th>State Of Registration</th>
						<th>Date Of Registration</th>
						<th>Frca</th>
						<th>Contact City</th>
						<th>Contact State</th>
						<th>Contact Country</th>
						<th>Telephone</th>
						<th>Telephone 2</th>
						<th>Mobile Number</th>
						<th>Address</th>
						<th>Email</th>
						<th>Website</th>
						<th>Fax</th>
						

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
			     	echo "<td>".$row[13]."</td>" ;
			     	echo "<td>".$row[14]."</td>" ;
			     	echo "<td>".$row[15]."</td>" ;
			     	echo "<td>".$row[16]."</td>" ;
			     	echo "<td>".$row[17]."</td>" ;
			     	echo "<td>".$row[18]."</td>" ;
			     	echo "<td>".$row[19]."</td>" ;
			     	echo "<td>".$row[20]."</td>" ;
			     	echo "<td>".$row[21]."</td>" ;
			     	echo "<td>".$row[22]."</td>" ;
			     	echo "<td>".$row[23]."</td>" ;
			     	echo "<td>".$row[24]."</td>" ;
			     	
			     	
			  
			     	echo "</tr>" ;
			     }


			?>
		</tbody>

	</table>

</div>

</body>
</html>